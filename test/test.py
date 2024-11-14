import pytest
from translator import MultiLanguageTranslator

translator = MultiLanguageTranslator()

def test_translation_uz_to_en():
    translated_text = translator.translate("salom", "en", "uz")
    assert translated_text == "hello"

def test_translation_en_to_uz():
    translated_text = translator.translate("how are you", "uz", "en")
    assert translated_text == "qalaysiz"