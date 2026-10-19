# 2025. Maximizar parejas entre grupos

[Timus 2025](https://acm.timus.ru/problem.aspx?space=1&num=2025) · dificultad 60 · math

Problema original de Alexey Danilyuk, del Concurso Regional Escolar de Programación de los Urales 2014.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Divide `n` objetos distintos en entre dos y `k` grupos no vacíos,
asignando cada objeto a exactamente un grupo. Una pareja no ordenada
aporta uno si sus objetos están en grupos distintos, y cero en otro
caso. Calcula el máximo número de parejas que aportan. Solo se pide el
número, no una partición concreta.

Hay `1 ≤ T ≤ 10` casos independientes, cada uno con `2 ≤ k ≤ n ≤ 10000`.
Límites: 1 segundo y 64 MB.

## Entrada

La primera línea contiene `T`. Cada una de las siguientes `T` líneas
contiene `n` y `k`.

## Salida

Para cada caso, imprime un entero en una línea, respetando el orden de entrada.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
3
6 3
5 5
4 2
```

```
12
10
4
```

## Solución

Primero, conviene usar los `k` grupos. Si solo hay `m < k`, entonces `n
≥ k > m` obliga a que algún grupo tenga al menos dos objetos. Sepáralo
en dos partes no vacías de tamaños `a` y `b`. Se conservan todas las
parejas anteriores entre grupos y se añaden las `ab > 0` parejas entre
las dos partes. Usar menos grupos es peor.

Con exactamente `k` grupos de tamaños `s₁, …, sₖ`, el número de parejas
entre grupos es `(n² - Σ sᵢ²) / 2`. El término `n²` cuenta todas las
parejas ordenadas; los cuadrados eliminan las parejas internas,
incluidas las de un objeto consigo mismo. Cada pareja no ordenada
restante aparece dos veces, por lo que se divide entre dos.

Hay que minimizar la suma de cuadrados. Si dos tamaños cumplen `a ≥
b+2`, mover un objeto del grupo grande al pequeño cambia esa suma en
`(a-1)² + (b+1)² - a² - b² = -2(a-b-1) < 0`, aumentando el total en
`a-b-1` parejas. Así, en un óptimo los tamaños no difieren en dos o más.
Repetir estas mejoras termina en tamaños equilibrados; todas las
particiones equilibradas tienen la misma suma de cuadrados y alcanzan el
máximo.

Sean `q = n // k` y `r = n % k`: hay `r` grupos de tamaño `q+1` y `k-r`
de tamaño `q`. Son no vacíos porque `k ≤ n`. La respuesta es `(n² -
(k-r)q² - r(q+1)²) / 2`. Usa división entera; el numerador es par porque
el cuadrado de cada entero tiene su misma paridad.

En el ejemplo, los tamaños `2,2,2` dan 12 parejas; cinco grupos
unitarios dan 10; los tamaños `2,2` dan 4. También se puede comprobar
que `k = n` da `n(n-1)/2` y `k = 2` da `floor(n²/4)`.

Cada caso requiere `O(1)` tiempo aritmético y `O(1)` espacio de trabajo;
todos requieren `O(T)` tiempo. El almacenamiento de entrada o salida usa
hasta `O(T)` espacio en estos programas; C++ y Go procesan los casos con
búferes de tamaño fijo.

Trampas:

- Se permite como máximo `k` grupos: demuestra por qué exactamente `k`
  es óptimo.
- Los grupos son no vacíos y cada objeto se asigna una sola vez.
- Usa el resto para distinguir tamaños `q` y `q+1`, sin promedios en
  coma flotante.
- Las parejas no son ordenadas: la fórmula de cuadrados necesita dividir
  entre dos.
- Lee todos los casos y escribe una respuesta por línea. El máximo es 49995000;
  los enteros amplios mantienen exactos todos los productos.

## Notas por lenguaje

C++ usa `long long`, Go `int64`, Java `long` y Rust `u64`. Python usa
enteros exactos y `divmod`. La resta sin signo de Rust es segura: la
suma de cuadrados internos no supera `n²`. Todos calculan el cociente y
el resto enteros, sin construir la partición. CPython no necesita otro
entorno.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2025_math.cpp](2025_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.031 s | 444 KB |
| [2025_math.go](2025_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1128 KB |
| [2025_math.java](2025_math.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 392 KB |
| [2025_math.py](2025_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 448 KB |
| [2025_math.rs](2025_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 228 KB |
