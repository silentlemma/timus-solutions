# 1934. La ruta más segura entre las más cortas

[Timus 1934](https://acm.timus.ru/problem.aspx?space=1&num=1934) · difficulty 359 · shortest_paths, probability

Original problem from Open Ural FU Championship 2012 | by Denis Dublennykh (prepared by Egor Shchelkonogov).

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Buscar una ruta de s a t en un grafo simple no dirigido. Una arista
con porcentaje entero p falla de forma independiente con probabilidad
p/100. Primero se minimiza el número de vértices visitados, incluidos
ambos extremos; después, la probabilidad de al menos un fallo.
También sirve una ruta mínima cuyo riesgo difiera del óptimo en
como máximo 10⁻⁶. Límites: 1 segundo, 64 MB.

## Entrada

Primero n,m: 2≤n≤100000 y 1≤m≤100000. Después, s,t distintos en 1..n.
Siguen m ternas a,b,p con 1≤a,b≤n, a≠b y 0≤p≤99. Hay como máximo
una arista por pareja no ordenada. La salida solicitada describe
una ruta existente de s a t.

## Salida

Primero k y la probabilidad de fallo de la ruta, como fracción entre
0 y 1 con error absoluto de hasta 10⁻⁶. Después, los k identificadores
en el orden de la ruta. k debe ser mínimo; el riesgo real puede
superar el mínimo para esa longitud en hasta 10⁻⁶. Cualquier ruta
que cumpla ambas condiciones es válida.

## Evaluación

Un comprobador verifica que la ruta existe, tiene el menor número de
vértices y que tanto su probabilidad de fallo como la impresa están a
10⁻⁶ del óptimo. Se acepta cualquier ruta así.

## Ejemplos

```
4 4
1 3
1 2 50
2 3 50
1 4 10
4 3 10
```

```
3 0.19
1 4 3
```

## Solución

Sea q=1−p/100 la probabilidad de éxito de una arista. La supervivencia
de una ruta es el producto de sus q y el riesgo es uno menos ese
producto. Como q>0, el coste c=−log(q) es finito y aditivo.
Minimizar su suma equivale a maximizar la supervivencia.

Se ejecuta BFS FIFO desde s. Para cada vértice se guardan distancia,
coste mínimo entre rutas de esa distancia y predecesor. Una arista
u→v descubre v a distancia[u]+1, si es nueva. Solo se relaja el coste
cuando distance[v]=distance[u]+1. Las aristas de retorno o entre
vértices de la misma capa no deben introducir rutas más largas.
FIFO procesa toda la capa anterior antes de extraer un vértice.
Por inducción, al extraerlo todos sus predecesores mínimos ya han
ofrecido sus candidatos, y su coste es óptimo. Se puede terminar
al extraer t, pero no al descubrirlo por primera vez.

Se siguen predecesores desde t y se invierte el resultado. Para
coste total C, el riesgo es −expm1(−C). log1p y expm1 conservan
precisión cerca de cero; los logaritmos evitan que productos largos
subdesborden a cero. Doble precisión y doce decimales bastan para
la tolerancia 10⁻⁶. La tabla de costes tiene solo 100 elementos.

Tiempo O(n+m) y espacio O(n+m), incluidos grafo, estado BFS, ruta
y búferes de entrada/salida. No hacen falta cola de prioridad ni recursión.

s,t aparecen antes de las aristas. La longitud tiene prioridad:
una ruta larga sin riesgo no gana a una corta arriesgada. Sumar
porcentajes es incorrecto: multiplicar supervivencias o sumar sus
logaritmos negativos. No terminar al descubrir t. No comparar rutas
byte a byte. Son legales las aristas sin riesgo y riesgos que se
redondean a 1.

## Notas por lenguaje

Cada arista se codifica como 100·vecino+p, con índices desde cero;
el máximo 9 999 999 cabe en 32 bits. C++, Go y Rust usan vectores
de aristas codificadas. Java usa arreglos primitivos head/next/edge
y lectura rápida de enteros. Python libera el iterador de tokens
antes del BFS y usa arreglos tipados para distancias, padres y costes.
Todas las versiones reconstruyen sin recursión y almacenan la salida.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1934_shortest_paths.cpp](1934_shortest_paths.cpp) | G++ 13.2 x64 | shortest_paths | O(n+m) | AC | 0.093 s | 7288 KB |
| [1934_shortest_paths.go](1934_shortest_paths.go) | Go 1.14 x64 | shortest_paths | O(n+m) | AC | 0.187 s | 15636 KB |
| [1934_shortest_paths.java](1934_shortest_paths.java) | Java 1.8 | shortest_paths | O(n+m) | AC | 0.125 s | 9180 KB |
| [1934_shortest_paths.py](1934_shortest_paths.py) | Python 3.12 x64 | shortest_paths | O(n+m) | AC | 0.406 s | 33792 KB |
| [1934_shortest_paths.rs](1934_shortest_paths.rs) | Rust 1.75 x64 | shortest_paths | O(n+m) | AC | 0.046 s | 14136 KB |
