### Herencia y polimorfismo

base_geometry.py: Define una clase base para figuras geométricas, con un método de área no implementado y otro que valida enteros positivos, lanzando excepciones cuando corresponde.

- `1-rectangle.py`: Define una clase que hereda de BaseGeometry, valida el ancho y la altura como enteros positivos y los almacena como atributos privados.

- `2-rectangle.py`: Define un rectángulo que hereda de BaseGeometry, valida sus dimensiones, calcula y devuelve el área y proporciona una representación textual del objeto.

- `1-square.py`: Define un cuadrado que hereda de Rectangle, valida su tamaño como entero positivo, calcula y devuelve su área y reutiliza la representación textual de la clase padre.
