# 1314. Persecución en el metro

[Timus 1314](https://acm.timus.ru/problem.aspx?space=1&num=1314) · dificultad 588 · bfs

Problema original con idea de Leonid Volkov, preparado por Alexander Somov, Leonid Volkov e Igor Goldberg, del Octavo Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 11–16 de marzo de 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un metro tiene hasta 50 líneas de 2 a 50 estaciones cada una; una
estación es un número hasta 32 767, y una estación que aparece en
varias líneas (o varias veces en una) es un único lugar donde se
cruzan. Un fugitivo entra por la primera de M estaciones registradas
por una baliza y viaja hasta un destino elegido por una ruta más corta,
contando solo los tramos recorridos. La baliza registra en orden todas
las estaciones del camino. Hay que imprimir, en orden creciente, todas
las estaciones que pueden ser el destino.

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

N; N líneas, cada una con K y luego K estaciones; luego M y las M
estaciones registradas.

## Salida

Los destinos posibles, uno por línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
2 61 62
5 75 20 85 50 61
3 10 20 30
3 30 20 85
```

Salida:

```
50
61
62
85
```

## Solución

Se une con una arista cada par de estaciones vecinas de una línea. Sea
s la primera estación registrada y e la última, y d la distancia en
tramos. El fugitivo sigue una ruta más corta de s al destino t, y el
registro es su principio, así que:

- el registro debe ser un camino por aristas y él mismo una ruta más
  corta, d(s, e) = M − 1;
- t puede ser el destino exactamente cuando una ruta más corta de s a t
  pasa por e, es decir, d(s, t) = d(s, e) + d(e, t).

Dos búsquedas en anchura, desde s y desde e, dan todas las distancias.
`O(V + E)` para estaciones y aristas, como mucho 2500 de cada.

El enunciado promete un registro coherente. Si no lo es (una estación
desconocida, dos estaciones que no son vecinas o un rodeo), no sirve
ningún destino y no se imprime nada.

Detalles a tener en cuenta:

- la propia e es un destino, ya que el viaje puede terminar justo ahí
  (prueba 01);
- con una sola estación registrada sirve cualquier estación alcanzable
  desde ella (pruebas 02 y 07);
- un registro de dos estaciones que no son vecinas no sirve para nada
  (prueba 04);
- una estación más adelante en la línea no sirve si un atajo llega
  antes (prueba 05).

Las respuestas se compararon con la lista de todas las rutas más cortas
desde s en 400 redes aleatorias pequeñas.

## Notas por lenguaje

- Los números de estación indexan arreglos directamente, porque son
  menores que 32 768; Python usa un diccionario.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1314_bfs.cpp](1314_bfs.cpp) | G++ 13.2 x64 | bfs | O(V + E) | AC | 0.015 s | 1272 KB |
| [1314_bfs.go](1314_bfs.go) | Go 1.14 x64 | bfs | O(V + E) | AC | 0.015 s | 1920 KB |
| [1314_bfs.java](1314_bfs.java) | Java 1.8 | bfs | O(V + E) | AC | 0.093 s | 2884 KB |
| [1314_bfs.py](1314_bfs.py) | Python 3.12 x64 | bfs | O(V + E) | AC | 0.062 s | 1980 KB |
| [1314_bfs.rs](1314_bfs.rs) | Rust 1.75 x64 | bfs | O(V + E) | AC | 0.031 s | 1532 KB |
