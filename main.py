import sys
from stats import get_book_text, word_count, character_count, character_count_sorted

if len(sys.argv) < 2:
  print("Usage: python3 main.py <path_to_book>")
  sys.exit(1)

filepath = sys.argv[1]

def main():
  book_text = get_book_text(filepath)
  w_count = word_count(book_text)
  cc_sorted = character_count_sorted(book_text)

  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {filepath}...")
  print("----------- Word Count ----------")
  print(f"Found {w_count} total words")
  print("--------- Character Count -------")
  for item in cc_sorted:
    if item["char"].isalpha():
      print(f"{item["char"]}: {item["num"]}")
  print("============= END ===============")


main()
