# 1073. La menor cantidad de parcelas cuadradas que cuestan exactamente N

[Timus 1073](https://acm.timus.ru/problem.aspx?space=1&num=1073) · dificultad 140 · number_theory

Problema original de Stanislav Vasiliev, del Ural State University Personal Contest Online, febrero de 2001, Students Session.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una parcela cuadrada de lado `a` cuesta `a²`. Hay que gastar exactamente
`N` (`1 ≤ N ≤ 60000`) en el menor número posible de parcelas, es decir,
escribir `N` como suma del menor número de cuadrados de enteros
positivos. Imprime cuántas parcelas hacen falta.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N`.

## Salida

El menor número de cuadrados.

## Evaluación

La salida se compara token a token; los espacios en blanco de más no
importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
344
```

Salida:

```
3
```

## Solución

La respuesta nunca pasa de 4: por el teorema de Lagrange todo entero
positivo es suma de cuatro cuadrados. Los demás casos se distinguen
fácilmente.

- 1 si `N` es un cuadrado perfecto.
- 2 si `N − a²` es un cuadrado perfecto para algún `1 ≤ a < √N`; son como
  mucho 244 comprobaciones.
- 4 si `N = 4^a (8b + 7)`: por el teorema de los tres cuadrados de
  Legendre, son exactamente los números que no son suma de tres
  cuadrados. Se divide entre 4 mientras se pueda y se mira el resto
  módulo 8.
- 3 en otro caso.

`O(√N)`.

Una programación dinámica sobre todas las cantidades,
`best[v] = 1 + min best[v − a²]`, en `O(N√N)`, unos 10 millones de pasos,
también entra en los límites en lenguajes compilados, pero es lenta en
Python, y los teoremas la hacen innecesaria.

Detalles a tener en cuenta:

- el factor `4^a` importa: 28 = 4 · 7 también necesita cuatro cuadrados,
  así que comprobar solo `N mod 8 = 7` no basta;
- la raíz cuadrada en coma flotante se redondea antes de volver a elevarla
  al cuadrado, para que un resultado como `6.9999…` no oculte un cuadrado
  perfecto.

La fórmula se comprobó con la programación dinámica para cada `N` hasta
60000.

## Soluciones optimizadas

La solución optimizada en Java lee el único número byte a byte con
`System.in.read` en lugar de crear un `Scanner`, así que la JVM no carga
el escáner ni sus expresiones regulares; las comprobaciones son las
mismas: {1073_number_theory_optimized.java}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1073_number_theory_optimized.java`: reducción de tiempo -14.68%;
  reducción de memoria +77.94%; base: `1073_number_theory.java`.

## Notas por lenguaje

En la clasificación del 2026-10-31, las siguientes implementaciones
básicas ya alcanzan los objetivos de tiempo y memoria. Se conservan sus
archivos en el conjunto básico; estos lenguajes no necesitan otra
implementación para alcanzar el objetivo.

- [1073_number_theory.cpp](1073_number_theory.cpp).
- [1073_number_theory.go](1073_number_theory.go).
- [1073_number_theory.rs](1073_number_theory.rs).

- Python usa `math.isqrt`, que es exacta; los demás lenguajes redondean la
  raíz cuadrada en coma flotante, lo que es exacto para números tan
  pequeños.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1073_number_theory.cpp](1073_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(√N) | AC | 0.015 s | 132 KB | 11278937 |
| [1073_number_theory.go](1073_number_theory.go) | Go 1.14 x64 | number_theory | O(√N) | AC | 0.031 s | 1076 KB | 11278938 |
| [1073_number_theory.java](1073_number_theory.java) | Java 1.8 | number_theory | O(√N) | AC | 0.109 s | 1596 KB | 11278942 |
| [1073_number_theory.py](1073_number_theory.py) | Python 3.12 x64 | number_theory | O(√N) | AC | 0.078 s | 440 KB | 11278940 |
| [1073_number_theory.rs](1073_number_theory.rs) | Rust 1.75 x64 | number_theory | O(√N) | AC | 0.015 s | 228 KB | 11278944 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1073_number_theory_optimized.java](1073_number_theory_optimized.java) \* | Java 1.8 | number_theory | O(√N) | AC | 0.125 s | 352 KB | 11304462 |

\* Aceptada; aún no cumple el objetivo de clasificación. Puede optimizarse más.
