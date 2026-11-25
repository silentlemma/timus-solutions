# 1854. Negociaciones con los partos

[Timus 1854](https://acm.timus.ru/problem.aspx?space=1&num=1854) · dificultad 424 · number_theory

Problema original de Grigoriy Nazarov, del Ural SU Team.GOV Contest en la sesión de verano de Petrozavodsk, agosto de 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

El emperador Adriano sacrifica un rebaño de n carneros, con n impar,
repartiéndolo por igual entre cierto número de dioses. Teón de Esmirna
quiere que ese número sea impar y tenga un número impar de divisores
positivos. Hallar el mayor número de dioses así.

## Entrada

Un entero impar n (1 ≤ n ≤ 10¹⁸ − 1).

## Salida

El mayor número de dioses que sirve.

## Ejemplos

### Ejemplo 1

Entrada:

```
45
```

Salida:

```
9
```

## Solución

Un número tiene una cantidad impar de divisores exactamente cuando es
un cuadrado perfecto: los divisores se emparejan como k y m/k, y solo un
cuadrado tiene un divisor emparejado consigo mismo. Todo divisor de un n
impar es impar, así que la respuesta es el mayor cuadrado que divide a
n, el producto de p^(2⌊e/2⌋) sobre las potencias de primos p^e de n.

Se extraen los primos impares p mientras p³ ≤ n, con n disminuyendo por
el camino. Lo que queda no tiene factores primos hasta su raíz cúbica,
así que es 1, un primo, un producto de dos primos o el cuadrado de un
primo, y solo el último aporta un cuadrado: se comprueba con una raíz
cuadrada entera exacta. La división de prueba da como mucho 10⁶ pasos,
y la solución en Python solo prueba los primos de una criba.
`O(n^(1/3))`.

En el ejemplo 45 = 3²·5, así que la respuesta es 9.

Trampas:

- el cuadrado de un primo grande, como (10⁹ − 63)², queda tras la
  división de prueba y hay que reconocerlo igualmente;
- la raíz cuadrada en coma flotante de un número cercano a 10¹⁸ puede
  equivocarse en uno; se corrige con comprobaciones enteras.

Las respuestas coinciden con una búsqueda directa en cien números
pequeños y con una implementación aceptada independiente en primos
grandes, productos de dos primos grandes, cuadrados de primos grandes y
productos de muchos primos pequeños.

## Soluciones optimizadas

`1854_number_theory_optimized.py`. Conserva la factorización exacta del mayor divisor cuadrado para la entrada impar garantizada. Quita todos los factores tres y prueba solo divisores 6k-1 y 6k+1. Tras quitar cada potencia prima, isqrt exacto permite devolver un resto cuadrado; al terminar el bucle hasta la raíz cúbica decreciente solo un resto cuadrado contribuye. Sin criba ni respuestas guardadas. O(n^(1/3)) divisiones y estado aritmético constante para n<10^18; conserva la base Python legible con criba.

Accepted exacto PyPy 3.10 x64 #11327061: 0.125 s / 1068 KB. Comparación guardada del 2026-11-20 de compiladores Python actuales: tiempo 2/23, memoria 7/23; ambas metas estrictas de diez primeros pasan. Desde 1024 KB se exigen tiempo y memoria. No cumple la meta propia de primero en ambas: conserva el asterisco. Registro optimizado CPython 3.12 anterior #11314964: 0.203 s / 392 KB. El PyPy elegido registra menor tiempo pero más memoria; son pares independientes en intérpretes distintos, sin atribuir toda mejora al algoritmo ni mezclar mínimos. La base CPython conservada tiene Accepted actual #11327562: 0.171 s / 1928 KB. No necesita copia extra ni reenvío.

Accepted propios tras cambiar solo formato: `1854_number_theory.java` #11327560, `1854_number_theory.cpp` #11327561, `1854_number_theory.py` #11327562. Conserva algoritmos básicos y todos los demás fuentes.

Go, Python y Rust mantienen la división de prueba hasta la raíz cúbica del resto decreciente. Si la entrada o el resto tras quitar un factor es cuadrado, puede devolverse entero como su mayor divisor cuadrado. Python elimina la criba de un millón de elementos, quita por separado el factor tres y prueba solo 6k±1: estado aritmético constante y O(n^(1/3)) pruebas. Un divisor compuesto no divide el resto una vez quitados sus factores primos menores. Python usa isqrt exacto; Go y Rust, raíz cuadrada binaria entera acotada por 10⁹. Incluso el siguiente cubo en 1000001 cabe en 64 bits con signo; el factor cuadrado acumulado divide el n original. Go usa manejadores estándar y Rust una entrada C con E/S de caracteres acotada. Se conservan las bases, incluida la criba Python; C++ y Java reutilizan las ya admitidas para la cobertura rápida.

Las bases Accepted conservadas [1854_number_theory.cpp](1854_number_theory.cpp), [1854_number_theory.java](1854_number_theory.java) cumplen diez primeros o 15% superior en las métricas exigidas de la comparación guardada, sin copias optimizadas idénticas. La tabla contiene pares actuales exactos; el asterisco indica la meta propia del lenguaje. El formato no cambia algoritmos ni recibe crédito por mejoras de velocidad.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1854_number_theory.cpp](1854_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(n^(1/3)) | AC | 0.015 s | 112 KB | 11327561 |
| [1854_number_theory.go](1854_number_theory.go) | Go 1.14 x64 | number_theory | O(n^(1/3)) | AC | 0.031 s | 1160 KB | 11290776 |
| [1854_number_theory.java](1854_number_theory.java) \* | Java 1.8 | number_theory | O(n^(1/3)) | AC | 0.125 s | 488 KB | 11327560 |
| [1854_number_theory.py](1854_number_theory.py) | Python 3.12 x64 | number_theory | O(n^(1/3)) | AC | 0.171 s | 1928 KB | 11327562 |
| [1854_number_theory.rs](1854_number_theory.rs) | Rust 1.75 x64 | number_theory | O(n^(1/3)) | AC | 0.062 s | 224 KB | 11290781 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1854_number_theory_optimized.go](1854_number_theory_optimized.go) \* | Go 1.14 x64 | number_theory | O(n^(1/3)) | AC | 0.031 s | 280 KB | 11314959 |
| [1854_number_theory_optimized.py](1854_number_theory_optimized.py) | PyPy 3.10 x64 | number_theory | O(n^(1/3)) trial divisions; O(1) arithmetic state | AC | 0.125 s | 1068 KB | 11327061 |
| [1854_number_theory_optimized.rs](1854_number_theory_optimized.rs) \* | Rust 1.75 x64 | number_theory | O(n^(1/3)) | AC | 0.031 s | 48 KB | 11314970 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
