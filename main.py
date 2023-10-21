from fastapi import FastAPI, Query, Path
from enum import Enum
import solve_weaver as sw
from typing import Union, Annotated
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results
    
def read_words(words: set, filename: str):
    with open(filename, 'r') as f:
        for line in f:
            words.add(line.strip().lower())
    print(f"Read {len(words)} from {filename}")
    return words

# Create word list
def create_word_graph(words, excluded_words):
    return sw.build_word_graph(words - excluded_words)

words = read_words(set(), 'four_letter_words.txt')
excluded_words = read_words(set(), 'excluded_words.txt')
word_graph = create_word_graph(words, excluded_words)

@app.get("/wordladder/")
async def getwordladder(start:Annotated[str, Query(min_length=4, max_length=4, title = "Starting word")], 
                        end:Annotated[str, Query(min_length=4, max_length=4, title = "Target word")]):
    print(f"Going from {start} to {end}")
    path = sw.word_ladder(start, end, word_graph)
    print(f"Path from {start} to {end} is {path}")
    return { "result": path }

@app.get("/wordladder/{start}/{end}")
async def getwordladder2(
        start:Annotated[str, Path(min_length=4, max_length=4, title="Starting word")], 
        end:Annotated[str, Path(min_length=4, max_length=4, title="Target word")]):
    print(f"Going from {start} to {end}")
    path = sw.word_ladder(start, end, word_graph)
    print(f"Path from {start} to {end} is {path}")
    return { "result": path }

@app.get("/exclude/{word}")
async def exclude_word(word: Annotated[str, Path(min_length=4, max_length=4, title="Excluded word")]):
    if word in excluded_words:
        print(f"Word {word} already excluded.")
        return None
    else:
        print(f"Excluding {word}")
        excluded_words.add(word)
        sw.build_word_graph(words - excluded_words)
        with(open("excluded_words.txt",'a')) as f:
            print(word, file=f)
        return word
    




