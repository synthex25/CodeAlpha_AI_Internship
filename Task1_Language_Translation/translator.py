from googletrans import Translator, LANGUAGES
from gtts import gTTS
import os

translator = Translator()

print("=== AI Language Translation Tool ===\n")

# Display available languages
lang_list = list(LANGUAGES.items())

for i, (code, name) in enumerate(lang_list, start=1):
    print(f"{i}. {name.title()}")

choice = int(input("\nChoose target language number: "))
text = input("Enter text to translate: ")

if 1 <= choice <= len(lang_list):
    lang_code = lang_list[choice - 1][0]
    lang_name = lang_list[choice - 1][1]

    translated = translator.translate(text, dest=lang_code)

    print("\n" + "-" * 40)
    print(f"Translated Text ({lang_name.title()}):\n")
    print(translated.text)
    print("-" * 40)

    speak = input("\nDo you want to hear the translation? (y/n): ")
    if speak.lower() == "y":
        tts = gTTS(translated.text, lang=lang_code)
        tts.save("output.mp3")
        os.system("start output.mp3")

else:
    print("Invalid language selection.")
