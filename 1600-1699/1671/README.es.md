# 1671. La telaraña de Anansi

[Timus 1671](https://acm.timus.ru/problem.aspx?space=1&num=1671) · dificultad 108 · dsu

Problema original de Dmitry Poletaev (preparado por Alex Samsonov), del Ural SU Contest en el campus de verano de Petrozavodsk, agosto de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una telaraña tiene N nudos y M hilos entre pares de nudos. Q de los
hilos se rompen uno a uno en un orden dado. Tras cada corte hay que
imprimir en cuántos trozos (partes conexas) queda la telaraña.

## Entrada

N y M (2 ≤ N ≤ 100000, 1 ≤ M ≤ 100000), los M hilos como pares de nudos
distintos, luego Q (1 ≤ Q ≤ M) y los números de los hilos a romper, todos
distintos.

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
Con compresión de caminos es `O((N + M) α(N))`.

Detalles a tener en cuenta:

- los mismos dos nudos pueden estar unidos por varios hilos, y romper
  uno de ellos no cambia nada (prueba 03);
- la respuesta tras un corte es la cuenta antes de devolver ese hilo.

Las respuestas coinciden con un recuento de trozos por búsqueda tras cada
corte en 200 telarañas pequeñas aleatorias.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1671_dsu.cpp](1671_dsu.cpp) | G++ 13.2 x64 | dsu | O((N + M) alpha(N)) | AC | 0.218 s | 2716 KB |
| [1671_dsu.go](1671_dsu.go) | Go 1.14 x64 | dsu | O((N + M) alpha(N)) | AC | 0.031 s | 5912 KB |
| [1671_dsu.java](1671_dsu.java) | Java 1.8 | dsu | O((N + M) alpha(N)) | AC | 0.140 s | 6400 KB |
| [1671_dsu.py](1671_dsu.py) | Python 3.12 x64 | dsu | O((N + M) alpha(N)) | AC | 0.265 s | 35132 KB |
| [1671_dsu.rs](1671_dsu.rs) | Rust 1.75 x64 | dsu | O((N + M) alpha(N)) | AC | 0.031 s | 11476 KB |
