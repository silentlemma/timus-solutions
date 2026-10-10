# 1176. Tender todos los canales de un solo sentido que faltan en un viaje de ida y vuelta

[Timus 1176](https://acm.timus.ru/problem.aspx?space=1&num=1176) · dificultad 335 · graphs

Problema original de Pavel Atnashev, del Tercer Concurso Individual de Programación de la Universidad Estatal de los Urales, Ekaterimburgo, 16 de febrero de 2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

`N ≤ 1000` planetas tienen algunos canales de un solo sentido, dados como
matriz de adyacencia. Cada par ordenado de planetas distintos necesita un
canal. Un constructor empieza en el planeta `A`, solo puede moverse
tendiendo un canal nuevo, debe tender exactamente los que faltan y volver
a `A`. Faltan como mucho 32 000 canales y se garantiza una solución. Hay
que imprimir los canales en el orden en que se tienden.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y `A`, y luego la matriz `N×N`.

## Salida

Los canales tendidos, un par `desde hasta` por línea.

## Evaluación

Se acepta cualquier orden que sea un recorrido de `A` de vuelta a `A` que
use cada canal que falta exactamente una vez y nada más.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 2
0 0 1 0
0 0 1 0
1 1 0 1
0 0 1 0
```

Salida:

```
2 4
4 1
1 2
2 1
1 4
4 2
```

## Solución

La ruta del constructor es un recorrido cerrado por todos los canales que
faltan, cada uno una vez: un circuito de Euler del grafo de canales que
faltan. Se promete una solución, así que cada planeta tiene tantos
canales que faltan de salida como de entrada, y los que tienen alguno son
alcanzables desde `A`.

El algoritmo de Hierholzer construye el circuito con una pila explícita.
Desde el planeta en la cima de la pila se sigue por canales sin usar.
Cuando a un planeta no le queda ninguno, se saca y pasa a la respuesta.
Los planetas salen en orden inverso del circuito, con cada lazo lateral
insertado donde se encontró. `O(N² + M)`, donde domina leer la matriz.

Detalles a tener en cuenta:

- la matriz tiene un millón de números, así que conviene leer la entrada
  de golpe;
- la diagonal no es un canal que falte;
- si no falta nada, la respuesta está vacía;
- un recorrido recursivo podría bajar 32 000 niveles, de ahí la pila
  explícita.

Cada ruta impresa se comprobó contra los canales que faltan en 100
imperios pequeños aleatorios y en otros generados con mil planetas y
32 000 canales que faltan.

## Notas por lenguaje

- C++ y Rust leen la matriz con sus medios habituales, Go con un escáner
  de palabras, Java con un lector de bytes escrito a mano y Python
  partiendo toda la entrada de una vez.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1176_graphs.cpp](1176_graphs.cpp) | G++ 13.2 x64 | graphs | O(N² + M) | AC | 0.531 s | 368 KB |
| [1176_graphs.go](1176_graphs.go) | Go 1.14 x64 | graphs | O(N² + M) | AC | 0.062 s | 5968 KB |
| [1176_graphs.java](1176_graphs.java) | Java 1.8 | graphs | O(N² + M) | AC | 0.156 s | 2608 KB |
| [1176_graphs.py](1176_graphs.py) | Python 3.12 x64 | graphs | O(N² + M) | AC | 0.203 s | 18940 KB |
| [1176_graphs.rs](1176_graphs.rs) | Rust 1.75 x64 | graphs | O(N² + M) | AC | 0.031 s | 3560 KB |
