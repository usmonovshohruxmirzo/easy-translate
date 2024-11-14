from typing import Optional
import requests

class EasyTranslate:
    def __init__(self, lingva_url: str = "https://lingva.ml"):
        self.lingva_url = lingva_url

    def lingva_translate(self, text: str, target_language: str, source_language: Optional[str] = "en"):
        url = f"{self.lingva_url}/api/v1/{source_language}/{target_language}/{text}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            response_data = response.json()

            return response_data.get("translation", "")
        except requests.RequestException as error:
            print(f"Request failed {error}")
            return ""

    def translate(self, text: str, target_language: str, source_language: Optional[str] = "en") -> str:
        return self.lingva_translate(text, target_language, source_language)