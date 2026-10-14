# 1552. Brainfuck

[Timus 1552](https://acm.timus.ru/problem.aspx?space=1&num=1552) · dificultad 1156 · dp

Problema original del Novosibirsk SU Contest en el campus de Petrozavodsk, septiembre de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una máquina brainfuck que solo conoce las órdenes > < + − . tiene 30000
celdas de un byte, todas a 0, y un puntero a la de más a la izquierda;
el puntero y los bytes dan la vuelta. Hay que escribir un programa lo
más corto posible que imprima una cadena dada de como mucho 50 letras
minúsculas. Un programa óptimo nunca necesita más de cuatro celdas.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

La cadena.

## Salida

Un programa lo más corto posible, en una línea. Se acepta cualquiera.

## Ejemplos

### Ejemplo 1

Entrada:

```
a
```

Salida:

```
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.
```

## Solución

Solo importan las celdas que usa el programa, y quitar las celdas sin
usar entre ellas o acercarlas a la celda inicial solo acorta los
recorridos, así que forman un bloque de cuatro celdas vecinas con la
celda inicial en algún lugar de él; ir a la izquierda de la celda 0 es
posible gracias a la vuelta. Una celda que se cambia sin imprimirla
podría cambiarse igual más tarde, así que cada celda guarda 0 o la
última letra impresa desde ella.

Se imprimen las letras una a una. Tras una letra, el estado es la celda
bajo el puntero (que guarda esa letra) y los valores de las otras tres,
0 o una letra: 4·27³ ≈ 79000 estados. Imprimir la siguiente letra desde
la celda q cuesta el recorrido |p − q|, el cambio del valor (de 0 a una
letra, su código; entre letras, su diferencia; dar la vuelta por 256
nunca sale más barato) y el punto. La DP guarda el camino más barato a
cada estado y el estado anterior, así que el programa se reconstruye
recorriendo hacia atrás. `O(n·4·27³·4)` pasos.

Detalles a tener en cuenta:

- el programa del ejemplo aparece en varias líneas, pero la respuesta es
  una sola línea;
- una celda nueva empieza en 0, 97 pasos por debajo de a, mientras que
  una ya usada puede estar mucho más cerca (pruebas 03, 04);
- letras muy separadas mezcladas ocupan tres celdas, una a la izquierda
  de la inicial, a la que se llega dando la vuelta (prueba 08);
- Python se ejecuta con PyPy: las pruebas de 50 letras tardan unos 3,2 s
  con CPython y unos 0,2 s con PyPy.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1552_dp.cpp](1552_dp.cpp) | G++ 13.2 x64 | dp | O(n * 4 * 27^3 * 4) | AC | 0.046 s | 16232 KB |
| [1552_dp.go](1552_dp.go) | Go 1.14 x64 | dp | O(n * 4 * 27^3 * 4) | AC | 0.062 s | 30712 KB |
| [1552_dp.java](1552_dp.java) | Java 1.8 | dp | O(n * 4 * 27^3 * 4) | AC | 0.140 s | 27348 KB |
| [1552_dp.py](1552_dp.py) | PyPy 3.10 x64 | dp | O(n * 4 * 27^3 * 4) | AC | 0.390 s | 22812 KB |
| [1552_dp.rs](1552_dp.rs) | Rust 1.75 x64 | dp | O(n * 4 * 27^3 * 4) | AC | 0.078 s | 16100 KB |
