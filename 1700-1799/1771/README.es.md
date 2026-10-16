# 1771. La mañana de un diputado

[Timus 1771](https://acm.timus.ru/problem.aspx?space=1&num=1771) · dificultad 5549 · implementation

Problema original de Alex Samsonov, del XIV Campeonato de los Urales de Programación Competitiva, 10 de abril de 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una ciudad tiene n paradas y m líneas de autobús; cada línea es una
lista de paradas distintas, un autobús tarda un minuto entre paradas
vecinas y no da la vuelta, los autobuses salen de la primera parada de
una línea en minutos enteros desde las 07:00, nunca dos de una misma
línea a la vez, y no hay otro horario. Cada pasajero está en su parada
a las 06:59 y toma el primer autobús que va a su destino; entre los que
llegan a la vez, el que llega antes, y luego el de número de línea
menor.

Desde las 07:00 un hombre en la parada 1 anotó cada autobús que paró
allí, con su minuto y su línea, incluidos todos los del minuto del
último, en el que subió. Ya llevaba 42 personas y otras 13 subieron con
él. ¿Cuántas como mínimo y como máximo de esas 55 pueden seguir a bordo
cuando el autobús llega a la parada 2?

## Entrada

n y m (3 ≤ n, m ≤ 100), luego las m líneas, cada una una lista de
paradas terminada en −1, luego k (1 ≤ k ≤ 100) y las k anotaciones
`hh:mm línea` en orden de tiempo, la última su autobús. Ese autobús
sigue hasta la parada 2, y la parada 1 no es la primera de su línea.

## Salida

El menor y el mayor número de las 55 personas que viajan con él de la
parada 1 a la parada 2.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 3
1 4 -1
4 1 -1
3 1 4 2 -1
2
07:00 1
07:10 3
```

Salida:

```
13 55
```

## Solución

Un autobús anotado tiene una salida conocida: su minuto en la parada 1
menos la posición de la parada 1 en su línea, así que se conoce su
minuto en cada parada de su línea. Un pasajero que espera en la parada
`src` para ir a `dst` tomó este autobús justo cuando ningún autobús
anotado que hace ese trayecto llegó antes a `src`, o en el mismo minuto
llegando antes a `dst`, o igual pero con número de línea menor. Los
autobuses que no están en el cuaderno no restringen los trayectos
posibles: tanto los que pasarían por la parada 1 después de que él se
fuera como los de líneas que no pasan por esa parada pueden
simplemente no circular.

Las 13 subieron en la parada 1 y las 42 en paradas anteriores, y como
todas siguen a bordo en la parada 1, van a paradas posteriores. Para
cada grupo basta saber si algún trayecto con destino antes de la parada
2 puede elegir este autobús, y si alguno hasta la parada 2 o más allá
puede: todo el grupo puede entonces compartir ese destino. Así, el
mínimo suma un grupo solo cuando ningún destino temprano es posible, y
el máximo solo cuando lo es uno tardío. `O(mn + L² · k)` para la
línea elegida de longitud L.

En el ejemplo el autobús anterior de la línea 1 también va de la
parada 1 a la 4, así que las 13 no pueden ir a la 4 y deben seguir
hasta la parada 2, mientras que las 42 de la parada 3 pueden ir a la 4
o a la 2: entre 13 y 55.

Trampas:

- el hombre mismo no cuenta, y no necesariamente siguió la regla;
- entre autobuses del mismo minuto gana el que llega antes al destino,
  y solo después la línea menor;
- un autobús visto en la parada 1 puede llegar a las paradas anteriores
  de esta línea antes que este autobús y llevarse a esos pasajeros.

Las respuestas coinciden con una implementación aceptada independiente
en 450 cuadernos aleatorios, todos posibles según las reglas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1771_implementation.cpp](1771_implementation.cpp) | G++ 13.2 x64 | implementation | O(mn + L^2 k) | AC | 0.015 s | 284 KB |
| [1771_implementation.go](1771_implementation.go) | Go 1.14 x64 | implementation | O(mn + L^2 k) | AC | 0.031 s | 1604 KB |
| [1771_implementation.java](1771_implementation.java) | Java 1.8 | implementation | O(mn + L^2 k) | AC | 0.125 s | 3292 KB |
| [1771_implementation.py](1771_implementation.py) | Python 3.12 x64 | implementation | O(mn + L^2 k) | AC | 0.078 s | 1748 KB |
| [1771_implementation.rs](1771_implementation.rs) | Rust 1.75 x64 | implementation | O(mn + L^2 k) | AC | 0.031 s | 384 KB |
