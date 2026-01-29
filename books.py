from fastapi import FastAPI

app = FastAPI()


BOOKS=[
    {'title':'title1','author':'author1'},
    {'title':'title2','author':'author2'},
    {'title':'title3','author':'author2'},
    {'title':'title4','author':'author4'},
    {'title':'title5','author':'author5'},
    {'title':'title6','author':'author6'},
]
@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/mybook")
async def read_my_book():
    return {"book_title": "My fav book"}

@app.get("/books/title/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get("title").casefold() == book_title.casefold():
            return book

# query by author only
@app.get("/books/")
async def read_author(author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("author").casefold() == author.casefold():
            books_to_return.append(book)
    return books_to_return

# author in path + title in query
@app.get("/books/author/{author}")
async def read_author_and_title(author: str, title: str):
    books_to_return = []
    for book in BOOKS:
        if (
            book.get("title").casefold() == title.casefold()
            and book.get("author").casefold() == author.casefold()
        ):
            books_to_return.append(book)
    return books_to_return
