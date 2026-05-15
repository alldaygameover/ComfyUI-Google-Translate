# ComfyUI-Google-Translate

A ComfyUI custom node for translating text using Google Translate API.

## Features

- Translate text to multiple languages
- Automatic source language detection
- Simple dropdown interface for target language selection
- Supports 14 languages including Chinese, Japanese, Korean, and European languages

## Installation

1. Clone or download this repository into your ComfyUI custom_nodes directory:
   ```
   cd ComfyUI/custom_nodes
   git clone https://github.com/alldaygameover/ComfyUI-Google-Translate.git
   ```

2. Install the required dependencies:
   ```bash
   cd ComfyUI-Google-Translate
   pip install -r requirements.txt
   ```

3. Restart ComfyUI to load the new node.

## Usage

1. Add the "Translate Text" node to your workflow (found under "Text/Translate" category)
2. Connect your text input to the "text" field
3. Select your desired target language from the dropdown
4. The node will automatically detect the source language and translate the text

## Supported Languages

- 中文 (Simplified Chinese)
- 繁體中文 (Traditional Chinese)
- English
- 日本語 (Japanese)
- 한국어 (Korean)
- fr (French)
- es (Spanish)
- de (German)
- it (Italian)
- pt (Portuguese)
- ru (Russian)
- ar (Arabic)
- hi (Hindi)
- th (Thai)

## Node Inputs

- **text**: The text you want to translate (multiline string)
- **target_language**: Dropdown selection of target language

## Node Outputs

- **translated_text**: The translated text in the selected language

## Notes

- Source language is automatically detected
- Uses Google's unofficial translate API
- Requires internet connection for translations
- No API key required (uses public Google Translate endpoint)

## License

MIT License