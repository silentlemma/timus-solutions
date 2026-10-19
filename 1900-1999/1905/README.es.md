# 1905. Routes Through Space-Time Events

[Timus 1905](https://acm.timus.ru/problem.aspx?space=1&num=1905) · difficulty 1131 · bfs

Original problem by Dmitry Ivankov, from Ural Championship 2012.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Los vuelos conectan lugares con instantes fijos de salida y llegada;
pueden llegar antes de salir. Parte de un lugar e instante dados y alcanza
el destino en su instante objetivo, esperando hacia el futuro si hace falta.
Dos visitas separadas al mismo lugar no pueden compartir un instante antes
de terminar, ni durante la espera. Límites: 3 segundos y 64 MB.

## Entrada

Primero n y m, con 1 ≤ n ≤ 100 000 y 0 ≤ m ≤ 100 000. Cada una de las
siguientes m líneas contiene origen, destino, salida y llegada de un vuelo.
Los lugares van de 1 a n y los tiempos enteros de 0 a 10⁶. La última línea
da lugar inicial, destino, tiempo actual y tiempo objetivo. Los vuelos
se numeran desde 1 en el orden de entrada.

## Salida

Imprime `Impossible` si no hay ruta. En otro caso, k y los k índices de
vuelos en orden de viaje. Se permiten cero vuelos: imprime 0 y una segunda
línea vacía. Se acepta cualquier secuencia válida.

## Evaluación

El comprobador verifica índices, lugares y embarques, y que se llegue no
después del objetivo; la espera completa el instante exacto. Recoge todos
los intervalos cerrados de visita, los ordena por lugar y tiempo, y rechaza
solapamientos, incluidos extremos compartidos.
Se acepta cualquier ruta válida.

## Ejemplos

```
4 3
1 2 10 20
2 4 50 20
4 3 20 30
1 3 10 30
```

```
3
1 2 3
```

## Solución

Crea un vértice por cada par distinto (lugar,tiempo) de los extremos de
vuelos, inicio y objetivo. Unifica eventos iguales. En cada lugar, ordena
los eventos y conecta cada uno con el siguiente mediante espera hacia
adelante. Añade las aristas de vuelos, también si retroceden en el tiempo.

Haz BFS desde el inicio. Guarda el padre y el índice de vuelo al descubrir
un vértice; una espera usa índice 0. Si el objetivo es inalcanzable, imprime
`Impossible`. En caso contrario, sigue los padres, conserva índices positivos
y revierte su orden.

Toda ruta real induce un recorrido del grafo, pues la espera pasa por todos
los eventos intermedios. Así, la ausencia de camino demuestra imposibilidad.
A la inversa, un objetivo alcanzable admite un camino simple, como el del
árbol BFS. Si dos visitas separadas a un lugar se solaparan, un extremo
de una estaría en la otra. Ese extremo es un evento de vuelo, inicio o
destino, y la otra cadena de espera también visita su vértice. Esto repetiría
un vértice, contradiciendo la simplicidad. Por tanto, no hay colisión.
Esperas consecutivas son una visita continua; un transbordo instantáneo usa
una vez el evento compartido.

Codifica `lugar·B+tiempo`, B=1 000 001. Ordena y elimina duplicados; ubica
extremos por búsqueda binaria. El orden agrupa lugares: i puede esperar
hasta i+1 si ambos cocientes por B coinciden. No almacenes esas aristas;
guarda solo vuelos en listas enlazadas mediante arrays head/next.

Hay como máximo 2m+2 vértices y 3m+1 aristas. Ordenar y buscar cuesta
`O((m+1) log(m+2))`; BFS y reconstrucción son lineales. Espacio `O(m+1)`,
sin reservar nada para lugares sin eventos.

El ejemplo espera en el lugar 2 hasta 50, retrocede al lugar 4 en el
instante 20 y transborda inmediatamente al último vuelo.

## Notas por lenguaje

Las claves necesitan 64 bits: pueden superar 10¹¹. Los índices caben en
32 bits. C++, Go, Java y Rust usan arrays/vectores primitivos. Python guarda
índices y cola en `array`, con una lista de claves enteras ordenada; elimina
duplicados in situ y libera el generador de tokens antes del BFS para reducir
el máximo de memoria. Se usa CPython 3.12.

No exijas llegada posterior a salida. Incluye inicio y objetivo aunque no
sean extremos de vuelos. La espera solo avanza, los eventos iguales se
unifican y también cuentan las colisiones durante la espera.

Las respuestas coinciden con una búsqueda sobre secuencias de vuelos que
comprueba las colisiones directamente en 3048 casos pequeños; el
comprobador acepta cinco rutas válidas y rechaza 16 erróneas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1905_bfs.cpp](1905_bfs.cpp) | G++ 13.2 x64 | bfs | O((m+1) log(m+2)) | AC | 0.125 s | 6596 KB |
| [1905_bfs.go](1905_bfs.go) | Go 1.14 x64 | bfs | O((m+1) log(m+2)) | AC | 0.156 s | 16544 KB |
| [1905_bfs.java](1905_bfs.java) | Java 1.8 | bfs | O((m+1) log(m+2)) | AC | 0.234 s | 9452 KB |
| [1905_bfs.py](1905_bfs.py) | Python 3.12 x64 | bfs | O((m+1) log(m+2)) | AC | 0.609 s | 15064 KB |
| [1905_bfs.rs](1905_bfs.rs) | Rust 1.75 x64 | bfs | O((m+1) log(m+2)) | AC | 0.078 s | 15332 KB |
