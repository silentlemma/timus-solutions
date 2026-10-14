# 1548. Sakura y estadística

[Timus 1548](https://acm.timus.ru/problem.aspx?space=1&num=1548) · dificultad 10900 · greedy

Problema original de Sergey Pupyrev, del XI Campeonato Universitario por Equipos de Programación de los Urales, Ekaterimburgo, 21 de abril de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se da una imagen en blanco y negro de N × M píxeles (1 ≤ N, M ≤ 50) en la
que los píxeles negros de cada columna forman como mucho un tramo
vertical. Hay que hallar el menor conjunto de rectángulos de píxeles
negros cuya unión sea exactamente el conjunto de píxeles negros; los
rectángulos pueden solaparse. Vale cualquier conjunto mínimo.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y M, y luego N líneas de M caracteres: `1` es negro, `0` es blanco.

## Salida

El número de rectángulos y luego cada rectángulo como la fila y la
columna de dos esquinas opuestas, con las filas contadas desde arriba.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 3
010
111
010
```

Salida:

```
2
1 2 3 2
2 1 2 3
```

### Ejemplo 2

Entrada:

```
4 5
00000
11100
11010
10000
```

Salida:

```
4
2 1 2 3
3 1 3 2
2 1 4 1
3 4 3 4
```

## Solución

Como cada columna tiene como mucho un tramo de filas negras, las
columnas de un intervalo [l, r) son todas negras justo en las filas donde
se cortan sus tramos, que es de nuevo un tramo de filas, quizá vacío.
Así que un rectángulo siempre puede estirarse a todas esas filas, y
queda descrito solo por su intervalo de columnas.

Cada fila se parte en tramos máximos de píxeles negros. Un conjunto de
intervalos da un recubrimiento de la imagen justo cuando cada uno de
esos tramos de fila es la unión de los intervalos elegidos que caben en
él. La tarea es entonces la familia mínima de intervalos que genera así
todos los tramos de fila, y la respuesta es su tamaño.

Esa familia se halla de forma voraz, como Franzblau y Kleitman cubren
polígonos verticalmente convexos. Se parte de los distintos tramos de
fila y se recorren los extremos derechos de izquierda a derecha. Un
recorrido hacia atrás, contando los intervalos elegidos, halla un
intervalo que se puede eliminar. Se descarta y se mueven a la derecha
los extremos izquierdos de algunos intervalos que terminan antes,
recorriendo los extremos derechos en orden decreciente, para que todos
los tramos de fila sigan generados. Se repite el recorrido para el mismo
extremo derecho hasta que no se pueda eliminar ninguno más;
`O(N·M + M⁴)`, poco para M ≤ 50.

Detalles a tener en cuenta:

- los rectángulos pueden solaparse, y las mejores respuestas lo
  necesitan: la cruz del primer ejemplo y los dos cuadrados de la prueba
  05 usan dos rectángulos, donde cualquier partición necesita tres;
- una fila puede tener varios tramos, y cada uno se genera por
  separado: la fila 3 del segundo ejemplo tiene el de las columnas 1–2 y
  el de la columna 4;
- una imagen blanca no necesita rectángulos (prueba 03).

Las cantidades se compararon con una búsqueda exhaustiva sobre
conjuntos de rectángulos máximos en 400 imágenes pequeñas aleatorias y
con una implementación aceptada independiente en 300 imágenes de hasta
50 × 50. Las pruebas usan un comprobador que acepta cualquier
recubrimiento mínimo.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1548_greedy.cpp](1548_greedy.cpp) | G++ 13.2 x64 | greedy | O(N·M + M⁴) | AC | 0.015 s | 220 KB |
| [1548_greedy.go](1548_greedy.go) | Go 1.14 x64 | greedy | O(N·M + M⁴) | AC | 0.031 s | 1164 KB |
| [1548_greedy.java](1548_greedy.java) | Java 1.8 | greedy | O(N·M + M⁴) | AC | 0.109 s | 516 KB |
| [1548_greedy.py](1548_greedy.py) | Python 3.12 x64 | greedy | O(N·M + M⁴) | AC | 0.093 s | 800 KB |
| [1548_greedy.rs](1548_greedy.rs) | Rust 1.75 x64 | greedy | O(N·M + M⁴) | AC | 0.046 s | 236 KB |
