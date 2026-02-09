from fastapi import FastAPI
from pydantic import BaseModel,Field
from typing import Optional

app=FastAPI()


class Book:
    id:int
    title:str
    author:str
    description:str
    rating:int

    def __init__(self, id:int, title:str, author:str, description:str, rating:int):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

class BookRequest(BaseModel):
    id:Optional[int]=Field(description='ID is not needed on creation',default=None)
    title:str=Field(min_length=3)
    author:str=Field(min_length=1)
    description:str=Field(min_length=3,max_length=100)
    rating:int=Field(gt=-1,lt=6)

    model_config = {
        "json_schema_extra":{
            "example":{
                "title":"A new book",
                "author":"Eric",
                "description":"A new book",
                "rating":1,
            }
        }
    }



BOOKS =[
    Book(1,"Computer science","Eric","An excellent book",5),
    Book(2,"Computer science-II","Eric Roby","An excellent book and great",5),
    Book(3,"Database","Eric Ling","An okay book",3),
    Book(4,"Data structures","Mathew Linddg","A book that made me cry",2),
    Book(5,"Personality developement","Ash","A great book",4)
]

@app.get("/books")
async def read_books():
    return BOOKS


@app.get("/books/{book_id}")
async def read_book(book_id:int):
    for book in BOOKS:
        if book.id == book_id:
            return book

@app.get("/books/")
async def get_book_by_rating(rating:int):
    books_to_return=[]
    for book in BOOKS:
        if book.rating==rating:
            books_to_return.append(book)
    return books_to_return



@app.put("/books/{book_id}")
async def update_book_by_id(book_id:int,book:BookRequest):
    for i in range(len(BOOKS)):
        if book.id == BOOKS[i].id:
            BOOKS[i]=book

@app.post("/books/create_book")
async def create_book(book_request:BookRequest):
    new_book=Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))

def find_book_id(book:Book):
    if len(BOOKS)>0:
        book.id=BOOKS[-1].id+1
    else:
        book.id=1
    return book



@app.put('/books/update_books/by_id')
async def update_book_by_body(book:BookRequest):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i]=book





