# 1474. Sobre ranas

[Timus 1474](https://acm.timus.ru/problem.aspx?space=1&num=1474) · dificultad 725 · constructive

Problema original de Alexander Ipatov, del concurso de la Universidad Estatal de los Urales y la Universidad Técnica Estatal de Oriol en el campus de verano de Petrozavodsk, agosto de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

En los montículos 0 … 2N (1 ≤ N ≤ 499) hay N ranas blancas en
0 … N − 1, el montículo N vacío y N ranas negras en N + 1 … 2N. Una
rana blanca avanza a la derecha al vecino vacío o salta a la derecha
por encima de una rana negra hasta el montículo vacío; una negra hace
lo mismo hacia la izquierda. Los movimientos van en cualquier orden.
Hay que intercambiar los colores en como mucho un millón de
movimientos, escribiendo el número de movimientos y el montículo de
salida de cada uno, o −1 si es imposible.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N.

## Salida

K y luego los K montículos de salida. Se acepta cualquier secuencia
correcta.

## Ejemplos

### Ejemplo 1

Entrada:

```
1
```

Salida:

```
3
2 0 1
```

## Solución

Las ranas solo avanzan, así que cada rana blanca adelanta exactamente
una vez a cada rana negra, y solo un salto adelanta a una rana: N²
saltos. Entre todas recorren 2N(N + 1) montículos, dos por salto y uno
por paso, así que hay 2N pasos. Por tanto, toda partida con éxito dura
N² + 2N movimientos, 249 999 para N = 499, y la respuesta nunca es −1;
el único peligro es un callejón sin salida, en el que dos ranas del
mismo color se bloquean.

Los movimientos van en tandas de 1, 2, …, N, luego N otra vez y
luego N, …, 1, alternando negras y blancas, primero las negras.
Dentro de una tanda, se salta al hueco si es posible y, si no, se
avanza un paso. Este orden evita los callejones sin salida, así que
siempre hay un movimiento; reproducirlo confirma el intercambio para
cada N de 1 a 499. `O(N²)`.

Detalles a tener en cuenta:

- el orden importa: moverse con avidez sin el esquema de tandas puede
  dejar atascadas dos ranas del mismo color una tras otra (02; el
  comprobador reproduce cada movimiento);
- −1 nunca es la respuesta (todas las pruebas);
- con N = 499 se escriben 249 999 índices de salida. Conviene usar
  salida con búfer (gen4).

## Soluciones optimizadas

Las versiones optimizadas calculan directamente la siguiente posición del hueco. El paso corto cierra cada tanda creciente y abre cada tanda decreciente. La tanda central contiene solo saltos. Se reutiliza la representación decimal de cada posición.

G++ 13.2 x64, envío 11320508. Tiempo 0,031 → 0,015 s, memoria 1524 → 224 KB.

Go 1.14 x64, envío 11320528. Tiempo 0,046 → 0,046 s, memoria 10276 → 1152 KB.

Java 1.8, envío 11320556. Tiempo 0,14 → 0,109 s, memoria 8416 → 772 KB.

Python 3.12 x64, envío 11320580. Tiempo 0,25 → 0,109 s, memoria 23792 → 2044 KB.

Rust 1.75 x64, envío 11320607. Tiempo 0,031 → 0,015 s, memoria 14900 → 248 KB.

**Envíos de las versiones sencillas en Timus**

G++ 13.2 x64 №11322266 · Go 1.14 x64 №11322267 · Java 1.8 №11322268 · Python 3.12 x64 №11322269 · Rust 1.75 x64 №11322270.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1474_constructive.cpp](1474_constructive.cpp) | G++ 13.2 x64 | constructive | O(N^2) | AC | 0.031 s | 1524 KB | 11322266 |
| [1474_constructive.go](1474_constructive.go) | Go 1.14 x64 | constructive | O(N^2) | AC | 0.046 s | 10276 KB | 11322267 |
| [1474_constructive.java](1474_constructive.java) | Java 1.8 | constructive | O(N^2) | AC | 0.14 s | 8416 KB | 11322268 |
| [1474_constructive.py](1474_constructive.py) | Python 3.12 x64 | constructive | O(N^2) | AC | 0.25 s | 23792 KB | 11322269 |
| [1474_constructive.rs](1474_constructive.rs) | Rust 1.75 x64 | constructive | O(N^2) | AC | 0.031 s | 14900 KB | 11322270 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1474_constructive_optimized.cpp](1474_constructive_optimized.cpp) | G++ 13.2 x64 | constructive | O(N^2) | AC | 0.015 s | 224 KB | 11320508 |
| [1474_constructive_optimized.go](1474_constructive_optimized.go) \* | Go 1.14 x64 | constructive | O(N^2) | AC | 0.046 s | 1152 KB | 11320528 |
| [1474_constructive_optimized.java](1474_constructive_optimized.java) \* | Java 1.8 | constructive | O(N^2) | AC | 0.109 s | 772 KB | 11320556 |
| [1474_constructive_optimized.py](1474_constructive_optimized.py) | Python 3.12 x64 | constructive | O(N^2) | AC | 0.109 s | 2044 KB | 11320580 |
| [1474_constructive_optimized.rs](1474_constructive_optimized.rs) | Rust 1.75 x64 | constructive | O(N^2) | AC | 0.015 s | 248 KB | 11320607 |

\* Las versiones marcadas aún pueden mejorar su clasificación.
