

def fetch_words_from_url(url):
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.text.splitlines()

def valid_word(word, l):
    return len(word) == l and all('a' <= char <= 'z' for char in word)

def filter_four_letter_words(words):
    return [word for word in words if valid_word(word, 4)]

def save_to_file(words, filename):
    with open(filename, 'w') as f:
        for word in words:
            f.write(word + '\n')

def main():
    # url = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"
    # all_words = fetch_words_from_url(url)
    # four_letter_words = filter_four_letter_words(all_words)
    # save_to_file(four_letter_words, "four_letter_words.txt")
    count4 = 0
    count5 = 0
    #input_file = "words_alpha.txt"
    input_file = "twl06.txt"  # This is the file used by the actual game, should avoid needing excluded words...
    output_file4 = "four_letter_words.txt"
    output_file5 = "five_letter_words.txt"
    with open(input_file, "r") as i_f:
        with open(output_file4, "w") as o_f4:
            with open (output_file5, "w") as o_f5:
                for line in i_f:
                    word = line.strip()
                    if valid_word(word, 4):
                        o_f4.write(word + "\n")
                        count4 = count4 + 1
                    if valid_word(word, 5):
                        o_f5.write(word + "\n")
                        count5 = count5 + 1
    print(f"Saved {count4} 4 letter and {count5} 5-letter words from '{input_file}' to '{output_file4}' and '{output_file5}'.")

if __name__ == "__main__":
    main()
