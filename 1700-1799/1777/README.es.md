# 1777. Anindilyakwa

[Timus 1777](https://acm.timus.ru/problem.aspx?space=1&num=1777) · dificultad 128 · simulation

Problema original de Ivan Burmistrov, del XV Campeonato Abierto por Equipos de Programación de la Universidad Estatal de los Urales.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

En un claro hay tres montones de piedras de tamaños distintos. Cada
persona, por turno, encuentra los dos montones cuyos tamaños difieren
menos y trae un montón nuevo de exactamente esa diferencia; todos los
montones se quedan. Las preguntas terminan con la persona que encuentra
dos montones iguales. ¿A cuántas personas se pregunta?

## Entrada

Los tres tamaños distintos x₁, x₂, x₃ (1 ≤ xᵢ ≤ 10¹⁸).

## Salida

El número de personas preguntadas.

## Ejemplos

### Ejemplo 1

Entrada:

```
11 5 9
```

Salida:

```
3
```

## Solución

El proceso se simula tal cual: ordenar los montones, tomar la menor
diferencia entre vecinos, parar si es 0 y, si no, añadir un montón de
ese tamaño. La menor diferencia se encoge de forma parecida a los
números en el algoritmo de Euclides, así que el proceso es corto: el
más largo encontrado, con tres números de Fibonacci consecutivos cerca
de 10¹⁸, pregunta a 85 personas; una muestra de 10 000 tríos válidos
uniformemente aleatorios dio una media de 3,7 personas (mediana 3).
`O(s² log s)` para s pasos.

En el ejemplo las diferencias son 2, 4 y 6: la primera persona trae un
montón de 2, la segunda vuelve a ver 9 y 11 y trae otro de 2, y la
tercera señala los dos montones de 2.

Trampas:

- la persona que encuentra montones iguales también cuenta;
- el montón nuevo puede repetir un tamaño viejo, lo que acaba con la
  persona siguiente;
- tamaños de hasta 10¹⁸ necesitan números de 64 bits.
- las ejecuciones aleatorias cortas no establecen el peor caso: el test 08
  pregunta a 85 personas.

Las respuestas coinciden con una implementación aceptada independiente
en 90 tríos aleatorios, incluidos tríos de números de Fibonacci.

## Soluciones optimizadas

La solución optimizada en C++ no guarda la lista de montones: solo los
dos montones menores a < b y la menor diferencia actual g. El nuevo
montón g no pasa de b − a, así que es menor que b, y en orden sus únicos
vecinos posibles son a y b. Todas las diferencias viejas siguen ahí, de
modo que la siguiente menor diferencia es la menor de g, |g − a| y
b − g, y los dos montones menores pasan a ser g y a, o a y g. Cada paso
cuesta `O(1)` de tiempo y toda la ejecución `O(1)` de memoria en lugar
de ordenar un vector que crece; todos los valores caben en `long long`,
porque no pasan de 10¹⁸: {1777_simulation_optimized.cpp}.

La solución optimizada en Java lee los tres tamaños byte a byte de
`System.in` en lugar de crear un `Scanner`, cuyas expresiones regulares
y datos de configuración regional cuestan más que la breve simulación,
que sigue igual: {1777_simulation_optimized.java}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1777_simulation_optimized.cpp`: reducción de tiempo +0.00%; reducción
  de memoria +47.92%; base: `1777_simulation.cpp`.

- `1777_simulation_optimized.java`: reducción de tiempo +0.00%;
  reducción de memoria +74.18%; base: `1777_simulation.java`.

## Notas por lenguaje

En la clasificación del 2026-10-31, las siguientes implementaciones
básicas ya alcanzan los objetivos de tiempo y memoria. Se conservan sus
archivos en el conjunto básico; estos lenguajes no necesitan otra
implementación para alcanzar el objetivo.

- [1777_simulation.go](1777_simulation.go).
- [1777_simulation.rs](1777_simulation.rs).

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1777_simulation.cpp](1777_simulation.cpp) | G++ 13.2 x64 | simulation | O(s^2 log s) for s steps | AC | 0.015 s | 192 KB | 11304057 |
| [1777_simulation.go](1777_simulation.go) | Go 1.14 x64 | simulation | O(s^2 log s) for s steps | AC | 0.031 s | 1124 KB | 11289732 |
| [1777_simulation.java](1777_simulation.java) | Java 1.8 | simulation | O(s^2 log s) for s steps | AC | 0.140 s | 1704 KB | 11304058 |
| [1777_simulation.py](1777_simulation.py) | Python 3.12 x64 | simulation | O(s^2 log s) for s steps | AC | 0.093 s | 436 KB | 11289733 |
| [1777_simulation.rs](1777_simulation.rs) | Rust 1.75 x64 | simulation | O(s^2 log s) for s steps | AC | 0.046 s | 252 KB | 11304059 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1777_simulation_optimized.cpp](1777_simulation_optimized.cpp) | G++ 13.2 x64 | simulation | O(s) for s steps | AC | 0.015 s | 100 KB | 11304425 |
| [1777_simulation_optimized.java](1777_simulation_optimized.java) | Java 1.8 | simulation | O(s^2 log s) for s steps | AC | 0.140 s | 440 KB | 11304426 |
