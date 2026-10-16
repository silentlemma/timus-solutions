# 1770. El Partido de los Campeones de los Urales

[Timus 1770](https://acm.timus.ru/problem.aspx?space=1&num=1770) · dificultad 1744 · graphs

Problema original de Igor Chevdar, del XIV Campeonato de los Urales de Programación Competitiva, 10 de abril de 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una ciudad tiene n cruces unidos por carreteras de doble sentido en una
red conexa. Una carretera puede tener un cartel, visible solo para
quien va en un sentido. Una tabla da, para cada par ordenado de cruces,
el menor número de carteles que ve un conductor yendo del primero al
segundo. Construir una red de carreteras con carteles que dé
exactamente esa tabla, o informar de que no existe.

## Entrada

n (2 ≤ n ≤ 300) y luego la tabla de n × n con valores de 0 a n − 1 y
ceros en la diagonal.

## Salida

`NO`, o `YES` y n filas de n caracteres: 0 si no hay carretera entre i
y j, 1 para una carretera en la que no se ve nada yendo de i a j, 2 para
una carretera cuyo cartel se ve yendo de i a j. Se acepta cualquier red
válida.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
0 1 1 1 1
1 0 1 0 1
0 0 0 0 0
2 1 2 0 2
0 0 0 0 0
```

Salida:

```
YES
00202
00210
11001
02000
10100
```

### Ejemplo 2

Entrada:

```
2
0 1
1 0
```

Salida:

```
NO
```

## Solución

Una carretera de i a j cuesta 0 o 1 carteles en cada sentido, y el
viaje de i a j siempre puede tomarla, así que una carretera solo es
posible donde cuesta al menos lo de la tabla en ambos sentidos. Como una
carretera muestra a lo sumo un cartel, el par de la tabla (de i a j, de
j a i) debe ser (0, 0), (1, 0) o (0, 1), es decir, sumar a lo sumo 1; la
carretera cuesta entonces exactamente lo de la tabla.

Se ponen todas esas carreteras. Con todos los costes de carretera al
menos los de la tabla, todo viaje cuesta también al menos lo de la
tabla, mientras la propia tabla cumpla la desigualdad triangular, y
añadir carreteras solo baja los costes; así que esta red da los menores
costes que puede dar cualquier red. La tabla es posible justo cuando
esta red la reproduce, lo que además hace la red conexa. Los costes
salen de Floyd–Warshall en `O(n³)`; la solución en Python busca en
cambio desde cada cruce nivel a nivel, guardando los cruces de un mismo
coste como máscaras de bits.

En el primer ejemplo los cruces 3 y 5 no ven ningún cartel en ningún
viaje: una carretera libre los une, y carreteras desde 1 y 2 llegan a
ambos con un cartel visible al entrar. El cruce 4 solo recibe una
carretera hacia 2, con un cartel visible al salir, y 1 y 4 ven
demasiados carteles entre sí para tener carretera. El programa conserva
además la carretera de 2 a 5, que el ejemplo omite; ambas redes dan la
tabla.

Trampas:

- un par con 1 en ambos sentidos no puede tener carretera, pues una
  carretera tiene un solo cartel;
- una tabla puede no cumplir la desigualdad triangular, lo que detecta
  la comparación;
- la respuesta es una red, y no única, así que el verificador recalcula
  la tabla a partir de las carreteras impresas.

Las respuestas coinciden con una implementación aceptada independiente,
comprobadas por ambos lados, en 100 casos aleatorios: tablas de redes
aleatorias de hasta 8 y de 300 cruces, tablas pequeñas aleatorias y
tablas con un valor cambiado.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1770_graphs.cpp](1770_graphs.cpp) | G++ 13.2 x64 | graphs | O(n^3) | AC | 0.093 s | 692 KB |
| [1770_graphs.go](1770_graphs.go) | Go 1.14 x64 | graphs | O(n^3) | AC | 0.125 s | 3164 KB |
| [1770_graphs.java](1770_graphs.java) | Java 1.8 | graphs | O(n^3) | AC | 0.171 s | 7360 KB |
| [1770_graphs.py](1770_graphs.py) | Python 3.12 x64 | graphs | O(n^3) | AC | 0.250 s | 7252 KB |
| [1770_graphs.rs](1770_graphs.rs) | Rust 1.75 x64 | graphs | O(n^3) | AC | 0.062 s | 2560 KB |
