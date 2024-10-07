from fastapi import FastAPI,Body

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]

@app.get("/api-endpoint")
async def first_api():
    return {"message": "Hello Eric!"}

@app.get("/libros")
async def mostrar_libros():
    return BOOKS

@app.get("/libros/{libro_titulo}")
async def leer_libro(libro_titulo: str):
	for book in BOOKS:
		title=book.get('title')
		if title and title.casefold() == libro_titulo.casefold():
			return book

@app.get("/libros/")
async def leer_categoria_por_consulta(category:str):
	return_libros = []

	for book in BOOKS:
		categoria = book.get('category')
		if categoria and categoria.casefold() == category.casefold():
			return_libros.append(book)
	return return_libros		

@app.get("/libros/{autor_libros}/")
async def leer_author_categoria_por_consulta(autor_libros: str,category:str):
	return_libros = []

	for book in BOOKS:
		autor=book.get('author')
		categoria=book.get('category')
		if autor and autor.casefold() == autor_libros.casefold() and \
				categoria and categoria.casefold() == category.casefold():
			return_libros.append(book)

	return return_libros

@app.get("/libros/author/{author_libros}")
async def libros_autor(author_libros: str):

	libros=[]
	for book in BOOKS:
		author=book.get('author')
		if author and author.casefold() == author_libros.casefold():
			libros.append(book)
	return libros


@app.post("/libros/crear_libro")
async def crear_libro(new_book = Body()):
	BOOKS.append(new_book)

@app.put("/libros/actualizar_libro")
async def actualizar_libro(actualizar_libro = Body()):
	for i in range(len(BOOKS)):
		libro = BOOKS[i].get('title')
		if libro and libro.casefold() == actualizar_libro.get('title').casefold():
			BOOKS[i]=actualizar_libro


@app.delete("/libros/eliminar_libros/{titulo_libro}")
async def eliminar_libros(titulo_libro):
	for i in range(len(BOOKS)):
		libro = BOOKS[i].get('title')
		if libro and libro.casefold() == titulo_libro.casefold():
			BOOKS.pop(i)
			break










