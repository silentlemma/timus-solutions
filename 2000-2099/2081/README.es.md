# 2081. Tiempos decrecientes tras un visor averiado

[Timus 2081](https://acm.timus.ru/problem.aspx?space=1&num=2081) · dificultad 721 · greedy

Problema original de Pavel Egorov, preparado por Ivan Burmistrov.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un temporizador muestra MM:SS en un visor de siete segmentos dibujado
con `_`, `|` y `.`, pero algunos segmentos encendidos pueden no verse
(un segmento visible siempre es correcto). Dadas n lecturas, recuperar
tiempos de 00:00 a 59:59, estrictamente decrecientes y coherentes con
cada lectura. Se acepta cualquier respuesta válida. Los límites son
2 segundos y 256 MB.

## Entrada

n ≤ 100 y después tres líneas de 17 caracteres por lectura: los cuatro
dígitos ocupan las columnas 1–3, 5–7, 11–13 y 15–17.

## Salida

n líneas MM:SS.

## Evaluación

Un comprobador verifica el formato, el decrecimiento estricto y que
cada segmento visible pertenezca al dígito elegido.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
._..._........._.
|...._|.*...|.._|
|_|.._..*...|.|..
....._....._..._.
|.|...|.*.|.|.._.
|.|.|_..*.|_|.._.
```

Salida:

```
03:12
00:05
```

## Solución

Un dígito encaja en una celda si cada carácter visible coincide con el
del dígito en ese lugar. Para cada lectura las cuatro celdas dan una
tabla de dígitos que encajan. Recorriendo las lecturas en orden, se toma
el mayor tiempo que encaja y queda por debajo de la respuesta anterior,
bajando desde ella.

Esto nunca falla si existe alguna respuesta: por inducción el valor
voraz de cada lectura es al menos el de esa respuesta, porque el valor
de la respuesta encaja y está por debajo de su valor anterior, que es a
lo sumo el valor voraz anterior. El recorrido cuesta a lo sumo 3600
pasos por lectura.

En el ejemplo la primera lectura encaja tanto con 09:48 como con 03:12,
así que la salida puede diferir del ejemplo.

**Envíos de las versiones sencillas en Timus**

G++ 13.2 x64 №11321978 · Java 1.8 №11321972 · Python 3.12 x64 №11321979 · Rust 1.75 x64 №11321974 · Go 1.14 x64 №11322308.

## Soluciones optimizadas

`2081_bitmask_optimized.java`. Conserva máscaras exactas de 60 bits para minutos/segundos y la elección voraz del mayor tiempo bajo el límite. Lee pantallas de ancho fijo como bytes, sin reader, cadenas decodificadas ni recodificación; cada respuesta ocupa seis bytes. No cambian factibilidad ni orden decreciente. Para R pantallas: O(R) tiempo y salida O(R), máscaras/búfer constantes. Conserva la anterior implementación bitmask y la didáctica.

Accepted de fuente exacto Java 1.8 #11326954: 0.125 s / 464 KB. Comparación guardada de Java actual, 2026-11-20: tiempo 10/17, memoria 1/17. Al usar menos de 1024 KB, la admisión estricta usa solo tiempo.

- `2081_bitmask_optimized.java`: 0.125 s / 464 KB; base didáctica conservada `2081_greedy.java`: 0.14 s / 2372 KB; cambio de tiempo -10.7%; cambio de memoria -80.4%.

Dos máscaras de bits representan por separado los minutos y los segundos posibles. El bit activo más alto da el mayor valor dentro del límite actual. Si el minuto actual no admite ningún segundo, se elige el minuto válido anterior y su mayor segundo.

Go 1.14 x64, envío 11322015. Tiempo 0,031 → 0,031 s, memoria 1128 → 928 KB.

Java 1.8, envío 11322017. Tiempo 0,14 → 0,156 s, memoria 2372 → 536 KB.

Rust asigna a cada patrón de celdas encendidas una máscara de dígitos y elige el mayor tiempo inferior a la lectura anterior. Rust 1.75 x64, envío 11323256. Tiempo 0,062 → 0,046 s, memoria 252 → 64 KB.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [2081_greedy.cpp](2081_greedy.cpp) | G++ 13.2 x64 | greedy | O(n) | AC | 0.015 s | 372 KB | 11321978 |
| [2081_greedy.go](2081_greedy.go) | Go 1.14 x64 | greedy | O(n) | AC | 0.031 s | 1128 KB | 11322308 |
| [2081_greedy.java](2081_greedy.java) | Java 1.8 | greedy | O(n) | AC | 0.14 s | 2372 KB | 11321972 |
| [2081_greedy.py](2081_greedy.py) | Python 3.12 x64 | greedy | O(n) | AC | 0.109 s | 596 KB | 11321979 |
| [2081_greedy.rs](2081_greedy.rs) | Rust 1.75 x64 | greedy | O(n) | AC | 0.062 s | 252 KB | 11321974 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [2081_bitmask.go](2081_bitmask.go) | Go 1.14 x64 | bitmask | O(n) | AC | 0.031 s | 928 KB | 11322015 |
| [2081_bitmask_optimized.java](2081_bitmask_optimized.java) \* | Java 1.8 | bitmask | O(R) time; O(R) output space | AC | 0.125 s | 464 KB | 11326954 |
| [2081_bitmask.java](2081_bitmask.java) \* | Java 1.8 | bitmask | O(n) | AC | 0.156 s | 536 KB | 11322017 |
| [2081_bitmask.rs](2081_bitmask.rs) \* | Rust 1.75 x64 | bitmask | O(N) | AC | 0.046 s | 64 KB | 11323256 |

\* Las versiones marcadas aún pueden mejorar su clasificación.
