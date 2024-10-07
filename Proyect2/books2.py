from typing_extensions import Optional
from fastapi import  Body, FastAPI
from pydantic import BaseModel,Field
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


class LibroRequest(BaseModel):
	id: Optional[int] = Field(description="ID no es necesario crearlo",default=None)
	title: str = Field(min_length=3)
	author: str = Field(min_length=1)
	description: str = Field(min_length=1,max_length=100)
	rating: int = Field(gt=0,lt=6)#entre <0,6> entero = [1,5]
	published_date: int

	model_config = {
		"json_schema_extra":{
			"example":{
				"title": "A new book",
				"author": "codingwithroby",
				"description": "A new description of a book",
				"rating":5,
				"published_date":2000
			}
		}
	}




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


@app.post("/crear-libro")
async def crear_libro(libro_request: LibroRequest):
	new_libro = Libro(**libro_request.model_dump())
	print(type(new_libro))
	BOOKS.append(aumentar_Id_libro(new_libro))


def aumentar_Id_libro(libro:Libro):
	libro.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id+1
	return libro