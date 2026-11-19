# 1545. Jeroglíficos

[Timus 1545](https://acm.timus.ru/problem.aspx?space=1&num=1545) · dificultad 50 · implementation

Problema original de Evgeny Krokhalev, del XI Campeonato Universitario por Equipos de Programación de los Urales, Ekaterimburgo, 21 de abril de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un diccionario contiene N ≤ 1000 jeroglíficos, cada uno escrito con dos
letras minúsculas. Dada una letra tecleada, hay que escribir los
jeroglíficos que empiezan por ella.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N, las N entradas de dos letras y luego la letra.

## Salida

Las entradas que coinciden, una por línea, en cualquier orden; nada si
no hay ninguna.

## Evaluación

El repositorio usa un comprobador semántico y acepta cualquier salida que satisfaga estas condiciones. El comprobador del repositorio divide la salida en tokens y compara listas ordenadas con sus multiplicidades. Las coincidencias pueden aparecer en cualquier orden; deben conservarse los duplicados.

## Ejemplos

### Ejemplo 1

Entrada:

```
6
na
no
ni
ki
ka
ku
k
```

Salida:

```
ka
ki
ku
```

## Solución

Se compara la primera letra de cada entrada con la tecleada y se
escriben las coincidencias en el orden de entrada. `O(N)`.

Detalles a tener en cuenta:

- sin coincidencias la salida queda vacía (pruebas 02, 05);
- una entrada que aparece dos veces se escribe dos veces (prueba 03);
- la letra debe ir primero: una coincidencia en el segundo lugar no
  cuenta (prueba 05).

## Soluciones optimizadas

La solución optimizada en C++ guarda las entradas de dos letras en un
arreglo local de cadenas C de tres bytes en lugar de `std::string`,
leídas con `scanf("%2s")` e impresas con `puts`: 120 KB en lugar de
392 KB, con el mismo tiempo.

Cada jeroglífico son dos letras. La solución optimizada en Java los
guarda en arreglos de bytes llenados desde bloques de 256 bytes y
escribe la respuesta desde un solo arreglo de bytes, sin `Scanner` ni
cadenas: 392 KB en lugar de 1804 KB, con el mismo tiempo. La solución
optimizada en Rust guarda cada jeroglífico como un par de bytes y
escribe con un `BufWriter` de búfer pequeño: 0.015 s en lugar de 0.046 s
y 196 KB en lugar de 236 KB.

`1545_implementation_optimized.py`. Conserva el filtro del diccionario, su orden y duplicados. Divide bytes crudos, comprueba el prefijo de una letra con startswith y une coincidencias como bytes. No retiene un diccionario decodificado ni otra lista de textos coincidentes, pero tokens, referencias de la sección y respuesta unida siguen ocupando O(N), con entradas de dos letras. Tiempo O(N). El programa independiente para el juez vacía stdout antes de os._exit(0), omitiendo la finalización normal del intérprete. Su propio Accepted acredita la mejora de memoria. El cambio de salida por sí solo no mejora la complejidad asintótica y su beneficio de ejecución no se garantiza en otras plataformas. La versión sencilla no cambia.

Frente a `1545_implementation.py`: tiempo 0.062 s → 0.14 s; memoria 460 KB → 216 KB.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1545_implementation_optimized.py`: puesto de tiempo 168/175 y de memoria 2/175 en esta muestra comparable.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1545_implementation.cpp](1545_implementation.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.015 s | 392 KB | 11287555 |
| [1545_implementation.go](1545_implementation.go) | Go 1.14 x64 | implementation | O(N) | AC | 0.031 s | 1104 KB | 11287556 |
| [1545_implementation.java](1545_implementation.java) | Java 1.8 | implementation | O(N) | AC | 0.093 s | 1804 KB | 11287558 |
| [1545_implementation.py](1545_implementation.py) | Python 3.12 x64 | implementation | O(N) | AC | 0.062 s | 460 KB | 11287557 |
| [1545_implementation.rs](1545_implementation.rs) | Rust 1.75 x64 | implementation | O(N) | AC | 0.046 s | 236 KB | 11287559 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1545_implementation_optimized.cpp](1545_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.015 s | 120 KB | 11303617 |
| [1545_implementation_optimized.java](1545_implementation_optimized.java) | Java 1.8 | implementation | O(N) | AC | 0.109 s | 392 KB | 11303759 |
| [1545_implementation_optimized.rs](1545_implementation_optimized.rs) | Rust 1.75 x64 | implementation | O(N) | AC | 0.015 s | 196 KB | 11303760 |
| [1545_implementation_optimized.py](1545_implementation_optimized.py) \* | PyPy 3.10 x64 | implementation | O(N) | AC | 0.14 s | 216 KB | 11324837 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
