# 2214. Mejor valor de una ventana deslizante que puede moverse K veces

[Timus 2214](https://acm.timus.ru/problem.aspx?space=1&num=2214) · dificultad 2005 · dp

Problema original de Vladimir Cherepanov, de la Olimpiada Académica Universitaria Escolar de Informática 2024.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un emisor cubre L plantas consecutivas de N, y el día i suma a_ij a
cada planta cubierta j. Empieza en cualquier lugar y, a lo sumo una vez
al día y K veces en total, puede moverse a mitad del día; entonces ese
día cuentan la posición vieja y la nueva, cada planta una vez. Hallar el
mayor total en M días. Los límites son 3.5 segundos y 256 MB.

## Entrada

N, M, L y K, 1 ≤ N ≤ 5000, 1 ≤ M ≤ 100, 1 ≤ L ≤ N, 0 ≤ K ≤ M, y luego
los M × N valores entre 0 y 10⁹.

## Salida

El mayor total.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 4 2 1
3 2 0
4 1 1
0 3 7
2 1 1
```

Salida:

```
23
```

## Solución

Un estado es (día, movimientos usados, posición al final del día). Como
moverse a la misma posición no cambia nada, todo plan se puede rellenar
hasta usar exactamente K movimientos, así que solo se guardan los
números de movimientos que aún pueden llegar a K el último día.

Con sumas de prefijo de la fila del día, un día sin movimiento añade la
suma de la ventana w(x). Un día con movimiento de x a y añade la unión
de las dos ventanas:

- si |x − y| < L la unión es un intervalo, que vale
  prefix(mayor final) − prefix(menor inicio), lo que se separa en un
  término de x y otro de y; el mejor x para cada y es un máximo de
  ventana deslizante sobre las últimas L posiciones, mantenido con una
  cola monótona, una vez para x a la izquierda de y y otra a la derecha;
- si las ventanas son disjuntas, el valor es w(x) + w(y), y el mejor
  dp(x) + w(x) con x a distancia al menos L es un máximo de prefijo
  acumulado.

Así cada capa cuesta O(N), y hay M · (K + 1) capas.

En el ejemplo el emisor cubre las plantas 1 y 2, se mueve a 2 y 3 a
mitad del segundo día, y las plantas terminan en 7, 7 y 9, que suman
23.

Esto cuesta O(N M K) de tiempo y O(N K) de memoria.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2214_dp.cpp](2214_dp.cpp) | G++ 13.2 x64 | dp | O(N M K) | AC | 0.250 s | 2244 KB |
| [2214_dp.go](2214_dp.go) | Go 1.14 x64 | dp | O(N M K) | AC | 0.265 s | 27244 KB |
| [2214_dp.java](2214_dp.java) | Java 1.8 | dp | O(N M K) | AC | 0.593 s | 16348 KB |
| [2214_dp.py](2214_dp.py) | PyPy 3.10 x64 | dp | O(N M K) | AC | 1.218 s | 63468 KB |
| [2214_dp.rs](2214_dp.rs) | Rust 1.75 x64 | dp | O(N M K) | AC | 0.250 s | 10548 KB |
