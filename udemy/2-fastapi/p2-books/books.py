from fastapi import FastAPI, Body

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Auth one', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Auth Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Auth Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Auth Four', 'category': 'history'},
    {'title': 'Title Five', 'author': 'Auth Five', 'category': 'fiction'},
    {'title': 'Title Six', 'author': 'Auth Three', 'category': 'fiction'}
]

@app.get('/books')
async def read_all_books():
    return BOOKS