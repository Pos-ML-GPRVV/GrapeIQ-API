from bs4 import BeautifulSoup 
from web.web_scrapping_request import WebScrappingRequest
from utils.extract_data_table import ExtractDataTable
from db.insert import salvar_dataframe, salvar_json
from db.connection import get_connection


BASE_URL = "http://vitibrasil.cnpuv.embrapa.br/index.php"

class WebScrapping:

    def __init__(self):
        self.web_scrapping_request = WebScrappingRequest(BASE_URL)
        pass

    def __end_point_buttons(self):
        response = self.web_scrapping_request.do('/')
        end_points: list = []
        html_content = response
        soup = BeautifulSoup(html_content, "html.parser")
        buttons = soup.find_all("button", {"class": "btn_opt"})

        for button in buttons:
            value = button.get("value")
            end_points.append(value)

        return end_points                    

    def get_content_page(self, year: int):

        end_points = ["opt_02"]
        data: list = []
        
        for end_point in end_points:
            response =  WebScrappingRequest(BASE_URL).do(f"?opcao={end_point}&ano={year}")
            print(response)
            html_content = response
            soup = BeautifulSoup(html_content, "html.parser")
            buttons = soup.find_all("button", {"class": "btn_opt"})
            
            if len(buttons):
                end_points_subopcoes = [end_point.get("value") for end_point in buttons]
                for end_point_subopcao in end_points_subopcoes:
                    response_subopcao = WebScrappingRequest(BASE_URL).do(
                        f"?subopcao={end_point_subopcao}&opcao={end_point}&ano={year}"
                    )
                    html_content_subopcao = response_subopcao
                    soup_subopcao = BeautifulSoup(html_content_subopcao, "html.parser")
                    table = ExtractDataTable(soup_subopcao).do()
                    # salvar_dataframe(table, tipo=end_point, ano=year)
                    data.append(table.to_json(orient="records", force_ascii=False))
            else:
                table = ExtractDataTable(soup).do()
                # salvar_dataframe(table, tipo=end_point, ano=year)
                data.append(table.to_json(orient="records", force_ascii=False))
        
        return data

    def get_content_page_json(self, year: int):
        conn = get_connection()
        end_points = self.__end_point_buttons()
        end_points.pop(0)
        end_points.pop(len(end_points) - 1)
        data_year: list = []
        
        for end_point in end_points:
            response = WebScrappingRequest(BASE_URL).do(f"?opcao={end_point}&ano={year}")
            html_content = response
            soup = BeautifulSoup(html_content, "html.parser")
            buttons = soup.find_all("button", {"class": "btn_opt"})
            
            if len(buttons):
                end_points_subopcoes = [end_point.get("value") for end_point in buttons]
                for end_point_subopcao in end_points_subopcoes:
                    response_subopcao = WebScrappingRequest(BASE_URL).do(
                        f"?subopcao={end_point_subopcao}&opcao={end_point}&ano={year}"
                    )
                    html_content_subopcao = response_subopcao
                    soup_subopcao = BeautifulSoup(html_content_subopcao, "html.parser")
                    table = ExtractDataTable(soup_subopcao).do()
                    json_data = table.to_dict(orient="records")
                    data_year.extend(json_data)
            else:
                table = ExtractDataTable(soup).do()
                json_data = table.to_dict(orient="records")
                data_year.extend(json_data)
        
        # salvar_json(conn, ano=ano, dados=data_year)
        return data_year
    