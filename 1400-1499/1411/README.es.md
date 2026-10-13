# 1411. Caballeros de las 40 islas

[Timus 1411](https://acm.timus.ru/problem.aspx?space=1&num=1411) · dificultad 3171 · constructive

Problema original de Alexander Klepinin, del Campeonato de la Universidad Estatal de los Urales, 29 de octubre de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay una isla en cada nodo de una cuadrícula W × H (1 ≤ W, H ≤ 50). Los
puentes pueden unir islas vecinas en horizontal, vertical o diagonal, y
no pueden cruzarse. Cada isla debe tener exactamente tres puentes, y la
red debe seguir conexa tras destruir cualquier puente. Hay que imprimir
un mapa así, o «Imaginary world» si no existe.

El mapa tiene 2H − 1 líneas de 2W − 1 caracteres: `O` para una isla,
uno de `-|/\` para un puente y un espacio en lo demás.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

W y H.

## Salida

Un mapa o «Imaginary world».

## Ejemplos

### Ejemplo 1

Entrada:

```
8 5
```

Salida:

```
O-O-O-O-O-O O-O
|\| |  \|/|/|/|
O-O O-O O O O O
 \ / /|  /  |/|
O-O O-O-O-O O-O
|\  |    / \  |
O-O O O-O-O O-O
|/ /| |\  |\ \|
O-O-O-O-O-O-O-O
```

## Solución

Cada isla tiene tres extremos de puente, así que 3WH es par y un número
impar de islas es imposible. Un lado de longitud 1 o 2 también: en una cuadrícula
de dos islas de ancho, la isla de la esquina necesita la diagonal `\`
de la primera celda y la de debajo la diagonal `/`, y se cruzan. Un
programa de búsqueda muestra que 3 × 4 y 3 × 6 (y sus giros) tampoco
tienen mapa, mientras que todos los demás casos pares desde 3 × 8 sí.

El mapa se pega a partir de bloques pequeños. La búsqueda da mapas
cúbicos sin puentes de corte y con todo el borde construido para
anchos 4 y 6 con alturas de 4 a 7, y para altura 3 con anchos 8, 10,
12 y 14. Dos mapas así se pegan por una costura quitando un puente del
borde de cada lado y añadiendo en su lugar los dos puentes que cruzan
la costura: cada isla conserva tres puentes y, como cada lado sigue
conexo y la costura tiene dos puentes, ninguna pérdida aislada divide el
mapa.

Si W es impar, H es par, así que se construye el mapa girado y se
imprime girado de vuelta, cambiando `-` por `|`. W se divide en cuatros
y una última parte de 4 o 6, y H en cuatros y una última parte de 4 a 7
(con H = 3, W en ochos y una última parte de 8 a 14). Cada fila de
bloques se pega por costuras en sus dos filas inferiores, y las filas
se pegan por las dos últimas columnas, de modo que ninguna línea
termina en espacio. `O(WH)`.

Detalles a tener en cuenta:

- 6 × 3 y 3 × 6 no tienen mapa, pero 8 × 3 sí (pruebas 05, 07, 08);
- se acepta cualquier mapa válido, así que las pruebas usan un
  verificador de grados, cruces y puentes;
- una costura con un solo puente lo dejaría como puente de corte, así
  que cada costura lleva dos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1411_constructive.cpp](1411_constructive.cpp) | G++ 13.2 x64 | constructive | O(WH) | AC | 0.015 s | 420 KB |
| [1411_constructive.go](1411_constructive.go) | Go 1.14 x64 | constructive | O(WH) | AC | 0.078 s | 1152 KB |
| [1411_constructive.java](1411_constructive.java) | Java 1.8 | constructive | O(WH) | AC | 0.171 s | 1732 KB |
| [1411_constructive.py](1411_constructive.py) | Python 3.12 x64 | constructive | O(WH) | AC | 0.078 s | 888 KB |
| [1411_constructive.rs](1411_constructive.rs) | Rust 1.75 x64 | constructive | O(WH) | AC | 0.062 s | 260 KB |
