from fastapi import FastAPI, Query, Path
from enum import Enum
import solve_weaver as sw
from typing import Union, Annotated, Any
from pydantic import BaseModel
import sys
from collections import defaultdict

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []


@app.post("/items/", response_model=Item)
async def create_item(item: Item) -> Any:
    return item


@app.get("/items/", response_model=list[Item])
async def read_items() -> Any:
    return [
        {"name": "Portal Gun", "price": 42.0},
        {"name": "Plumbus", "price": 32.0},
    ]
    
def read_words(words: set, filename: str):
    with open(filename, 'r') as f:
        for line in f:
            words.add(line.strip().lower())
    print(f"Read {len(words)} from {filename}")
    return words

# Create word list
def create_word_graph(words, excluded_words):
    return sw.build_word_graph(words - excluded_words, defaultdict(list))

words4 = read_words(set(), 'four_letter_words.txt')
words5 = read_words(set(), 'five_letter_words.txt')
excluded_words = read_words(set(), 'excluded_words.txt')
word_graph4 = create_word_graph(words4, excluded_words)
print(f"Word_graph4 length is {len(word_graph4)}")
word_graph5 = create_word_graph(words5, excluded_words)
print(f"Word_graph5 length is {len(word_graph5)}")
word_graphs = { 4: word_graph4, 5: word_graph5}

print(f"Python version: {sys.version}")

def getwordladder(start: str, end: str) -> list[str] | None:
    print(f"Going from {start} to {end}")
    if len(start) != len(end):
        print(f"Length of {start} does not match length of {end}")
        return None
    if len(start) == 4:
        print("4 letters")
    elif len(start) == 5:
        print("5 letters")
    else:
        print("Only 4 or 5 letter words accepted at this time.")
        return None

    word_graph = word_graphs[len(start)]
    print(f"Word graph length is {len(word_graph)}")
    path = sw.word_ladder(start, end, word_graph)
    print(f"Path from {start} to {end} is {path}.")
    # return { "result": path }
    return path

@app.get("/wordladder/")
async def getwordladder1(start:Annotated[str, Query(min_length=4, max_length=5, title = "Starting word")], 
                        end:Annotated[str, Query(min_length=4, max_length=5, title = "Target word")]) -> list[str]:
    return getwordladder(start, end)

@app.get("/wordladder/{start}/{end}")
async def getwordladder2(
        start:Annotated[str, Path(min_length=4, max_length=5, title="Starting word")], 
        end:Annotated[str, Path(min_length=4, max_length=5, title="Target word")]):
    return getwordladder(start, end)

@app.get("/exclude/{word}")
async def exclude_word(word: Annotated[str, Path(min_length=4, max_length=5, title="Excluded word")]):
    if word in excluded_words:
        print(f"Word {word} already excluded.")
        return None
    else:
        print(f"Excluding {word}")
        excluded_words.add(word)
        word_graph4 = sw.build_word_graph(words4 - excluded_words, defaultdict(list))
        word_graph5 = sw.build_word_graph(words5 - excluded_words, defaultdict(list))
        word_graphs[4] = word_graph4
        word_graphs[5] = word_graph5
        with(open("excluded_words.txt",'a')) as f:
            print(word, file=f)
        return word
    




