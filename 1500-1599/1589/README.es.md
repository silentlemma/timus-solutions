# 1589. Sokoban

[Timus 1589](https://acm.timus.ru/problem.aspx?space=1&num=1589) · dificultad 28561 · bidirectional

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

La búsqueda avanza por empujes, no por pasos. Un estado es el conjunto de
cajas y la zona a la que puede llegar el jugador, nombrada por su casilla
más baja; todo cabe en una clave de 64 bits, y la zona se obtiene haciendo
crecer una máscara de bits.

Dos búsquedas primero-el-mejor se encuentran en el medio: empujes desde el
inicio y tirones desde la posición resuelta (las cajas en las metas, el
jugador en cualquier zona libre). Comparten una tabla de direccionamiento
abierto de 2²² claves, y un estado hallado por ambas une las dos mitades
del plan. Cada búsqueda toma estados por `g + 3h`, donde h suma la
distancia en empujes de cada caja a su meta (o casilla inicial) más
cercana; un emparejamiento entre las cajas y las casillas que aún pueden
alcanzar detecta cajas que no pueden colocarse todas. Las listas abiertas
son cubetas enlazadas a través de la tabla, así que la memoria es fija.

La mayor parte del trabajo está en descartar posiciones muertas:

- casillas muertas, desde las que una caja sola nunca llega a una meta;
- cajas congeladas: una caja fuera de meta bloqueada en ambos ejes por
  paredes, casillas muertas u otras cajas congeladas;
- corrales: si el jugador no puede entrar en una región y todos los
  empujes de las cajas que la rodean van hacia dentro, uno de ellos es
  necesario y solo se prueban esos (si la región no está terminada y
  ninguno es posible aún, el estado está muerto);
- subconjuntos pequeños: para cada grupo de dos a cuatro cajas una tabla,
  construida con una búsqueda solo con esas cajas, dice si ellas solas aún
  pueden resolverse (para la búsqueda de tirones: alcanzarse desde el
  inicio). Pares y tríos se comprueban con todas las cajas, cuartetos solo
  cerca de la caja movida.

El plan se reconstruye con el movimiento guardado en cada clave, y los
pasos entre empujes salen de un recorrido en anchura. `O(S · B)` para S
estados visitados (a lo sumo unos 3,7 millones) y B cajas.

Detalles a tener en cuenta:

- las cajas pueden estar ya en sus metas: imprime una línea vacía (prueba
  03);
- el jugador puede empezar sobre una meta (`+`) y las filas pueden empezar
  con espacios (prueba 04);
- una caja sobre una meta a la que el jugador no llega nunca se mueve y
  cuenta como pared (prueba 05).

Los planes se comprobaron con las pruebas de aquí y con unos 1 500 niveles
generados, y las soluciones resuelven cada nivel aleatorio que resuelve
una implementación independiente aceptada.

## Notas por lenguaje

- Go consulta la tabla una sola vez por estado nuevo y calcula los
  índices de los subconjuntos pequeños directamente a partir de las
  casillas de las cajas: una primera versión, unas 1,4 veces más lenta
  que C++, se rendía tras 4,6 s en la prueba 92 del juez, que C++
  resuelve en 2,2 s. Go busca hasta los 4,85 s.

- Java usa una tabla de 2²¹ claves para que la JVM quepa en 64 MB y
  tiene las mismas mejoras que Go. Marca un área completa del jugador en
  cuanto la encuentra, construye las tablas de subconjuntos con
  operaciones de bits y guarda las máscaras en las claves, lo que bajó
  la prueba 92 del juez de más de 5 s a 4,34 s.

- Python guarda los estados en arreglos compactos y se ejecuta con PyPy;
  CPython es varias veces más lento. Tarda unos 0,5 s en las pruebas de
  aquí, pero excede el límite de 5 s en la prueba 62 del juez, mucho más
  pesada: C++ necesita 2,2 s en la prueba 92. Se probaron tres búsquedas
  distintas en Python: esta bidireccional, la misma con reinicios de
  primero el mejor y asignaciones de coste mínimo de cajas a metas
  (prueba 55), y una búsqueda voraz según esa asignación con casillas
  muertas, cajas congeladas, corrales y tablas de pares y tríos de cajas
  (prueba 56). Con el mismo número de estados, Python con PyPy es unas
  35 veces más lento que C++, así que para pasar haría falta una
  búsqueda que visite muchos menos estados. Se mantiene marcada TLE:
  pasa todas las pruebas de aquí, pero no se afirma que quepa en el
  tiempo en cada prueba del juez.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1589_bidirectional.cpp](1589_bidirectional.cpp) | G++ 13.2 x64 | bidirectional | O(S · B) | AC | 2.203 s | 54384 KB |
| [1589_bidirectional.go](1589_bidirectional.go) | Go 1.14 x64 | bidirectional | O(S · B) | AC | 3.000 s | 58376 KB |
| [1589_bidirectional.java](1589_bidirectional.java) | Java 1.8 | bidirectional | O(S · B) | AC | 4.343 s | 28700 KB |
| [1589_bidirectional.py](1589_bidirectional.py) | PyPy 3.10 x64 | bidirectional | O(S · B) | TLE (test 62) | 5.015 s | 50612 KB |
| [1589_bidirectional.rs](1589_bidirectional.rs) | Rust 1.75 x64 | bidirectional | O(S · B) | AC | 2.390 s | 55068 KB |
