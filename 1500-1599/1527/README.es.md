# 1527. Malos caminos

[Timus 1527](https://acm.timus.ru/problem.aspx?space=1&num=1527) · dificultad 1131 · shortest_paths

Problema original de Dmitry Gozman, del Dmitry Gozman Contest 1 en el campus de invierno de Petrozavodsk, enero de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

n ciudades (1 ≤ n ≤ 100) están unidas por m carreteras de un solo
sentido (1 ≤ m ≤ 10⁴). Cada carretera tarda cierto tiempo, puede costar
un peaje y exige un coche con al menos cierta altura libre. Hay que
hallar la menor altura libre de un coche que pueda ir de s a f en t
minutos y con b peajes como mucho, y una ruta para él, o escribir -1.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

n, m, s y f; luego b y t; luego cada carretera: origen, destino, peaje
(0 o 1), tiempo y altura.

## Salida

La menor altura, el número de carreteras de una ruta y sus números en
orden; o -1. Se acepta cualquier ruta que cumpla.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 2 1 2
1 100
1 2 1 100 77
1 2 1 100 66
```

Salida:

```
66
1
2
```

### Ejemplo 2

Entrada:

```
2 2 1 2
0 100
1 2 0 101 77
1 2 1 100 66
```

Salida:

```
-1
```

## Solución

Si s = f, se devuelve altura 0 y una ruta vacía. En otro caso, la
respuesta es la altura de alguna carretera, y una altura mayor solo
añade carreteras, así que se hace búsqueda binaria sobre las alturas
ordenadas. Para probar una altura se ejecuta el algoritmo de Dijkstra
sobre estados (ciudad, peajes pagados), usando solo carreteras no más
altas y respetando ambos límites. Una ruta que repite una ciudad puede
quitar el bucle sin pagar más, así que importan como mucho n − 1 peajes
y el presupuesto puede limitarse a eso. Un estado se omite si menos
peajes ya llegan a su ciudad igual de rápido, lo que mantiene la
búsqueda pequeña. Se recorren las carreteras salientes por tiempo creciente
para que las paralelas más lentas no llenen la cola con entradas obsoletas.
En caso de empate se conserva el orden de entrada.
La carretera predecesora de cada estado da la ruta.
Con n² estados como mucho y las comprobaciones de dominancia, una prueba cuesta
`O(n·m·log(n·m) + n³)`, y en total `O(log m · (n·m·log(n·m) + n³))`,
mucho menos en la práctica.

Detalles a tener en cuenta:

- si s = f, no se necesita ninguna carretera y la respuesta es 0 aunque
  todas exijan una altura positiva (prueba 09);
- los ciclos de tiempo cero y las carreteras paralelas requieren cuidado
  al relajar (prueba 11);
- el presupuesto puede ser 10⁶, pero más de n − 1 peajes nunca ayudan
  (prueba 08);
- las carreteras pueden no tardar nada (prueba 03, gen3);
- la ruta más barata en dinero puede ser demasiado lenta, y al revés
  (pruebas 04, 05);
- la meta puede ser inalcanzable dentro de los límites o del todo
  (pruebas 02, 06, gen5);
- las alturas pueden ser 0 (prueba 07);
- puede haber muchas rutas válidas, así que las pruebas usan un
  comprobador (todas las pruebas).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1527_shortest_paths.cpp](1527_shortest_paths.cpp) | G++ 13.2 x64 | shortest_paths | O(log m * (n * m * log(n * m) + n^3)) | AC | 0.031 s | 484 KB |
| [1527_shortest_paths.go](1527_shortest_paths.go) | Go 1.14 x64 | shortest_paths | O(log m * (n * m * log(n * m) + n^3)) | AC | 0.031 s | 5480 KB |
| [1527_shortest_paths.java](1527_shortest_paths.java) | Java 1.8 | shortest_paths | O(log m * (n * m * log(n * m) + n^3)) | AC | 0.140 s | 5672 KB |
| [1527_shortest_paths.py](1527_shortest_paths.py) | Python 3.12 x64 | shortest_paths | O(log m * (n * m * log(n * m) + n^3)) | AC | 0.187 s | 6608 KB |
| [1527_shortest_paths.rs](1527_shortest_paths.rs) | Rust 1.75 x64 | shortest_paths | O(log m * (n * m * log(n * m) + n^3)) | AC | 0.031 s | 1016 KB |
