def main():
	book_path = "books/frankenstein.txt"
	text = get_book_text(book_path)
	count = count_words(text)
	chars = count_chars(text)
	char_report = sorted_count(chars)
	print(f"--- Begin report of {book_path} ---")
	print(f"The number of words in this book is {count}.")
	for character in char_report:
		print(f"The '{character}' character was found {char_report[character]} in the book.")

def get_book_text(path):
	with open(path) as f:
		return f.read()

def count_words(text):
	word_count = text.split()
	return len(word_count)

def count_chars(text):
	lowercase_text = text.lower()
	character_counts = {}
	for count in lowercase_text:
		if count not in character_counts and count.isalpha():
			character_counts[count] = 1
		elif count.isalpha():
			character_counts[count] +=1
	return character_counts

def sorted_count(chars):
	sorted_chars = sorted(chars.items(), key=lambda x: x[1], reverse=True)
	return dict(sorted_chars)


	
main()

