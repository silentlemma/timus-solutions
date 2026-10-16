# 1802. Rompecabezas de cubo

[Timus 1802](https://acm.timus.ru/problem.aspx?space=1&num=1802) · dificultad 2070 · backtracking

Problema original de Stanislav Vasilyev, de la subregión oriental del NEERC 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Seis cuadrados planos de n × n están barnizados por un lado; por el
otro, cada celda lleva una columna de cubos unitarios de altura 0 a n.
Las alturas suman n³. Girando las piezas libremente, montar un cubo de
n × n × n barnizado por todas partes, o indicar que no se puede.

## Entrada

n (2 ≤ n ≤ 20) y luego las seis piezas, cada una como n filas de n
alturas.

## Salida

"No", o "Yes" y luego n capas de abajo arriba, cada una con n filas de
atrás adelante de n números de pieza de 1 a 6, de izquierda a derecha.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
0 0 0
1 0 1
1 2 0
1 0 0
1 1 1
0 0 0
0 2 1
1 0 0
0 0 0
0 1 0
0 0 0
0 2 1
1 0 0
0 0 1
0 2 1
0 0 1
0 2 1
1 0 0
```

Salida:

```
Yes
3 4 4
1 4 1
1 1 5
3 3 2
5 6 2
5 1 2
6 4 2
3 6 6
5 5 6
```

### Ejemplo 2

Entrada:

```
3
0 0 0
0 3 0
0 0 0
2 0 0
0 0 0
0 0 0
0 0 2
0 0 0
0 0 0
2 0 0
0 0 0
0 0 0
0 0 2
0 0 0
0 0 0
2 1 2
2 1 2
2 2 2
```

Salida:

```
No
```

## Solución

Con el barniz hacia fuera, una pieza se apoya en una cara del cubo con
las columnas hacia dentro, girada de una de cuatro formas. Las
colocaciones reflejadas son imposibles, así que las seis caras se fijan
como la cara inferior movida por rotaciones del cubo. Una pieza en una
cara con un giro ocupa un conjunto conocido de celdas, guardado como
máscara de bits, y las máscaras iguales de una pieza simétrica se
cuentan una vez. Como se puede girar el cubo entero, la pieza mayor va
abajo sin girar. Después una búsqueda con vuelta atrás llena las demás
caras, tomando siempre la cara con menos piezas y giros que no pisan
celdas ya ocupadas, y retrocediendo enseguida cuando una cara no tiene
ninguno. Como los volúmenes suman n³, seis piezas sin solaparse llenan
el cubo. Hay como mucho 5! · 4⁵ asignaciones, y la poda mantiene la
búsqueda diminuta. `O(n³)` por paso.

En el primer ejemplo cada celda del cubo de 3 × 3 × 3 recibe el número
de su pieza; en el segundo las piezas no encajan de ningún modo.

Trampas:

- una pieza no se puede voltear: el barniz quedaría dentro;
- las piezas simétricas dan colocaciones iguales, que solo frenan la
  búsqueda;
- las piezas de altura cero también necesitan su propia cara.

El verificador exige que las celdas de cada pieza sean esa pieza en
alguna cara con uno de sus cuatro giros, con una cara distinta para
cada pieza, y la respuesta dada del primer ejemplo lo supera. Las
respuestas coinciden con una implementación aceptada independiente en
cubos cortados al azar en seis piezas, con y sin una celda movida entre
piezas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1802_backtracking.cpp](1802_backtracking.cpp) | G++ 13.2 x64 | backtracking | O(n^3) per search step | AC | 0.031 s | 696 KB |
| [1802_backtracking.go](1802_backtracking.go) | Go 1.14 x64 | backtracking | O(n^3) per search step | AC | 0.062 s | 1484 KB |
| [1802_backtracking.java](1802_backtracking.java) | Java 1.8 | backtracking | O(n^3) per search step | AC | 0.140 s | 5416 KB |
| [1802_backtracking.py](1802_backtracking.py) | Python 3.12 x64 | backtracking | O(n^3) per search step | AC | 0.234 s | 1152 KB |
| [1802_backtracking.rs](1802_backtracking.rs) | Rust 1.75 x64 | backtracking | O(n^3) per search step | AC | 0.031 s | 404 KB |
