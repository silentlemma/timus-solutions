# 2102. Exactamente veinte factores primos

[Timus 2102](https://acm.timus.ru/problem.aspx?space=1&num=2102) · dificultad 147 · number_theory

Problema original de Vladimir Leskov, del Campeonato Juvenil de la UrFU 2016.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Decir si en la factorización de n los exponentes suman exactamente 20,
es decir, si n es producto de exactamente 20 primos contados con
multiplicidad. Los límites son 2 segundos y 64 MB.

## Entrada

n, 1 ≤ n ≤ 10¹⁸.

## Salida

`Yes` o `No`.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
```

Salida:

```
No
```

### Ejemplo 2

Entrada:

```
1048576
```

Salida:

```
Yes
```

### Ejemplo 3

Entrada:

```
10000000000
```

Salida:

```
Yes
```

## Solución

Se divide n entre cada d de 2 a B = 2·10⁶ mientras d² ≤ n, contando los
factores primos quitados. Si el bucle se detiene porque d² supera lo que
queda, el resto es 1 o un primo y aporta 0 o 1. Si no, el resto es al
menos B² = 4·10¹², así que la parte quitada es a lo sumo 10¹⁸ / B²,
menos de 2¹⁸, es decir, menos de 18 factores hasta ahora; el resto no
tiene factores menores que B y es a lo sumo 10¹⁸ < B³, así que aporta a
lo sumo dos. El total no puede llegar a 20, y la respuesta es No. El
trabajo es O(min(sqrt n, B)).

En el tercer ejemplo 10¹⁰ = 2¹⁰ · 5¹⁰ tiene 20 factores primos.

## Soluciones optimizadas

`2102_number_theory_optimized.java`. Mantiene exactamente 20 factores primos. Quita doses y treses, prueba 6k-1/6k+1; enough comprueba el mínimo producto restante dividiendo antes de multiplicar para evitar overflow. Con hasta dos factores pendientes, un cuadrado aporta exactamente dos solo si su raíz es prima. Math.sqrt propone un candidato, aceptado únicamente tras root*root==n exacto en long; si pierde un cuadrado sigue la rueda original correcta. Tras quitar al menos 18 factores, queda como máximo 10^18/2^18; primalidad de la raíz requiere divisores menores de 1400 y la alternativa tiene cota 1953125. Lee el único long byte a byte y escribe bytes constantes. Sin tabla de respuestas ni primalidad probabilística. Código Java real comprobado en 315488 casos exactos y 100000 comparaciones del límite de producto sin overflow. Conserva la división didáctica.

Accepted exacto Java 1.8 #11327435: 0.109 s / 468 KB. Comparación guardada del grupo de compiladores del 2026-11-20: tiempo 1/78, memoria 1/78. Bajo 1024 KB la admisión estricta solo usa tiempo: diez primeros o 15% superior, con empates compartidos y corte porcentual redondeado hacia arriba. Ambas métricas son primeras; cumple también la meta propia del lenguaje, sin asterisco. El registro optimizado documentado antes #11304532 era 0.14 s / 400 KB; es un par histórico distinto, no la medición actual de este fuente. Las bases didácticas permanecen intactas.

- `2102_number_theory_optimized.java`: 0.109 s / 468 KB; base didáctica conservada `2102_number_theory.java`: 0.125 s / 1592 KB.

`2102_number_theory_optimized.py`. Mantiene exactamente 20 factores primos con multiplicidad. Quita potencias de dos y tres y prueba divisores 6k-1 y 6k+1. Si faltan más de dos factores, divisor**remaining>n demuestra rechazo. Con dos o menos usa isqrt exacto: un cuadrado solo sirve si faltan dos y su raíz es prima. Se han quitado al menos 18 factores, quedando como máximo 10^18/2^18; la prueba de primalidad de esa raíz necesita divisores menores de 1400. Los no cuadrados mantienen la rueda, con cota de divisor de 1953125 en esta fase. Límites fijos dan espacio constante, sin flotantes, primalidad probabilística ni tabla de respuestas. Este Accepted usa PyPy 3.10; la medición antigua de CPython es un par de otro runtime. Salida directa al nivel superior seguida de os._exit(0).

Accepted exacto PyPy 3.10 x64 #11327440: 0.125 s / 928 KB. Comparación guardada del grupo de compiladores del 2026-11-20: tiempo 8/28, memoria 6/28. Bajo 1024 KB la admisión estricta solo usa tiempo: diez primeros o 15% superior, con empates compartidos y corte porcentual redondeado hacia arriba. Conserva el asterisco por la meta propia del lenguaje: primer puesto en ambas métricas. El registro optimizado documentado antes #11304531 (Python 3.12 x64) era 0.265 s / 424 KB; es un par histórico distinto, no la medición actual de este fuente. Las bases didácticas permanecen intactas.

- `2102_number_theory_optimized.py`: 0.125 s / 928 KB; base didáctica conservada `2102_number_theory.py`: 0.453 s / 388 KB.

`2102_number_theory_optimized.cpp`. Conserva el recuento exacto de factores primos y la cota del producto restante. Para n positivo≤10^18, ctz cuenta todos los doses; se retiran los tres y solo se prueban divisores 6k±1. Si faltan más de dos factores, multiplica la cota en enteros sin signo de 128 bits y para al superar el resto. Antes de multiplicar, la cota es≤10^18 y el divisor ronda como máximo 10^9, de modo que el producto cabe en 128 bits. Para los dos últimos factores mantiene la cota cuadrática. ctz nunca recibe cero; la decisión sigue siendo exactamente veinte factores con multiplicidad.

Accepted del fuente exacto #11326999: 0.015 s / 108 KB. Comparación G++ 13.2 guardada el 2026-11-20: tiempo 1/113, memoria 1/113.

### Mejora medida

Cada versión optimizada conservada tiene Accepted. Cumple por situarse entre las diez primeras o el 15% superior en ambas métricas, por estar en el 30% superior en ambas y mejorar la posición base en al menos una, o por reducir al menos un 30% el tiempo o la memoria respecto a la base del mismo lenguaje. Una reducción negativa indica mayor coste. El asterisco se refiere al objetivo de clasificación específico del lenguaje.

## Notas por lenguaje

En la clasificación del 2026-10-31, las siguientes implementaciones
básicas ya alcanzan los objetivos de tiempo y memoria. Se conservan sus
archivos en el conjunto básico; estos lenguajes no necesitan otra
implementación para alcanzar el objetivo.

- [2102_number_theory.rs](2102_number_theory.rs).

Accepted del fuente exacto #11326999: 0.015 s / 108 KB; base conservada: 0.031 s / 116 KB. El tiempo se compara con suelo 0.015 s.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2102_number_theory.cpp](2102_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(min(sqrt n, B)) | AC | 0.031 s | 116 KB | 11304072 |
| [2102_number_theory.go](2102_number_theory.go) | Go 1.14 x64 | number_theory | O(min(sqrt n, B)) | AC | 0.046 s | 1120 KB | 11294722 |
| [2102_number_theory.java](2102_number_theory.java) | Java 1.8 | number_theory | O(min(sqrt n, B)) | AC | 0.125 s | 1592 KB | 11304073 |
| [2102_number_theory.py](2102_number_theory.py) | Python 3.12 x64 | number_theory | O(min(sqrt n, B)) | AC | 0.453 s | 388 KB | 11304074 |
| [2102_number_theory.rs](2102_number_theory.rs) | Rust 1.75 x64 | number_theory | O(min(sqrt n, B)) | AC | 0.031 s | 232 KB | 11294726 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2102_number_theory_optimized.java](2102_number_theory_optimized.java) | Java 1.8 | number_theory | Pruned trial division; O(1) storage | AC | 0.109 s | 468 KB | 11327435 |
| [2102_number_theory_optimized.py](2102_number_theory_optimized.py) | PyPy 3.10 x64 | number_theory | Pruned trial division; O(1) bounded storage | AC | 0.125 s | 928 KB | 11327440 |
| [2102_number_theory_optimized.cpp](2102_number_theory_optimized.cpp) | G++ 13.2 x64 | number_theory | O(min(sqrt n, B)) | AC | 0.015 s | 108 KB | 11326999 |
