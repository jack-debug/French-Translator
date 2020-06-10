from translate import Translator ## imports

translator= Translator(to_lang="fr") ## initiating the translation
print("Start typing")
while True: ## infinite loop
  totrans = input("") ## this takes in the text and stuff
  print(translator.translate(totrans)) ## it translates then prints without being in a variable
