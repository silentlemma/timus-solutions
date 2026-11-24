# 1072. La ruta más corta entre dos ordenadores a través de subredes IP

[Timus 1072](https://acm.timus.ru/problem.aspx?space=1&num=1072) · dificultad 504 · bfs, graphs

Problema original de Evgeny Kobzev, del Ural State University Personal Contest Online, febrero de 2001, Students Session.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada uno de `N` ordenadores (`2 ≤ N ≤ 90`) tiene hasta 5 interfaces de
red; una interfaz es una dirección IP y una máscara de subred (unos
seguidos de ceros). Dos interfaces están en la misma subred cuando
`IP1 AND mask1` es igual a `IP2 AND mask2`. Un paquete va directamente
entre ordenadores que comparten una subred, y de una subred a otra solo a
través de un ordenador con interfaces en ambas. Halla un camino por el
menor número de ordenadores entre dos ordenadores dados.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N`; luego, para cada ordenador, el número de interfaces `K` y `K` líneas
con una dirección IP y una máscara en notación con puntos; al final los
números de los dos ordenadores.

## Salida

`Yes` y los ordenadores del camino en orden, o `No` si no hay camino.

## Evaluación

Se acepta cualquier camino más corto. El comprobador verifica que el
camino va del primer ordenador al segundo, que cada dos vecinos en él
comparten una subred y que tiene el menor número posible de ordenadores.

## Ejemplos

### Ejemplo 1

Entrada:

```
6
2
10.0.0.1 255.0.0.0
192.168.0.1 255.255.255.0
1
10.0.0.2 255.0.0.0
3
192.168.0.2 255.255.255.0
212.220.31.1 255.255.255.0
212.220.35.1 255.255.255.0
1
212.220.31.2 255.255.255.0
2
212.220.35.2 255.255.255.0
195.38.54.65 255.255.255.224
1 
195.38.54.94 255.255.255.224
1 6
```

Salida:

```
Yes
1 3 5 6
```

## Solución

Cada interfaz se reduce al número `IP AND mask`. Dos ordenadores están
unidos cuando tienen un número igual entre sus interfaces; un salto entre
ordenadores unidos es exactamente una transferencia directa, y un
ordenador en medio del camino tiene interfaces en las subredes de ambos
lados. Así que la tarea es un camino más corto en este grafo de
ordenadores, y una búsqueda en anchura desde el primer ordenador lo
encuentra. Siguiendo los padres guardados hacia atrás desde el segundo
ordenador se obtiene el camino. `O(N^2 · K^2)`.

Detalles a tener en cuenta:

- la prueba de subred usa la máscara propia de cada interfaz:
  `10.0.0.77/255.0.0.0` y `10.0.0.5/255.255.255.0` están en la misma
  subred, porque ambas dan `10.0.0.0`, mientras que `10.1.0.1/255.0.0.0` y
  `10.1.0.2/255.255.0.0` no lo están, aunque cada dirección cae dentro del
  rango de la otra;
- las máscaras `0.0.0.0` y `255.255.255.255` están permitidas y no
  necesitan un caso especial;
- las direcciones son números sin signo de 32 bits; un tipo con signo
  también sirve, siempre que solo se compare la igualdad.

Las longitudes de los caminos se comprobaron con Floyd–Warshall sobre el
mismo grafo, construido por separado y comprobando que las máscaras
tienen la forma de unos seguidos de ceros.

## Soluciones optimizadas

El BFS de Go mantiene una lista de computadoras por valor de subred, en vez de comparar todos los pares de interfaces. Al extraer una computadora de la cola, expande sus subredes y visita a cada miembro aún no visitado. La primera expansión procede de una computadora de distancia mínima, por lo que todos los miembros reciben su menor distancia posible en el siguiente salto. Después se elimina la lista de esa subred: una expansión posterior no mejora ninguna ruta. Cada interfaz se procesa un número constante de veces: tiempo esperado O(N·K) con la tabla hash y espacio O(N·K). Los padres reconstruyen un camino mínimo; los duplicados son inocuos y, si los extremos coinciden, basta una computadora.

El envío aceptado en Go 1.14 x64 tarda 0.031 s frente a 0.015 s de la base y usa 280 KB frente a 1180 KB.

Las implementaciones base aceptadas [1072_bfs.cpp](1072_bfs.cpp), [1072_bfs.java](1072_bfs.java), [1072_bfs.py](1072_bfs.py), [1072_bfs.rs](1072_bfs.rs) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Notas por lenguaje

Se conservan las cinco bases BFS con entrada habitual. La nueva versión Go analiza las direcciones como valores sin signo de 32 bits y usa manejadores estándar de E/S. Se comparan los valores IP AND su propia máscara, no los pares (IP AND máscara, máscara); máscaras distintas pueden producir la misma subred. Los archivos existentes de C++, Java, Python y Rust también cubren el conjunto rápido según las reglas de admisión de la instantánea guardada.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1072_bfs.cpp](1072_bfs.cpp) | G++ 13.2 x64 | bfs | O(N^2 · K^2) | AC | 0.015 s | 208 KB | 11278927 |
| [1072_bfs.go](1072_bfs.go) | Go 1.14 x64 | bfs | O(N^2 · K^2) | AC | 0.015 s | 1180 KB | 11278929 |
| [1072_bfs.java](1072_bfs.java) | Java 1.8 | bfs | O(N^2 · K^2) | AC | 0.078 s | 776 KB | 11278935 |
| [1072_bfs.py](1072_bfs.py) \* | Python 3.12 x64 | bfs | O(N^2 · K^2) | AC | 0.078 s | 612 KB | 11278931 |
| [1072_bfs.rs](1072_bfs.rs) | Rust 1.75 x64 | bfs | O(N^2 · K^2) | AC | 0.015 s | 224 KB | 11278936 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1072_bfs_optimized.go](1072_bfs_optimized.go) | Go 1.14 x64 | bfs | O(N·K) | AC | 0.031 s | 280 KB | 11314790 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
