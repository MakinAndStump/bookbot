def main():
	book_path = "books/frankenstein.txt"
	text = get_book_text(book_path)
	count = count_words(book_path)
	print(text)
	count(text)

def get_book_text(path):
	with open(path) as f:
		return f.read()

def count_words(path):
	with open(path) as t:
		
		word_count = len(t.read().split())
		return word_count

main()

