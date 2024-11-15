from typing import Optional
import requests
try:
    from .supported_languages import SUPPORTED_LANGUAGES
except ImportError:
    from supported_languages import SUPPORTED_LANGUAGES

class SimpleTranslate:
    def __init__(self):
        self.__lingva_url: str = "https://lingva.ml"

    @staticmethod
    def get_supported_languages():
        return SUPPORTED_LANGUAGES

    def __lingva_translate(self, text: str, target_language: str, source_language: Optional[str] = "en"):
        url = f"{self.__lingva_url}/api/v1/{target_language}/{source_language}/{text}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            response_data = response.json()

            return response_data.get("translation", "")
        except requests.RequestException as error:
            print(f"Request failed {error}")
            return ""

    def translate(self, text: str, target_language: str, source_language: Optional[str] = "en") -> str:
        return self.__lingva_translate(text, target_language, source_language)