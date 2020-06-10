from translate import Translator ## imports

setthing = 10
translator= Translator(to_lang="fr") ## initiating the translation
print("Start typing")
while setthing == 10: ## infinite loop
  totrans = input("") ## this takes in the text and stuff
  print(translator.translate(totrans)) ## it translates then prints without being in a variable
