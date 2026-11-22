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

`1574_strings_optimized.java`. Java conserva el balance actual, el mínimo prefijo y sus visitas. Lee bloques de 16384 bytes e ignora separadores que no sean paréntesis. Un mínimo nuevo reinicia la cuenta en uno; un mínimo igual la incrementa. Si el balance final no es cero, devuelve cero. En otro caso, los prefijos de longitudes 1..N cuentan los cortes válidos: el prefijo completo sustituye al vacío, que representa el mismo corte. No guarda la cadena ni un arreglo de prefijos. Tiempo O(N), espacio auxiliar O(1) con búfer fijo; con N<=100000 los contadores caben en int. Conserva la base con prefijos y la implementación Python descrita aparte.

Accepted exacto Java 1.8 #11327330: 0.109 s / 560 KB. Comparación guardada del grupo de compiladores del 2026-11-20: tiempo 5/22, memoria 2/22. Bajo 1024 KB la admisión estricta solo usa tiempo: diez primeros o 15% superior, con empates compartidos y corte porcentual redondeado hacia arriba. Conserva el asterisco por la meta propia del lenguaje: primer puesto en ambas métricas. El registro optimizado documentado antes #11325019 era 0.125 s / 480 KB; es un par histórico distinto, no la medición actual de este fuente. Las bases didácticas permanecen intactas.

- `1574_strings_optimized.java`: 0.109 s / 560 KB; base didáctica conservada `1574_strings.java`: 0.125 s / 1196 KB.

`1574_strings_optimized.py`. Mantiene balance, mínimo prefijo y visitas a ese mínimo; balance final no nulo da cero. En una cadena equilibrada, omitir el prefijo vacío conserva el número exacto de rotaciones válidas. Python lee bloques B=4096 en vez de toda la cadena, sin arreglo/cadena del largo de entrada. O(N) tiempo, búfer O(B) y contadores acotados; vacía antes de salir. Java ya transmite; conserva la base de prefijos.

Accepted exacto CPython 3.12 #11326664: 0.093 s / 676 KB. Comparación guardada 2026-11-20 con compiladores actuales de la familia: tiempo 1/45, memoria 9/45. Por debajo de 1024 KB, admisión estricta solo por tiempo.

- `1574_strings_optimized.py`: 0.093 s / 676 KB; base didáctica conservada `1574_strings.py` (Python 3.12 x64): 0.093 s / 5252 KB; cambio de tiempo +0.0%; cambio de memoria -87.1%.

`1574_strings_optimized.cpp`. Conserva el recuento exacto del balance mínimo de prefijos. Lee bloques de 16 KiB con fread en lugar de una llamada getchar con bloqueo por carácter. Un mínimo menor reinicia el contador en uno; uno igual lo incrementa. Omite separadores que no sean paréntesis y devuelve cero si el balance final no es cero. El prefijo no vacío de longitud completa representa el corte cíclico inicial. Tiempo O(n), almacenamiento auxiliar fijo.

Accepted del fuente exacto #11326997: 0.015 s / 92 KB. Muestra G++ 13.2 guardada el 2026-11-20: tiempo 1/58, memoria 1/56. Se conservan los fuentes didácticos.

Medición de Python documentada anteriormente: Frente a `1574_strings.py`: tiempo 0.093 s → 0.14 s; memoria 5252 KB → 1 412 KB.

Las versiones en C++, Go y Rust cuentan las apariciones del saldo mínimo de los prefijos mientras leen la entrada. Al aparecer un saldo menor, el contador vuelve a uno. Se cuentan los prefijos de longitudes de 1 a n. Cuando el saldo total es cero, el prefijo completo sustituye al vacío, ya que los dos representan el mismo corte cíclico. C++ usa entrada estándar con búfer, Go lee bloques de tamaño fijo y Rust usa el búfer de la entrada estándar. El tiempo es O(n) y el espacio adicional es O(1).

Las bases aceptadas conservadas [1574_strings.rs](1574_strings.rs) cumplen la admisión estricta en la comparación guardada: diez primeros puestos o 15% superior en los indicadores requeridos. Se reutilizan sin copias idénticas y se conservan los otros fuentes didácticos. Un asterisco indica el objetivo de clasificación propio del lenguaje.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

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
| [1574_strings_optimized.cpp](1574_strings_optimized.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.015 s | 92 KB | 11326997 |
| [1574_strings_optimized.go](1574_strings_optimized.go) \* | Go 1.14 x64 | strings | O(n) | AC | 0.031 s | 824 KB | 11310380 |
| [1574_strings_optimized.rs](1574_strings_optimized.rs) \* | Rust 1.75 x64 | strings | O(n) | AC | 0.015 s | 208 KB | 11310379 |
| [1574_strings_optimized.java](1574_strings_optimized.java) \* | Java 1.8 | strings | O(N) time; O(1) auxiliary space | AC | 0.109 s | 560 KB | 11327330 |
| [1574_strings_optimized.py](1574_strings_optimized.py) \* | Python 3.12 x64 | strings | O(N) time; O(B) buffer space | AC | 0.093 s | 676 KB | 11326664 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
