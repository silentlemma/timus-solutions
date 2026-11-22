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

## Evaluación

Las pruebas del repositorio comparan exactamente los tokens de salida; los espacios entre tokens no son significativos.

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

`1777_simulation_optimized.java`. Conserva simulación comprimida exacta. Para menores pilas a≤b y diferencia mínima positiva g≤b−a<b: si g<a, b−g≥a−g y sigue min(g,a−g); si no, g−a≤g y sigue min(g−a,b−g). Solo elimina operaciones redundantes, sin cambiar actualizaciones ni conteo. O(s) tiempo para s pasos, O(1) espacio auxiliar; no supone pasos constantes.

Accepted exacto Java 1.8 #11327759: 0.109 s / 404 KB. Comparación guardada del grupo de compiladores del 2026-11-20: tiempo 8/77, memoria 1/77. Bajo 1024 KB la admisión estricta solo usa tiempo: diez primeros o 15% superior, con empates compartidos y corte porcentual redondeado hacia arriba. Conserva el asterisco por la meta propia del lenguaje: primer puesto en ambas métricas. El registro optimizado documentado antes #11304426 era 0.14 s / 440 KB; es un par histórico distinto, no la medición actual de este fuente. Las bases didácticas permanecen intactas.

- `1777_simulation_optimized.java`: 0.109 s / 404 KB; base didáctica conservada `1777_simulation.java`: 0.14 s / 1704 KB.

La solución optimizada en C++ no guarda la lista de montones: solo los
dos montones menores a < b y la menor diferencia actual g. El nuevo
montón g no pasa de b − a, así que es menor que b, y en orden sus únicos
vecinos posibles son a y b. Todas las diferencias viejas siguen ahí, de
modo que la siguiente menor diferencia es la menor de g, |g − a| y
b − g, y los dos montones menores pasan a ser g y a, o a y g. Cada paso
cuesta `O(1)` de tiempo y toda la ejecución `O(1)` de memoria en lugar
de ordenar un vector que crece; todos los valores caben en `long long`,
porque no pasan de 10¹⁸: {1777_simulation_optimized.cpp}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1777_simulation_optimized.cpp`: reducción de tiempo +0.00%; reducción
  de memoria +47.92%; base: `1777_simulation.cpp`.

`1777_simulation_optimized.rs`. Mantiene todos los montones en un vector dinámico ordenado. Recorre diferencias vecinas, busca por bisección el nuevo mínimo y lo inserta en su posición, evitando ordenar todo en cada paso. Si el tamaño ya existe, cuenta a la siguiente persona que detecta la igualdad y termina. La capacidad dinámica no depende de un límite de montones observado solo experimentalmente. En s pasos, recorridos y desplazamientos cuestan O(s²) en total y espacio O(s). La versión Rust lee y escribe mediante el entorno de C, sin conservar un String de entrada decodificada ni construir un String de salida con formato. Se conserva la fuente sencilla con Accepted.

Frente a `1777_simulation.rs`: tiempo 0.046 s → 0.031 s; memoria 252 KB → 76 KB.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1777_simulation_optimized.rs`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

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
| [1777_simulation_optimized.java](1777_simulation_optimized.java) \* | Java 1.8 | simulation | O(s) for s simulation steps; O(1) auxiliary state | AC | 0.109 s | 404 KB | 11327759 |
| [1777_simulation_optimized.rs](1777_simulation_optimized.rs) \* | Rust 1.75 x64 | simulation | O(s²) for s steps | AC | 0.031 s | 76 KB | 11324872 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
