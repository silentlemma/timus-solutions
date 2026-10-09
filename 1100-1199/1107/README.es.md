# 1107. Separar multiconjuntos que difieren en un elemento

[Timus 1107](https://acm.timus.ru/problem.aspx?space=1&num=1107) · dificultad 424 · math

Problema original de Dmitry Filimonenkov, del Tetrahedron Team Contest, mayo de 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay `K ≤ 50 000` multiconjuntos distintos de artículos numerados `1..N`,
cada uno con 1 a 100 elementos; el orden de los elementos no importa, las
repeticiones sí. Dos multiconjuntos son parecidos si uno se convierte en
el otro quitando un elemento o cambiando un elemento por otro artículo.
Asigna a cada multiconjunto uno de `M` grupos (`0 < N < M ≤ 100`) de modo
que dos multiconjuntos parecidos nunca compartan grupo, o imprime `NO` si
es imposible.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N K M` y luego `K` líneas: el tamaño de un multiconjunto seguido de sus
elementos, separados por espacios simples.

## Salida

`YES` y luego el grupo de cada multiconjunto, uno por línea, en el orden
de la entrada; o `NO`.

## Evaluación

Se acepta cualquier asignación válida. El comprobador resume cada
multiconjunto como la suma de pesos aleatorios de 64 bits de sus
elementos: un multiconjunto a una eliminación de otro, o dos
multiconjuntos a un cambio de distancia, comparten entonces el resumen de
un multiconjunto con un elemento menos, y ese par no puede estar en un
mismo grupo.

## Ejemplos

### Ejemplo 1

Entrada:

```
8 20 12
5 1 3 5 6 4
5 1 3 5 6 3
4 5 6 3 3
4 5 6 3 4
4 4 6 5 8
4 7 7 7 7
3 7 7 7
2 2 2
3 2 2 7
3 1 2 3
3 1 2 4
10 1 2 3 4 5 6 7 8 7 6
10 8 7 6 5 4 3 2 1 2 1
20 1 2 3 4 5 6 7 8 1 2 3 4 5 6 7 8 1 3 5 7
5 4 6 4 6 4
5 6 4 6 4 6
6 6 6 6 6 6 6
3 6 6 6
1 1
1 2
```

Salida:

```
YES
2
1
9
1
6
2
4
5
3
7
8
5
4
8
7
9
1
1
2
3
```

## Solución

La respuesta es siempre `YES`: un multiconjunto de suma `S` va al grupo
`S mod (N + 1) + 1`, que existe porque `M ≥ N + 1`. Quitar un elemento
cambia la suma en su valor, `1..N`; cambiar un artículo por otro la
cambia en una cantidad no nula entre `−(N − 1)` y `N − 1`. Ningún cambio
es múltiplo de `N + 1`, así que los multiconjuntos parecidos siempre
reciben grupos distintos. `O(tamaño total)`.

Detalles a tener en cuenta:

- la entrada tiene hasta cinco millones de números, así que hay que leer
  rápido: un `scanf` simple o una lista de tokens por número son
  demasiado lentos o demasiado grandes;
- multiconjuntos iguales compartirían grupo, pero la entrada garantiza
  que todos son distintos.

Las respuestas se comprobaron con el comprobador de resúmenes en todas
las pruebas; el propio comprobador se contrastó con una comparación de
cada par de multiconjuntos en un centenar de entradas pequeñas, con
asignaciones correctas y aleatorias.

## Notas por lenguaje

- C++, Go y Java leen los bytes con sus propios lectores de números con
  búfer.
- Python lee toda la entrada de una vez y la parte en líneas; una lista
  de tokens con los cinco millones de números no cabría en 64 MB, y leer
  línea a línea es el doble de lento.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1107_math.cpp](1107_math.cpp) | G++ 13.2 x64 | math | O(total size) | AC | 0.015 s | 404 KB |
| [1107_math.go](1107_math.go) | Go 1.14 x64 | math | O(total size) | AC | 0.046 s | 980 KB |
| [1107_math.java](1107_math.java) | Java 1.8 | math | O(total size) | AC | 0.078 s | 1608 KB |
| [1107_math.py](1107_math.py) | Python 3.12 x64 | math | O(total size) | AC | 0.562 s | 16972 KB |
| [1107_math.rs](1107_math.rs) | Rust 1.75 x64 | math | O(total size) | AC | 0.031 s | 9300 KB |
