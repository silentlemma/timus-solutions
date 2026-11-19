# 1194. Cuántos apretones de manos cuando una fiesta se dispersa de vuelta a casa

[Timus 1194](https://acm.timus.ru/problem.aspx?space=1&num=1194) · dificultad 84 · math

Problema original de Leonid Volkov, del Quinto Campeonato por Equipos de Programación para Escolares, 2 de marzo de 2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

`N ≤ 20000` hobbits, `K` de ellos matrimonios, salen juntos de una
fiesta. En cada cruce un grupo se divide en grupos menores, y cada uno da
la mano a todos aquellos de los que se separa. Los grupos se siguen
dividiendo hasta que cada uno es un hobbit solo o un matrimonio. Se dan
las divisiones; hay que contar todos los apretones de manos.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y `K`, y luego, para cada división, el número del grupo, el número de
grupos nuevos y el número y tamaño de cada uno.

## Salida

El número de apretones de manos.

## Evaluación

Las pruebas del repositorio comparan exactamente los tokens de salida; los espacios entre tokens no son significativos.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 0
1 2 2 2 3 1
2 2 4 1 5 1
```

Salida:

```
3
```

## Solución

Dos hobbits que no son cónyuges se dan la mano exactamente una vez: en la
división en la que acaban por primera vez en grupos distintos. Los únicos
pares que nunca se separan son los matrimonios, que vuelven juntos a
casa. Así que la respuesta es `N·(N − 1)/2 − K`, y la descripción de las
divisiones no importa. `O(1)`, aparte de leer la primera línea.

Detalles a tener en cuenta:

- las líneas de las divisiones pueden ignorarse por completo, pero una
  solución que suma los pares separados en cada división obtiene el mismo
  número;
- `N·(N − 1)/2` llega a unos `2·10⁸`, que aún cabe en 32 bits, aunque la
  aritmética de 64 bits no cuesta nada aquí.

Las respuestas se compararon con una solución escrita aparte, que suma
los apretones división a división, en 200 fiestas aleatorias y en todas
las pruebas.

## Soluciones optimizadas

`1194_math_optimized.go`. Mantiene pares no ordenados h(h−1)/2 menos las parejas dadas. Solo aritmética escalar y espacio auxiliar constante. Buffers acotados de entrada de 256 bytes y salida de 64 usan syscall.Read/Write de Go 1.14, reintentan EINTR/escrituras parciales y tratan EOF de cero bytes. Elimina inicialización fmt/bufio/os.File. Pruebas Linux y compilación cruzada Windows validan funcionamiento y construcción; las métricas pareadas siguientes vienen de nuestro Accepted exacto en juez Windows. Se conserva fuente didáctica legible.

Frente a `1194_math.go`: tiempo 0.015 s → 0.015 s; memoria 1064 KB → 280 KB.

La solución optimizada en Java analiza los dos números a mano con
`System.in.read` en lugar de `Scanner`: 308 KB en lugar de 1552 KB, con
el mismo tiempo. La fórmula es la misma.

`1194_math_optimized.cpp`. Conserva N(N-1)/2-K: cada pareja no casada se separa una vez, con independencia de las descripciones de partición. Lee solo los dos números iniciales y convierte bytes de C explícitamente para leer y escribir, en lugar del formato entero. El algoritmo y el estado auxiliar tienen tamaño constante.

Frente a `1194_math.cpp`: tiempo 0.031 s → 0.015 s; memoria 128 KB → 80 KB.

`1194_math_optimized.py`. Lee en bytes solo la primera línea documentada con N y K; no lee el registro de particiones porque el invariante de parejas no depende de él. Imprime N(N-1)/2-K, vacía explícitamente la salida y termina sin la limpieza normal del intérprete. No retiene una cadena ni una lista de tokens de toda la entrada.

Frente a `1194_math.py`: tiempo 0.093 s → 0.125 s; memoria 328 KB → 220 KB.

`1194_math_optimized.rs`. Usa el mismo invariante de parejas leyendo solo dos enteros con signo mediante C. Las descripciones de partición no se almacenan ni procesan. La salida decimal manual evita el formato de Rust y cadenas completas de entrada/salida; con las cotas enteras, tiempo y estado auxiliar son O(1).

Frente a `1194_math.rs`: tiempo 0.015 s → 0.015 s; memoria 208 KB → 48 KB.

## Notas por lenguaje

- Todos los lenguajes leen solo `N` y `K`.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1194_math.cpp](1194_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.031 s | 128 KB | 11283468 |
| [1194_math.go](1194_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 1064 KB | 11283469 |
| [1194_math.java](1194_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1552 KB | 11283472 |
| [1194_math.py](1194_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.093 s | 328 KB | 11283471 |
| [1194_math.rs](1194_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 208 KB | 11283473 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1194_math_optimized.java](1194_math_optimized.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 308 KB | 11303576 |
| [1194_math_optimized.cpp](1194_math_optimized.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 80 KB | 11325056 |
| [1194_math_optimized.py](1194_math_optimized.py) \* | PyPy 3.10 x64 | math | O(1) | AC | 0.125 s | 220 KB | 11324849 |
| [1194_math_optimized.rs](1194_math_optimized.rs) \* | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 48 KB | 11324859 |
| [1194_math_optimized.go](1194_math_optimized.go) \* | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 280 KB | 11325654 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
