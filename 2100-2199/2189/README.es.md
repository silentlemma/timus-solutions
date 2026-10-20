# 2189. El valor ausente en menos subarreglos bajo cambios puntuales

[Timus 2189](https://acm.timus.ru/problem.aspx?space=1&num=2189) · dificultad 1198 · fenwick, bitmask

Problema original de Artyom Abaturov y Artyom Stepanov, del Concurso Escolar de Programación de los Urales 2024.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un arreglo de n roles recibe q asignaciones puntuales. Tras cada una,
dar el menor número, sobre todo x, de subarreglos que no contienen x.
Los límites son 2 segundos y 256 MB.

## Entrada

n y q, 1 ≤ n, q ≤ 10⁵, luego a₁ … a_n con 1 ≤ aᵢ ≤ 10⁹, y luego q
cambios s r que ponen a_s = r con 1 ≤ r ≤ 10⁹.

## Salida

El mínimo tras cada cambio.

## Ejemplos

### Ejemplo 1

Entrada:

```
6 5
1 2 3 1 1 2
3 4
5 4
2 1
3 1
6 1
```

Salida:

```
4
5
4
3
1
```

### Ejemplo 2

Entrada:

```
7 4
2 3 2 3 4 2 3
1 4
4 2
6 5
2 1
```

Salida:

```
5
5
9
9
```

## Solución

Los subarreglos sin x son exactamente los que caben en los huecos entre
apariciones consecutivas de x y los dos extremos, así que un hueco de
longitud g aporta g(g + 1) / 2. Un valor ausente da n(n + 1) / 2, el
máximo posible, así que solo importan los valores presentes.

Quitar una aparición en p une sus dos huecos vecinos, y con las
apariciones más cercanas ℓ < p < r (o los extremos 0 y n + 1) la cuenta
crece exactamente en (p − ℓ)(r − p); añadir una aparición la reduce en
el mismo producto. Así un cambio modifica las puntuaciones de dos
valores en uno de esos productos cada uno, una vez conocidos los vecinos
de p entre sus apariciones.

Todas las posiciones que un valor ocupará se conocen tras leer la
entrada, así que cada valor guarda sus posiciones candidatas ordenadas,
con una estructura que marca las actuales: un árbol de Fenwick con
búsqueda del k-ésimo uno en los lenguajes compilados, y en Python un
bitset de palabras de 64 bits con un resumen de palabras no vacías. El
mínimo sobre los valores es un montículo de pares (puntuación, valor)
donde las entradas obsoletas se saltan al llegar a la cima.

En el primer ejemplo tras el primer cambio el arreglo es
[1, 2, 4, 1, 1, 2], y el valor 1 deja huecos de longitudes 2 y 1, lo que
da 3 + 1 = 4.

Cada cambio cuesta O(log n), y los recorridos de palabras en Python son
cortos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2189_bitmask.py](2189_bitmask.py) | Python 3.12 x64 | bitmask | O((n + q) log n) | AC | 1.109 s | 53288 KB |
| [2189_fenwick.cpp](2189_fenwick.cpp) | G++ 13.2 x64 | fenwick | O((n + q) log n) | AC | 0.125 s | 12016 KB |
| [2189_fenwick.go](2189_fenwick.go) | Go 1.14 x64 | fenwick | O((n + q) log n) | AC | 0.203 s | 43852 KB |
| [2189_fenwick.java](2189_fenwick.java) | Java 1.8 | fenwick | O((n + q) log n) | AC | 0.296 s | 18440 KB |
| [2189_fenwick.rs](2189_fenwick.rs) | Rust 1.75 x64 | fenwick | O((n + q) log n) | AC | 0.125 s | 16668 KB |
