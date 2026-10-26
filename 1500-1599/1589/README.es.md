# 1589. Sokoban

[Timus 1589](https://acm.timus.ru/problem.aspx?space=1&num=1589) · dificultad 14456 · greedy

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
obtiene haciendo crecer una máscara de bits.

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

En la tabla, P es el tiempo de preprocesamiento, E los estados
expandidos y B las cajas.

Detalles a tener en cuenta:

- las cajas pueden estar ya en sus metas: imprime una línea vacía
  (prueba 03);
- el jugador puede empezar sobre una meta (`+`) y las filas pueden
  empezar con espacios (prueba 04);
- una caja sobre una meta aislada del jugador por paredes, ignorando
  otras cajas, nunca se mueve y se excluye de la búsqueda (prueba 05);
- los límites dejan poco margen a la búsqueda voraz: hasta 3,8 s y 57 MB
  en el juez.

Los planes pasan el verificador en las pruebas de aquí y en 2 291
niveles generados, los voraces en como mucho 2,4 s y 63 MB cada uno.

## Notas por lenguaje

- Go, Java y Rust siguen al C++ paso a paso; sus planes son los de C++
  byte a byte.
- El Java voraz numera los subconjuntos de cajas con bucles simples y
  guarda todos los búferes en arreglos primitivos: una primera versión
  excedía el límite en la prueba 88 del juez.
- Aquí no hay solución en Python: la búsqueda voraz necesita 3,8 s en
  C++, y las búsquedas anteriores en Python, entre ellas una
  bidireccional, excedían el límite en las pruebas 55 a 67 del juez.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1589_greedy.cpp](1589_greedy.cpp) | G++ 13.2 x64 | greedy | O(P + E · B⁴) | AC | 3.812 s | 57152 KB |
| [1589_greedy.go](1589_greedy.go) | Go 1.14 x64 | greedy | O(P + E · B⁴) | AC | 2.546 s | 58752 KB |
| [1589_greedy.java](1589_greedy.java) | Java 1.8 | greedy | O(P + E · B⁴) | AC | 4.078 s | 31196 KB |
| [1589_greedy.rs](1589_greedy.rs) | Rust 1.75 x64 | greedy | O(P + E · B⁴) | AC | 2.984 s | 55436 KB |
