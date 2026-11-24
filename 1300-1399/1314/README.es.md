# 1314. Persecución en el metro

[Timus 1314](https://acm.timus.ru/problem.aspx?space=1&num=1314) · dificultad 561 · bfs

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
`O(V + E)` para estaciones y aristas, como mucho 2500 de cada;
Python tarda `O(V log V + E)` por ordenar los destinos.

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

## Soluciones optimizadas

Se comprimen los números de estación en orden y se guardan las listas de vecinos en un
arreglo plano. Un BFS desde la primera estación registrada obtiene las capas de distancia.
Tras validar el prefijo, se marca la última estación registrada y se propagan las marcas por
aristas hacia la siguiente capa en orden BFS. Exactamente las estaciones marcadas admiten
una continuación mínima. La compresión cuesta O((V + E) log(V + E)) en tiempo y los arreglos
usan O(V + E) en espacio. El envío 11316949 tardó 0,015 s y usó 224 KB. La versión sencilla tardó 0,015 s y usó 1256 KB.

Go comprime los números de estación con un conjunto de bits y guarda la adyacencia y la cola de BFS en arreglos fijos. El bit alto de cada distancia marca qué estaciones pueden continuar el camino mínimo registrado. Go 1.14 x64, envío 11322926. Tiempo 0,015 → 0,015 s, memoria 1844 → 376 KB.

Rust asigna índices compactos a las estaciones y guarda sus vecinos en un único arreglo contiguo. El envío 11317248 tardó 0,062 s y usó 320 KB frente a 0,046 s y 1532 KB en la base.

Java guarda los índices compactos de las estaciones y los enlaces de adyacencia en arreglos de enteros cortos. El envío 11317252 tardó 0,109 s y usó 636 KB frente a 0,093 s y 2864 KB en la base.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1314_bfs_implementation_optimized.rs`. La adyacencia usa arreglos enlazados, identificadores de vértice de 16 bits e índices next/head con signo, en vez de miles de vectores. Se mantienen las distancias de BFS. Se leen tokens con un búfer nativo acotado; los cortos se guardan dentro del objeto y solo los largos reservan espacio extra. La conversión decimal conserva las cotas con signo sin guardar toda la entrada de comandos. La entrada de C llama directamente al solucionador y vacía la salida de Rust antes de volver; se conserva la implementación de entrada habitual.

Accepted #11328977 (Rust 1.75 x64): **0.015 s / 556 KB**. Comparación archivada: `1314_bfs.rs` (Rust 1.75 x64) — 0.046 s / 1532 KB (#11322322).

## Notas por lenguaje

- Los números de estación indexan arreglos directamente, porque son
  menores que 32 768; Python usa un diccionario.

**Envíos de las versiones sencillas en Timus**

G++ 13.2 x64 №11322317 · Go 1.14 x64 №11322318 · Python 3.12 x64 №11321737 · Java 1.8 №11322321 · Rust 1.75 x64 №11322322.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1314_bfs.cpp](1314_bfs.cpp) | G++ 13.2 x64 | bfs | O(V + E) | AC | 0.015 s | 1256 KB | 11322317 |
| [1314_bfs.go](1314_bfs.go) | Go 1.14 x64 | bfs | O(V + E) | AC | 0.015 s | 1844 KB | 11322318 |
| [1314_bfs.java](1314_bfs.java) | Java 1.8 | bfs | O(V + E) | AC | 0.093 s | 2864 KB | 11322321 |
| [1314_bfs.py](1314_bfs.py) | Python 3.12 x64 | bfs | O(V log V + E) | AC | 0.078 s | 1884 KB | 11321737 |
| [1314_bfs.rs](1314_bfs.rs) | Rust 1.75 x64 | bfs | O(V + E) | AC | 0.046 s | 1532 KB | 11322322 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1314_bfs_optimized.cpp](1314_bfs_optimized.cpp) | G++ 13.2 x64 | bfs | O((V + E) log(V + E)) | AC | 0.015 s | 224 KB | 11316949 |
| [1314_bfs_optimized.go](1314_bfs_optimized.go) \* | Go 1.14 x64 | bfs | O(S + V + E) | AC | 0.015 s | 376 KB | 11322926 |
| [1314_bfs_optimized.rs](1314_bfs_optimized.rs) | Rust 1.75 x64 | bfs | O(S + V + E) | AC | 0.062 s | 320 KB | 11317248 |
| [1314_bfs_optimized.java](1314_bfs_optimized.java) | Java 1.8 | bfs | O(S + V + E) | AC | 0.109 s | 636 KB | 11317252 |
| [1314_bfs_implementation_optimized.rs](1314_bfs_implementation_optimized.rs) | Rust 1.75 x64 | bfs, implementation | O(V + E) | AC | 0.015 s | 556 KB | 11328977 |

\* Accepted; aún no se alcanza el objetivo de [RATING_CRITERIA.md](../../RATING_CRITERIA.md). Esta versión puede optimizarse más.
