# 1841. Teleféricos

[Timus 1841](https://acm.timus.ru/problem.aspx?space=1&num=1841) · dificultad 2141 · segment_tree

Problema original de Denis Dublennykh, del Ural SU Contest en la sesión de verano de Petrozavodsk, agosto de 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un sendero sube una montaña como una poligonal de n tramos cuyos
vértices van estrictamente cuesta arriba; el eje y apunta cuesta
arriba. Recorrer el tramo i cuesta vᵢ por unidad de cambio en x.
Algunos puntos del sendero son extremos inferiores de teleféricos: un
teleférico sube recto por la ladera desde su inicio y termina en el
siguiente punto donde corta el sendero, y el viaje dura un tiempo dado.
Nadie baja a pie. Hallar el menor tiempo del pie a la cima.

## Entrada

n (1 ≤ n ≤ 10⁵), luego las n + 1 coordenadas x de los vértices del pie
a la cima; las vecinas son distintas. Luego n líneas: vᵢ, el número mᵢ
de teleféricos que salen del tramo i y mᵢ pares (x del inicio, tiempo
del viaje), en orden cuesta arriba. Dos teleféricos nunca salen del
mismo punto, uno que sale de un vértice compartido aparece una sola
vez, y todos terminan en el sendero. Las coordenadas valen como mucho
10⁶ en valor absoluto, los tiempos son positivos y como mucho 10⁶, y
hay como mucho 10⁵ teleféricos.

## Salida

El menor tiempo para llegar a la cima.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
0 5 15 10 0
1 1 1 100
1 1 7 1
1 0
1 0
```

Salida:

```
15
```

### Ejemplo 2

Entrada:

```
3
0 10 0 10
10 0
10 1 10 1
10 0
```

Salida:

```
101
```

## Solución

Solo importa el orden de los puntos a lo largo del sendero, y llegar a
pie a un punto cuesta una cantidad conocida: lo que cuesta llegar al
primer vértice de su tramo más vᵢ por la distancia en x. Llamémoslo el
coste a pie del punto; crece estrictamente a lo largo del sendero.

Dónde llega un teleférico. Cada punto del sendero salvo el pie
pertenece a un único tramo si cada tramo es dueño de su rango de x sin
su primer vértice (un inicio en un vértice compartido pertenece, pues,
al tramo de abajo). Un teleférico que sale de x en el tramo s llega al
primer tramo posterior a s cuyo rango contiene x. Se recorren los
tramos de arriba abajo sobre las coordenadas de inicio (comprimidas
salvo en Python): antes de pintar el tramo s sobre su rango de x en un árbol de
segmentos, se consultan todos los teleféricos de s. Un nodo guarda solo
la última pintura puesta sobre él, y las pinturas bajan por el sendero,
así que el menor número de tramo en el camino de una hoja a la raíz es
el tramo de llegada.

Los mejores tiempos. Sea best(p) el menor tiempo para llegar a p, y
gain = min(best(p) − coste a pie(p)) sobre los puntos alcanzados hasta
ahora; en el pie gain es 0, y caminar conserva esa diferencia, así que
best(p) = coste a pie(p) + gain en el punto actual. Se
procesan los inicios y las llegadas por coste a pie, las llegadas
primero si empatan. Un inicio guarda best = coste + gain; una llegada
asigna a gain min(gain, best(inicio) + tiempo − coste(llegada)). La
respuesta es el coste a pie de la cima más gain. `O((n + m) log(n + m))`; Python: `O(U + (n + m) log U + m log(m + 1))`,
donde U = max(x) − min(x) + 1.

En el primer ejemplo el teleférico de x = 1 sube del primer tramo al
último, con coste a pie 29, y tarda 100, peor que caminar. El de x = 7
sale con coste a pie 7 y también llega al último tramo, con coste 23,
tras 1 unidad de tiempo, así que gain pasa a ser 7 + 1 − 23 = −15, y la
respuesta es 30 − 15 = 15.

Trampas:

- un teleférico que sale de un vértice compartido pertenece al tramo de
  abajo, sea cual sea la línea que lo menciona;
- un teleférico puede llegar muchos tramos después, o justo al inicio
  de otro teleférico, lo que resuelve el orden de llegadas primero;
- los tiempos llegan a unos 2·10¹⁷, más allá de 32 bits pero dentro de 64;
- la solución en Python corre en PyPy y guarda sus datos en arreglos
  planos de enteros de máquina, unos 20 MB; una versión anterior con
  listas de enteros de Python ocupaba 69 MB en la prueba 17 del juez.

Las respuestas coinciden con una implementación aceptada independiente
y con una búsqueda de camino más corto en cuatrocientas montañas
aleatorias, y en las pruebas grandes.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1841_segment_tree.cpp](1841_segment_tree.cpp) | G++ 13.2 x64 | segment_tree | O((n + m) log(n + m)) | AC | 0.453 s | 22568 KB |
| [1841_segment_tree.go](1841_segment_tree.go) | Go 1.14 x64 | segment_tree | O((n + m) log(n + m)) | AC | 0.250 s | 27812 KB |
| [1841_segment_tree.java](1841_segment_tree.java) | Java 1.8 | segment_tree | O((n + m) log(n + m)) | AC | 0.421 s | 40208 KB |
| [1841_segment_tree.py](1841_segment_tree.py) | PyPy 3.10 x64 | segment_tree | O(U + (n + m) log U + m log(m + 1)) | AC | 0.468 s | 32236 KB |
| [1841_segment_tree.rs](1841_segment_tree.rs) | Rust 1.75 x64 | segment_tree | O((n + m) log(n + m)) | AC | 0.125 s | 25724 KB |
