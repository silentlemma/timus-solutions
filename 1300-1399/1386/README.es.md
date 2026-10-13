# 1386. Otra vez el laberinto

[Timus 1386](https://acm.timus.ru/problem.aspx?space=1&num=1386) · dificultad 1143 · simulation

Problema original de Andrew Khalyavin, del campus de entrenamiento de verano de Petrozavodsk, agosto de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un laberinto es un campo de N × M, 1 ≤ N, M ≤ 100, con cuatro órdenes.
Para cada casilla y cada orden, el mapa da la casilla a la que pasa el
jugador. No se sabe dónde empezó el jugador, pero se conocen las
S ≤ 4000 órdenes de la partida. Hay que imprimir todas las casillas en
las que puede estar ahora.

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

N y M, luego cuatro bloques, uno por orden, de N líneas con M pares: el
par de la columna i de la línea j del bloque k es la casilla a la que
lleva la orden k desde la casilla (j, i). Después S y las S órdenes.

## Salida

El número de casillas y luego las casillas ordenadas por fila y después
por columna.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 3
1 2  1 3  1 3
2 2  2 3  2 3
2 1  2 2  2 3
2 1  2 2  2 3
1 1  1 1  1 2
2 1  2 1  2 2
1 1  1 2  1 3
1 1  1 2  1 3
4
1 2 3 4
```

Salida:

```
2
1 1
1 2
```

## Solución

Se guarda el conjunto de casillas donde puede estar el jugador, al
principio todo el campo, y se pasa por cada orden. Varias casillas
pueden llevar a la misma, así que se eliminan duplicados: C++, Go, Java
y Rust añaden una casilla solo si su marca aún no es el paso actual.
El conjunto nunca crece: como mucho N·M consultas por paso, hasta 4·10⁷
en total. Con la ordenación final, el tiempo es `O(N·M·(S + log(N·M)))`.

Detalles a tener en cuenta:

- los mapas pueden ser permutaciones, como en un toro, y entonces nada
  se junta: cada paso recorre las 10 000 casillas (pruebas generadas 1
  y 3);
- el límite es de medio segundo, así que las casillas se numeran con un
  solo índice y cada paso es un bucle compacto;
- la salida va ordenada primero por fila y luego por columna.

Las respuestas se compararon en 400 campos pequeños aleatorios con una
simulación desde cada casilla inicial.

## Notas por lenguaje

- Python se ejecuta con PyPy y aplica las órdenes de cuatro en cuatro:
  16 tablas para pares de órdenes y una tabla para cada bloque de cuatro,
  hecha con dos pares cuando el bloque aparece por primera vez, así que
  las casillas recorren aproximadamente la cuarta parte de los pasos,
  eliminando duplicados periódicamente con un set. Orden a orden
  excedía el límite de 0,5 s en la prueba 46 del juez; ahora tarda
  0,33 s.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1386_simulation.cpp](1386_simulation.cpp) | G++ 13.2 x64 | simulation | O(N·M·(S + log(N·M))) | AC | 0.078 s | 280 KB |
| [1386_simulation.go](1386_simulation.go) | Go 1.14 x64 | simulation | O(N·M·(S + log(N·M))) | AC | 0.093 s | 1584 KB |
| [1386_simulation.java](1386_simulation.java) | Java 1.8 | simulation | O(N·M·(S + log(N·M))) | AC | 0.203 s | 1152 KB |
| [1386_simulation.py](1386_simulation.py) | PyPy 3.10 x64 | simulation | O(N·M·(S + log(N·M))) | AC | 0.328 s | 45076 KB |
| [1386_simulation.rs](1386_simulation.rs) | Rust 1.75 x64 | simulation | O(N·M·(S + log(N·M))) | AC | 0.093 s | 924 KB |
