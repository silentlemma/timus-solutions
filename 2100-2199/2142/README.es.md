# 2142. Pagar maná rojo, azul y de cualquier color con tierras dobles

[Timus 2142](https://acm.timus.ru/problem.aspx?space=1&num=2142) · dificultad 127 · greedy

Problema original de Valentin Zuev, del Concurso Escolar de Programación de los Urales 2019.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay A tierras rojas, B azules y C dobles; cada una da un maná, y una
doble da rojo o azul a elegir. Un hechizo necesita X maná rojo, Y azul y
Z más de cualquier color. Decidir si las tierras bastan. Los límites son
1 segundo y 256 MB.

## Entrada

A, B, C, y luego X, Y, Z, todos entre 0 y 10⁹.

## Salida

"It is a kind of magic" si el hechizo se puede pagar, y si no "There are
no miracles in life".

## Evaluación

Las pruebas del repositorio comparan todo el texto de salida, ignorando solo el espacio en blanco final. Conserva los espacios significativos, los saltos de línea, las mayúsculas y la puntuación.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 3 1
2 2 1
```

Salida:

```
It is a kind of magic
```

### Ejemplo 2

Entrada:

```
5 6 5
6 5 6
```

Salida:

```
There are no miracles in life
```

## Solución

Las tierras rojas deben pagar primero el maná rojo y las azules el azul,
porque la parte de cualquier color la puede pagar cualquier tierra. Lo
que dejan sin pagar, max(0, X − A) + max(0, Y − B), tiene que salir de
las tierras dobles. Después cada tierra restante de cualquier clase puede
pagar el maná Z de cualquier color, así que la segunda condición es
A + B + C ≥ X + Y + Z. Las dos juntas son necesarias y suficientes. Las
sumas llegan a 3 · 10⁹, más allá de los enteros de 32 bits.

Trampa (prueba 02, segundo ejemplo): cubrir ambos colores no basta.
El rojo necesita 6 − 5 = 1 tierra doble, pero en total hay 16 tierras
para 17 de maná.

## Soluciones optimizadas

`2142_greedy_optimized.go`. Conserva las dos condiciones necesarias y suficientes: tierras dobles cubren max(0,X-A)+max(0,Y-B), y el total debe alcanzar X+Y+Z. Tras cubrir colores, cualquier tierra restante paga maná neutral. Mantiene ambas frases exactas y el caso todo cero. Las sumas alcanzan3·10^9, por lo que Go usa int64 y Python enteros exactos. Tiempo y estado O(1), con bytes y salida directa en vez de envolventes básicas. os.Stdin.Read/os.Stdout.Write portables y conversión entera directa usan búferes fijos de entrada y salida de 4096 bytes. Se atienden escrituras parciales antes de reutilizar el búfer de salida. Se conserva la fuente sencilla original con Accepted.

Frente a `2142_greedy.go`: tiempo 0.031 s → 0.031 s; memoria 1088 KB → 860 KB.

`2142_greedy_optimized.py`. Conserva las dos condiciones necesarias y suficientes: tierras dobles cubren max(0,X-A)+max(0,Y-B), y el total debe alcanzar X+Y+Z. Tras cubrir colores, cualquier tierra restante paga maná neutral. Mantiene ambas frases exactas y el caso todo cero. Las sumas alcanzan3·10^9, por lo que Go usa int64 y Python enteros exactos. Tiempo y estado O(1), con bytes y salida directa en vez de envolventes básicas. El programa independiente para el juez vacía stdout antes de os._exit(0), omitiendo la finalización normal del intérprete. Su propio Accepted acredita la mejora de memoria. El cambio de salida por sí solo no mejora la complejidad asintótica y su beneficio de ejecución no se garantiza en otras plataformas. La versión sencilla no cambia.

Frente a `2142_greedy.py`: tiempo 0.078 s → 0.125 s; memoria 416 KB → 208 KB.

La solución optimizada en Java lee los seis números byte a byte de
`System.in` en lugar de crear un `Scanner`, cuyas expresiones regulares
y datos de configuración regional son el gasto principal de un programa
que hace dos comparaciones; las sumas siguen en `long`, porque llegan a
3 · 10⁹: {2142_greedy_optimized.java}.

### Mejora medida

Cada versión optimizada tiene Accepted y cumple un criterio de clasificación
o de mejora de recursos. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `2142_greedy_optimized.java`: reducción de tiempo +12.80%; reducción
  de memoria +76.67%; base: `2142_greedy.java`.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`2142_greedy_optimized.go`: puesto de tiempo 5/12 y de memoria 3/12 en esta muestra comparable.

`2142_greedy_optimized.py`: puesto de tiempo 66/79 y de memoria 1/79 en esta muestra comparable.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2142_greedy.cpp](2142_greedy.cpp) | G++ 13.2 x64 | greedy | O(1) | AC | 0.015 s | 124 KB | 11294928 |
| [2142_greedy.go](2142_greedy.go) | Go 1.14 x64 | greedy | O(1) | AC | 0.031 s | 1088 KB | 11294929 |
| [2142_greedy.java](2142_greedy.java) | Java 1.8 | greedy | O(1) | AC | 0.125 s | 1560 KB | 11304055 |
| [2142_greedy.py](2142_greedy.py) | Python 3.12 x64 | greedy | O(1) | AC | 0.078 s | 416 KB | 11294930 |
| [2142_greedy.rs](2142_greedy.rs) | Rust 1.75 x64 | greedy | O(1) | AC | 0.046 s | 228 KB | 11304056 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2142_greedy_optimized.java](2142_greedy_optimized.java) \* | Java 1.8 | greedy | O(1) | AC | 0.109 s | 364 KB | 11304424 |
| [2142_greedy_optimized.go](2142_greedy_optimized.go) \* | Go 1.14 x64 | greedy | O(1) | AC | 0.031 s | 860 KB | 11325054 |
| [2142_greedy_optimized.py](2142_greedy_optimized.py) \* | PyPy 3.10 x64 | greedy | O(1) | AC | 0.125 s | 208 KB | 11324931 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
