# 1800. La ley de Murphy

[Timus 1800](https://acm.timus.ru/problem.aspx?space=1&num=1800) · dificultad 169 · math

Problema original de Alex Samsonov, de la subregión oriental del NEERC 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una tostada, un segmento delgado de longitud l, cae desde la altura h
con la mantequilla hacia abajo, sostenida horizontal. Cae libremente
(g = 9,81 m/s²) y gira alrededor de su centro a ω revoluciones por
minuto en un plano vertical. ¿Qué lado toca primero el suelo? Se
garantiza que no lo toca estando vertical.

## Entrada

l y h en centímetros y ω en revoluciones por minuto, enteros de 1 a
1000.

## Salida

"butter" o "bread".

## Ejemplos

### Ejemplo 1

Entrada:

```
10 400 15
```

Salida:

```
butter
```

### Ejemplo 2

Entrada:

```
10 500 15
```

Salida:

```
bread
```

## Solución

Se convierten las longitudes a metros y ω a radianes por segundo.
Tras t segundos el centro está a h − g·t²/2 y la tostada ha girado
ω·t, así que su extremo inferior está a
gap(t) = h − g·t²/2 − (l/2)·|sin ωt|. La respuesta solo depende del
cuarto de vuelta en que gap llega a cero por primera vez: en los
cuartos 0 y 3 de una vuelta la mantequilla mira hacia abajo, en el 1 y
el 2 el pan. Así que se recorren los cuartos en orden.

En un cuarto par |sin ωt| crece, el extremo inferior baja más rápido
que el centro y gap solo decrece: la tostada toca en él exactamente
cuando gap ≤ 0 al final del cuarto. En un cuarto impar el extremo sube
respecto al centro, y gap puede bajar, luego subir y luego bajar de
nuevo. Su derivada ahí es cóncava, pues la tercera derivada es
(l/2)·ω³·cos ≤ 0. Se halla el pico de la derivada por bisección sobre
la segunda derivada. Si la derivada en el pico es positiva, una
segunda bisección encuentra dónde se vuelve positiva, el mínimo local
de gap. El cuarto contiene el primer contacto si ese mínimo o el valor
al final es como mucho cero. El centro llega al suelo en
aproximadamente 1,5 segundos, así que hay como mucho un centenar de
cuartos. `O(ω)`.

En el primer ejemplo la tostada gira un cuarto de vuelta por segundo y
cae tras unos 0,9 s, a unos 81°: mantequilla. Desde 5 m cae justo
pasados los 90°: pan.

Trampas:

- el extremo de la tostada puede tocar antes de que el centro haya
  caído mucho: una tostada larga sostenida baja toca en el primer
  cuarto (pruebas 05 y 06, ambas butter);
- en un cuarto impar gap no es monótona, así que su valor al final del
  cuarto puede perder un contacto;
- las unidades: centímetros a metros, revoluciones por minuto a
  radianes por segundo;
- los generadores usados por gen1, gen3 y gen4 también deben respetar la
  garantía de contacto no vertical. Con centímetros enteros y velocidad r
  en rpm, el primer contacto es vertical exactamente cuando
  (2h − l)·r² = 981·15²·n² para un entero positivo impar n. Se rechazan
  estos casos mediante aritmética entera exacta; no tienen un lado de
  salida especificado.

Las respuestas coinciden con un oráculo independiente que subdivide
intervalos de tiempo en 3000 entradas aleatorias (1500 pequeñas), 64
entradas límite, las nueve pruebas guardadas y los cinco casos de
generador configurados.

## Soluciones optimizadas

La solución optimizada en C++ lee los tres números con `scanf` e imprime
el lado con `puts` en lugar de usar `iostream`, cuyo entorno de
ejecución aquí sobra; el cálculo en coma flotante es exactamente el
mismo: {1800_math_optimized.cpp}.

La solución optimizada en Java lee los tres números de un bloque de 4 KB
y los analiza a mano en lugar de usar `Scanner`, cuya maquinaria de
expresiones regulares tarda en cargarse y ocupa memoria; el cálculo en
coma flotante es exactamente el mismo: {1800_math_optimized.java}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1800_math_optimized.cpp`: reducción de tiempo +0.00%; reducción de
  memoria +73.12%; base: `1800_math.cpp`.

- `1800_math_optimized.java`: reducción de tiempo -14.68%; reducción de
  memoria +76.14%; base: `1800_math.java`.

## Notas por lenguaje

En la clasificación del 2026-10-31, las siguientes implementaciones
básicas ya alcanzan los objetivos de tiempo y memoria. Se conservan sus
archivos en el conjunto básico; estos lenguajes no necesitan otra
implementación para alcanzar el objetivo.

- [1800_math.go](1800_math.go).
- [1800_math.rs](1800_math.rs).

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1800_math.cpp](1800_math.cpp) | G++ 13.2 x64 | math | O(omega) | AC | 0.015 s | 372 KB | 11304236 |
| [1800_math.go](1800_math.go) | Go 1.14 x64 | math | O(omega) | AC | 0.031 s | 1084 KB | 11289935 |
| [1800_math.java](1800_math.java) | Java 1.8 | math | O(omega) | AC | 0.109 s | 1576 KB | 11304238 |
| [1800_math.py](1800_math.py) | Python 3.12 x64 | math | O(omega) | AC | 0.093 s | 592 KB | 11289938 |
| [1800_math.rs](1800_math.rs) | Rust 1.75 x64 | math | O(omega) | AC | 0.046 s | 236 KB | 11304241 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1800_math_optimized.cpp](1800_math_optimized.cpp) | G++ 13.2 x64 | math | O(omega) | AC | 0.015 s | 100 KB | 11307243 |
| [1800_math_optimized.java](1800_math_optimized.java) \* | Java 1.8 | math | O(omega) | AC | 0.125 s | 376 KB | 11307242 |

\* Aceptada; aún no cumple el objetivo de clasificación. Puede optimizarse más.
