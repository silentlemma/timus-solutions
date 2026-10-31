# 1650. Multimillonarios

[Timus 1650](https://acm.timus.ru/problem.aspx?space=1&num=1650) · dificultad 174 · segment_tree

Problema original de Pavel Atnashev, del cuarto de final de la subregión oriental del NEERC 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

n multimillonarios con fortunas conocidas empiezan en ciudades dadas.
Durante m días viajan: un viaje del día d sale por la tarde y llega a la
mañana siguiente, así que cuenta desde el día d + 1. Para cada ciudad hay
que contar los días en que sus multimillonarios juntos fueron
estrictamente los más ricos de todas las ciudades, y listar las ciudades
con al menos un día así, ordenadas por nombre.

## Entrada

n (1 ≤ n ≤ 10000) y luego n líneas «nombre ciudad fortuna» (fortunas de
1 a 10¹¹). Después m y k (1 ≤ m ≤ 50000, 0 ≤ k ≤ 50000) y k líneas «día
nombre destino» (1 ≤ día ≤ m − 1) en orden creciente de día; nadie viaja
más de una vez al día. Nombres y ciudades tienen hasta 20 letras
latinas, distinguiendo mayúsculas.

## Salida

«ciudad días» para cada ciudad que lideró al menos un día, en el orden
llano de los caracteres (ABC…Zabc…z).

## Ejemplos

### Ejemplo 1

Entrada:

```
5
Abramovich London 15000000000
Deripaska Moscow 10000000000
Potanin Moscow 5000000000
Berezovsky London 2500000000
Khodorkovsky Chita 1000000000
25 9
1 Abramovich Anadyr
5 Potanin Courchevel
10 Abramovich Moscow
11 Abramovich London
11 Deripaska StPetersburg
15 Potanin Norilsk
20 Berezovsky Tbilisi
21 Potanin StPetersburg
22 Berezovsky London
```

Salida:

```
Anadyr 5
London 14
Moscow 1
```

## Solución

Cada ciudad que aparece recibe un índice y se mantiene un árbol de
segmentos sobre los totales de las ciudades. Cada nodo guarda el mayor
total por debajo, cuántas hojas lo alcanzan y una de ellas, así que la
raíz dice al instante si una ciudad va estrictamente delante y cuál. Un
viaje son dos actualizaciones puntuales: la fortuna sale de una ciudad y
entra en otra.

Entre dos días de viaje el líder no cambia, así que los días se cuentan
por bloques: antes de aplicar los viajes del día d, el líder actual (si
es único) recibe los días desde el último contado hasta d; tras el último
viaje recibe los días hasta m. Los totales llegan a 10¹⁵, así que son de
64 bits. `O((n + k) log C)` para C ciudades.

Detalles a tener en cuenta:

- un empate arriba significa que nadie lidera ese día (prueba 03), así
  que la entrada puede no producir salida alguna;
- los viajes del día d aún dejan el día d a la ciudad de antes;
- el orden es por códigos de carácter, así que los nombres con mayúscula
  van antes que todos los de minúscula (prueba 05).

Las respuestas coinciden con un recuento día a día en 60 historias
aleatorias y con una implementación aceptada independiente en las pruebas
generadas. Esa implementación falla cuando alguien «viaja» a la ciudad en
la que ya está, algo que las pruebas del juez al parecer nunca contienen;
el programa de aquí trata ese viaje como quedarse.

## Soluciones optimizadas

La solución optimizada en C++ lee los viajes de uno en uno y aplica cada
uno en el acto en lugar de guardarlos todos antes: un viaje trae como
mucho una ciudad nueva, así que el árbol se dimensiona desde el
principio para las ciudades iniciales más k. Un solo mapa de un nombre a
su ciudad y su fortuna sustituye a dos, un nodo guarda el índice de su
única ciudad en cabeza, o una marca de empate, en lugar de un número de
hojas, el árbol se construye de abajo arriba a partir de los totales
iniciales, y una actualización deja de subir en cuanto un nodo conserva
su máximo y su líder, porque entonces nada por encima puede cambiar. Los
nombres se leen con `scanf` en búferes de 21 bytes en lugar de con
`iostream`: {1650_segment_tree_optimized.cpp}.

La solución optimizada en Go lee los viajes de uno en uno y aplica cada
uno en el acto en lugar de guardarlos todos antes: un viaje trae como
mucho una ciudad nueva, así que el árbol se dimensiona desde el
principio para las ciudades iniciales más k. Un solo mapa de un nombre a
su ciudad y su fortuna sustituye a dos, un nodo guarda el índice de su
única ciudad en cabeza, o una marca de empate, en lugar de un número de
hojas, el árbol se construye de abajo arriba a partir de los totales
iniciales, y una actualización deja de subir en cuanto un nodo conserva
su máximo y su líder, porque entonces nada por encima puede cambiar. Las
palabras vienen de un `bufio.Scanner` en lugar de `fmt.Fscan`:
{1650_segment_tree_optimized.go}.

La solución optimizada en Java lee los viajes de uno en uno y aplica
cada uno en el acto en lugar de guardarlos todos antes: un viaje trae
como mucho una ciudad nueva, así que el árbol se dimensiona desde el
principio para las ciudades iniciales más k. Un solo mapa de un nombre a
su ciudad y su fortuna sustituye a dos, un nodo guarda el índice de su
única ciudad en cabeza, o una marca de empate, en lugar de un número de
hojas, el árbol se construye de abajo arriba a partir de los totales
iniciales, y una actualización deja de subir en cuanto un nodo conserva
su máximo y su líder, porque entonces nada por encima puede cambiar. Los
tokens se leen línea a línea en lugar de juntar antes toda la entrada en
un `StringBuilder`: {1650_segment_tree_optimized.java}.

La solución optimizada en Python lee los viajes de uno en uno y aplica
cada uno en el acto en lugar de guardarlos todos antes: un viaje trae
como mucho una ciudad nueva, así que el árbol se dimensiona desde el
principio para las ciudades iniciales más k. Un solo mapa de un nombre a
su ciudad y su fortuna sustituye a dos, un nodo guarda el índice de su
única ciudad en cabeza, o una marca de empate, en lugar de un número de
hojas, el árbol se construye de abajo arriba a partir de los totales
iniciales, y una actualización deja de subir en cuanto un nodo conserva
su máximo y su líder, porque entonces nada por encima puede cambiar. La
entrada se lee línea a línea, un registro por línea, en lugar de toda de
una vez: {1650_segment_tree_optimized.py}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1650_segment_tree_optimized.cpp`: reducción de tiempo -49.60%;
  reducción de memoria +50.94%; base: `1650_segment_tree.cpp`.

- `1650_segment_tree_optimized.go`: reducción de tiempo +45.61%;
  reducción de memoria +1.04%; base: `1650_segment_tree.go`.

- `1650_segment_tree_optimized.java`: reducción de tiempo -15.27%;
  reducción de memoria +46.58%; base: `1650_segment_tree.java`.

- `1650_segment_tree_optimized.py`: reducción de tiempo +1.51%;
  reducción de memoria +41.56%; base: `1650_segment_tree.py`.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1650_segment_tree.cpp](1650_segment_tree.cpp) | G++ 13.2 x64 | segment_tree | O((n + k) log C) | AC | 0.125 s | 20700 KB | 11304018 |
| [1650_segment_tree.go](1650_segment_tree.go) | Go 1.14 x64 | segment_tree | O((n + k) log C) | AC | 0.171 s | 18416 KB | 11288517 |
| [1650_segment_tree.java](1650_segment_tree.java) | Java 1.8 | segment_tree | O((n + k) log C) | AC | 0.203 s | 27324 KB | 11288519 |
| [1650_segment_tree.py](1650_segment_tree.py) | Python 3.12 x64 | segment_tree | O((n + k) log C) | AC | 1.062 s | 27776 KB | 11288518 |
| [1650_segment_tree.rs](1650_segment_tree.rs) | Rust 1.75 x64 | segment_tree | O((n + k) log C) | AC | 0.046 s | 13036 KB | 11304019 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1650_segment_tree_optimized.cpp](1650_segment_tree_optimized.cpp) \* | G++ 13.2 x64 | segment_tree | O((n + k) log C) | AC | 0.187 s | 10156 KB | 11307264 |
| [1650_segment_tree_optimized.go](1650_segment_tree_optimized.go) \* | Go 1.14 x64 | segment_tree | O((n + k) log C) | AC | 0.093 s | 18224 KB | 11307269 |
| [1650_segment_tree_optimized.java](1650_segment_tree_optimized.java) \* | Java 1.8 | segment_tree | O((n + k) log C) | AC | 0.234 s | 14596 KB | 11307271 |
| [1650_segment_tree_optimized.py](1650_segment_tree_optimized.py) \* | Python 3.12 x64 | segment_tree | O((n + k) log C) | AC | 1.046 s | 16232 KB | 11307267 |

\* Aceptada; aún no cumple el objetivo de clasificación. Puede optimizarse más.
