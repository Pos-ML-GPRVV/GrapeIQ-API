from requests import get, RequestException
from file.manager_files import ManagerFiles

class WebScrappingRequest:
    def __init__(self, base_url: str):
        self.base_url = base_url
        pass
    
    def do(self, end_point: str):
        url = f"{self.base_url}?{end_point}"
        try:
            response = get(url)
            response.raise_for_status()
        except RequestException as e:
            content_file: str = ManagerFiles.read(f"app/data/{end_point}.txt")
            if not content_file:
                raise RuntimeError(f"Error for request {e}") from e
            return content_file

        if not hasattr(self, '_response'):
            self._response = response
            return response.text
        return response.text