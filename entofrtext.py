from translate import Translator

setthing = 10
translator= Translator(to_lang="fr")
print("Start typing")
while setthing == 10:
  totrans = input("")
  fullytrans = translator.translate(totrans)
  print(fullytrans)
