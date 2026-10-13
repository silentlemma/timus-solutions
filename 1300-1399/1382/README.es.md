# 1382. Juego de cartas

[Timus 1382](https://acm.timus.ru/problem.aspx?space=1&num=1382) · dificultad 1697 · graphs

Problema original de Alexander Ipatov, con agradecimiento especial a Dmitry Ivankov, del campus de entrenamiento de verano de Petrozavodsk, agosto de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N ≤ 1000 amigos toman en secreto una carta cada uno, numeradas de 1 a N.
Luego el amigo i hace dos afirmaciones: «tengo la carta aᵢ» y «el amigo
bᵢ tiene la carta cᵢ», con bᵢ ≠ i. Exactamente una de las dos es
verdad. Ningún par de amigos afirma lo mismo sobre la misma persona, y
nadie atribuye a un amigo la carta que ese amigo dice tener. Hay que
imprimir para cada amigo qué afirmación, 1 o 2, es verdadera; hay
solución.

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

N, luego N líneas aᵢ, bᵢ, cᵢ.

## Salida

N números 1 o 2. Se acepta cualquier respuesta coherente.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
3 4 3
1 3 2
3 2 5
2 5 4
3 4 1
```

Salida:

```
1 2 2 2 2
```

## Solución

Al amigo i se le da una variable xᵢ: verdadera si vale la primera
afirmación. Cada afirmación es una pretensión «la persona p tiene la
carta q», verdadera cuando su literal lo es. Dos pretensiones
verdaderas chocan si dan dos cartas a una persona o una carta a dos
personas.

Las reglas de la entrada hacen que todas las pretensiones sobre una
persona nombren cartas distintas, y todas las pretensiones sobre una
carta nombren personas distintas. Así que las condiciones son simples:
a lo sumo una pretensión verdadera sobre cada persona y a lo sumo una
sobre cada carta. Es 2-SAT. «A lo sumo uno» entre k literales se
codifica con k variables auxiliares s₁ … s_k: lⱼ → sⱼ para cada j,
y sⱼ₋₁ → sⱼ y sⱼ₋₁ → ¬lⱼ para j ≥ 2.
Así la fórmula sigue siendo lineal aunque una carta se nombre mil veces.
El algoritmo de Tarjan halla las componentes fuertemente conexas del
grafo de implicaciones, y un literal se toma como verdadero si su
componente va antes que la de su negación en el orden en que Tarjan las
termina.

Detalles a tener en cuenta:

- codificar directamente cada par de pretensiones que chocan exige
  499 500 cláusulas para un grupo de 1000 pretensiones sobre una misma
  carta (prueba 14);
- la afirmación falsa de cada amigo debe seguir siendo falsa; las reglas
  de la entrada lo garantizan si las pretensiones verdaderas no chocan.

Las pruebas se juzgan con un verificador que comprueba que las
pretensiones verdaderas no chocan y luego, con un emparejamiento
bipartito, que las cartas pueden repartirse de modo que todas las
pretensiones falsas sean falsas. Repartos aleatorios de 2 a 28 amigos lo
pasaron todos.

## Notas por lenguaje

- La búsqueda en profundidad del algoritmo de Tarjan lleva su propia
  pila en las cinco soluciones, porque el grafo de implicaciones tiene
  hasta 10 000 nodos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1382_graphs.cpp](1382_graphs.cpp) | G++ 13.2 x64 | graphs | O(N log N) | AC | 0.031 s | 696 KB |
| [1382_graphs.go](1382_graphs.go) | Go 1.14 x64 | graphs | O(N) | AC | 0.046 s | 3424 KB |
| [1382_graphs.java](1382_graphs.java) | Java 1.8 | graphs | O(N) | AC | 0.171 s | 5276 KB |
| [1382_graphs.py](1382_graphs.py) | Python 3.12 x64 | graphs | O(N) | AC | 0.093 s | 4616 KB |
| [1382_graphs.rs](1382_graphs.rs) | Rust 1.75 x64 | graphs | O(N) | AC | 0.046 s | 1916 KB |
