# 1290. Sabotaje

[Timus 1290](https://acm.timus.ru/problem.aspx?space=1&num=1290) · dificultad 80 · sorting

Problema original del folclore (preparado por Den Raskovalov), de la Novena Competición Abierta por Equipos de Programación para Escolares, 13 de marzo de 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una función lenta recibe N ≤ 25 000 enteros positivos, cada uno como
mucho 25 000. Imprime cuántos son al menos 1, luego cuántos son mayores
que 1, mayores que 2, etc., y se detiene antes del primer 0. Los números
impresos se vuelven a leer como un nuevo arreglo y se aplica el mismo
paso otra vez; la segunda lista es el resultado. Hay que obtenerlo
rápido.

Para 4 1 6 la primera lista es 3 2 2 2 1 1 y la segunda es 6 4 1.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y luego los N números, uno por línea. N puede ser 0.

## Salida

Los números del resultado, uno por línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
4
1
6
```

Salida:

```
6
4
1
```

## Solución

Dibujemos los números como filas de casillas: el número p es una fila
de p casillas, todas alineadas a la izquierda. El j-ésimo número impreso
cuenta las filas que llegan a la columna j, así que la primera lista son
las longitudes de las columnas: el dibujo girado (la partición
conjugada). Girarlo otra vez devuelve las filas, de la más larga a la
más corta.

Así que la función solo ordena el arreglo de mayor a menor. Los valores
son como mucho 25 000, de modo que basta un ordenamiento por conteo:
contar cada valor e imprimir los valores de 25 000 a 1, cada uno tantas
veces como apareció. `O(N + 25 000)`.

Detalles a tener en cuenta:

- con N = 0 la salida está vacía (prueba 02);
- los números iguales vuelven todos (pruebas 04 y 06).

La equivalencia se comprobó con una simulación directa de los dos pasos
en 200 arreglos aleatorios.

## Soluciones optimizadas

Las soluciones optimizadas (C++, Python) guardan los mismos contadores,
pero como números de 16 bits, ya que un valor aparece a lo sumo 25 000
veces, y formatean la línea de cada valor una vez para repetirla tantas
veces como aparece. C++ analiza los números a mano desde bloques de 8 KB
en lugar de `scanf`; Python lee bloques de 4 KB mediante un generador en
lugar de partir toda la entrada, y guarda los contadores en un
`array("H")`. C++: 156 KB en lugar de 280 KB, con el mismo tiempo;
Python: 0.078 s en lugar de 0.109 s y 880 KB en lugar de 4732 KB.

## Notas por lenguaje

- Todos los lenguajes guardan un contador por valor, 25 001 en total, e
  imprimen a través de un búfer.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1290_sorting.cpp](1290_sorting.cpp) | G++ 13.2 x64 | sorting | O(N + 25000) | AC | 0.031 s | 280 KB | 11284563 |
| [1290_sorting.go](1290_sorting.go) | Go 1.14 x64 | sorting | O(N + 25000) | AC | 0.031 s | 1384 KB | 11284564 |
| [1290_sorting.java](1290_sorting.java) | Java 1.8 | sorting | O(N + 25000) | AC | 0.125 s | 2056 KB | 11284571 |
| [1290_sorting.py](1290_sorting.py) | Python 3.12 x64 | sorting | O(N + 25000) | AC | 0.109 s | 4732 KB | 11284569 |
| [1290_sorting.rs](1290_sorting.rs) | Rust 1.75 x64 | sorting | O(N + 25000) | AC | 0.015 s | 724 KB | 11284575 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1290_sorting_optimized.cpp](1290_sorting_optimized.cpp) | G++ 13.2 x64 | sorting | O(N + 25000) | AC | 0.015 s | 156 KB | 11303588 |
| [1290_sorting_optimized.py](1290_sorting_optimized.py) | Python 3.12 x64 | sorting | O(N + 25000) | AC | 0.078 s | 880 KB | 11303589 |
