from fastapi import FastAPI, Query, Path
from enum import Enum
import solve_weaver as sw
from typing import Union, Annotated
from pydantic import BaseModel


app = FastAPI()

@app.get("/items/")
async def read_items(q: Annotated[Union[str, None], Query(min_length=3, max_length=50)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# Create word list
def create_word_graph():
    words = set()
    excluded_words = set()
    with open('four_letter_words.txt', 'r') as f:
        for line in f:
            words.add(line.strip().lower())
    try:
        with open("excluded_words.txt") as f:
            for line in f:
                excluded_words.add(line.strip().lower())
    except FileNotFoundError:
        pass
    print(f"Read {len(words)} words and {len(excluded_words)} excluded words")
    return sw.build_word_graph(words - excluded_words)


    
word_graph = create_word_graph()

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





