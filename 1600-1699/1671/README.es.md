# 1671. La telaraña de Anansi

[Timus 1671](https://acm.timus.ru/problem.aspx?space=1&num=1671) · dificultad 105 · dsu

Problema original de Dmitry Poletaev (preparado por Alex Samsonov), del Ural SU Contest en el campus de verano de Petrozavodsk, agosto de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una telaraña tiene N nudos y M hilos entre pares de nudos. Q de los
hilos se rompen uno a uno en un orden dado. Tras cada corte hay que
imprimir en cuántos trozos (partes conexas) queda la telaraña.

## Entrada

N y M (2 ≤ N ≤ 100000, 1 ≤ M ≤ 100000), los M hilos como pares de nudos
distintos numerados de 1 a N, luego Q (1 ≤ Q ≤ M) y los números de los
hilos a romper, todos distintos; los hilos se numeran de 1 a M en el
orden de entrada.

## Salida

Los Q números de trozos, separados por espacios.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 4
1 2
2 3
1 3
3 4
3
2 4 3
```

Salida:

```
1 2 3
```

### Ejemplo 2

Entrada:

```
3 1
1 2
1
1
```

Salida:

```
3
```

## Solución

Seguir los cortes es difícil, pero unir es fácil con una estructura de
conjuntos disjuntos, así que el proceso se recorre al revés. Se empieza
por la telaraña tras todos los cortes: se unen todos los hilos que nunca
se rompen. Luego se recorren los cortes del último al primero: el número
actual de trozos es la respuesta tras ese corte, y después el hilo vuelve
a su sitio. Cada unión de dos conjuntos distintos baja la cuenta en uno.
Con compresión de caminos es `O((N + M) log N)`.

Detalles a tener en cuenta:

- los mismos dos nudos pueden estar unidos por varios hilos, y romper
  uno de ellos no cambia nada (prueba 03);
- la respuesta tras un corte es la cuenta antes de devolver ese hilo.

Las respuestas coinciden con un recuento de trozos por búsqueda tras cada
corte en 200 telarañas pequeñas aleatorias.

## Soluciones optimizadas

La solución optimizada en C++ analiza los números a mano en bloques de
8 KB leídos con `fread` en lugar de llamar a `scanf` para cada uno, une
por tamaño, con la raíz guardando el tamaño de su conjunto con signo
menos, para que los árboles sigan siendo bajos, escribe cada respuesta
sobre el corte al que pertenece una vez procesado ese corte en lugar de
usar un segundo arreglo, e imprime las respuestas con `printf` en lugar
de reunirlas en una cadena: {1671_dsu_optimized.cpp}.

La solución optimizada en Go analiza los números byte a byte desde un
lector con búfer de 64 KB y los imprime con `strconv` a través de un
escritor de 64 KB, en lugar de usar `fmt.Fscan` y `fmt.Fprint`; la unión
de conjuntos es la misma: {1671_dsu_optimized.go}.

La solución optimizada en Java analiza los números a mano en bloques de
8 KB en lugar de usar `StreamTokenizer`, une por tamaño, con la raíz
guardando el tamaño de su conjunto con signo menos, para que los árboles
sigan siendo bajos, escribe cada respuesta sobre el corte al que
pertenece una vez procesado ese corte en lugar de usar un segundo
arreglo, e imprime los dígitos a través de un búfer de bytes de 8 KB en
lugar de reunir la salida en un `StringBuilder`:
{1671_dsu_optimized.java}.

La solución optimizada en Python lee la entrada línea a línea y guarda
los extremos de los hilos y los cortes en arreglos de enteros sin signo
de 32 bits, que bastan porque no pasan de 100000, en lugar de conservar
cada token de la entrada como cadena de bytes; une por tamaño, con la
raíz guardando el tamaño de su conjunto con signo menos, para que los
árboles sigan siendo bajos, y escribe cada respuesta sobre el corte al
que pertenece una vez procesado ese corte en lugar de construir una
segunda lista: {1671_dsu_optimized.py}.

La solución optimizada en Rust analiza los números directamente desde
los bytes de la entrada en lugar de reunirlos antes en un vector, guarda
los hilos como pares de `u32` y los padres como `i32`, que bastan porque
N y M no pasan de 100000, en lugar de `usize`, une por tamaño, con la
raíz guardando el tamaño de su conjunto con signo menos, para que los
árboles sigan siendo bajos, escribe cada respuesta sobre el corte al que
pertenece una vez procesado ese corte e imprime con un `BufWriter` en
lugar de unir un vector de cadenas: {1671_dsu_optimized.rs}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1671_dsu_optimized.cpp`: reducción de tiempo +83.42%; reducción de
  memoria +50.73%; base: `1671_dsu.cpp`.

- `1671_dsu_optimized.go`: reducción de tiempo +81.87%; reducción de
  memoria +21.86%; base: `1671_dsu.go`.

- `1671_dsu_optimized.java`: reducción de tiempo +10.71%; reducción de
  memoria +67.75%; base: `1671_dsu.java`.

- `1671_dsu_optimized.py`: reducción de tiempo -4.57%; reducción de
  memoria +70.52%; base: `1671_dsu.py`.

- `1671_dsu_optimized.rs`: reducción de tiempo +32.61%; reducción de
  memoria +65.71%; base: `1671_dsu.rs`.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1671_dsu.cpp](1671_dsu.cpp) | G++ 13.2 x64 | dsu | O((N + M) log N) | AC | 0.187 s | 2736 KB | 11304020 |
| [1671_dsu.go](1671_dsu.go) | Go 1.14 x64 | dsu | O((N + M) log N) | AC | 0.171 s | 7576 KB | 11304036 |
| [1671_dsu.java](1671_dsu.java) | Java 1.8 | dsu | O((N + M) log N) | AC | 0.140 s | 6400 KB | 11304022 |
| [1671_dsu.py](1671_dsu.py) | Python 3.12 x64 | dsu | O((N + M) log N) | AC | 0.328 s | 35904 KB | 11304037 |
| [1671_dsu.rs](1671_dsu.rs) | Rust 1.75 x64 | dsu | O((N + M) log N) | AC | 0.046 s | 11480 KB | 11304038 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1671_dsu_optimized.cpp](1671_dsu_optimized.cpp) | G++ 13.2 x64 | dsu | O((N + M) log N) | AC | 0.031 s | 1348 KB | 11304032 |
| [1671_dsu_optimized.go](1671_dsu_optimized.go) | Go 1.14 x64 | dsu | O((N + M) log N) | AC | 0.031 s | 5920 KB | 11304261 |
| [1671_dsu_optimized.java](1671_dsu_optimized.java) \* | Java 1.8 | dsu | O((N + M) log N) | AC | 0.125 s | 2064 KB | 11304033 |
| [1671_dsu_optimized.py](1671_dsu_optimized.py) \* | Python 3.12 x64 | dsu | O((N + M) log N) | AC | 0.343 s | 10584 KB | 11304034 |
| [1671_dsu_optimized.rs](1671_dsu_optimized.rs) | Rust 1.75 x64 | dsu | O((N + M) log N) | AC | 0.031 s | 3936 KB | 11304035 |

\* Aceptada; aún no cumple el objetivo de clasificación. Puede optimizarse más.
