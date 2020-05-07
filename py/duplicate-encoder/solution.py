def duplicate_encode(word):
  new_word = ''

  for character in word.lower():
    if word.lower().count(character) > 1:
      new_word += (')')
    else:
      new_word += ('(')

  return new_word

print(duplicate_encode("din"))
print(duplicate_encode("Success"))
print(duplicate_encode("(( @"))
print(duplicate_encode('recede'))

# Solution below uses O(n) time complexity, whereas above uses O(n ^ 2) since count() is also O(n)
import collections

def default_dict(word):
  new_word = ''

  d = collections.defaultdict(int)

  for character in word:
    d[character] += 1
  
  for character in word:
    new_word = new_word + ('(' if d[character] == 1 else ')')

  print(new_word)

default_dict('hello')