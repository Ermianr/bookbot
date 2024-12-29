def main():
  path = "books/frankenstein.txt"
  book = get_book_text(path)
  number_words = get_word_text(book)
  number_chars = get_chars_text(book)
  print("--- Begin report of books/frankenstein.txt ---\n")
  print(f"{number_words} words found in the document\n")
  print(number_chars)
  print("--- End report --")

def get_word_text(text):
  words = text.split()
  return len(words)

def get_chars_text(text):
  chars = {}
  full_text = ""
  for c in text:
    c = c.lower()
    if c in chars:
      chars[c] += 1
    else:
      chars[c] = 1
  sorted_dict = dict(sorted(chars.items()))
  for key, value in sorted_dict.items():
    if key.isalpha():
      full_text += f"The '{key}' character was found {value} times\n"
  return full_text

def get_book_text(path):
  with open(path) as f:
    return f.read()

main()