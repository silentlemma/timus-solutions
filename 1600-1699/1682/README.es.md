# 1682. El profesor chiflado

[Timus 1682](https://acm.timus.ru/problem.aspx?space=1&num=1682) · dificultad 539 · dsu

Problema original de Pavel Egorov, del X Campeonato Abierto Individual de la Universidad Estatal de los Urales, 28 de febrero de 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se escriben uno a uno los números 1, 2, 3, … Un número nuevo a se une
con cada número anterior b tal que b + a² ≡ 0 o a + b² ≡ 0 (mod k).
Imprimir el número tras el cual el grafo tiene un ciclo por primera
vez, o −1 si nunca lo tiene.

## Entrada

k (1 ≤ k ≤ 100000).

## Salida

Ese número.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
```

Salida:

```
5
```

## Solución

Que dos números estén unidos depende solo de sus restos. Cada resto r
tiene la pareja s = −r² mod k, y todos los números de resto r están
unidos a todos los de resto s. Si s ≠ r, dos números de cada resto ya
forman un 4-ciclo; si s = r, tres números de resto r forman un
triángulo. Ambas cosas ocurren a más tardar en el número 3k, así que
siempre aparece un ciclo y nunca se imprime −1.

Así que se simula. Se guardan los números escritos agrupados por resto
y una unión-búsqueda sobre los números. Para un número nuevo a de resto
r, los vecinos anteriores son los números de resto −r² mod k y los de
resto s con s² ≡ −r; los restos s con un −s² mod k dado se listan de
antemano. Las aristas se añaden una a una: una arista entre dos números
del mismo árbol cierra el primer ciclo, y a es la respuesta. Cualquier
otra arista une dos árboles, lo que ocurre menos de 3k veces en total,
así que el trabajo es `O(k α(k))`.

Trampas:

- las dos condiciones pueden señalar el mismo resto; hay que tomarlo
  una sola vez, o la misma arista cuenta dos veces y crea un ciclo
  falso;
- con k = 1 todo par está unido y la respuesta es 3;
- r · r llega a 10¹⁰, más de 32 bits, así que los restos se elevan al
  cuadrado en aritmética de 64 bits.

Las respuestas coinciden con una implementación aceptada independiente
para todo k ≤ 299 y para 34 valores de k mayores.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1682_dsu.cpp](1682_dsu.cpp) | G++ 13.2 x64 | dsu | O(k α(k)) | AC | 0.062 s | 7344 KB |
| [1682_dsu.go](1682_dsu.go) | Go 1.14 x64 | dsu | O(k α(k)) | AC | 0.062 s | 15044 KB |
| [1682_dsu.java](1682_dsu.java) | Java 1.8 | dsu | O(k α(k)) | AC | 0.218 s | 26412 KB |
| [1682_dsu.py](1682_dsu.py) | Python 3.12 x64 | dsu | O(k α(k)) | AC | 0.359 s | 27804 KB |
| [1682_dsu.rs](1682_dsu.rs) | Rust 1.75 x64 | dsu | O(k α(k)) | AC | 0.109 s | 12944 KB |
