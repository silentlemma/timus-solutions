# 1574. Matemáticos y paréntesis

[Timus 1574](https://acm.timus.ru/problem.aspx?space=1&num=1574) · dificultad 353 · strings

Problema original de Alexander Toropov, del USU Junior Contest (XIV Campeonato Abierto por Equipos de Programación para Escolares de la Región de Sverdlovsk), octubre de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dada una línea no vacía de hasta 100000 paréntesis, hay que contar los
desplazamientos cíclicos, de 0 a n − 1 caracteres, que la convierten en
una secuencia correcta de paréntesis. Los desplazamientos de distinta
cantidad cuentan por separado aunque den la misma línea.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

La línea de paréntesis.

## Salida

El número de esos desplazamientos.

## Evaluación

Las pruebas del repositorio comparan todo el texto de salida, ignorando solo el espacio en blanco final. Conserva los espacios significativos, los saltos de línea, las mayúsculas y la puntuación.

## Ejemplos

### Ejemplo 1

Entrada:

```
)(()
```

Salida:

```
1
```

### Ejemplo 2

Entrada:

```
)()(
```

Salida:

```
2
```

### Ejemplo 3

Entrada:

```
()
```

Salida:

```
1
```

## Solución

Si los números de paréntesis de apertura y de cierre difieren, ningún
desplazamiento sirve. Si no, se toma el balance tras cada prefijo:
aperturas menos cierres. Un desplazamiento que empieza justo tras la
posición i cambia cada balance en −p(i), donde p(i) es el balance ahí,
así que nunca baja de cero exactamente cuando p(i) es el menor de todos
los balances. La respuesta es el número de prefijos cuyo balance es ese
mínimo. `O(n)`.

Detalles a tener en cuenta:

- una línea como `)()(` da la misma línea correcta con dos
  desplazamientos distintos, y ambos cuentan (el segundo ejemplo);
- el desplazamiento por cero también cuenta (el tercer ejemplo);
- una línea desequilibrada solo tiene la respuesta 0, aunque algún
  desplazamiento mantenga todos los balances no negativos
  (pruebas 04, 05).

## Soluciones optimizadas

`1574_strings_optimized.java`. Cuenta en línea las apariciones del balance prefijo mínimo; devuelve cero si el balance final no es cero. En una cadena equilibrada el mínimo no es positivo: lowest=0 sin contar el prefijo vacío conserva el número de rotaciones. Java lee bytes de paréntesis sin guardar la línea, con entrada fija. Python elimina la lista de prefijos, pero aún lee toda la cadena de bytes: espacio total O(n), frente a auxiliar O(1) en Java. Ambos tardan O(n). Python vacía la salida antes de os._exit(0); finalizar así el intérprete no cambia la cota algorítmica.

Frente a `1574_strings.java`: tiempo 0.125 s → 0.125 s; memoria 1196 KB → 480 KB.

`1574_strings_optimized.py`. Cuenta en línea las apariciones del balance prefijo mínimo; devuelve cero si el balance final no es cero. En una cadena equilibrada el mínimo no es positivo: lowest=0 sin contar el prefijo vacío conserva el número de rotaciones. Java lee bytes de paréntesis sin guardar la línea, con entrada fija. Python elimina la lista de prefijos, pero aún lee toda la cadena de bytes: espacio total O(n), frente a auxiliar O(1) en Java. Ambos tardan O(n). Python vacía la salida antes de os._exit(0); finalizar así el intérprete no cambia la cota algorítmica.

Frente a `1574_strings.py`: tiempo 0.093 s → 0.14 s; memoria 5252 KB → 1 412 KB.

Las versiones en C++, Go y Rust cuentan las apariciones del saldo mínimo de los prefijos mientras leen la entrada. Al aparecer un saldo menor, el contador vuelve a uno. Se cuentan los prefijos de longitudes de 1 a n. Cuando el saldo total es cero, el prefijo completo sustituye al vacío, ya que los dos representan el mismo corte cíclico. C++ usa entrada estándar con búfer, Go lee bloques de tamaño fijo y Rust usa el búfer de la entrada estándar. El tiempo es O(n) y el espacio adicional es O(1).

Las implementaciones base aceptadas [1574_strings.java](1574_strings.java), [1574_strings.py](1574_strings.py) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1574_strings_optimized.java`: puesto de tiempo 13/22 y de memoria 2/22 en esta muestra comparable.

`1574_strings_optimized.py`: puesto de tiempo 28/45 y de memoria 25/45 en esta muestra comparable.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1574_strings.cpp](1574_strings.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.031 s | 500 KB | 11287829 |
| [1574_strings.go](1574_strings.go) | Go 1.14 x64 | strings | O(n) | AC | 0.031 s | 1768 KB | 11287832 |
| [1574_strings.java](1574_strings.java) \* | Java 1.8 | strings | O(n) | AC | 0.125 s | 1196 KB | 11287835 |
| [1574_strings.py](1574_strings.py) \* | Python 3.12 x64 | strings | O(n) | AC | 0.093 s | 5252 KB | 11287834 |
| [1574_strings.rs](1574_strings.rs) | Rust 1.75 x64 | strings | O(n) | AC | 0.046 s | 2068 KB | 11287836 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1574_strings_optimized.cpp](1574_strings_optimized.cpp) \* | G++ 13.2 x64 | strings | O(n) | AC | 0.031 s | 88 KB | 11310381 |
| [1574_strings_optimized.go](1574_strings_optimized.go) \* | Go 1.14 x64 | strings | O(n) | AC | 0.031 s | 824 KB | 11310380 |
| [1574_strings_optimized.rs](1574_strings_optimized.rs) \* | Rust 1.75 x64 | strings | O(n) | AC | 0.015 s | 208 KB | 11310379 |
| [1574_strings_optimized.java](1574_strings_optimized.java) \* | Java 1.8 | strings | O(n) | AC | 0.125 s | 480 KB | 11325019 |
| [1574_strings_optimized.py](1574_strings_optimized.py) \* | PyPy 3.10 x64 | strings | O(n) | AC | 0.14 s | 1412 KB | 11325071 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
