# 1769. Vieja leyenda de los Urales

[Timus 1769](https://acm.timus.ru/problem.aspx?space=1&num=1769) · dificultad 206 · strings

Problema original de Daniil Ayzenshteyn, del XIV Campeonato de los Urales de Programación Competitiva, 10 de abril de 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dada una línea no vacía de cifras decimales, hallar el menor entero
positivo cuya notación decimal no aparece en la línea.

## Entrada

La línea, de a lo sumo 10⁵ cifras.

## Salida

Ese entero.

## Evaluación

Se comparan los tokens; los espacios adicionales no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
10123456789
```

Salida:

```
11
```

## Solución

Una línea de n cifras tiene a lo sumo n trozos de cada longitud,
mientras que hay 9·10⁵ números de seis cifras, así que siempre falta
algún número de seis cifras y la respuesta tiene a lo sumo seis. Cada
trozo de una a seis cifras que no empieza por cero es la notación de un
número; marcándolos todos y contando desde 1 hasta el primer número sin
marcar se obtiene la respuesta. `O(6n)`.

En el ejemplo aparecen del 1 al 9 y el 10, pero no el 11.

Trampas:

- los trozos que empiezan por 0 no son notaciones de números, aunque el
  número tras el cero sigue apareciendo una cifra después;
- una línea de ceros no contiene el 1;
- buscar en la línea cada número por turno puede ser lento en líneas
  largas con una respuesta grande.

Las respuestas coinciden con buscar en la línea 1, 2, 3 y así
sucesivamente en 90 líneas aleatorias y con una implementación
aceptada independiente en 20 líneas largas.

## Soluciones optimizadas

`1769_strings_optimized.java`. Conserva un bitmap de códigos decimales positivos de una longitud y busca el ausente menor. Lee bloques de 4096 bytes. Al avanzar la ventana resta el dígito saliente por 10^length, sin división: el código sigue exacto. Solo marca primera cifra no nula. Para D<=6 y N cifras: trabajo O(DN+10^D), espacio O(N+10^D) bits con factores fijos de palabra/byte. El nuevo envío es más rápido, pero usa 588 KB frente a 556 KB anteriores; no mejora memoria frente a aquella revisión.

Accepted de fuente exacto Java 1.8 #11326952: 0.109 s / 588 KB. Comparación guardada de Java actual, 2026-11-20: tiempo 5/42, memoria 1/42. Al usar menos de 1024 KB, la admisión estricta usa solo tiempo.

- `1769_strings_optimized.java`: 0.109 s / 588 KB; base didáctica conservada `1769_strings.java`: 0.156 s / 2124 KB; cambio de tiempo -30.1%; cambio de memoria -72.3%.

Se marcan subcadenas decimales de una sola longitud mediante códigos numéricos deslizantes y un mapa compacto de bits. Se recorren candidatos crecientes hasta el primero ausente; si aparecen todos, se aumenta la longitud y reutiliza memoria. Los ceros iniciales y el mínimo requerido respetan la definición numérica original. No se crean cadenas por subcadena ni conjuntos simultáneos para todas las longitudes.

- `1769_strings_optimized.cpp`: 0.031 s / 376 KB; base `1769_strings.cpp`: 0.015 s / 612 KB; cambio respecto a la base: tiempo +106.7%, memoria -38.6%.
- `1769_strings_optimized.go`: 0.046 s / 1444 KB; base `1769_strings.go`: 0.031 s / 2740 KB; cambio respecto a la base: tiempo +48.4%, memoria -47.3%.

- `1769_strings_optimized.py`: 0.250 s / 1452 KB; base `1769_strings.py`: 0.312 s / 23740 KB; cambio respecto a la base: tiempo -19.9%, memoria -93.9%.
- `1769_strings_optimized.rs`: 0.031 s / 468 KB; base `1769_strings.rs`: 0.031 s / 1472 KB; cambio respecto a la base: tiempo -0.0%, memoria -68.2%.

## Notas por lenguaje

Se usa la instantánea guardada del 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en tiempo y memoria; las demás familias exigen el primer puesto en ambas métricas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

- C++: base didáctica preferida `1769_strings.cpp`; versión que cubre `1769_strings.cpp`; puestos tiempo/memoria 1/7, registros de otros autores 72/72.

- Go: base didáctica preferida `1769_strings.go`; versión que cubre `1769_strings.go`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

- Java: Accepted de fuente exacto Java 1.8 #11326952: 0.109 s / 588 KB. Comparación guardada de Java actual, 2026-11-20: tiempo 5/42, memoria 1/42. Al usar menos de 1024 KB, la admisión estricta usa solo tiempo.

- Python/PyPy: base didáctica preferida `1769_strings.py`; versión que cubre `1769_strings_optimized.py`; puestos tiempo/memoria 7/1, registros de otros autores 14/14.

- Rust: base didáctica preferida `1769_strings.rs`; versión que cubre `1769_strings.rs`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

## Soluciones

La tabla sencilla incluye las fuentes didácticas preferidas y las alternativas Accepted conservadas. Las notas identifican la base preferida de cada familia.

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1769_strings.cpp](1769_strings.cpp) | G++ 13.2 x64 | strings | O(6n) | AC | 0.015 s | 612 KB | 11308926 |
| [1769_strings.go](1769_strings.go) | Go 1.14 x64 | strings | O(6n) | AC | 0.031 s | 2740 KB | 11289655 |
| [1769_strings.java](1769_strings.java) | Java 1.8 | strings | O(6n) | AC | 0.156 s | 2124 KB | 11308927 |
| [1769_strings.py](1769_strings.py) | Python 3.12 x64 | strings | O(6n) | AC | 0.312 s | 23740 KB | 11308928 |
| [1769_strings.rs](1769_strings.rs) | Rust 1.75 x64 | strings | O(6n) | AC | 0.031 s | 1472 KB | 11289658 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1769_strings_optimized.cpp](1769_strings_optimized.cpp) \* | G++ 13.2 x64 | strings | O(DN+10^D) | AC | 0.031 s | 376 KB | 11308082 |
| [1769_strings_optimized.go](1769_strings_optimized.go) | Go 1.14 x64 | strings | O(DN+10^D) | AC | 0.046 s | 1444 KB | 11308083 |
| [1769_strings_optimized.java](1769_strings_optimized.java) | Java 1.8 | strings | O(DN+10^D) | AC | 0.109 s | 588 KB | 11326952 |
| [1769_strings_optimized.py](1769_strings_optimized.py) | Python 3.12 x64 | strings | O(DN+10^D) | AC | 0.250 s | 1452 KB | 11308079 |
| [1769_strings_optimized.rs](1769_strings_optimized.rs) | Rust 1.75 x64 | strings | O(DN+10^D) | AC | 0.031 s | 468 KB | 11308085 |

\* Accepted; todavía no se alcanza el objetivo de clasificación. Esta versión admite mejoras.
