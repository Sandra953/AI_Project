 # Lista de productos de ejemplo; cada producto tiene nombre, categoría y precio.
productos = [
	{"nombre": "Cuaderno", "categoria": "papelería", "precio": 2500},
	{"nombre": "Lápiz", "categoria": "papelería", "precio": 500},
	{"nombre": "Audífonos", "categoria": "tecnología", "precio": 12000},
	{"nombre": "Mouse", "categoria": "tecnología", "precio": 8000},
	{"nombre": "Botella de agua", "categoria": "hogar", "precio": 6000},
]

# Solicitamos una categoría y quitamos espacios y diferencias entre mayúsculas.
categoria_buscada = input("Escribe una categoría (papelería, tecnología u hogar): ")
categoria_buscada = categoria_buscada.strip().lower()

# Recorremos los productos y mostramos los que pertenecen a la categoría indicada.
print("\nProductos recomendados:")
hay_recomendaciones = False

for producto in productos:
	if producto["categoria"] == categoria_buscada:
		print(f"- {producto['nombre']} (${producto['precio']})")
		hay_recomendaciones = True

# Si no hubo coincidencias, avisamos al usuario.
if not hay_recomendaciones:
	print("No encontramos productos para esa categoría.")
