# 1329. Historia galáctica

[Timus 1329](https://acm.timus.ru/problem.aspx?space=1&num=1329) · dificultad 453 · dfs

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
abierto: enter[A] ≤ enter[B] < leave[A]. Cada pregunta requiere hasta dos
comprobaciones de intervalos. `O(N + L)`.

El recorrido usa una pila explícita. Tras sacar un hito, se apila su
complemento ~v antes que sus hijos para marcar el
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

## Soluciones optimizadas

Los nuevos fuentes C++, Go y Rust mantienen intervalos DFS con cinco campos de 16 bits por identificador: padre, primer hijo, siguiente hermano, entrada y salida. Identificadores y reloj no superan 40000; 65535 es un centinela distinto incluso del nodo cero. La tabla U=40001 contiene 400010 bytes de campos. Al entrar se baja al primer hijo; al terminar se visita un hermano o se asciende por los padres hasta encontrarlo. Cada arista se recorre como máximo dos veces, sin recursión ni pila de eventos. Se leen todas las aristas antes del recorrido. Inicializar cuesta O(U); recorrer y consultar O(N+L). C++ usa entrada C stdio acotada, Go búferes de manejadores estándar; Rust retiene además el texto de entrada. Se conservan las bases; Java/Python reutilizan las ya admitidas.

El envío aceptado en Rust 1.75 x64 tarda 0.062 s frente a 0.046 s de la base y usa 2 116 KB frente a 5376 KB.

Las implementaciones base aceptadas [1329_dfs.java](1329_dfs.java), [1329_dfs.py](1329_dfs.py) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Notas por lenguaje

Estas notas describen las implementaciones sencillas.

- Java lee la entrada con su propio búfer de bytes, porque un flujo con
  búfer que se bloquea en cada byte es aquí bastante más lento.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1329_dfs.cpp](1329_dfs.cpp) | G++ 13.2 x64 | dfs | O(N + L) | AC | 0.078 s | 2064 KB | 11284994 |
| [1329_dfs.go](1329_dfs.go) | Go 1.14 x64 | dfs | O(N + L) | AC | 0.031 s | 5948 KB | 11284995 |
| [1329_dfs.java](1329_dfs.java) | Java 1.8 | dfs | O(N + L) | AC | 0.140 s | 2420 KB | 11284997 |
| [1329_dfs.py](1329_dfs.py) \* | Python 3.12 x64 | dfs | O(N + L) | AC | 0.156 s | 17292 KB | 11284996 |
| [1329_dfs.rs](1329_dfs.rs) | Rust 1.75 x64 | dfs | O(N + L) | AC | 0.046 s | 5376 KB | 11284998 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1329_dfs_optimized.cpp](1329_dfs_optimized.cpp) | G++ 13.2 x64 | dfs | O(U + N + L) | AC | 0.015 s | 468 KB | 11315161 |
| [1329_dfs_optimized.go](1329_dfs_optimized.go) \* | Go 1.14 x64 | dfs | O(U + N + L) | AC | 0.031 s | 692 KB | 11315171 |
| [1329_dfs_optimized.rs](1329_dfs_optimized.rs) \* | Rust 1.75 x64 | dfs | O(U + N + L) | AC | 0.062 s | 2116 KB | 11315177 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
