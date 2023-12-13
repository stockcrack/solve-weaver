from collections import defaultdict, deque

def build_word_graph(words: set, word_graph = defaultdict(list)):
    word_graph.clear()
    d = defaultdict(list)

    # Populate the dictionary with word families
    for word in words:
        for i in range(len(word)):
            bucket = word[:i] + "_" + word[i+1:]
            d[bucket].append(word)

    # Build the word graph
    for bucket, words in d.items():
        for word1 in words:
            for word2 in words:
                if word1 != word2:
                    word_graph[word1].append(word2)

    return word_graph

def word_ladder(start, target, word_graph):
    visited = set()
    queue = deque([(start, [start])])

    while queue:
        current_word, path = queue.popleft()

        if current_word == target:
            return path

        for neighbor in word_graph[current_word]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None

def valid_word(word):
    return (len(word) == 4 or len(word) == 5) and all('a' <= char <= 'z' for char in word)

def user_input_word_ladder(l = 4):
    word_file = 'four_letter_words.txt' if (l == 4) else 'five_letter_words.txt'
    with open(word_file, 'r') as f:
        word_list = [word.strip().lower() for word in f.readlines()]

    print("Read " + str(len(word_list)) + " words.")
    
    word_graph = build_word_graph(word_list)
    # print(word_graph)

    start = input("Enter the starting word: ").strip().lower()
    target = input("Enter the target word: ").strip().lower()

    # Ensure the provided words are valid
    if not (valid_word(start) and valid_word(target)):
        print("Please ensure both words are valid four-letter words containing only lowercase letters a to z.")
        return

    path = word_ladder(start, target, word_graph)

    if path:
        print(" -> ".join(path))
    else:
        print(f"No path found from {start} to {target}.")


def main():
    # Simulating the user input for demonstration purposes
    user_input_word_ladder()
    
if __name__ == "__main__":
    main()
