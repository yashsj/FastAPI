from fastapi import FastAPI

app = FastAPI()


BOOKS=[
    {'title':'title1','author':'author1'},
    {'title':'title2','author':'author2'},
    {'title':'title3','author':'author3'},
    {'title':'title4','author':'author4'},
    {'title':'title5','author':'author5'},
    {'title':'title6','author':'author6'},
]
@app.get("/books")
async  def read_all_books():
    return BOOKS

@app.get("/books/mybook")
async def read_all_books():
    return {'book_title':'My fav book'}

@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold()==book_title.casefold():
            return book



