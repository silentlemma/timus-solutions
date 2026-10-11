# 1242. Sospechosos de ser el hombre lobo en una aldea de parientes

[Timus 1242](https://acm.timus.ru/problem.aspx?space=1&num=1242) · dificultad 177 · graphs

Problema original de Leonid Volkov, del Concurso Individual de la Universidad Estatal de los Urales, 1 de marzo de 2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una aldea tiene N habitantes (1 < N ≤ 1000), y de algunos se sabe quiénes
son sus padres (como mucho dos cada uno, sin ciclos). Entre ellos vive un
hombre lobo, que nunca ataca a sus antepasados ni a sus descendientes.
Dada la lista de víctimas, hay que imprimir en orden creciente a todos los
que pueden ser el hombre lobo, o 0 si no puede serlo nadie.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N, luego líneas `hijo padre`, luego la palabra `BLOOD` y las víctimas, una
por línea.

## Salida

Los posibles hombres lobo en orden creciente, o 0.

## Ejemplos

### Ejemplo 1

Entrada:

```
8
1 3
3 6
4 5
6 2
4 6
8 1
BLOOD
3
8
```

Salida:

```
4 5 7
```

### Ejemplo 2

Entrada:

```
6
1 2
3 2
1 4
3 4
2 6
5 2
5 4
BLOOD
2
5
```

Salida:

```
0
```

## Solución

Basta una víctima para descartar a alguien: a la propia víctima, a
cualquier antepasado de una víctima (la víctima sería descendiente del
hombre lobo) y a cualquier descendiente de una víctima (la víctima sería
su antepasado). Todos los demás son compatibles con cada ataque.

Así que se sube por los enlaces a los padres desde todas las víctimas a
la vez marcando a todos los que se alcanzan, y luego se baja igual por
los enlaces a los hijos; quien queda sin marcar es sospechoso. Cada
recorrido visita a cada persona y cada enlace como mucho una vez.
`O(N + enlaces)`.

Detalles a tener en cuenta:

- los parientes que no son antepasados ni descendientes, como primos o
  hermanos, siguen siendo sospechosos (prueba 05);
- la lista de víctimas puede estar vacía, y entonces todos son
  sospechosos;
- una sola línea de 1000 generaciones necesita una pila explícita en vez
  de una recursión profunda.

## Notas por lenguaje

- Python y Rust leen toda la entrada y la parten en la palabra `BLOOD`;
  C++, Go y Java leen palabra a palabra hasta ella.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1242_graphs.cpp](1242_graphs.cpp) | G++ 13.2 x64 | graphs | O(N + links) | AC | 0.015 s | 232 KB |
| [1242_graphs.go](1242_graphs.go) | Go 1.14 x64 | graphs | O(N + links) | AC | 0.015 s | 1120 KB |
| [1242_graphs.java](1242_graphs.java) | Java 1.8 | graphs | O(N + links) | AC | 0.093 s | 1100 KB |
| [1242_graphs.py](1242_graphs.py) | Python 3.12 x64 | graphs | O(N + links) | AC | 0.078 s | 912 KB |
| [1242_graphs.rs](1242_graphs.rs) | Rust 1.75 x64 | graphs | O(N + links) | AC | 0.031 s | 312 KB |
