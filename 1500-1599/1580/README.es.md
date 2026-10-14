# 1580. Las deudas del decano

[Timus 1580](https://acm.timus.ru/problem.aspx?space=1&num=1580) · dificultad 880 · graphs

Problema original de Alexey Efremov, del USU Junior Contest (XIV Campeonato Abierto por Equipos de Programación para Escolares de la Región de Sverdlovsk), octubre de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

El decano debe a cada uno de N ≤ 1000 estudiantes una suma desconocida.
Cada uno de M ≤ 10⁵ días, un par distinto de estudiantes le dice al
decano cuánto se les debe a los dos juntos. Hay que imprimir lo que se
le debe a cada estudiante, con dos cifras tras el punto, si las
declaraciones lo determinan de forma única, e `IMPOSSIBLE` si no.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

N y M, y luego cada declaración como dos estudiantes y su total A
(−10000 ≤ A ≤ 10000).

## Salida

N sumas, una por línea, o `IMPOSSIBLE`.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 3
1 2 2
2 3 4
3 1 6
```

Salida:

```
2.00
0.00
4.00
```

### Ejemplo 2

Entrada:

```
4 3
1 2 2
1 3 4
1 4 6
```

Salida:

```
IMPOSSIBLE
```

## Solución

Cada declaración es una ecuación x_u + x_v = A, una arista de un grafo
sobre los estudiantes. Dentro de una componente conexa se elige la deuda
t de un estudiante; recorriendo las aristas con una búsqueda en anchura,
cada otra deuda es ±t más una constante, y el signo cambia en cada paso.
Si la componente no tiene ciclo impar, todas sus deudas pueden moverse
+d y −d en los dos lados y toda declaración se sigue cumpliendo, así que
la respuesta no es única. Una arista que cierra un ciclo impar une a dos
estudiantes con el mismo signo y da 2t = A − constantes, lo que fija t.

Las deudas se calculan en medios rublos, donde todo es entero, y se
imprimen con `.00` o `.50`. Al final se vuelven a comprobar todas las
declaraciones: las que se contradicen tampoco dejan respuesta.
`O(N + M)`. Los resultados se contrastaron con una eliminación gaussiana
exacta sobre los racionales en 500 sistemas pequeños aleatorios.

Detalles a tener en cuenta:

- una suma puede ser de medio rublo, también negativa: −0.50 debe
  conservar su signo menos (pruebas 03, 04);
- cada componente debe tener un ciclo impar, no solo una de ellas
  (prueba 05);
- las declaraciones a lo largo de dos ciclos impares pueden
  contradecirse (pruebas 06, gen2).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1580_graphs.cpp](1580_graphs.cpp) | G++ 13.2 x64 | graphs | O(N + M) | AC | 0.203 s | 7628 KB |
| [1580_graphs.go](1580_graphs.go) | Go 1.14 x64 | graphs | O(N + M) | AC | 0.156 s | 11500 KB |
| [1580_graphs.java](1580_graphs.java) | Java 1.8 | graphs | O(N + M) | AC | 0.109 s | 11772 KB |
| [1580_graphs.py](1580_graphs.py) | Python 3.12 x64 | graphs | O(N + M) | AC | 0.359 s | 47816 KB |
| [1580_graphs.rs](1580_graphs.rs) | Rust 1.75 x64 | graphs | O(N + M) | AC | 0.046 s | 10468 KB |
