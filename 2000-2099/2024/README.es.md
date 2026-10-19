# 2024. Elegir grupos completos de colores

[Timus 2024](https://acm.timus.ru/problem.aspx?space=1&num=2024) · dificultad 340 · sorting, combinatorics

Problema original de Nikita Sivukhin, del Concurso Regional Escolar de Programación de los Urales 2014.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada posición de una cadena representa un objeto distinto; su letra
minúscula indica su color. Elige un subconjunto con como máximo `k`
colores distintos. Calcula el tamaño máximo y cuántos subconjuntos
alcanzan ese tamaño. Dos subconjuntos difieren si algún índice pertenece
solo a uno. Cambiar el orden o elegir nombres de colores ausentes no
crea otro subconjunto de objetos.

Restricciones: `1 ≤ n ≤ 100000`, `1 ≤ k ≤ 26`, colores de `a` a `z`.
Tiempo: 1 segundo. Memoria: 64 MB. El número de subconjuntos es un
entero exacto, sin módulo.

## Entrada

La primera línea contiene la cadena de colores de longitud `n`; `n` no
se da aparte. La segunda contiene `k`.

## Salida

Dos enteros separados por un espacio: el tamaño máximo y el número de
subconjuntos que alcanzan ese tamaño.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
abcde
1
```

```
1 5
```

```
ababac
2
```

```
5 1
```

## Solución

Cuenta las frecuencias de los 26 colores, incluidos los ceros, y
ordénalas de mayor a menor. El tamaño máximo es la suma de las primeras
`k`. Sea `b` la frecuencia en la posición `k` de este orden.

Si `b = 0`, aparecen menos de `k` colores. Se pueden tomar todos los
objetos y existe un único subconjunto así. Elegir distintos colores
ausentes no cambia los índices.

En otro caso, sean `g` las frecuencias estrictamente mayores que `b` y
`t` las iguales a `b`. Son obligatorios los `g` grupos mayores y hay que
elegir `r = k-g` de los `t` grupos empatados en la frontera. Por tanto,
el número de opciones es `C(t,r)`.

¿Por qué bastan grupos completos? Si un color ya está elegido y falta
algún objeto de ese color, añadirlo mejora el tamaño sin aumentar el
número de colores. El conjunto anterior no podía ser óptimo. Si todavía
cabe otro color, añadir cualquier grupo positivo restante también mejora
el tamaño. Así, se eligen los `k` grupos positivos más frecuentes, o
todos cuando hay menos de `k`.

Cambiar un grupo elegido menor por otro mayor no elegido aumenta
estrictamente el tamaño. Luego todos los grupos por encima de `b` son
obligatorios, los inferiores quedan fuera y solo varían los grupos de
igual frecuencia positiva en la frontera. Cualquier elección de `r`
grupos empatados tiene el mismo tamaño. Como son no vacíos, elecciones
distintas cambian los índices de objetos. Fijados los colores, todos sus
objetos deben incluirse, sin opciones adicionales dentro de un grupo.

Para calcular el coeficiente, toma `q = min(r,t-r)`, inicia `ways = 1` y
aplica `ways = ways * (t-i+1) / i` para `i = 1..q`. Cada resultado es
`C(t,i)`, por lo que la división es exacta. Multiplica con enteros
amplios, sin factoriales: el máximo final es `C(26,13) = 10400600`, pero
`26!` no cabe en 64 bits.

En el primer ejemplo las cinco frecuencias son uno: se puede elegir un
objeto de cinco maneras. En el segundo las frecuencias son 3, 2 y 1; los
grupos de tamaños 3 y 2 dan tamaño 5 y están determinados de forma
única.

Para un alfabeto de tamaño `σ`, el tiempo es `O(n + σ log σ)` y las
frecuencias ocupan `O(σ)`. Aquí `σ = 26`, así que el tiempo es `O(n)`.
Los programas guardan la cadena: su memoria adicional total es `O(n +
σ)`, es decir, `O(n)` con este alfabeto fijo. Una alternativa es una
mochila sobre grupos completos con límite de colores, con `O(σk)`
trabajo después del recuento, útil como comprobación independiente.

Trampas:

- Se limita el número de colores distintos, no el número de objetos.
- Los objetos de un mismo color tienen índices distintos, pero el grupo
  elegido es completo.
- Cuenta subconjuntos, no permutaciones. Las frecuencias cero no añaden
  opciones.
- Resuelve los empates en la frontera, incluidos `k = 1` y `k = 26`.
- No uses factoriales ni coma flotante para este recuento exacto.

## Notas por lenguaje

C++, Go y Rust usan enteros de 64 bits para el coeficiente; Java usa
`long` y Python enteros exactos. Las sumas caben en enteros ordinarios.
Java ordena de menor a mayor y toma las últimas `k` frecuencias; los
demás toman las primeras `k` en orden descendente. Go usa `fmt.Fscan`
con lectura con búfer, que admite un token de 100000 caracteres sin el
límite predeterminado de Scanner. CPython hace el mismo recorrido
lineal.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2024_sorting_combinatorics.cpp](2024_sorting_combinatorics.cpp) | G++ 13.2 x64 | sorting, combinatorics | O(n) | AC | 0.015 s | 668 KB |
| [2024_sorting_combinatorics.go](2024_sorting_combinatorics.go) | Go 1.14 x64 | sorting, combinatorics | O(n) | AC | 0.046 s | 1772 KB |
| [2024_sorting_combinatorics.java](2024_sorting_combinatorics.java) | Java 1.8 | sorting, combinatorics | O(n) | AC | 0.109 s | 1232 KB |
| [2024_sorting_combinatorics.py](2024_sorting_combinatorics.py) | Python 3.12 x64 | sorting, combinatorics | O(n) | AC | 0.109 s | 776 KB |
| [2024_sorting_combinatorics.rs](2024_sorting_combinatorics.rs) | Rust 1.75 x64 | sorting, combinatorics | O(n) | AC | 0.046 s | 472 KB |
