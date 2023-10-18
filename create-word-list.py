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
    # url = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"
    # all_words = fetch_words_from_url(url)
    # four_letter_words = filter_four_letter_words(all_words)
    # save_to_file(four_letter_words, "four_letter_words.txt")
    count = 0
    input_file = "words_alpha.txt"
    output_file = "four_letter_words.txt"
    with open(input_file, "r") as i_f:
        with open(output_file, "w") as o_f:
            for line in i_f:
                word = line.strip()
                if valid_word(word):
                    o_f.write(word + "\n")
                    count = count + 1
    print(f"Saved {count} four-letter words from '{input_file}' to '{output_file}'.")

if __name__ == "__main__":
    main()
