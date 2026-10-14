# 1579. Transporte de abrigos

[Timus 1579](https://acm.timus.ru/problem.aspx?space=1&num=1579) · dificultad 499 · greedy

Problema original de Alexander Kokovin, del USU Junior Contest (XIV Campeonato Abierto por Equipos de Programación para Escolares de la Región de Sverdlovsk), octubre de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N ≤ 10⁵ abrigos con tallas dadas en orden no decreciente se sacan de una
tienda poniéndolos uno encima de otro. Un abrigo cabe sobre otro solo si
su talla es mayor en más de R. Hay que repartir los abrigos en el menor
número de viajes e imprimir cada viaje como su número de abrigos y sus
números en orden creciente.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y R, y luego las N tallas.

## Salida

El número K de viajes y luego K líneas con los abrigos de cada viaje.
Se acepta cualquier respuesta óptima.

## Ejemplos

### Ejemplo 1

Entrada:

```
8 3
1 2 3 5 7 10 12 13
```

Salida:

```
3
2 3 6
3 1 4 7
3 2 5 8
```

## Solución

Los abrigos cuyas tallas difieren como máximo en R entre sí nunca pueden
compartir viaje, así que el mayor número de tallas en una ventana
[x, x + R] es una cota inferior K; dos punteros sobre las tallas
ordenadas la hallan en una pasada.

K viajes también bastan: se reparten los abrigos en rueda, el abrigo i
al viaje i mod K. En un viaje, tras el abrigo i va el abrigo i + K, y los
K + 1 abrigos de i a i + K no caben en una misma ventana, así que la
talla del abrigo i + K supera en más de R a la del abrigo i. `O(N)`. Los
resultados se contrastaron con una búsqueda exhaustiva sobre todos los
repartos en viajes en 400 casos pequeños aleatorios.

Detalles a tener en cuenta:

- la talla debe crecer en más de R, así que tallas que difieren
  exactamente en R no pueden compartir viaje (prueba 04);
- con R = 0, las tallas iguales necesitan viajes distintos (pruebas 03,
  gen2);
- hay varias respuestas válidas, así que un verificador comprueba los
  viajes.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1579_greedy.cpp](1579_greedy.cpp) | G++ 13.2 x64 | greedy | O(N) | AC | 0.109 s | 984 KB |
| [1579_greedy.go](1579_greedy.go) | Go 1.14 x64 | greedy | O(N) | AC | 0.093 s | 4040 KB |
| [1579_greedy.java](1579_greedy.java) | Java 1.8 | greedy | O(N) | AC | 0.140 s | 9960 KB |
| [1579_greedy.py](1579_greedy.py) | Python 3.12 x64 | greedy | O(N) | AC | 0.203 s | 19332 KB |
| [1579_greedy.rs](1579_greedy.rs) | Rust 1.75 x64 | greedy | O(N) | AC | 0.046 s | 7672 KB |
