from requests import get, RequestException
from file.manager_files import ManagerFiles
import requests

class WebScrappingRequest:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def do(self, end_point: str) -> str:
        try:
            url = f"{self.base_url}{end_point}"
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except RequestException as e:
            raise RuntimeError(f"Error searching for url: {url}") from e
