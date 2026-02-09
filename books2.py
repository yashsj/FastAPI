from fastapi import FastAPI, Path, Query,HTTPException
from pydantic import BaseModel,Field
from typing import Optional

app=FastAPI()


class Book:
    id:int
    title:str
    author:str
    description:str
    rating:int
    published_date:int

    def __init__(self, id:int, title:str, author:str, description:str, rating:int, published_date:int):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date

class BookRequest(BaseModel):
    id:Optional[int]=Field(description='ID is not needed on creation',default=None)
    title:str=Field(min_length=3)
    author:str=Field(min_length=1)
    description:str=Field(min_length=3,max_length=100)
    rating:int=Field(gt=-1,lt=6)
    published_date:int=Field(gt=0,lt=2026)

    model_config = {
        "json_schema_extra":{
            "example":{
                "title":"A new book",
                "author":"Eric",
                "description":"A new book",
                "rating":1,
                "published_date":2000
            }
        }
    }



BOOKS =[
    Book(1,"Computer science","Eric","An excellent book",5,2000),
    Book(2,"Computer science-II","Eric Roby","An excellent book and great",5,2011),
    Book(3,"Database","Eric Ling","An okay book",3,2012),
    Book(4,"Data structures","Mathew Linddg","A book that made me cry",2,2005),
    Book(5,"Personality developement","Ash","A great book",4,2004)
]

@app.get("/books")
async def read_books():
    return BOOKS

@app.get("/books/publish/")
async def get_book_by_date(published_date:int=Query(gt=0,lt=2026)):
    books_to_return=[]
    for book in BOOKS:
        if book.published_date == published_date:
            books_to_return.append(book)
    return books_to_return




@app.get("/books/{book_id}")
async def read_book(book_id:int=Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book

    raise HTTPException(status_code=404,detail="Book not found")

@app.get("/books/")
async def get_book_by_rating(rating:int=Query(gt=0,lt=6)):
    books_to_return=[]
    for book in BOOKS:
        if book.rating==rating:
            books_to_return.append(book)
    return books_to_return



@app.put("/books/{book_id}")
async def update_book_by_id(book_id:int,book:BookRequest):
    book_changed=False
    for i in range(len(BOOKS)):
        if book.id == BOOKS[i].id:
            BOOKS[i]=book
            book_changed = True
    if not book_changed:
        raise HTTPException(status_code=404,detail="Book not found")

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
    book_changed=False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i]=book
            book_changed = True
    if not book_changed:
        raise HTTPException(status_code=404,detail="Book not found")


@app.delete("/books/{book_id}")
async def delete_book(book_id:int = Path(gt=0)):
    book_changed=False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            del BOOKS[i]
            book_changed = True
            break
        if not book_changed:
            raise HTTPException(status_code=404,detail="Book not found")



