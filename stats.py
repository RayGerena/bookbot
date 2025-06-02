def get_book_text(filepath):
  with open(filepath) as f:
    file_contents = f.read()
  return file_contents

def word_count(book_text):
  words = book_text.split()
  return len(words)
  

def character_count(book_text):
  book_text = book_text.lower()
  char_count = {}
  for char in book_text:
    if char in char_count:
      char_count[char] += 1
    else:
      char_count[char] = 1
  return char_count

def sort_on(dict):
  return dict["num"]

def character_count_sorted(book_text):
  char_count = character_count(book_text)
  character_count_list = [{'char': c, 'num': n} for c, n in char_count.items()]
  character_count_list.sort(reverse=True, key=sort_on)
  return character_count_list
