from fastapi import Body, FastAPI


app = FastAPI()



BOOKS=[
    {'title':'title1','author':'author1','category':'science'},
    {'title':'title2','author':'author2','category':'history'},
    {'title':'title3','author':'author3','category':'math'},
    {'title':'title3','author':'author2','category':'math'},
    {'title':'title4','author':'author4','category':'history'},
    {'title':'title5','author':'author5','category':'math'},
    {'title':'title5','author':'author5','category':'history'},
    {'title':'title6','author':'author6','category':'math'}
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


@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)


@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i]["title"] = updated_book


@app.delete("/books/delete_book")
async def delete_book(book_title:str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            del BOOKS[i]
            break

