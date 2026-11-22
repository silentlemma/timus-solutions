# 1756. Excavador y medio

[Timus 1756](https://acm.timus.ru/problem.aspx?space=1&num=1756) · dificultad 179 · math

Problema original de Magaz Asanov, del XI Concurso Individual Abierto de la Universidad Estatal de los Urales, 13 de marzo de 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

m excavadores cavan una zanja en exactamente d₁ días, trabajando todos
cada día. Planificar cuántos excavadores trabajan cada uno de d₂ días
para cavar la misma zanja en exactamente d₂ días contratando el menor
número posible. Se permiten días sin nadie trabajando.

## Entrada

m, d₁ y d₂ (1 ≤ m, d₁, d₂ ≤ 10000).

## Salida

d₂ números: los excavadores que trabajan cada día. Se acepta cualquier
plan óptimo.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 1 2
```

Salida:

```
1 2
```

## Solución

La zanja requiere W = m·d₁ días-excavador. Hay que contratar tantos
excavadores como trabajan el día de más carga, y d₂ días con a lo sumo
k excavadores cada uno dan a lo sumo k·d₂ días-excavador, así que hacen
falta al menos ⌈W / d₂⌉. Esa cantidad basta: con W = q·d₂ + r, se ponen
q excavadores en d₂ − r días y q + 1 en los otros r. `O(d₂)`.

En el ejemplo W = 3 en 2 días: un día con 1 excavador y otro con 2, así
que se contratan dos excavadores, no uno y medio.

Trampas:

- m·d₁ llega a 10⁸, que cabe en 32 bits pero conviene tenerlo en
  cuenta;
- cuando W < d₂ algunos días no trabaja nadie;
- los números diarios deben sumar exactamente W, no solo alcanzarlo.

Los planes pasan un verificador que comprueba la suma y el día de más
carga, en entradas pequeñas, aleatorias y cercanas al límite; una
implementación aceptada independiente imprime los mismos días en otro
orden.

## Soluciones optimizadas

`1756_math_optimized.java`. Java conserva el plan diario equilibrado: total=m*d1, low=total/d2 y extra=total%d2. Emite d2-extra días con low trabajadores y extra días con low+1, alcanzando el pico mínimo ceil(total/d2). Los días sin trabajadores siguen siendo válidos. Convierte cada uno de los dos números a bytes una vez y reutiliza un bloque de hasta 16384 bytes con grupos espacio-número, sin construir toda la línea ni escribir cada día por separado. Omite tramos vacíos sin alterar el estado del primer número. Tiempo O(d2) con cifras acotadas, espacio auxiliar fijo. Conserva la construcción didáctica.

Accepted exacto Java 1.8 #11327526: 0.093 s / 444 KB. Comparación guardada del grupo de compiladores del 2026-11-20: tiempo 4/54, memoria 1/54. Bajo 1024 KB la admisión estricta solo usa tiempo: diez primeros o 15% superior, con empates compartidos y corte porcentual redondeado hacia arriba. Conserva el asterisco por la meta propia del lenguaje: primer puesto en ambas métricas. El registro optimizado documentado antes #11307303 era 0.171 s / 456 KB; es un par histórico distinto, no la medición actual de este fuente. Las bases didácticas permanecen intactas.

- `1756_math_optimized.java`: 0.093 s / 444 KB; base didáctica conservada `1756_math.java`: 0.125 s / 2020 KB.

La solución optimizada en Python formatea una sola vez los dos números
diarios posibles y construye la línea repitiendo las dos cadenas, en
lugar de crear una lista de hasta 10000 enteros y convertir cada uno en
cadena: {1756_math_optimized.py}.

La solución optimizada en Rust formatea una sola vez los dos números
diarios posibles y los escribe directamente en un `BufWriter`, en lugar
de crear hasta 10000 cadenas y unirlas en otra más:
{1756_math_optimized.rs}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1756_math_optimized.py`: reducción de tiempo +37.60%; reducción de
  memoria +59.93%; base: `1756_math.py`.

- `1756_math_optimized.rs`: reducción de tiempo +51.61%; reducción de
  memoria +68.39%; base: `1756_math.rs`.

## Notas por lenguaje

En la clasificación del 2026-10-31, las siguientes implementaciones
básicas ya alcanzan los objetivos de tiempo y memoria. Se conservan sus
archivos en el conjunto básico; estos lenguajes no necesitan otra
implementación para alcanzar el objetivo.

- [1756_math.cpp](1756_math.cpp).
- [1756_math.go](1756_math.go).

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1756_math.cpp](1756_math.cpp) | G++ 13.2 x64 | math | O(d2) | AC | 0.015 s | 124 KB | 11304258 |
| [1756_math.go](1756_math.go) | Go 1.14 x64 | math | O(d2) | AC | 0.031 s | 1060 KB | 11289576 |
| [1756_math.java](1756_math.java) | Java 1.8 | math | O(d2) | AC | 0.125 s | 2020 KB | 11304259 |
| [1756_math.py](1756_math.py) | Python 3.12 x64 | math | O(d2) | AC | 0.125 s | 1148 KB | 11289577 |
| [1756_math.rs](1756_math.rs) | Rust 1.75 x64 | math | O(d2) | AC | 0.031 s | 620 KB | 11304260 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1756_math_optimized.java](1756_math_optimized.java) \* | Java 1.8 | math | O(d2) time; O(1) auxiliary space | AC | 0.093 s | 444 KB | 11327526 |
| [1756_math_optimized.py](1756_math_optimized.py) | Python 3.12 x64 | math | O(d2) | AC | 0.078 s | 460 KB | 11307291 |
| [1756_math_optimized.rs](1756_math_optimized.rs) | Rust 1.75 x64 | math | O(d2) | AC | 0.015 s | 196 KB | 11307300 |

\* Aceptada; aún no cumple el objetivo de clasificación. Puede optimizarse más.
