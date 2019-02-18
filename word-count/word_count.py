import re

def word_count(phrase):
  replaced = re.sub('[.|:]', '', phrase.lower())
  return {word: len(re.findall(word, re.escape(replaced))) for word in re.split('\s|\,|\\n', replaced)}
