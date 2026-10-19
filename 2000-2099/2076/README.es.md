# 2076. Un círculo sobre un eje de simetría de una curva cuadrática

[Timus 2076](https://acm.timus.ru/problem.aspx?space=1&num=2076) · dificultad 6156 · geometry, math

Problema original de Mikhail Rubinchik.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una curva es el conjunto de puntos (a t² + b t + c, d t² + e t + f) para
todo t real. Un punto P se proyecta sobre uno de los ejes de simetría de
la curva, lo que da un punto Q. ¿El disco cerrado de centro Q y radio R
corta la curva? Responder `YES` si ocurre para todo eje, `NO` si no
ocurre para ninguno y `MAYBE` si depende del eje. Se garantiza que la
curva tiene al menos un eje. Los límites son 2 segundos y 256 MB.

## Entrada

T ≤ 7000 pruebas, cada una de tres líneas `a b c`, `d e f`, `Px Py R`
de enteros con valor absoluto hasta 10²⁰, R ≥ 1.

## Salida

`YES`, `NO` o `MAYBE` para cada prueba.

## Ejemplos

### Ejemplo 1

Entrada:

```
1
0 1 0
1 0 0
2 1 1
```

Salida:

```
YES
```

## Solución

Se escribe la curva como C + B t + A t² con A = (a, d), B = (b, e),
C = (c, f), y sea W = P − C. La curva es un punto, una recta, un rayo o
una parábola.

- A = B = 0: un solo punto C. Toda recta por C es un eje, y el pie Q
  recorre la circunferencia de diámetro CP, desde el propio C (distancia
  0) hasta P (distancia |CP|). Así que la respuesta es `YES` si
  |CP| ≤ R y `MAYBE` en otro caso.
- A = 0, B ≠ 0: una recta. La propia recta es un eje, con Q sobre ella,
  lo que da `YES`. Toda recta perpendicular también es un eje, y Q queda
  a la distancia de P a la recta, |W × B| / |B|. De nuevo `YES` o
  `MAYBE`.
- A ≠ 0: el único eje es la recta por el vértice con dirección A (para
  una parábola, y también para un rayo, cuando A × B = 0). Con
  t₀ = −(A·B) / (2|A|²) en el vértice, la coordenada de Q a lo largo del
  eje medida desde el vértice resulta N / (4|A|³), donde
  N = 4|A|² (W·A) + (A·B)². En sentido transversal la parábola se abre como
  s = κw² con κ = |A|³ / K, K = (A × B)².

Para un punto Q = (s, 0) del eje, el cuadrado de la distancia a la curva
es el mínimo sobre u = w² ≥ 0 de (κu − s)² + u. Su derivada se anula en
u = s/κ − 1/(2κ²). Si eso no es positivo (s ≤ 1/(2κ), es decir,
N ≤ 2K), el punto más cercano es el vértice, a distancia |s|, y la
prueba es N² ≤ 16 R² |A|⁶. Si no, el cuadrado de la distancia es
s/κ − 1/(4κ²) = K (N − K) / (4|A|⁶), y la prueba es
K (N − K) ≤ 4 R² |A|⁶. Para un rayo K = 0, y las fórmulas siguen
diciendo lo correcto: dentro del rayo la distancia es 0, detrás de su
extremo es |s|. La respuesta es `YES` o `NO`, ya que hay un solo eje.

Todo se compara de forma exacta. Las entradas llegan a 10²⁰, así que los
productos llegan a unos 10¹⁶³: Python, Go y Java usan sus enteros
grandes, mientras que las soluciones en C++ y Rust llevan un pequeño
entero grande con signo propio, con suma, resta, multiplicación y
comparación sobre dígitos de 32 bits. El trabajo es O(1) operaciones con
números grandes por prueba.

En el ejemplo la curva es la parábola y = x², el eje es x = 0, y
Q = (0, 1) está en el lado interior de la parábola a distancia √3/2 < 1
de ella, así que la respuesta es `YES`.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2076_geometry_math.cpp](2076_geometry_math.cpp) | G++ 13.2 x64 | geometry, math | O(T) | AC | 0.312 s | 444 KB |
| [2076_geometry_math.go](2076_geometry_math.go) | Go 1.14 x64 | geometry, math | O(T) | AC | 0.093 s | 6760 KB |
| [2076_geometry_math.java](2076_geometry_math.java) | Java 1.8 | geometry, math | O(T) | AC | 0.203 s | 17400 KB |
| [2076_geometry_math.py](2076_geometry_math.py) | Python 3.12 x64 | geometry, math | O(T) | AC | 0.109 s | 6764 KB |
| [2076_geometry_math.rs](2076_geometry_math.rs) | Rust 1.75 x64 | geometry, math | O(T) | AC | 0.281 s | 2144 KB |
