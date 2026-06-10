from googletrans import Translator

translator = Translator()

text = input("Enter text: ")
translated = translator.translate(text, dest='hi')

print("Translated:", translated.text)
