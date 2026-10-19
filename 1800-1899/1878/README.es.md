# 1878. El cubo de Rubinchik

[Timus 1878](https://acm.timus.ru/problem.aspx?space=1&num=1878) · dificultad 219 · implementation

Problema original de Denis Mukhametianov, del Concurso Regional Escolar de Programación de los Urales 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un rompecabezas consta de cuatro capas transparentes de 4 × 4 en un
eje común. Cada capa tiene cuatro cuadritos de color, uno de cada uno
de cuatro colores, colocados de modo que un cuarto de vuelta de la capa
lleva cada uno al cuadrante siguiente. Los cuatro cuadritos de cada capa
forman una órbita de ese giro. Todas las capas comparten el mismo orden
cíclico de colores en sentido horario, salvo rotación, como en el
[diagrama original de las capas](https://acm.timus.ru/image/get.aspx/a394d0eb-f9d5-4bc2-846a-74ef972e9e4b).
Vistas desde arriba, las capas
llenan la cuadrícula 4 × 4. Está resuelto cuando cada cuadrante de
2 × 2 es de un solo color. Un movimiento gira una capa 90° en cualquier
sentido. Dada la vista desde arriba, hay que hallar el menor número de
movimientos que lo resuelve.

## Entrada

Cuatro líneas de cuatro colores de 1 a 4: la vista desde arriba.

## Salida

El menor número de movimientos.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 1 2 3
1 1 2 2
4 4 3 3
1 4 3 4
```

Salida:

```
1
```

## Solución

Todas las capas comparten el mismo orden cíclico de colores, por lo que
alinear sus cuadritos de color 1 también alinea los demás colores.
Cada capa tiene exactamente un cuadrito de color 1, y su cuadrante
indica la orientación de la capa. Se numeran los cuadrantes en el orden
en que un cuarto de vuelta lleva un cuadrito por ellos (arriba a la
izquierda, arriba a la derecha, abajo a la derecha, abajo a la
izquierda). Está resuelto cuando los cuatro cuadritos de color 1 están
en el mismo cuadrante t. Una capa cuyo cuadrito está en el cuadrante p
necesita min(d, 4 − d) movimientos, con d = (p − t) mod 4. Se prueban
los cuatro t y se toma el más barato. `O(1)`.

En el ejemplo tres cuadritos de color 1 están arriba a la izquierda y
uno abajo a la izquierda, a un cuarto de vuelta: un movimiento.

Trampas:

- alinear solo el color 1 depende del orden cíclico común de los colores
  (como en la prueba 01); tener cada color una vez por capa no basta;
- en el estado resuelto el color 1 puede estar en cualquier cuadrante:
  el cubo puede quedar girado entero;
- una capa a media vuelta cuesta dos movimientos gire hacia donde gire;
- los cuadrantes deben numerarse en círculo, no por filas, para que las
  distancias salgan bien.

La solución en Python coincide con una búsqueda en anchura independiente
mediante giros de las capas físicas en los 1536 estados resolubles,
incluidas todas las correspondencias entre números y colores.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1878_implementation.cpp](1878_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.015 s | 128 KB |
| [1878_implementation.go](1878_implementation.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.031 s | 1084 KB |
| [1878_implementation.java](1878_implementation.java) | Java 1.8 | implementation | O(1) | AC | 0.140 s | 1668 KB |
| [1878_implementation.py](1878_implementation.py) | Python 3.12 x64 | implementation | O(1) | AC | 0.109 s | 420 KB |
| [1878_implementation.rs](1878_implementation.rs) | Rust 1.75 x64 | implementation | O(1) | AC | 0.031 s | 212 KB |
