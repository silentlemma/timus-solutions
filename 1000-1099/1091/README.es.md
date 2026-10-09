# 1091. Contar conjuntos de números con un divisor común

[Timus 1091](https://acm.timus.ru/problem.aspx?space=1&num=1091) · dificultad 526 · number_theory

Problema original de Stanislav Vasiliev, del USU Open Collegiate Programming Contest, marzo de 2001, Senior Session.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cuenta los conjuntos de `K` enteros positivos distintos, ninguno mayor
que `S` (`2 ≤ K ≤ S ≤ 50`), cuyo máximo común divisor es mayor que 1.
Imprime la cuenta, o 10000 si es mayor.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`K` y `S`.

## Salida

El número de conjuntos, como mucho 10000.

## Evaluación

La salida se compara token a token; los espacios en blanco de más no
importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 10
```

Salida:

```
11
```

## Solución

Los conjuntos cuyos números son todos múltiplos de `d` son
`C(⌊S/d⌋, K)`. Un conjunto con un divisor común mayor que 1 tiene un
divisor primo común, así que la respuesta es el tamaño de la unión de
estas familias sobre los primos. La inclusión-exclusión sobre los
`d > 1` libres de cuadrados da

`respuesta = Σ −μ(d) · C(⌊S/d⌋, K)`,

donde la función de Möbius `μ(d)` es `(−1)^(número de factores primos)`
para `d` libre de cuadrados y 0 en otro caso: los productos de un número
impar de primos se suman y los de un número par se restan. Una pequeña
criba calcula `μ` hasta `S`, y los binomiales salen del triángulo de
Pascal. `O(S²)`.

Detalles a tener en cuenta:

- la cuenta real puede pasar con mucho de 10000, por ejemplo `C(25, 5)`
  conjuntos solo de números pares para `K = 5`, así que solo se limita el
  valor final y las sumas se guardan en 64 bits;
- un conjunto contado para `d = 2` y para `d = 3` también se cuenta para
  `d = 6`, y por eso los signos alternan;
- los números deben ser distintos, así que `C(m, K)` es 0 cuando `m < K`.

Las respuestas se comprobaron para todos los pares `K ≤ S ≤ 50` con las
cuentas de conjuntos de mcd exactamente `g`, halladas desde el mayor `g`
hacia abajo restando las de los múltiplos de `g`, y para `S ≤ 20` listando
todos los conjuntos.

## Notas por lenguaje

- Python usa `math.comb`; los demás lenguajes llenan una tabla de
  coeficientes binomiales.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1091_number_theory.cpp](1091_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(S^2) | AC | 0.015 s | 232 KB |
| [1091_number_theory.go](1091_number_theory.go) | Go 1.14 x64 | number_theory | O(S^2) | AC | 0.015 s | 1088 KB |
| [1091_number_theory.java](1091_number_theory.java) | Java 1.8 | number_theory | O(S^2) | AC | 0.109 s | 1640 KB |
| [1091_number_theory.py](1091_number_theory.py) | Python 3.12 x64 | number_theory | O(S^2) | AC | 0.078 s | 424 KB |
| [1091_number_theory.rs](1091_number_theory.rs) | Rust 1.75 x64 | number_theory | O(S^2) | AC | 0.046 s | 228 KB |
