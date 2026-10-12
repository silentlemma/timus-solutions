# 1338. Automóviles

[Timus 1338](https://acm.timus.ru/problem.aspx?space=1&num=1338) · dificultad 1747 · bfs

Problema original de Alexander Klepinin, del USU Championship 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un plano de ciudad de W × H ≤ 500 × 500 celdas tiene edificios (`.`),
carretera (`#`) y puntos de control (`o`) que también son carretera;
las celdas de carretera se unen por lados comunes. Los puntos de control
se numeran desde la fila de abajo hacia arriba y, dentro de una fila, de
izquierda a derecha. En cada uno de hasta 20 experimentos se elige un
punto destino T, y desde cada otro punto de control un coche va a T por
una ruta más corta. Cuando hay varias continuaciones más cortas, el
coche prefiere el sur, luego el norte, el oeste y el este. Para cada
experimento hay que imprimir cuántos coches llegan a T desde el norte,
el sur, el este y el oeste.

Límite de tiempo: 3 segundos. Límite de memoria: 64 MB.

## Entrada

W y H, luego H líneas del plano, luego M y M números de destino.

## Salida

Para cada experimento una línea
`Experiment #N: North: Rn, South: Rs, East: Re, West: Rw`.

## Ejemplos

### Ejemplo 1

Entrada:

```
10 5
..####....
..o..o....
..####.#o.
......##..
.o#####...
1
4
```

Salida:

```
Experiment #1: North: 0, South: 1, East: 0, West: 0
```

## Solución

Una búsqueda en anchura desde T da a cada celda de carretera su
distancia a T. Un coche en una celda a distancia d pasa a la primera
vecina a distancia d − 1 en el orden sur, norte, oeste, este. Así cada
celda tiene una siguiente celda fija, y su coche llega a T por el mismo
lado que el coche de esa siguiente celda. Recorriendo las celdas en el
orden en que las halló la búsqueda, cada siguiente celda ya está
resuelta, y cada celda copia su lado. Una celda junto a T llega por el
lado en que está: dar un paso al norte hacia T es llegar desde el sur.
Contando los lados de todos los puntos de control, salvo T, que T
alcanza, se obtiene la respuesta. `O(M · W · H)`.

Detalles a tener en cuenta:

- la numeración empieza por la fila de abajo, no por la de arriba
  (prueba 04);
- los puntos en carreteras que no llegan a T no envían coches
  (prueba 04);
- el giro preferido decide entre rutas de igual longitud en cada paso,
  no solo al salir (pruebas 01 y 06);
- simular cada coche por separado cuesta su ruta entera para cada uno de
  hasta 250 000 puntos, lo que es demasiado lento.

Las respuestas se compararon con conducir cada coche paso a paso en 500
planos pequeños aleatorios.

## Notas por lenguaje

- CPython necesita unos 2,5 segundos con un plano completo y 20
  experimentos, demasiado cerca del límite de 3 segundos, así que la
  solución en Python se envía con PyPy 3.10, donde tarda unos 0,4
  segundos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1338_bfs.cpp](1338_bfs.cpp) | G++ 13.2 x64 | bfs | O(M·W·H) | AC | 0.093 s | 5048 KB |
| [1338_bfs.go](1338_bfs.go) | Go 1.14 x64 | bfs | O(M·W·H) | AC | 0.218 s | 30164 KB |
| [1338_bfs.java](1338_bfs.java) | Java 1.8 | bfs | O(M·W·H) | AC | 0.218 s | 5960 KB |
| [1338_bfs.py](1338_bfs.py) | PyPy 3.10 x64 | bfs | O(M·W·H) | AC | 1.234 s | 31900 KB |
| [1338_bfs.rs](1338_bfs.rs) | Rust 1.75 x64 | bfs | O(M·W·H) | AC | 0.187 s | 9900 KB |
