# 1868. Concurso de pronósticos

[Timus 1868](https://acm.timus.ru/problem.aspx?space=1&num=1868) · dificultad 158 · implementation

Problema original de Denis Dublennykh, del Campeonato Abierto de la Universidad Federal de los Urales, 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

En la final mundial los cuatro primeros equipos ganan oro, los cuatro
siguientes plata y los cuatro siguientes bronce. Varios veteranos
hicieron pronósticos del tipo "el equipo X gana una medalla de tipo Y",
y Vadik paga cinco dólares a cada veterano con más aciertos. Dados los
doce medallistas en el orden de sus puestos y todos los pronósticos,
¿cuánto paga Vadik?

## Entrada

Doce nombres de equipos del primer puesto al duodécimo, luego n
(1 ≤ n ≤ 100) y n pronósticos. Un pronóstico empieza con su número de
apuestas kᵢ, seguido de kᵢ líneas "equipo : medalla" con la medalla
"gold", "silver" o "bronze". Ningún pronóstico da dos medallas a un
equipo ni una misma medalla a más de cuatro equipos. Los nombres tienen
de 1 a 30 letras latinas, guiones bajos, puntos y comas. Cada nombre,
número y apuesta va en su propia línea.

## Salida

Lo que paga Vadik, en dólares.

## Ejemplos

### Ejemplo 1

Entrada:

```
North_A
North_B
North_C
North_D
East_A
East_B
East_C
East_D
West_A
West_B
West_C
West_D
3
3
North_A : gold
East_A : silver
West_A : bronze
4
North_B : gold
East_C : silver
West_D : bronze
Other : gold
3
North_C : silver
East_B : gold
Other : bronze
```

Salida:

```
10
```

## Solución

Los nombres no tienen espacios, así que la entrada es una secuencia de
palabras: doce nombres y, por cada apuesta, un nombre, dos puntos y una
medalla. Un diccionario de los doce nombres a sus medallas (puestos 1–4
oro, 5–8 plata, 9–12 bronce) dice si una apuesta acierta; un equipo que
no está en él no ganó nada. Se cuentan los aciertos de cada veterano y
se pagan cinco dólares a cada veterano con la cuenta más alta.
`O(n·k)` consultas al diccionario.

En el ejemplo cada veterano tiene tres aciertos, así que ganan los tres
y Vadik paga 15 dólares.

Trampas:

- la medalla sale del puesto: los nombres van en orden, así que los
  cuatro primeros son oro, y así sucesivamente;
- un pronóstico puede nombrar equipos que no ganaron ninguna medalla;
- los nombres distinguen mayúsculas y pueden constar solo de puntos y
  comas;
- si nadie acierta nada, todos los veteranos empatan con cero y cobran
  todos.

Las cantidades coinciden con una implementación aceptada independiente
en 150 concursos aleatorios.

## Soluciones optimizadas

`1868_implementation_optimized.java`. Mantiene la igualdad exacta de medallistas/premios y solo la mejor puntuación y sus empates. Un analizador ASCII de 1024 bytes sustituye StringTokenizer por línea. El nuevo envío da 0.078 s / 956 KB: más rápido que el anterior optimizado de 0.109 s / 900 KB, con algo más de memoria. La base Java conservada da 0.093 s / 1196 KB; no se afirma ahorro de memoria frente a la revisión optimizada anterior.

Accepted de fuente exacto Java 1.8 #11326969: 0.078 s / 956 KB. Comparación guardada de Java actual, 2026-11-20: tiempo 2/57, memoria 9/57. Al usar menos de 1024 KB, la admisión estricta usa solo tiempo.

- `1868_implementation_optimized.java`: 0.078 s / 956 KB; base didáctica conservada `1868_implementation.java`: 0.093 s / 1196 KB; cambio de tiempo -16.1%; cambio de memoria -20.1%.

La solución optimizada en C++ guarda los doce nombres en arreglos fijos
de `char` de 31 bytes, ya que un nombre tiene como mucho 30 caracteres,
lee cada apuesta con `scanf` en búferes de 31 y 7 bytes (el nombre de
una medalla tiene como mucho 6 letras) y la compara con los doce nombres
mediante `strcmp` en lugar de un `map` de `string`. Lleva sobre la
marcha el mejor número de aciertos y cuántos veteranos lo alcanzan en
lugar de un `vector` con todos los recuentos, y usa `stdio` en lugar de
`iostream`: {1868_implementation_optimized.cpp}.

La solución optimizada en Python lee la entrada línea a línea, ya que
cada nombre, número y apuesta va en su propia línea, en lugar de partir
toda la entrada en una lista de palabras; lleva sobre la marcha el mejor
número de aciertos y cuántos veteranos lo alcanzan en lugar de una lista
con todos los recuentos: {1868_implementation_optimized.py}.

La solución optimizada en Rust lee la entrada línea a línea en un mismo
`String` reutilizado, ya que cada nombre, número y apuesta va en su
propia línea, en lugar de leer toda la entrada; compara cada apuesta
directamente con los doce nombres guardados en lugar de usar un
`HashMap` y lleva sobre la marcha el mejor número de aciertos y cuántos
veteranos lo alcanzan en lugar de un vector con todos los recuentos:
{1868_implementation_optimized.rs}.

### Mejora medida

Cada versión optimizada conservada tiene Accepted. Cumple por situarse entre las diez primeras o el 15% superior en ambas métricas, por estar en el 30% superior en ambas y mejorar la posición base en al menos una, o por reducir al menos un 30% el tiempo o la memoria respecto a la base del mismo lenguaje. Una reducción negativa indica mayor coste. El asterisco se refiere al objetivo de clasificación específico del lenguaje.

- `1868_implementation_optimized.cpp`: reducción de tiempo +0.00%;
  reducción de memoria +75.45%; base: `1868_implementation.cpp`.

- `1868_implementation_optimized.py`: reducción de tiempo -19.23%;
  reducción de memoria +42.20%; base: `1868_implementation.py`.

- `1868_implementation_optimized.rs`: reducción de tiempo +0.00%;
  reducción de memoria +60.45%; base: `1868_implementation.rs`.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1868_implementation_parsing_optimized.py`. Los nombres de medallas se leen como bytes y se obtiene la mejor puntuación y el número de ganadores en una pasada, evitando conversiones y recorridos repetidos. El programa independiente vacía ambos flujos de salida antes de os._exit(0), evitando la limpieza del intérprete tras escribir la respuesta completa. Cambia el cierre del proceso, no el algoritmo matemático; se conserva la versión sencilla.

Accepted #11329012 (Python 3.12 x64): **0.062 s / 912 KB**. Comparación archivada: `1868_implementation.py` (Python 3.12 x64) — 0.078 s / 692 KB (#11290928).

## Notas por lenguaje

En la clasificación del 2026-10-31, las siguientes implementaciones
básicas ya alcanzan los objetivos de tiempo y memoria. Se conservan sus
archivos en el conjunto básico; estos lenguajes no necesitan otra
implementación para alcanzar el objetivo.

- [1868_implementation.go](1868_implementation.go).

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1868_implementation.cpp](1868_implementation.cpp) | G++ 13.2 x64 | implementation | O(n k) | AC | 0.015 s | 440 KB | 11304080 |
| [1868_implementation.go](1868_implementation.go) | Go 1.14 x64 | implementation | O(n k) | AC | 0.015 s | 1220 KB | 11290927 |
| [1868_implementation.java](1868_implementation.java) | Java 1.8 | implementation | O(n k) | AC | 0.093 s | 1196 KB | 11290930 |
| [1868_implementation.py](1868_implementation.py) | Python 3.12 x64 | implementation | O(n k) | AC | 0.078 s | 692 KB | 11290928 |
| [1868_implementation.rs](1868_implementation.rs) | Rust 1.75 x64 | implementation | O(n k) | AC | 0.015 s | 536 KB | 11290931 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1868_implementation_optimized.cpp](1868_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(n k) | AC | 0.015 s | 108 KB | 11305924 |
| [1868_implementation_optimized.py](1868_implementation_optimized.py) \* | Python 3.12 x64 | implementation | O(n k) | AC | 0.093 s | 400 KB | 11305927 |
| [1868_implementation_optimized.rs](1868_implementation_optimized.rs) | Rust 1.75 x64 | implementation | O(n k) | AC | 0.015 s | 212 KB | 11305928 |
| [1868_implementation_optimized.java](1868_implementation_optimized.java) | Java 1.8 | implementation | O(n k) | AC | 0.078 s | 956 KB | 11326969 |
| [1868_implementation_parsing_optimized.py](1868_implementation_parsing_optimized.py) | Python 3.12 x64 | implementation, parsing | O(n k) | AC | 0.062 s | 912 KB | 11329012 |

\* Accepted; aún no se alcanza el objetivo de [RATING_CRITERIA.md](../../RATING_CRITERIA.md). Esta versión puede optimizarse más.
