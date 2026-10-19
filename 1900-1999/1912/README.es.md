# 1912. Escapar juntos manteniendo la vecindad

[Timus 1912](https://acm.timus.ru/problem.aspx?space=1&num=1912) · difficulty 1266 · bfs

Problema original de Stanislav Vasilyev, preparado por Denis Mukhametianov, NEERC 2012, Eastern subregional contest.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dos participantes ocupan habitaciones diferentes de una cuadrícula rectangular.
Sus habitaciones comparten lado o esquina y deben mantener esa vecindad.
En cada paso uno atraviesa una pared delgada ortogonal, pagando un cruce.
No se atraviesan paredes gruesas ni se comparte habitación. Fuera del
rectángulo no hay paredes y caminar es gratis. Encuentra el mínimo total
de cruces para que ambos salgan o determina que es imposible.
Límites: 1 segundo y 64 MB.

## Entrada

Primero n,m, con 2≤n,m≤250; después exactamente 2n+1 líneas de 2m+1 caracteres.
Con índices desde cero, los centros están en filas y columnas impares.
`1`,`2` marcan las habitaciones iniciales; un espacio, una habitación vacía;
`+`, una esquina; `.`, una pared delgada; `-`,`|`, paredes gruesas.
Los inicios son distintos y comparten al menos una esquina. Conserva los
espacios. Se permite vecindad diagonal, pero entre habitaciones solo se
cruza una pared ortogonal compartida.

## Salida

El mínimo de cruces o `Death` si ambos no pueden escapar.

## Evaluación

Un entero exacto o el token exacto `Death`, comparado por tokens.

## Ejemplos

```
3 4
+.+-+-+-+
| . .1. |
+-+-+-+.+
| .2. . |
+.+.+.+-+
| . | | |
+.+.+-+-+
```

```
13
```

```
2 2
+-+-+
.1|2.
+-+-+
| | |
+-+-+
```

```
Death
```

## Solución

Busca posiciones conjuntas, no dos caminos independientes. Incluso si cada
uno podría salir solo, el movimiento de uno puede romper la vecindad,
como muestra el segundo ejemplo.

Añade un anillo exterior de una celda. Atravesar una pared delgada,
incluida la frontera, cuesta uno; caminar entre celdas exteriores cuesta
cero. Mientras uno siga dentro, las posiciones relevantes del otro están
a una celda de esa habitación fronteriza, así que el anillo basta.
Esos vecinos exteriores forman una banda o L conectada ortogonalmente:
los pasos diagonales gratuitos pueden sustituirse por pasos ortogonales.
También puede evitarse compartir una posición exterior recolocando gratis
al compañero antes de la última salida. El modelo finito de posiciones
distintas conserva el óptimo. No reduzcas todo el exterior a un único
vértice: permitiría escapar incorrectamente en el segundo ejemplo.

Como ambos tienen las mismas capacidades y objetivo, ordena sus índices
lineales a<b y olvida sus nombres. El desplazamiento relativo es uno de
(0,1),(1,−1),(1,0),(1,1). Con ancho ampliado W, codifica
`4·a+orientation`; la segunda celda es a más 1,W−1,W,W+1. Intercambiar
identidades es una simetría y no cambia los caminos ni sus costes.

Para cada orientación, precalcula los ocho candidatos: dos participantes
y cuatro direcciones. Descarta coincidencia o pérdida de vecindad,
ordena el nuevo par y guarda actor, bit de pared, cambio del estado
codificado y desplazamiento del actor. Quedan cuatro movimientos relativos.
Durante la búsqueda una máscara de paredes verifica legalidad y límites.

Ejecuta 0-1 BFS: los cruces cuestan uno y caminar fuera cero. Añade aristas
cero al frente de la deque y aristas uno al final. Finaliza un estado al
extraerlo y devuelve la distancia del primero extraído con ambos fuera.
No basta que salga uno, ni se debe terminar al descubrir una meta, pues
las aristas cero afectan a la prioridad.

Todo movimiento permitido aparece y toda arista representa un movimiento
válido con coste correcto. El anillo y la simetría conservan el óptimo,
y 0-1 BFS lo obtiene. Agotar la cola significa que no hay escape.

Hay como máximo 4(n+2)(m+2)≤254 016 estados y cuatro candidatos por estado.
Tiempo y espacio O(nm). Una ruta mínima no necesita ciclos de estados y
cada arista cuesta como máximo uno, así que bastan distancias de 32 bits.

## Notas por lenguaje

Todos usan arreglos compactos y transiciones precalculadas, sin ordenar ni
consultar hashes durante la búsqueda. Python 3.12 usa `array` y arreglos
de bytes; Go 1.14 y Java 8, deques circulares enteras que crecen sin nodos
empaquetados; C++ y Rust 1.75, deques estándar. Lee el dibujo por líneas
completas, eliminando solo terminadores. No hay recursión dependiente
del tamaño del laberinto.

Las respuestas coinciden con un Dijkstra simple sobre pares de
participantes etiquetados en las 24 576 configuraciones de una sala
2 × 2 y en 200 laberintos pequeños aleatorios; los campos de 250 × 250
se comprueban con fórmulas exactas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1912_bfs.cpp](1912_bfs.cpp) | G++ 13.2 x64 | bfs | O(nm) | AC | 0.015 s | 1632 KB |
| [1912_bfs.go](1912_bfs.go) | Go 1.14 x64 | bfs | O(nm) | AC | 0.031 s | 3116 KB |
| [1912_bfs.java](1912_bfs.java) | Java 1.8 | bfs | O(nm) | AC | 0.140 s | 4296 KB |
| [1912_bfs.py](1912_bfs.py) | Python 3.12 x64 | bfs | O(nm) | AC | 0.765 s | 2532 KB |
| [1912_bfs.rs](1912_bfs.rs) | Rust 1.75 x64 | bfs | O(nm) | AC | 0.031 s | 1992 KB |
