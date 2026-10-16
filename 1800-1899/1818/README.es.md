# 1818. Pescadores honrados

[Timus 1818](https://acm.timus.ru/problem.aspx?space=1&num=1818) · dificultad 1916 · number_theory

Problema original del Tavrida NU Akai Contest, sesión de verano de Petrozavodsk, agosto de 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

n pescadores reparten la captura uno tras otro. El i-ésimo en
despertar tira aᵢ peces para que el resto se divida en n partes
iguales, toma una parte y deja las otras n − 1, sin saber que otros ya
tomaron la suya. Dados todos los aᵢ, hallar la menor captura posible,
de al menos un pez.

## Entrada

n (2 ≤ n ≤ 2000), luego a₁, …, aₙ (0 ≤ aᵢ ≤ n − 1).

## Salida

La menor captura.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
1 1
```

Salida:

```
3
```

### Ejemplo 2

Entrada:

```
3
1 0 2
```

Salida:

```
19
```

## Solución

Si el pescador k encuentra Fₖ peces, necesita Fₖ ≡ aₖ (mod n), y el
siguiente encuentra Fₖ₊₁ = (Fₖ − aₖ)/n · (n − 1). Con Fₖ ≡ aₖ, la
desigualdad Fₖ ≥ aₖ se cumple sola, porque aₖ < n.

Sumar t a la captura suma t·((n − 1)/n)^(k−1) a Fₖ. Para t = s·nʲ eso
es múltiplo de n para los primeros j pescadores, cuyas condiciones se
mantienen, mientras que el pescador j + 1 recibe s·(n − 1)ʲ ≡ s·(−1)ʲ
más. Así la captura se fija cifra a cifra en base n: en el paso j se
toma el único s de [0, n) que arregla al pescador j + 1, se suma s·nʲ
a la captura y s·(n − 1)ʲ a lo que encuentra ese pescador, y se pasa al
siguiente. Las capturas válidas son exactamente un resto módulo nⁿ, así
que la respuesta es ese resto, o nⁿ si es 0.

Los números crecen hasta unas n·log₁₀ n ≈ 6600 cifras, así que todas
las soluciones usan enteros grandes: los de la biblioteca en Go, Java y
Python, y un tipo pequeño en base 10⁹ en C++ y Rust con solo las
operaciones necesarias: multiplicar y sumar, restar, dividir y tomar el
resto por un número pequeño. `O(n² log n)` operaciones con palabras de máquina.

Para el segundo ejemplo: el pescador 1 necesita X ≡ 1 (mod 3), así que
X = 1, encuentra 1 y deja 0 al pescador 2, que necesita 0: vale,
s = 0. Este deja 0 al pescador 3, que necesita 2; sumar s·9 a X le da
s·4 ≡ s más, así que s = 2 y X = 19.

Trampas:

- el resto 0 significa nⁿ peces, no 0: se pescó al menos uno;
- (n − 1)ʲ alterna entre 1 y −1 módulo n, así que la cifra cambia de
  signo en los pasos impares;
- lo que encuentra cada pescador debe guardarse exacto, no módulo n: la
  división entre n mezcla las cifras altas.

Las respuestas coinciden con una búsqueda exhaustiva para n hasta 5 y
con una implementación aceptada independiente en pruebas aleatorias
hasta n = 2000.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1818_number_theory.cpp](1818_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(n^2 log n) | AC | 0.031 s | 1032 KB |
| [1818_number_theory.go](1818_number_theory.go) | Go 1.14 x64 | number_theory | O(n^2 log n) | AC | 0.046 s | 5716 KB |
| [1818_number_theory.java](1818_number_theory.java) | Java 1.8 | number_theory | O(n^2 log n) | AC | 0.250 s | 5244 KB |
| [1818_number_theory.py](1818_number_theory.py) | Python 3.12 x64 | number_theory | O(n^2 log n) | AC | 0.109 s | 2064 KB |
| [1818_number_theory.rs](1818_number_theory.rs) | Rust 1.75 x64 | number_theory | O(n^2 log n) | AC | 0.046 s | 320 KB |
