"""
функция позволяет заменить буквы на заглавные
"""
def high_word(word):
  return word.upper()

"""
Make first letters high
"""
def title_word():
  new_word = str(high_word(word))
  print (new_word.title())

word = input("Введите слово!")
print (high_word(word))

title_word()

