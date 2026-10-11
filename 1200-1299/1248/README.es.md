# 1248. Sumar números con 19 cifras significativas

[Timus 1248](https://acm.timus.ru/problem.aspx?space=1&num=1248) · dificultad 658 · math

Problema original de Alexander Klepinin, del Concurso Individual de la Universidad Estatal de los Urales, 1 de marzo de 2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay que sumar hasta 1000 números en notación exponencial con 19 cifras
significativas cada uno, todos entre 10⁻¹⁰⁰ y 10¹⁰⁰, e imprimir la suma
en notación exponencial con 19 cifras significativas correctas.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y luego los N números, uno por línea.

## Salida

La suma, como `d.ddddddddddddddddddeE`.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
1.5e3
1.5e-3
```

Salida:

```
1.500001500000000000e3
```

## Solución

Un double guarda solo 15–17 cifras, e incluso un long double de 80 bits
pierde los términos pequeños junto a los grandes, así que la suma se hace
exacta. Cada entrada es un múltiplo entero de 10⁻³⁰⁰ (19 cifras cerca
de 10⁻¹⁰⁰ llegan a 10⁻¹¹⁸), así que al multiplicarla por 10³⁰⁰ se
convierte en un entero exacto: las cifras de la mantisa por una potencia
de diez. Los enteros se suman exactamente, la suma se corta a sus 19
cifras más altas redondeando el resto a la mitad hacia arriba, y se
imprime con el exponente `(número de cifras − 1) − 300`. Si el redondeo
convierte las 19 cifras en 10¹⁹, la mantisa pasa a ser un 1 seguido de
ceros y el exponente crece en uno. `O(N · L)` con L ≈ 400 cifras.

Detalles a tener en cuenta:

- los términos más allá de la 19.ª cifra aún pueden afectar al
  redondeo: la prueba 04 cae justo en la
  mitad y la 05 justo por debajo;
- la suma de dos números por debajo de 10¹⁰⁰ puede redondearse a 2·10¹⁰⁰
  (prueba 03); el redondeo puede pasar a una nueva potencia de diez (prueba 08);
- el exponente se imprime tal cual, `e3` y `e-100`, sin signo más ni ceros
  a la izquierda.

## Notas por lenguaje

- Python usa sus enteros exactos y Go `math/big`; Java suma `BigDecimal` y
  redondea con `MathContext(19, HALF_UP)`; C++ y Rust guardan una suma de
  cifras con signo por cada potencia de diez y reparten los acarreos al
  final.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1248_math.cpp](1248_math.cpp) | G++ 13.2 x64 | math | O(N · L) | AC | 0.015 s | 404 KB |
| [1248_math.go](1248_math.go) | Go 1.14 x64 | math | O(N · L) | AC | 0.015 s | 2084 KB |
| [1248_math.java](1248_math.java) | Java 1.8 | math | O(N · L) | AC | 0.125 s | 1716 KB |
| [1248_math.py](1248_math.py) | Python 3.12 x64 | math | O(N · L) | AC | 0.093 s | 536 KB |
| [1248_math.rs](1248_math.rs) | Rust 1.75 x64 | math | O(N · L) | AC | 0.031 s | 252 KB |
