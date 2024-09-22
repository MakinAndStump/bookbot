def main():
	book_path = "books/frankenstein.txt"
	text = get_book_text(book_path)
	count = count_words(text)
	print(text)
	print(f"The number of words in this book is {count}")

def get_book_text(path):
	with open(path) as f:
		return f.read()

def count_words(text):
	word_count = text.split()
	return len(word_count)

main()

