from bs4 import BeautifulSoup 
from web.web_scrapping_request import WebScrappingRequest
from utils.extract_data_table import ExtractDataTable

BASE_URL = "http://vitibrasil.cnpuv.embrapa.br/index.php"


class WebScrapping:

    def __init__(self):
        self.web_scrapping_request = WebScrappingRequest(BASE_URL)
        pass

    def __end_point_buttons(self):
        response = self.web_scrapping_request.do('/')
        end_points: list = []
        html_content = response.text
        soup = BeautifulSoup(html_content, "html.parser")
        buttons = soup.find_all("button", {"class": "btn_opt"})

        for button in buttons:
            value = button.get("value")
            end_points.append(value)

        return end_points                    

    def get_content_page(self):
        # end_points = self.__end_point_buttons()
        # end_points.pop(0)
        # end_points.pop(len(end_points) - 1)
        end_points: list = [1]
        data: list = []

        for end_point in end_points:
            # response =  WebScrappingRequest(BASE_URL).do(f"?opcao={end_point}")
            # html_content = response
            html_content = self.web_scrapping_request.do(f"opcao={end_point}")
            soup = BeautifulSoup(html_content, "html.parser")
            buttons = soup.find_all("button", {"class": "btn_sopt"})

            if len(buttons):
                end_points_subopcoes = [end_point.get("value") for end_point in buttons]
                for end_point_subopcao in end_points_subopcoes:
                    # response_subopcao = WebScrappingRequest(BASE_URL).do(
                    #     f"?subopcao={end_point_subopcao}&opcao={end_point}"
                    # )
                    # html_content_subopcao = response_subopcao
                    html_content_subopcao = self.web_scrapping_request.do(f"subopcao={end_point_subopcao}&opcao={end_point}")
                    soup_subopcao = BeautifulSoup(html_content_subopcao, "html.parser")
                    table = ExtractDataTable(soup_subopcao).do()
                    data.append(table.to_json(orient="records", force_ascii=False))
            else:
                table = ExtractDataTable(soup).do()
                # table.to_json('app/data/teste.txt',orient="records", force_ascii=False)
                data.append(table.to_json(orient="records", force_ascii=False))
        
        return data
                