# 1115. Repartir longitudes en filas de longitud total dada

[Timus 1115](https://acm.timus.ru/problem.aspx?space=1&num=1115) · dificultad 409 · backtracking

Problema original de la primera competición de selección del equipo búlgaro para la IOI.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay `N < 100` objetos con longitudes enteras de 1 a 100 y `M` filas
(`1 < M < 10`) de longitudes dadas. Reparte todos los objetos en las filas
de modo que las longitudes de cada fila sumen exactamente la longitud de
la fila; cada fila recibe al menos un objeto. Se sabe que existe un
reparto. Imprime uno.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N M`, luego `N` líneas con las longitudes de los objetos y luego `M`
líneas con las longitudes de las filas.

## Salida

Para cada fila, en el orden de la entrada, dos líneas: el número de
objetos que tiene y sus longitudes.

## Evaluación

Se acepta cualquier reparto válido. El comprobador verifica que cada fila
suma su longitud y que los objetos usados son exactamente los dados.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 2
4
10
2
5
3
11
13
```

Salida:

```
3
5 4 2
2
10 3
```

## Solución

Es una partición exacta en varias partes, un problema difícil en general,
así que las soluciones usan búsqueda con poda. Al principio se llenan las
filas de menor a mayor longitud y se prueban los objetos por longitud
decreciente. Es solo una heurística: una fila corta no tiene necesariamente
menos formas de llenarse. La última fila toma todos los objetos restantes.
Cada longitud igual se prueba una sola vez en cada posición, ya que los
objetos iguales son intercambiables.

Antes de llenar una fila, el conjunto de bits `reach[k]` guarda las sumas
que pueden formar los objetos libres desde la posición `k`. Se construye
desde el final con `reach[k] = reach[k+1] | reach[k+1] << len`. Si el
objetivo de cualquier fila pendiente es inalcanzable, la rama se descarta.
Solo se toma un objeto si el resto de la fila actual puede completarse
con los objetos posteriores.

Un orden fijo todavía puede perder mucho tiempo en llenados incompatibles.
Cada uno de los primeros 128 intentos permite 256 llamadas a la búsqueda
de subconjuntos; después deshace todas las asignaciones y permuta las
filas y el orden de las longitudes distintas. Las longitudes iguales
permanecen juntas. Todos los lenguajes usan el mismo generador entero con
estado inicial fijo, por lo que producen salidas idénticas. Si estos
intentos fallan, una búsqueda final sin límite de llamadas examina todas
las posibilidades; agotar el presupuesto no significa que no haya
reparto. Se conservan los índices originales de las filas para la salida.

Con longitud total `S` y ancho de palabra del conjunto de bits `W`, una
cota conservadora de tiempo es `O(M^N * N^2 * ceil(S/W))` en el peor caso,
y la memoria auxiliar es `O(M * N * ceil(S/W))` palabras. Los reinicios no
eliminan el peor caso exponencial; los tiempos medidos no garantizan la
misma rapidez para toda entrada válida.

Detalles a tener en cuenta:

- probar objetos iguales en todos los órdenes hace explotar la búsqueda
  cuando hay muchas longitudes repetidas;
- sin comprobar las sumas, permanecen ramas con filas actuales o futuras
  inalcanzables;
- la prueba **07** provoca millones de llamadas con el orden fijo de
  menor a mayor longitud; las filas cortas no siempre tienen menos
  llenados (objetos `[1,1,2,5]`, objetivos `[2,2,5]`: dos formas para 2,
  pero solo una para 5);
- un intento interrumpido debe deshacer todas las asignaciones, y la
  búsqueda final debe ejecutarse sin límite de llamadas;
- las filas deben imprimirse en el orden de la entrada, aunque se llenan
  en otro.

La solución de Python se comprobó en las 7 pruebas guardadas, los
5 casos declarados del generador, 1.500 casos aleatorios pequeños frente
a un oráculo exacto independiente y 406 casos grandes o de frontera.

## Notas por lenguaje

- C++ usa `std::bitset`; Go, Java y Rust guardan las sumas en arreglos de
  palabras de 64 bits con un desplazamiento con «o» escrito a mano; Python
  usa enteros grandes como conjuntos de bits.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1115_backtracking.cpp](1115_backtracking.cpp) | G++ 13.2 x64 | backtracking | O(M^N * N^2 * ceil(S/W)) worst case | AC | 0.015 s | 436 KB |
| [1115_backtracking.go](1115_backtracking.go) | Go 1.14 x64 | backtracking | O(M^N * N^2 * ceil(S/W)) worst case | AC | 0.031 s | 1904 KB |
| [1115_backtracking.java](1115_backtracking.java) | Java 1.8 | backtracking | O(M^N * N^2 * ceil(S/W)) worst case | AC | 0.156 s | 4448 KB |
| [1115_backtracking.py](1115_backtracking.py) | Python 3.12 x64 | backtracking | O(M^N * N^2 * ceil(S/W)) worst case | AC | 0.062 s | 732 KB |
| [1115_backtracking.rs](1115_backtracking.rs) | Rust 1.75 x64 | backtracking | O(M^N * N^2 * ceil(S/W)) worst case | AC | 0.015 s | 756 KB |
