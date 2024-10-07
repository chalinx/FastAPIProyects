from re import purge
from typing import Self
from fastapi import FastAPI

app = FastAPI()

class Libro:
	id: int
	title: str
	author: str
	description: str
	rating: int
	published_date: int


	def __init__(self,id,title,author,description,rating,published_date):
		self.id = id
		self.title = title
		self.author = author
		self.description = description
		self.rating = rating
		self.published_date = published_date



BOOKS = [
    Libro(1, 'Computer Science Pro', 'codingwithroby', 'A very nice book!', 5, 2030),
    Libro(2, 'Be Fast with FastAPI', 'codingwithroby', 'A great book!', 5, 2030),
    Libro(3, 'Master Endpoints', 'codingwithroby', 'A awesome book!', 5, 2029),
    Libro(4, 'HP1', 'Author 1', 'Book Description', 2, 2028),
    Libro(5, 'HP2', 'Author 2', 'Book Description', 3, 2027),
    Libro(6, 'HP3', 'Author 3', 'Book Description', 1, 2026)
]

@app.get("/libros")
async def mostrar_libros():
	return BOOKS