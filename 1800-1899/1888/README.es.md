# 1888. Experiencia de los pilotos

[Timus 1888](https://acm.timus.ru/problem.aspx?space=1&num=1888) · dificultad 463 · bfs

Problema original de Magaz Asanov, de la subregión oriental del NEERC 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada uno de n vuelos llevó a dos de p pilotos, y la experiencia de uno
era exactamente un año mayor que la del otro; no se sabe cuál. Cada
experiencia es un número entero de años de 1 a 50. Hay que hallar la
mayor diferencia posible entre el piloto más y el menos experimentado y
unas experiencias que la den, o escribir −1 si los datos se
contradicen.

## Entrada

n y p (2 ≤ n ≤ 1000, 2 ≤ p ≤ 50) y luego n vuelos, cada uno con dos
números de piloto distintos.

## Salida

La mayor diferencia y después las p experiencias, o −1. Se acepta
cualquier asignación válida.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 4
1 2
3 1
2 4
3 4
```

Salida:

```
2
1 2 2 3
```

### Ejemplo 2

Entrada:

```
3 3
1 2
2 3
1 3
```

Salida:

```
-1
```

## Solución

Los pilotos de un vuelo difieren en uno, así que sus experiencias
tienen distinta paridad. Por tanto un grupo conexo de pilotos debe ser
bipartito; un ciclo impar significa −1.

Dentro de un grupo, dos pilotos a distancia k difieren como mucho en k,
así que la diferencia es como mucho el diámetro. Y se alcanza: la
experiencia 1 + (distancia a un extremo de un diámetro) cambia
exactamente en uno a lo largo de cada vuelo, porque en un grafo
bipartito las distancias de vecinos difieren en uno. Con p ≤ 50 el
diámetro es como mucho 49, así que los valores quedan en 1 … 50.

Grupos distintos se desplazan por separado, así que con dos o más la
respuesta es el 49 completo: un grupo alterna 1 y 2 según la paridad y
los demás alternan 49 y 50. Un BFS desde cada piloto cuesta
`O(p·(p + n))`.

En el primer ejemplo los pilotos forman el ciclo 1–2–4–3 de longitud
cuatro, cuyo diámetro es 2: desde el piloto 1 las distancias son 0, 1,
1, 2.

Trampas:

- varios grupos dan 49 enseguida, por pequeños que sean;
- un grupo no puede superar su diámetro, aunque sea largo y estrecho;
- la misma pareja puede volar varias veces, lo que no cambia nada.

Las respuestas coinciden con una implementación aceptada independiente,
y las experiencias pasan un comprobador, en 200 conjuntos aleatorios de
vuelos.

## Soluciones optimizadas

Go y Rust guardan cada vecindad en una palabra de 64 bits, pues p≤50. BFS procesa capas completas: OR de sus vecindades menos los visitados produce la siguiente. Una arista dentro de una capa contradice la bipartición. En una componente se ejecuta BFS desde cada vértice y se conservan la máxima excentricidad y sus distancias; dos BFS no bastan en grafos generales. Varias componentes se desplazan según paridad a 1/2 y 50/49. Las máscaras eliminan vuelos repetidos. Cada BFS visita hasta p palabras: tiempo O(n+p²), espacio O(p) palabras. Se conservan las bases; C++, Java y Python reutilizan las admitidas.

Las implementaciones base aceptadas [1888_bfs.cpp](1888_bfs.cpp), [1888_bfs.java](1888_bfs.java), [1888_bfs.py](1888_bfs.py) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1888_bfs.cpp](1888_bfs.cpp) | G++ 13.2 x64 | bfs | O(p (p + n)) | AC | 0.015 s | 184 KB | 11328316 |
| [1888_bfs.go](1888_bfs.go) | Go 1.14 x64 | bfs | O(p (p + n)) | AC | 0.062 s | 1196 KB | 11291114 |
| [1888_bfs.java](1888_bfs.java) | Java 1.8 | bfs | O(p (p + n)) | AC | 0.109 s | 640 KB | 11328380 |
| [1888_bfs.py](1888_bfs.py) \* | Python 3.12 x64 | bfs | O(p (p + n)) | AC | 0.078 s | 712 KB | 11328319 |
| [1888_bfs.rs](1888_bfs.rs) | Rust 1.75 x64 | bfs | O(p (p + n)) | AC | 0.031 s | 248 KB | 11328320 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1888_bfs_bitmask.go](1888_bfs_bitmask.go) \* | Go 1.14 x64 | bfs, bitmask | O(n + p²) | AC | 0.031 s | 312 KB | 11315257 |
| [1888_bfs_bitmask.rs](1888_bfs_bitmask.rs) \* | Rust 1.75 x64 | bfs, bitmask | O(n + p²) | AC | 0.015 s | 68 KB | 11315673 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
