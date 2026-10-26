# 1589. Sokoban

[Timus 1589](https://acm.timus.ru/problem.aspx?space=1&num=1589) · dificultad 14456 · astar, greedy

Problema original de Stanislav Vasiliev y Sergey Pupyrev, de la subregión oriental del NEERC del ACM ICPC 2007–2008, Ekaterimburgo, 27 de octubre de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un nivel de Sokoban de a lo sumo 8 × 8 casillas: paredes `#`, metas `.`,
cajas `$` (`*` sobre una meta) y el jugador `@` (`+` sobre una meta). El
jugador camina por casillas libres y puede empujar una caja a la vez al
caminar hacia ella, nunca tirar de ella. Imprime un plan que lleve todas
las cajas a metas: los movimientos `u`, `d`, `l`, `r`, en mayúscula cuando
empujan una caja, a lo sumo 10 000. Siempre hay solución y se acepta
cualquier plan válido.

Límite de tiempo: 5 segundos. Límite de memoria: 64 MB.

## Entrada

El nivel, fila por fila; las filas pueden tener longitudes distintas y
espacios fuera de las paredes.

## Salida

Una línea con el plan.

## Ejemplos

### Ejemplo 1

Entrada:

```
########
#@  $ .#
########
```

Salida:

```
rrRR
```

### Ejemplo 2

Entrada:

```
######
##   .#
#@  ###
#   * #
#   $ #
#     #
#######
```

Salida:

```
dddrrrruLdlUUUluRR
```

## Solución

La búsqueda avanza por empujes, no por pasos. Un estado es el conjunto
de cajas y la zona a la que puede llegar el jugador, nombrada por su
casilla más baja; todo cabe en una clave de 64 bits, y la zona se
obtiene haciendo crecer una máscara de bits. Hay dos soluciones: la
voraz, una sola búsqueda primero-el-mejor con pruebas de bloqueo (C++,
Go, Java, Rust), y astar, una cadena de búsquedas con tablas de bloqueos
por regiones, mucho más rápida (los cinco lenguajes).

La búsqueda voraz toma estados por `empujes + 20·h`, donde h es el menor
número total de empujes con que cajas solas llegan a metas distintas (el
método húngaro); el peso grande hace la búsqueda casi voraz. Un estado
se descarta cuando:

- una caja quedaría en una casilla muerta, desde la que una caja sola no
  alcanza ninguna meta;
- quedan congeladas cajas fuera de meta: ninguna puede moverse por
  ningún eje aun quitando paso a paso todas las cajas movibles, o el
  jugador no puede empujar ninguna aun quitando todas las que sí puede
  empujar y ampliando su zona;
- el emparejamiento no tiene coste finito;
- algún conjunto de dos, tres o cuatro cajas que contiene la movida no
  puede resolverse por sí solo: para cada conjunto así, una tabla
  construida con búsquedas de tirones desde todos los conjuntos de metas
  de ese tamaño guarda las casillas del jugador desde las que sí puede.

Un corral, una zona en la que el jugador no puede entrar con una caja
sin terminar en su borde o una meta dentro, cuyos empujes de borde van
todos hacia dentro (y siguen siendo los mismos sin las cajas de fuera),
restringe los movimientos a esos empujes. Los estados vistos se guardan
en un conjunto de claves con direccionamiento abierto y los nodos en un
arreglo plano; el plan se reconstruye con el movimiento guardado en cada
nodo, y los pasos entre empujes salen de un recorrido en anchura.

En un nivel denso del foro, 13 cajas en 36 casillas, desde el inicio se
alcanzan más de 30 millones de estados y 22 millones desde la posición
resuelta, pero solo unos 6 300 están en ambos lados; la búsqueda voraz
necesita allí 1,8 s.

La cadena astar ordena los estados por la misma cota, aquí H, con las
cajas congeladas sobre metas como paredes, y descarta estados igual
salvo por las tablas de subconjuntos. Las etapas:

1. Sondeos baratos: una búsqueda hacia delante y una de tirones desde
   las metas, de 128 expansiones cada una, y luego el tablero en cuatro
   giros con 64 expansiones cada uno. La mayoría de los niveles termina
   aquí.
2. El tablero en su menor giro o reflejo se busca con dos pruebas más.
   Tablas regionales: para la franja de tres casillas de ancho a lo
   largo de cada lado del suelo, una búsqueda de tirones desde las metas
   de la franja, en la que las cajas pueden salir de la franja y entrar
   otras, registra cada conjunto de cajas de la franja y cada zona del
   jugador desde los que la franja aún puede terminarse; un estado cuya
   franja no está registrada está muerto. Orden de llenado: tirar cajas
   fuera de las metas de la posición resuelta, conservando las cajas
   congeladas, muestra qué metas habrá que llenar al final; un estado
   que no encaja con ninguno de esos restos está muerto. La prioridad es
   `H + 30·M - profundidad`, donde M cuenta las cajas que faltan para el
   resto más cercano, de modo que la búsqueda profundiza siguiendo un
   orden de llenado. Se detiene tras 600 000 estados o 1 s.
3. Si eso falla, o su plan supera los 10 000 movimientos, se libera su
   memoria y empieza desde cero una segunda cadena: los mismos sondeos,
   luego búsquedas con tablas de todos los subconjuntos de tres y
   después de cinco cajas cerca de la caja movida (construidas con
   búsquedas de tirones solo con esas cajas, las congeladas como
   paredes), y por último un A* sobre casillas exactas del jugador y
   costes de caminar, que mantiene todo plan dentro de 10 000
   movimientos.

Cada plan se reproduce antes de imprimirlo. En el nivel denso las
pruebas regionales y de orden de llenado permiten a la cadena expandir
2 700 estados.

En la tabla, P es el tiempo de preprocesamiento, E los estados
expandidos y B las cajas.

Detalles a tener en cuenta:

- las cajas pueden estar ya en sus metas: imprime una línea vacía
  (prueba 03);
- el jugador puede empezar sobre una meta (`+`) y las filas pueden
  empezar con espacios (prueba 04);
- una caja sobre una meta aislada del jugador por paredes, ignorando
  otras cajas, nunca se mueve y se excluye de la búsqueda (prueba 05);
- el plan de una búsqueda por zonas puede superar los 10 000
  movimientos: uno de los niveles generados dio 44 895, y una búsqueda
  exacta sin límites de uno más corto necesitó más de 170 MB;
- los límites dejan poco margen a la búsqueda voraz: hasta 3,8 s y 57 MB
  en el juez.

Los planes pasan el verificador en las pruebas de aquí y en 2 291
niveles generados, los voraces en como mucho 2,4 s y 63 MB cada uno; los
de `1589_astar.cpp`, también en 12 000 niveles más, muchos de ellos
evolucionados para romper la búsqueda regional, en como mucho 0,71 s y
20 MB cada uno.

## Notas por lenguaje

- Go, Java y Rust siguen al C++ paso a paso; sus planes son los de C++
  byte a byte.
- El Java voraz numera los subconjuntos de cajas con bucles simples y
  guarda todos los búferes en arreglos primitivos: una primera versión
  excedía el límite en la prueba 88 del juez.
- Python ejecuta la cadena astar con PyPy, con algunos cambios por
  velocidad: solo el primer sondeo (los otros cinco costaban hasta 0,5 s
  en niveles difíciles, sobre todo en compilación JIT), sin sondeos en
  la segunda cadena, la primera etapa limitada a 4,5 s y 300 000
  estados, y un JIT que compila menos (`trace_limit=3000`, sin
  desenrollar bucles): en niveles difíciles casi la mitad del tiempo se
  iba en compilar. El emparejamiento de un hijo continúa desde los
  potenciales óptimos del padre con un solo aumento, las tablas de
  franjas actualizan el índice del subconjunto con cada tirón, y las
  distancias con penalización por cruce usan tirones precalculados para
  cada conjunto de cajas congeladas. La búsqueda voraz, con 3,8 s en
  C++, queda fuera del alcance de Python, y las búsquedas anteriores en
  Python excedían el límite en las pruebas 55 a 67 del juez.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1589_astar.cpp](1589_astar.cpp) | G++ 13.2 x64 | astar | O(P + E · B · (B³ + C(B, 5))) | AC | 0.156 s | 12132 KB |
| [1589_astar.go](1589_astar.go) | Go 1.14 x64 | astar | O(P + E · B · (B³ + C(B, 5))) | AC | 0.281 s | 25644 KB |
| [1589_astar.java](1589_astar.java) | Java 1.8 | astar | O(P + E · B · (B³ + C(B, 5))) | AC | 0.640 s | 20156 KB |
| [1589_astar.py](1589_astar.py) | PyPy 3.10 x64 | astar | O(P + E · B · (B³ + C(B, 5))) | AC | 3.234 s | 49756 KB |
| [1589_astar.rs](1589_astar.rs) | Rust 1.75 x64 | astar | O(P + E · B · (B³ + C(B, 5))) | AC | 0.171 s | 10488 KB |
| [1589_greedy.cpp](1589_greedy.cpp) | G++ 13.2 x64 | greedy | O(P + E · B⁴) | AC | 3.812 s | 57152 KB |
| [1589_greedy.go](1589_greedy.go) | Go 1.14 x64 | greedy | O(P + E · B⁴) | AC | 2.546 s | 58752 KB |
| [1589_greedy.java](1589_greedy.java) | Java 1.8 | greedy | O(P + E · B⁴) | AC | 4.078 s | 31196 KB |
| [1589_greedy.rs](1589_greedy.rs) | Rust 1.75 x64 | greedy | O(P + E · B⁴) | AC | 2.984 s | 55436 KB |
