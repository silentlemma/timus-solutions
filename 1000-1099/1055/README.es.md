# 1055. El número de divisores primos de un coeficiente binomial

[Timus 1055](https://acm.timus.ru/problem.aspx?space=1&num=1055) · dificultad 422 · number_theory

Problema original de la Academia Estatal de Aviación de Rybinsk.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dados `1 ≤ M < N ≤ 50000`, halla cuántos primos distintos dividen al
coeficiente binomial `C(N, M) = N! / (M! · (N − M)!)`.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y `M`.

## Salida

El número de divisores primos distintos de `C(N, M)`.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 3
```

Salida:

```
2
```

### Ejemplo 2

Entrada:

```
10 5
```

Salida:

```
3
```

## Solución

`C(N, M)` tiene decenas de miles de cifras, así que nunca se calcula. Solo
los primos hasta `N` pueden dividirlo, y el exponente de un primo `p` en
`x!` lo da la fórmula de Legendre:

```text
e_p(x!) = ⌊x/p⌋ + ⌊x/p²⌋ + ⌊x/p³⌋ + …
```

así que `p` divide a `C(N, M)` exactamente cuando
`e_p(N!) − e_p(M!) − e_p((N − M)!) > 0`. Una criba de Eratóstenes da los
primos hasta `N`, y cada primo cuesta `O(log N)` divisiones:
`O(N log log N)` en total.

Detalles a tener en cuenta:

- los factoriales desbordan enseguida: se trabaja solo con exponentes;
- hay que comprobar todos los primos hasta `N`, también los mayores que
  `N / 2`;
- `M = N − 1` da `C = N`, cuyos divisores primos son los de `N`.

Una prueba equivalente es el teorema de Kummer: `p` divide a `C(N, M)`
exactamente cuando sumar `M` y `N − M` en base `p` produce un acarreo.
Las pruebas se comprobaron con él y, para `N ≤ 3000`, factorizando el
coeficiente exacto.

## Notas por lenguaje

- Todos los lenguajes usan la misma criba; Python marca los múltiplos de
  un primo con una sola asignación de corte sobre un `bytearray`.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1055_number_theory.cpp](1055_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(N log log N) | AC | 0.015 s | 184 KB |
| [1055_number_theory.go](1055_number_theory.go) | Go 1.14 x64 | number_theory | O(N log log N) | AC | 0.015 s | 1112 KB |
| [1055_number_theory.java](1055_number_theory.java) | Java 1.8 | number_theory | O(N log log N) | AC | 0.093 s | 1680 KB |
| [1055_number_theory.py](1055_number_theory.py) | Python 3.12 x64 | number_theory | O(N log log N) | AC | 0.078 s | 580 KB |
| [1055_number_theory.rs](1055_number_theory.rs) | Rust 1.75 x64 | number_theory | O(N log log N) | AC | 0.031 s | 268 KB |
