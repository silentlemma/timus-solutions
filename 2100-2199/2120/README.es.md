# 2120. Peso esperado de un árbol etiquetado aleatorio con algunos grados fijos

[Timus 2120](https://acm.timus.ru/problem.aspx?space=1&num=2120) · dificultad 1911 · math, probability

Problema original de Alexey Danilyuk, del concurso t.me/umnik_team, campamento de Petrozavodsk, verano de 2018.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

El peso de un árbol con vértices 1 … n es la suma sobre sus aristas
(u, v) de u · s(u) + v · s(v), donde s(u) es el tamaño de la parte que
contiene a u al quitar la arista. Algunos vértices tienen grado fijo y
los demás cualquier grado. Se elige uniformemente al azar un árbol con
esos grados; imprimir la parte entera de su peso esperado. Los límites
son 2 segundos y 64 MB.

## Entrada

n, 2 ≤ n ≤ 10⁶, y luego a₁ … aₙ: un grado fijo de 1 a n − 1, o −1 para
cualquier grado. La suma de |aᵢ| es a lo sumo 2n − 2.

## Salida

La parte entera del peso esperado.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
1 -1 -1 -1 -1
```

Salida:

```
67
```

### Ejemplo 2

Entrada:

```
5
-1 -1 -1 -1 1
```

Salida:

```
52
```

### Ejemplo 3

Entrada:

```
4
1 1 1 3
```

Salida:

```
42
```

### Ejemplo 4

Entrada:

```
4
1 1 2 2
```

Salida:

```
38
```

## Solución

Se agrupan los términos por vértice. Quitar las d aristas de un vértice
v divide los otros n − 1 vértices en d ramas, y en cada arista v conserva
todos los vértices menos los de esa rama, así que los tamaños s(v) de
sus aristas suman d · n − (n − 1). Por tanto el peso solo depende de los
grados:

W = Σ v · (n (d_v − 1) + 1) = n(n + 1)/2 + n · Σ v (d_v − 1).

Por los códigos de Prüfer, el número de árboles con grados d₁ … dₙ es
(n − 2)! / ∏ (d_v − 1)!, que no cambia cuando los vértices libres
intercambian sus grados. Así que todos los vértices libres tienen el
mismo d_v − 1 esperado, y esos valores suman R = n − 2 − Σ (d_v fijos − 1).
Con c vértices libres cuyas etiquetas suman S, la linealidad de la
esperanza da

E = n(n + 1)/2 + n · Σ_fijos v (d_v − 1) + n · R · S / c.

Solo el último término es fraccionario; su parte entera se calcula de
forma exacta con división entera, dividiendo primero R · S entre c con
resto para no salir de 64 bits. El trabajo es O(n).

En el tercer ejemplo todos los grados son fijos, Σ v (d_v − 1) = 4 · 2 = 8,
y W = 10 + 4 · 8 = 42.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2120_math_probability.cpp](2120_math_probability.cpp) | G++ 13.2 x64 | math, probability | O(n) | AC | 0.156 s | 448 KB |
| [2120_math_probability.go](2120_math_probability.go) | Go 1.14 x64 | math, probability | O(n) | AC | 0.062 s | 1088 KB |
| [2120_math_probability.java](2120_math_probability.java) | Java 1.8 | math, probability | O(n) | AC | 0.171 s | 572 KB |
| [2120_math_probability.py](2120_math_probability.py) | Python 3.12 x64 | math, probability | O(n) | AC | 0.468 s | 3036 KB |
| [2120_math_probability.rs](2120_math_probability.rs) | Rust 1.75 x64 | math, probability | O(n) | AC | 0.015 s | 280 KB |
