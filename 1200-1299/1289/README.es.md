# 1289. Billete de ida

[Timus 1289](https://acm.timus.ru/problem.aspx?space=1&num=1289) · dificultad 399 · math

Problema original de Leonid Volkov, del Concurso Individual de la Universidad Estatal de los Urales 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Los compartimentos de una nave están numerados de 0 a 10^N − 1, cada
número escrito con exactamente N cifras, ceros a la izquierda incluidos;
N es par y como mucho 200 000. Un compartimento vuelve libre de mineral
cuando la raíz digital de la primera mitad de su número es igual a la de
la segunda mitad. Hay que contar esos compartimentos.

La raíz digital de un número se obtiene sumando sus cifras una y otra
vez hasta que queda una sola cifra; la raíz digital de 0 es 0.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

El número par N.

## Salida

La cantidad, completa.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
```

Salida:

```
10
```

## Solución

Sea m = N / 2 y tomemos una mitad, un número de 0 a 10^m − 1. Su raíz
digital es 0 solo para el número 0. Para los positivos la raíz digital
recorre 1, 2, …, 9, 1, 2, … y 10^m − 1 es múltiplo de 9, así que cada
raíz de 1 a 9 la tienen exactamente k = (10^m − 1) / 9 números, donde
k = 11…1 se escribe con m unos. La cantidad es, por tanto,

1 + 9 · k².

Tiene hasta 200 000 cifras, pero no hace falta aritmética de enteros
grandes. Como 9 · k = 10^m − 1, resulta 9 · k² = k · 10^m − k: m unos
seguidos de m ceros, menos m unos. Para m ≥ 2 esa resta da
1…1 0 8…8 9 (m − 1 unos, m − 1 ochos), y sumar 1 convierte el 89 final
en 90:

- m = 0: 1;
- m = 1: 10;
- m ≥ 2: m − 1 unos, un 0, m − 2 ochos y luego 90.

Por ejemplo, N = 6 da 110890. La respuesta se imprime como texto,
`O(N)`.

Detalles a tener en cuenta:

- con N = 0 hay un compartimento, y cuenta (prueba 02);
- N = 2 no sigue el patrón general (prueba 01);
- la respuesta para N = 200 000 tiene 200 000 cifras (prueba gen3).

## Notas por lenguaje

- Python: desde la 3.11, convertir a texto un entero de más de 4300
  cifras da error si no se levanta el límite, otra razón para construir
  las cifras directamente.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1289_math.cpp](1289_math.cpp) | G++ 13.2 x64 | math | O(N) | AC | 0.001 s | 396 KB |
| [1289_math.go](1289_math.go) | Go 1.14 x64 | math | O(N) | AC | 0.015 s | 1688 KB |
| [1289_math.java](1289_math.java) | Java 1.8 | math | O(N) | AC | 0.093 s | 1272 KB |
| [1289_math.py](1289_math.py) | Python 3.12 x64 | math | O(N) | AC | 0.078 s | 648 KB |
| [1289_math.rs](1289_math.rs) | Rust 1.75 x64 | math | O(N) | AC | 0.001 s | 596 KB |
