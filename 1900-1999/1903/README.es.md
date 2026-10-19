# 1903. Counting Sorted Selections

[Timus 1903](https://acm.timus.ru/problem.aspx?space=1&num=1903) · difficulty 941 · combinatorics

Original problem by Alex Samsonov, prepared by Alexander Fetisov, from Ural Championship 2012.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay n identidades distintas, cada una con una clase. Elige exactamente t,
incluyendo la identidad k. Ordena las elegidas por clase no decreciente;
los empates permiten cualquier orden. k debe poder ocupar la posición x.
Cuenta conjuntos, no órdenes, módulo P = 10⁹+7. Límites: 1 segundo y 64 MB.

## Entrada

Primero n y t, con 1 ≤ t < n ≤ 5000. Después n clases cᵢ entre 1 y 5000.
Finalmente k y x, con 1 ≤ k ≤ n y 1 ≤ x ≤ t. k es el índice en la entrada
original, no el rango después de ordenar.

## Salida

El número de conjuntos válidos módulo 10⁹+7.

## Evaluación

Comparación exacta de un token entero; las pruebas usan `tokens`.

## Ejemplos

### Ejemplo 1

```
5 3
2 1 1 3 1
2 3
```

```
1
```

### Ejemplo 2

```
4 2
1 1 1 1
1 2
```

```
3
```

## Solución

Sea v = cₖ. Cuenta L clases estrictamente menores que v y G estrictamente
mayores. k no pertenece a ninguno de los grupos. Entre las otras t−1
identidades seleccionadas, sean a menores y b mayores.

El bloque de empates ocupa las posiciones a+1,…,t−b. k puede ocupar x
exactamente cuando `a ≤ x−1` y `b ≤ t−x`. No multipliques por permutaciones
de empates: solo se necesita que exista un orden.

Empieza por todos los `C(n−1,t−1)` conjuntos que incluyen k. Resta los
que tienen demasiadas clases menores:

`A = Σ(a=x…min(L,t−1)) C(L,a) C(n−1−L,t−1−a)`.

Resta también los que tienen demasiadas mayores:

`B = Σ(b=t−x+1…min(G,t−1)) C(G,b) C(n−1−G,t−1−b)`.

Cada término elige una cantidad exacta del grupo estricto y el resto
de su complemento, incluidos los empates. Las familias malas son disjuntas:
ambas exigirían `a+b ≥ t+1`, pero solo hay t−1 identidades adicionales.
La respuesta es `C(n−1,t−1) − A − B`, normalizada módulo P.

Cada conjunto que incluye k se cuenta una vez al principio. Se elimina
exactamente cuando su bloque de empates no contiene x, sin eliminación
doble. Los restantes permiten situar k en x, lo que prueba la fórmula.

Precalcula factoriales e inversos hasta n−1. Como P es primo y n < P,
todos son invertibles. Usa una potencia modular `factorial[n−1]^(P−2)`
y rellena los inversos hacia atrás. Entonces `C(N,r) = N! / (r!(N−r)!)`
se obtiene en tiempo constante; vale cero para r fuera de [0,N].

Cada suma tiene como máximo n términos. Tiempo `O(n + log P)` y espacio
`O(n)`; con P fijo el tiempo es lineal en n. No hace falta ordenar.

En el primer ejemplo, la tercera clase solo puede ser 1 si se eligen las
tres identidades de clase 1: 2, 3 y 5. En el segundo, k puede acompañarse
de cualquiera de las otras tres identidades: son tres conjuntos y no seis órdenes.

## Notas por lenguaje

Las cinco versiones usan las dos sumas malas disjuntas. C++, Go, Java y Rust
usan productos de 64 bits con reducción entre multiplicaciones; multiplicar
tres residuos sin reducir desbordaría. Normaliza cada resta inmediatamente.
Python usa CPython 3.12 y `pow` modular.

Usa comparaciones estrictas, incluye siempre k, distingue las identidades
empatadas y admite todas sus posiciones posibles. Una suma vacía vale cero;
un mínimo único no puede aparecer en la segunda posición.

Las respuestas coinciden con la enumeración de los 47 013 subconjuntos
etiquetados en 9117 consultas pequeñas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1903_combinatorics.cpp](1903_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(n + log P) | AC | 0.015 s | 428 KB |
| [1903_combinatorics.go](1903_combinatorics.go) | Go 1.14 x64 | combinatorics | O(n + log P) | AC | 0.031 s | 1232 KB |
| [1903_combinatorics.java](1903_combinatorics.java) | Java 1.8 | combinatorics | O(n + log P) | AC | 0.093 s | 540 KB |
| [1903_combinatorics.py](1903_combinatorics.py) | Python 3.12 x64 | combinatorics | O(n + log P) | AC | 0.078 s | 1588 KB |
| [1903_combinatorics.rs](1903_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(n + log P) | AC | 0.046 s | 264 KB |
