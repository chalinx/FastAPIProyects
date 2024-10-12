from typing import Optional
from fastapi import  FastAPI,Path,Query,HTTPException
from pydantic import BaseModel,Field
from starlette import status

from Proyect_FastAPI.Proyect1 import books
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
	published_date: int = Field(gt=1999,lt=2031)
##sd
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

@app.get("/libros", status_code=status.HTTP_200_OK)
async def mostrar_libros():
	return BOOKS

@app.get("/libros/{libro_id}/", status_code=status.HTTP_200_OK)
async def obtener_libro_x_id(libro_id:int = Path(gt=0)):
	for libro in BOOKS:
		if libro.id == libro_id:
			return libro
	raise HTTPException(status_code=404,detail='Item no found')#elementos no encontrado
	
 
@app.get("/libros/rating", status_code=status.HTTP_200_OK)
async def obtener_librox_rating(libro_rating:int = Query(gt=0,lt=6)):
	lib_rating=[]
	for libro in BOOKS:
		if libro.rating == libro_rating:
			lib_rating.append(libro)
	return lib_rating

@app.get("/libros/publicacion", status_code=status.HTTP_200_OK)
async def obtener_libros(publicacion: int = Query(gt=1999,lt=2031)):
	lib_publish=[]
	for libro in BOOKS:
		if libro.published_date==publicacion:
			lib_publish.append(libro)
	return lib_publish

@app.get("/libros/libro/{libro_publish}/")
async def obtener_librox_publish(libro_publish:int):
	for libro in BOOKS:
		if libro.published_date == libro_publish:
			return libro


@app.post("/crear-libro",status_code=status.HTTP_201_CREATED)
async def crear_libro(libro_request: LibroRequest):
	new_libro = Libro(**libro_request.dict())
	print(type(new_libro))
	BOOKS.append(aumentar_Id_libro(new_libro))

@app.put("/libros/actualizar_libro",status_code=status.HTTP_204_NO_CONTENT)
async def actualizar_libro(libro:LibroRequest):
	libro_changed = False
	for i in range(len(BOOKS)):
		if BOOKS[i].id == libro.id:
			BOOKS[i] = Libro(**libro.dict())
			libro_changed = True
	if not libro_changed:
		raise HTTPException(status_code=404,detail="Item not found")


@app.delete("/libros/{eliminar_libro}",status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_librox_id(eliminar_libro: int=Path(gt=0)):
	libro_changed = False
	for i in range(len(BOOKS)):
		if BOOKS[i].id == eliminar_libro:
			BOOKS.pop(i)
			libro_changed = True
			break
	if not libro_changed:
		raise HTTPException(status_code=404,detail="Item not found")



def aumentar_Id_libro(libro:Libro):
	libro.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id+1
	return libro