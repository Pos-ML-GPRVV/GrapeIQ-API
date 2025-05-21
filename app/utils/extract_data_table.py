from bs4 import BeautifulSoup 
from pandas import DataFrame

class ExtractDataTable:
    def __init__(self, data: BeautifulSoup):
        self.data = data
        pass
    
    def do(self) -> DataFrame:
        table = self.data.find("table", {"class": "tb_base tb_dados"})
        if table is None:
            return DataFrame()
        rows = table.find_all("tr")
        data_df: list = []
        current_item = None
        has_class_tb_item = [True for row in rows if row.find("td",{"class": "tb_item"})]
        if True in has_class_tb_item:
            for row in rows:
                cells = row.find_all(["th","td"])
                cell_text = [[cell.get_text(strip=True), cell.get("class")] for cell in cells]
                text, value = cell_text
                item, class_item = text
                value_item, _ = value
                if not class_item:
                    continue
                
                if class_item and "tb_item" in class_item:
                    current_item = item
                
                data_df.append([current_item, item, value_item])
            
            df = DataFrame(data_df, columns=["Item", "SubItem", "Quantidade"])
            return df
        else:
            for row in rows:
                cells = row.find_all(["th","td"])
                cell_text = [cell.get_text(strip=True) for cell in cells]
                data_df.append(cell_text)
            df = DataFrame(data_df[1:], columns=data_df[0])
            return df