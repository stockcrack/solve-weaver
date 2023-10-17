import requests

def fetch_words_from_url(url):
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.text.splitlines()

def valid_word(word):
    return len(word) == 4 and all('a' <= char <= 'z' for char in word)

def filter_four_letter_words(words):
    return [word for word in words if valid_word(word)]

def save_to_file(words, filename):
    with open(filename, 'w') as f:
        for word in words:
            f.write(word + '\n')

def main():
    url = "https://raw.githubusercontent.com/dwyl/english-words/master/words.txt"
    all_words = fetch_words_from_url(url)
    four_letter_words = filter_four_letter_words(all_words)
    save_to_file(four_letter_words, "four_letter_words.txt")
    print(f"Saved {len(four_letter_words)} four-letter words to 'four_letter_words.txt'.")

if __name__ == "__main__":
    main()
