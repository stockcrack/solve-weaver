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
with open('four_letter_words.txt', 'r') as f:
    word_list = [word.strip().lower() for word in f.readlines()]

print("Read " + str(len(word_list)) + " words.")
    
word_graph = sw.build_word_graph(word_list)

@app.get("/wordladder/")
async def getwordladder(start:str = "", end:str = ""):
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





