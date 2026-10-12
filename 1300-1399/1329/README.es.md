# 1329. Historia galáctica

[Timus 1329](https://acm.timus.ru/problem.aspx?space=1&num=1329) · dificultad 458 · dfs

Problema original de Evgeny Krokhalev, del Décimo Campeonato por Equipos de Programación para Escolares de la Región de Sverdlovsk, 16 de octubre de 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hasta 40 000 hitos de la historia forman un árbol con raíz; cada uno
tiene un número de 0 a 40 000 y el número de su padre, −1 para la raíz.
Hay que responder hasta 40 000 preguntas sobre dos hitos distintos A y
B: 1 si A es antecesor de B, 2 si B es antecesor de A y 0 en otro caso.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N, luego N líneas con un hito y su padre, luego L y L líneas con A y B.

## Salida

Una respuesta por línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
10
234 -1
12 234
13 234
14 234
15 234
16 234
17 234
18 234
19 234
233 19
5
234 233
233 12
233 13
233 15
233 19
```

Salida:

```
1
0
0
0
2
```

## Solución

Se recorre el árbol en profundidad y se marca en cada hito el momento
en que se entra en él y el momento en que se sale de todo su subárbol.
A es antecesor de B exactamente cuando se entra en B mientras A sigue
abierto: enter[A] ≤ enter[B] < leave[A]. Cada pregunta son dos
comparaciones. `O(N + L)`.

El recorrido usa una pila explícita. Un hito se apila junto con sus
hijos, y debajo de ellos se apila su complemento ~v para marcar el
momento en que su subárbol termina. Esto importa porque el árbol puede
ser una cadena de 40 000 hitos, demasiado profunda para la recursión en
algunos lenguajes.

Detalles a tener en cuenta:

- los hitos vienen en cualquier orden, hijos antes que padres
  (prueba 03);
- el hito 0 existe, así que la marca de salida no puede ser −v;
  ~v = −v − 1 sirve también para 0 (prueba 03);
- una cadena de 40 000 (prueba gen2);
- los hitos con el mismo padre o de ramas vecinas no son antecesores
  entre sí (prueba 05).

Las respuestas se compararon con subir por los padres en 300 árboles
aleatorios de hasta 12 hitos.

## Notas por lenguaje

- Java lee la entrada con su propio búfer de bytes, porque un flujo con
  búfer que se bloquea en cada byte es aquí bastante más lento.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1329_dfs.cpp](1329_dfs.cpp) | G++ 13.2 x64 | dfs | O(N + L) | AC | 0.078 s | 2064 KB |
| [1329_dfs.go](1329_dfs.go) | Go 1.14 x64 | dfs | O(N + L) | AC | 0.031 s | 5948 KB |
| [1329_dfs.java](1329_dfs.java) | Java 1.8 | dfs | O(N + L) | AC | 0.140 s | 2420 KB |
| [1329_dfs.py](1329_dfs.py) | Python 3.12 x64 | dfs | O(N + L) | AC | 0.156 s | 17292 KB |
| [1329_dfs.rs](1329_dfs.rs) | Rust 1.75 x64 | dfs | O(N + L) | AC | 0.046 s | 5376 KB |
