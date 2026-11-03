# 1244. Qué cartas faltan en una baraja, por su peso

[Timus 1244](https://acm.timus.ru/problem.aspx?space=1&num=1244) · dificultad 254 · dp

Problema original de Alexander Petrov, del Concurso Individual de la Universidad Estatal de los Urales, 1 de marzo de 2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

La baraja completa contiene `N` cartas numeradas, `2 ≤ N ≤ 100`,
con pesos enteros `1 ≤ w_i ≤ 1000` miligramos. Sea `T` su peso total.
Las cartas restantes pesan un entero `W`, `0 < W < T`. Determina los
índices que faltan: en orden creciente si el conjunto es único, `-1` si
hay varios conjuntos posibles y `0` si no existe ninguno. Las cartas de
igual peso siguen siendo distintas. Tiempo: 0,5 segundos. Memoria: 64 MB.

## Entrada

W, luego N y luego los N pesos de las cartas.

## Salida

Las cartas que faltan, -1 o 0.

## Evaluación

Se comparan enteros separados por espacios o saltos de línea. La solución única enumera los índices ausentes en orden creciente; en otro caso se escribe un único token, `0` o `-1`.

## Ejemplos

### Ejemplo 1

Entrada:

```
270
4
100
110
170
200
```

Salida:

```
2 4
```

### Ejemplo 2

Entrada:

```
270
4
100
110
160
170
```

Salida:

```
-1
```

### Ejemplo 3

Entrada:

```
270
4
100
120
160
180
```

Salida:

```
0
```

## Solución

Las cartas que quedan en la baraja forman un conjunto de peso total W, y
las que faltan son el resto. Así que se cuentan los conjuntos de cartas
que pesan W, pero solo hasta 2, porque no importa más: `ways[i][s]` es el
número de conjuntos de las primeras i cartas que pesan s, con tope 2, y
`ways[i][s] = min(2, ways[i−1][s] + ways[i−1][s − w_i])`. Entonces
`ways[N][W]` vale 0, 2 (se imprime -1) o exactamente 1.

Para el conjunto único, se recorre hacia atrás desde la última carta con
s = W: la carta i falta justo cuando las primeras i − 1 cartas ya forman
s por sí solas, `ways[i−1][s] = 1`; si no, está en la baraja y s baja en
su peso. La unicidad hace que solo pueda cumplirse una de las dos cosas.
`O(N·W)` con W < 100 000.

Detalles a tener en cuenta:

- cartas iguales son cartas distintas: con dos cartas de peso 1 y W = 1
  puede faltar cualquiera, así que la respuesta es -1 (prueba 04);
- pueden faltar varias cartas, hasta todas menos una (prueba 08).

Las respuestas se compararon con la prueba de todos los subconjuntos en
1500 barajas pequeñas aleatorias.

## Soluciones optimizadas

Tomar el complemento establece una biyección entre las cartas
restantes de peso `W` y las ausentes de peso `T−W`. Se cuentan subconjuntos
para `S = min(W,T−W)` y se complementan los índices cuando corresponda.
Se conservan los casos imposible, único y ambiguo; además `S ≤ 50000`.

Las cuatro versiones nativas actualizan una sola fila de contadores
saturados `0,1,2`, recorriendo las sumas en orden decreciente. Al alcanzar
una suma por primera vez guardan la última carta y nunca sobrescriben ese
predecesor. La suma anterior ya existía antes de procesar esa carta;
el recorrido decreciente y los pesos positivos hacen que los índices
disminuyan estrictamente durante la reconstrucción. No se reutiliza una
carta y, si el subconjunto final es único, ese testigo es el requerido.
Los índices son como máximo 100. Tiempo `O(N·S)`, espacio `O(S+N)`.

Python conserva un bitset de alcanzabilidad por prefijo, pero solo el
bitset actual de sumas con al menos dos representaciones. Propaga las
ambigüedades anteriores con y sin la carta; la intersección entre la
alcanzabilidad anterior y su desplazamiento también implica dos conjuntos.
Reconstruye la solución única usando los prefijos. Al detectar dos formas
de sumar `S` puede imprimir `-1`: omitir todas las cartas posteriores
conserva ambos testigos.

Sean `C` el mayor peso, `w` los bits por bloque del entero grande,
`B = ceil((S+C+1)/w)` y `B_W = ceil((W+C+1)/w)`. Una cota conservadora
de tiempo y espacio para Python optimizado es `O(N·B)` palabras; la versión
sencilla usa los prefijos correspondientes a `B_W`. El término `C` cubre
el temporal desplazado antes de aplicar la máscara. Se conservan sin
cambios las cinco fuentes sencillas.

Ahorro medido de memoria frente a las fuentes sencillas Accepted inalteradas: C++ 98.1%, Go 90.3%, Java 95.6%, Python 80.2%, Rust 97.7%. Las cinco cumplen el umbral por memoria. Un tick de diferencia temporal no demuestra una aceleración fiable. Instantánea: 2 de noviembre de 2026; las filas con asterisco admiten más optimización.

## Notas por lenguaje

Las fuentes sencillas C++/Go/Java/Rust conservan la tabla completa de prefijos; Python conserva bitsets de alcanzabilidad y multiplicidad por prefijo. Las nativas optimizadas guardan una fila y predecesores de primera llegada; Python guarda prefijos de alcanzabilidad y un bitset de multiplicidad. Python superó 40.770 entradas: enumeración independiente de subconjuntos indexados para barajas pequeñas o aleatorias y respuestas exactas para casos grandes. Cada uno de los cinco programas reales también superó 72 entradas de referencia seleccionadas en Docker.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1244_dp.cpp](1244_dp.cpp) | G++ 13.2 x64 | dp | O(N W) | AC | 0.031 s | 9472 KB | 11283911 |
| [1244_dp.go](1244_dp.go) | Go 1.14 x64 | dp | O(N W) | AC | 0.031 s | 11676 KB | 11283913 |
| [1244_dp.java](1244_dp.java) | Java 1.8 | dp | O(N W) | AC | 0.109 s | 12768 KB | 11283918 |
| [1244_dp.py](1244_dp.py) | Python 3.12 x64 | dp | O(N B_W) | AC | 0.093 s | 2848 KB | 11283915 |
| [1244_dp.rs](1244_dp.rs) | Rust 1.75 x64 | dp | O(N W) | AC | 0.031 s | 9692 KB | 11283921 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1244_dp_optimized.cpp](1244_dp_optimized.cpp) | G++ 13.2 x64 | dp | O(N S) | AC | 0.015 s | 184 KB | 11308168 |
| [1244_dp_optimized.go](1244_dp_optimized.go) | Go 1.14 x64 | dp | O(N S) | AC | 0.031 s | 1128 KB | 11308170 |
| [1244_dp_optimized.java](1244_dp_optimized.java) | Java 1.8 | dp | O(N S) | AC | 0.109 s | 560 KB | 11308171 |
| [1244_dp_optimized.py](1244_dp_optimized.py) | Python 3.12 x64 | dp | O(N B) | AC | 0.078 s | 564 KB | 11308167 |
| [1244_dp_optimized.rs](1244_dp_optimized.rs) | Rust 1.75 x64 | dp | O(N S) | AC | 0.015 s | 220 KB | 11308172 |
