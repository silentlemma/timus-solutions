# 1728. La maldición de Team.GOV

[Timus 1728](https://acm.timus.ru/problem.aspx?space=1&num=1728) · dificultad 524 · implementation

Problema original de Eugene Kurpilyansky (idea de Mikhail Rubinchik), del Concurso Regional de Programación por Equipos de los Urales 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Efremov y Kantorov eligen a un tercer miembro de una lista de
candidatos. La fuerza de un equipo es la suma de las puntuaciones de
sus miembros. Si el equipo elegido ya jugó en algún torneo anterior,
Efremov no acude; si el equipo sin él también jugó, queda
descalificado. Elegir al candidato que da el equipo más fuerte que
juega, o indicar que toda elección acaba en descalificación.

## Entrada

n (1 ≤ n ≤ 100) equipos anteriores, cada uno con un tamaño de 1 a 3 y
los apellidos en orden alfabético; todo equipo tiene a Kantorov y todo
equipo de tres tiene a Efremov. Luego las puntuaciones de Efremov y
Kantorov, m (1 ≤ m ≤ 100) y m candidatos con sus puntuaciones. Las
puntuaciones van de 1 a 666.

## Salida

`Win` y un candidato que da el equipo más fuerte, o `Fail`. Se acepta
cualquier candidato óptimo.

## Evaluación

El repositorio usa un comprobador semántico y acepta cualquier salida que satisfaga estas condiciones. El comprobador aplica a cada candidato las reglas de retirada y descalificación. Acepta Fail exactamente cuando no queda candidato; de lo contrario exige Win y un candidato que alcance la máxima fuerza restante del equipo. Cualquier empate óptimo es válido.

## Ejemplos

### Ejemplo 1

Entrada:

```
6
3 Efremov Kantorov Rubinchik
2 Efremov Kantorov
3 Efremov Kantorov Kokovin
3 Burmistrov Efremov Kantorov
3 Efremov Kantorov Pervukhin
2 Kantorov Pervukhin
100 10
6
Fominykh 200
Komarov 34
Pervukhin 250
Golubev 23
Soboleva 50
Gein 50
```

Salida:

```
Win
Fominykh
```

### Ejemplo 2

Entrada:

```
2
3 Efremov Fominykh Kantorov
2 Fominykh Kantorov
99 666
1
Fominykh 100
```

Salida:

```
Fail
```

## Solución

Las variantes didácticas C++, Go y Rust usan dos conjuntos de terceros apellidos. Toda formación histórica incluye Kantorov y toda terna también Efremov; el tercer apellido determina el par o terna relevante. Insertarlo en full para ternas y pairs para parejas; Kantorov solo y Efremov/Kantorov no afectan candidatos. Fuera de full: fuerza re+rk+r; en full pero no pairs: rk+r; en ambos: descalificado. Elegir cualquier máximo. Comparar apellidos completos respetando mayúsculas. Tiempo esperado O((n+m)L), L≤50, conjuntos O(nL). El método general original ordena hasta tres apellidos como clave canónica completa, consulta terna y, si repetida, elimina Efremov y consulta pareja. Se conservan los cinco Accepted originales; Java/Python mantienen ese método base.

## Soluciones optimizadas

`1728_implementation_optimized.java`. Java conserva el algoritmo y las estructuras descritas para la versión sencilla. Un búfer fijo de bytes y FastInput sustituyen Scanner y su maquinaria de expresiones regulares y configuración regional. Los enteros se analizan directamente; las cadenas siguen decodificándose como UTF-8 cuando se solicitan y los decimales mantienen conversión numérica explícita. La anticipación guarda un token solo cuando hace falta. El algoritmo de salida no cambia. Se elimina el coste del análisis general; la tabla describe el trabajo algorítmico, con lectura lineal en bytes y un búfer acotado.

Frente a `1728_implementation.java`: tiempo 0.140 s → 0.125 s; memoria 2172 KB → 928 KB.

La versión rápida de Go conserva los dos conjuntos de apellidos y usa los descriptores estándar, búferes fijos de entrada y salida y un búfer de 50 bytes por apellido. Rust rápido lee los apellidos por la entrada estándar de C y guarda ambas marcas de tamaño en una tabla fija con direccionamiento abierto. Si hay una colisión, compara los apellidos completos. Los conjuntos de apellidos en C++ también cubren la versión rápida. Java y Python reutilizan los programas originales admitidos. Los programas anteriores de C++, Go y Rust con formaciones canónicas figuran en Otros enfoques aceptados. El asterisco marca una versión rápida por debajo de su objetivo de clasificación.

Las implementaciones base aceptadas [1728_implementation.java](1728_implementation.java), [1728_implementation.py](1728_implementation.py) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Conserva los algoritmos didácticos. Las filas básicas revalidadas usan sus nuevas métricas e IDs de Accepted de fuente exacta; estas pruebas no cuentan como optimizaciones.

`1728_implementation_optimized.java`: puesto de tiempo 15/19 y de memoria 9/19 en esta muestra comparable.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1728_hashing.cpp](1728_hashing.cpp) | G++ 13.2 x64 | hashing | O((n + m)L) | AC | 0.015 s | 204 KB | 11315520 |
| [1728_hashing.go](1728_hashing.go) | Go 1.14 x64 | hashing | O((n + m)L) | AC | 0.031 s | 952 KB | 11315664 |
| [1728_implementation.java](1728_implementation.java) \* | Java 1.8 | implementation | O(n + m) | AC | 0.140 s | 2172 KB | 11289394 |
| [1728_implementation.py](1728_implementation.py) \* | Python 3.12 x64 | implementation | O(n + m) | AC | 0.109 s | 548 KB | 11289392 |
| [1728_hashing.rs](1728_hashing.rs) | Rust 1.75 x64 | hashing | O((n + m)L) | AC | 0.031 s | 420 KB | 11315666 |

### Otros enfoques Accepted

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1728_implementation.cpp](1728_implementation.cpp) | G++ 13.2 x64 | implementation | O((n + m) log n) | AC | 0.015 s | 460 KB | 11325579 |
| [1728_implementation.go](1728_implementation.go) | Go 1.14 x64 | implementation | O(n + m) | AC | 0.031 s | 1156 KB | 11289390 |
| [1728_implementation.rs](1728_implementation.rs) | Rust 1.75 x64 | implementation | O(n + m) | AC | 0.046 s | 464 KB | 11289397 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1728_hashing_optimized.go](1728_hashing_optimized.go) \* | Go 1.14 x64 | hashing | O((n + m)L) | AC | 0.031 s | 320 KB | 11315884 |
| [1728_hashing_optimized.rs](1728_hashing_optimized.rs) \* | Rust 1.75 x64 | hashing | O((n + m)L) | AC | 0.031 s | 60 KB | 11315888 |
| [1728_implementation_optimized.java](1728_implementation_optimized.java) \* | Java 1.8 | implementation | O(n + m) | AC | 0.125 s | 928 KB | 11324823 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
