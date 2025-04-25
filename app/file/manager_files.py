class ManagerFiles:
    def __init__(self):
        pass
    
    def create(data: str, name: str):
        with open(f'app/data/{name}.txt', "w", encoding="utf-8") as file:
            file.write(data)
            
    def read(path:str) -> str:
        with open(path, "r", encoding="utf-8") as file:
            content = file.read()
        return content
