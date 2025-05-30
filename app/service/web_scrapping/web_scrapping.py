from bs4 import BeautifulSoup 
from web.web_scrapping_request import WebScrappingRequest
from utils.extract_data_table import ExtractDataTable
from database.DAO import Insert, Select
from datetime import date


BASE_URL = "http://vitibrasil.cnpuv.embrapa.br/index.php"

class WebScrapping:

    def __init__(self):
        self.web_scrapping_request = WebScrappingRequest(BASE_URL)
        pass

    def __end_point_buttons(self):
        try:
            response = self.web_scrapping_request.do('/')
        except:
            return False 
        end_points: list = []
        html_content = response
        soup = BeautifulSoup(html_content, "html.parser")
        buttons = soup.find_all("button", {"class": "btn_opt"})

        for button in buttons:
            value = button.get("value")
            end_points.append(value)

        return end_points              

    def get_content_page(self, year: int):

        end_points = self.__end_point_buttons()
        if not end_points:
            data_saved_database = Select.fetch_data_by_year(year)
            return data_saved_database
        data = {}
        
        for end_point in end_points:
            response =  WebScrappingRequest(BASE_URL).do(f"?opcao={end_point}&ano={year}")
            html_content = response
            soup = BeautifulSoup(html_content, "html.parser")
            buttons = soup.find_all("button", {"class": "btn_sopt"})
            
            if len(buttons):
                end_points_subopcoes = [end_point.get("value") for end_point in buttons]
                for end_point_subopcao in end_points_subopcoes:
                    response_subopcao = WebScrappingRequest(BASE_URL).do(
                        f"?subopcao={end_point_subopcao}&opcao={end_point}&ano={year}"
                    )
                    html_content_subopcao = response_subopcao
                    soup_subopcao = BeautifulSoup(html_content_subopcao, "html.parser")
                    table = ExtractDataTable(soup_subopcao).do()
                    title_table = soup_subopcao.find('p', {"class": "text_center"}).text
                    page = soup_subopcao.find('button',{"class":"btn_opt", "value": end_point}).text
                    if page not in data:
                        data[page] = []
                    data[page].append( {
                        title_table: table.to_dict(orient="records")
                        }
                    )
            else:
                table = ExtractDataTable(soup).do()
                if len(table):
                    title_table = soup.find('p', {"class": "text_center"}).text
                    page = soup.find('button',{"class":"btn_opt", "value": end_point}).text
                    if page not in data:
                        data[page] = []
                    data[page].append( {
                        title_table: table.to_dict(orient="records")
                        }
                    )
        
        due_date = Select.fetch_due_date(year)[0][0]
        current_date = date.today()
        if current_date > due_date:
            print(f"Updating stored data from the year {year}")
            Insert.save_json(data, year)
        
        return data
