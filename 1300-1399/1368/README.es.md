# 1368. La cabra en el huerto 3

[Timus 1368](https://acm.timus.ru/problem.aspx?space=1&num=1368) · dificultad 2449 · geometry

Problema original de Alexey Lakhtin, del Noveno Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 19–24 de abril de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una cabra está en la celda (0, 0) de una cuadrícula infinita y solo se
mueve arriba, abajo, a la izquierda y a la derecha. Se pueden poner
secciones de valla en celdas sueltas. Hay que encerrar a la cabra en una
zona de exactamente K celdas, 1 ≤ K ≤ 10⁶, con el menor número de
secciones, e imprimir su número y las secciones en el orden de un paseo
alrededor de la zona.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

El número K.

## Salida

N, luego N líneas de coordenadas de celdas de la valla, en orden alrededor
de la zona.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
```

Salida:

```
7
-1 0
0 1
1 2
2 1
2 0
1 -1
0 -1
```

## Solución

La valla de una zona R debe ocupar cada celda vecina de R por un lado, y
esas celdas ya bastan para encerrar R, así que hay que elegir K celdas
conexas con el menor número de vecinas por lado. Las mejores formas son
rombos o sus variantes, y ningún grupo de K celdas tiene menos de ⌈√(8K − 4)⌉ + 2
vecinas: 4 para una celda, 4r + 4 para el rombo de radio r con
2r² + 2r + 1 celdas.

La zona se construye por filas. Si los extremos de filas consecutivas se
mueven a lo sumo una celda, la valla es una celda a la izquierda y otra
a la derecha de cada fila más las celdas bajo la primera fila y sobre la
última: con H filas tiene 2H + w₁ + w_H celdas. Un rombo crece una celda
por cada extremo en cada fila hasta su mitad y luego se estrecha. Se fija
el tamaño de la valla en la cota inferior y se prueban anchos 1 o 2 para
la primera y la última fila. Eso fija H. Las filas más anchas posibles
son min(w₁ + 2i, w_H + 2(H − 1 − i)). Se recortan al nivel más bajo que
aún da cabida a K celdas, hallado por búsqueda binaria, y después se
quita una celda a algunas filas interiores de ese nivel hasta que quedan
exactamente K. Si ninguna opción sirve, el tamaño de la valla sube en
uno; para todos los K probados se alcanzó la propia cota.

Luego se colocan las filas, moviendo primero el extremo izquierdo cuando
una fila se estrecha, y se enumera la valla alrededor de la zona: por
abajo, hacia arriba por la derecha, de vuelta por arriba y hacia abajo
por la izquierda. Las secciones consecutivas se tocan por un lado o una
esquina. `O(√K · log K)`.

Detalles a tener en cuenta:

- la valla puede tocarse solo por las esquinas, porque la cabra no se
  mueve en diagonal; una valla que se toca por los lados necesita muchas
  más secciones;
- el cuadrado no es la mejor forma: 1 000 000 de celdas necesitan 2 831
  secciones, frente a 4 000 alrededor de un cuadrado;
- el orden de la salida importa: las celdas van alrededor de la zona.

La construcción se comprobó para todo K hasta 3 000 y para K grandes
rellenando la zona desde (0, 0); la cota se comparó con todos los
poliominós de hasta 14 celdas. Las pruebas se juzgan con un verificador
que hace el mismo relleno y comprueba el tamaño y el orden.

## Notas por lenguaje

- Las cinco soluciones buscan las mismas formas; Java arma la salida
  antes de conocer la cantidad, y al final imprime la cantidad delante.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1368_geometry.cpp](1368_geometry.cpp) | G++ 13.2 x64 | geometry | O(√K·log K) | AC | 0.015 s | 256 KB |
| [1368_geometry.go](1368_geometry.go) | Go 1.14 x64 | geometry | O(√K·log K) | AC | 0.031 s | 1512 KB |
| [1368_geometry.java](1368_geometry.java) | Java 1.8 | geometry | O(√K·log K) | AC | 0.109 s | 1956 KB |
| [1368_geometry.py](1368_geometry.py) | Python 3.12 x64 | geometry | O(√K·log K) | AC | 0.093 s | 1500 KB |
| [1368_geometry.rs](1368_geometry.rs) | Rust 1.75 x64 | geometry | O(√K·log K) | AC | 0.015 s | 268 KB |
