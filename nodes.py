import requests


LANGUAGE_ALIASES = {
    "auto": "auto",
    "english": "en",
    "en": "en",
    "chinese": "zh-CN",
    "中文": "zh-CN",
    "简体中文": "zh-CN",
    "繁體中文": "zh-TW",
    "zh": "zh-CN",
    "zh-cn": "zh-CN",
    "zh-tw": "zh-TW",
    "japanese": "ja",
    "日本語": "ja",
    "ja": "ja",
    "korean": "ko",
    "한국어": "ko",
    "ko": "ko",
    "french": "fr",
    "fr": "fr",
    "spanish": "es",
    "es": "es",
    "german": "de",
    "de": "de",
    "italian": "it",
    "it": "it",
    "portuguese": "pt",
    "pt": "pt",
    "russian": "ru",
    "ru": "ru",
    "arabic": "ar",
    "ar": "ar",
    "hindi": "hi",
    "hi": "hi",
    "thai": "th",
    "th": "th",
}


def _normalize_language(language: str) -> str:
    language = str(language or "").strip()
    if not language:
        return "auto"
    normalized = LANGUAGE_ALIASES.get(language.lower(), language)
    return normalized


def _translate_text(text: str, source_language: str, target_language: str) -> str:
    if not isinstance(text, str):
        raise ValueError("Text must be a string.")

    src = _normalize_language(source_language)
    tgt = _normalize_language(target_language)

    if not tgt or tgt == "auto":
        raise ValueError("Target language must be set and cannot be auto.")

    url = "https://translate.googleapis.com/translate_a/single"
    params = {
        "client": "gtx",
        "sl": src,
        "tl": tgt,
        "dt": "t",
        "q": text,
    }

    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()
    result = response.json()

    if not result or not isinstance(result, list):
        raise RuntimeError("Unexpected translation response format.")

    translated_segments = []
    for segment in result[0]:
        if segment and isinstance(segment, list) and segment[0] is not None:
            translated_segments.append(segment[0])

    return "".join(translated_segments).strip()


class TranslateTextNode:
    CATEGORY = "Text/Translate"
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("translated_text",)
    FUNCTION = "translate"
    OUTPUT_NODE = False

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {
                    "multiline": True,
                    "default": "Hello, world!",
                    "placeholder": "Enter text to translate",
                }),
                "target_language": (
                    [
                        "中文",
                        "繁體中文",
                        "English",
                        "日本語",
                        "한국어",
                        "fr",
                        "es",
                        "de",
                        "it",
                        "pt",
                        "ru",
                        "ar",
                        "hi",
                        "th",
                    ],
                ),
            },
        }

    def translate(self, text, target_language):
        try:
            return (_translate_text(text, "auto", target_language),)
        except requests.exceptions.RequestException as exc:
            raise RuntimeError(f"Translation request failed: {exc}") from exc
        except Exception as exc:
            raise RuntimeError(f"Translation failed: {exc}") from exc


NODE_CLASS_MAPPINGS = {
    "Translate Text": TranslateTextNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Translate Text": "Translate Text",
}
