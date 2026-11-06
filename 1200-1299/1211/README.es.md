# 1211. Acusaciones sin círculo y con una sola confesión

[Timus 1211](https://acm.timus.ru/problem.aspx?space=1&num=1211) · dificultad 311 · graphs

Problema original de Leonid Volkov, del USU Open Collegiate Programming Contest, octubre de 2002, Junior Session.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada uno de los `N ≤ 25000` niños o confiesa haber roto la taza (anotado
como 0) o señala a un niño como culpable. Las declaraciones parecen
coherentes si confesó exactamente un niño y ningún grupo de niños se
acusa en círculo. Hay que responder `YES` o `NO` para cada una de hasta
16 pruebas.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

`T` y luego, para cada prueba, `N` y las `N` declaraciones.

## Salida

`YES` o `NO` para cada prueba, una por línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
4
2 0 2 2
4
2 0 2 1
5
2 3 4 1 3
3
0 3 2
```

Salida:

```
YES
YES
NO
NO
```

## Solución

Cada niño, salvo quien confiesa, señala exactamente a uno, así que las
declaraciones forman un grafo en el que de cada vértice sale como mucho
una arista. Con exactamente una confesión, no hay círculo justo cuando,
siguiendo las acusaciones desde cualquier niño, siempre se llega a quien
confesó.

Se camina desde cada niño por turno, marcando los niños del camino
actual. El camino se detiene en quien confesó o en un niño del que ya se
sabe que lleva allí; entonces cada niño del camino también lleva allí. Si
en cambio choca con un niño marcado en el camino actual, las acusaciones
forman un círculo. Cada niño se recorre una vez. `O(N)` por prueba.

Detalles a tener en cuenta:

- un niño que se señala a sí mismo es un círculo de uno;
- ninguna confesión, o dos, ya significa `NO`;
- las cadenas pueden tener 25000 niños, así que el recorrido es un bucle
  y no una recursión.

Las respuestas se compararon con una solución escrita aparte en 200
archivos de 16 pruebas aleatorias de todos los tipos.

## Soluciones optimizadas

C++ y Go procesan las acusaciones al leerlas mediante conjuntos disjuntos. Una acusación entre vértices ya conectados cierra un ciclo no dirigido. Cada vértice del ciclo puede emitir como máximo una acusación, así que cada uno aporta exactamente una arista y el ciclo resulta dirigido. Esto incluye la autoacusación y la acusación mutua. Se exige una sola confesión y ningún ciclo. Cada entrada con signo de 16 bits guarda un índice de padre o el tamaño negativo de la componente.

Las implementaciones base aceptadas [1211_graphs.java](1211_graphs.java), [1211_graphs.py](1211_graphs.py), [1211_graphs.rs](1211_graphs.rs) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Notas por lenguaje

Estas notas describen las implementaciones sencillas.

- Todos los lenguajes recorren las cadenas de forma iterativa con los
  mismos tres estados.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1211_graphs.cpp](1211_graphs.cpp) | G++ 13.2 x64 | graphs | O(N) per test | AC | 0.265 s | 592 KB | 11283637 |
| [1211_graphs.go](1211_graphs.go) | Go 1.14 x64 | graphs | O(N) per test | AC | 0.218 s | 6820 KB | 11283638 |
| [1211_graphs.java](1211_graphs.java) \* | Java 1.8 | graphs | O(N) per test | AC | 0.156 s | 5760 KB | 11283643 |
| [1211_graphs.py](1211_graphs.py) \* | Python 3.12 x64 | graphs | O(N) per test | AC | 0.343 s | 26364 KB | 11283642 |
| [1211_graphs.rs](1211_graphs.rs) \* | Rust 1.75 x64 | graphs | O(N) per test | AC | 0.031 s | 5212 KB | 11283644 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1211_dsu.cpp](1211_dsu.cpp) | G++ 13.2 x64 | dsu | O(N α(N)) per test | AC | 0.015 s | 136 KB | 11310412 |
| [1211_dsu.go](1211_dsu.go) \* | Go 1.14 x64 | dsu | O(N α(N)) per test | AC | 0.046 s | 3228 KB | 11310413 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
