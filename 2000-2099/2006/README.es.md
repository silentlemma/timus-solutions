# 2006. Bloquear la casilla más crítica

[Timus 2006](https://acm.timus.ru/problem.aspx?space=1&num=2006) · dificultad 3673 · graphs, shortest_paths

Problema original de Ilya Kuchumov. (Prepared by Oleg Merkurev), del Concurso Regional Escolar de Programación de los Urales 2013.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una cuadrícula rectangular tiene casillas libres `.` y bloqueadas `#`.
Moverse entre casillas libres que comparten lado cuesta un paso. Inicio
y destino son distintos, libres y están conectados inicialmente.
Bloquear exactamente otra casilla libre para maximizar la nueva
distancia mínima. Desconectarlos es mejor que cualquier distancia
finita. Se admite cualquier casilla óptima. Existe al menos una
candidata legal, que incluso puede estar en otro componente.

## Entrada

Enteros `n m`, `2 ≤ n,m ≤ 1000`, `n·m ≤ 100000`. Las dos líneas
siguientes dan inicio y destino como `fila columna`, numerados desde 1
arriba a la izquierda. Siguen `n` filas de `m` caracteres `.` o `#`. Los
extremos son distintos, libres y conectados; hay al menos tres casillas
libres. Tiempo 2 segundos, memoria 128 MB.

## Salida

Fila y columna de una casilla libre distinta de los extremos cuya
eliminación maximice la distancia mínima, dando prioridad absoluta a la
desconexión. Los empates son libres.

## Evaluación

Un comprobador bloquea la celda impresa, ejecuta una BFS y compara la
nueva distancia, o la desconexión, con el óptimo; se acepta cualquier
celda óptima.

## Ejemplos

```
4 4
1 1
4 4
..##
#.##
#...
###.
```

```
2 2
```

Eliminar `(2,2)` rompe el único pasaje entre los extremos y por tanto es óptimo.

## Solución

Sea `P[0..k]` un camino mínimo. Eliminar fuera de `P` conserva ese
camino y no aumenta la distancia; basta estudiar sus vértices internos.
Si `k=1`, los extremos son adyacentes y sirve cualquier otra casilla
libre.

BFS desde el inicio obtiene distancias `ds` y un árbol que contiene `P`;
BFS desde el destino obtiene `dt`. El nivel `λ(v)` es el índice del
último vértice de `P` en el camino del árbol hasta `v`. Se asigna en
orden BFS. Al eliminar `P[i]`, dividir el componente original restante
en `R` con nivel menor que `i`, `V` con nivel `i` salvo `P[i]`, y `S`
con nivel mayor que `i`.

Un prefijo mínimo hasta `R` permanece en `R`. Para `y` en `S`, sea
`j=λ(y)>i`: seguir su rama hasta `P[j]` y luego llegar al destino cuesta
`ds[y]+k−2j`. Cualquier ruta por `P[i]` cuesta al menos `ds[y]+k−2i`,
estrictamente más. Por ello un sufijo mínimo de longitud `dt[y]` evita
el vértice eliminado.

Hay dos maneras de cruzar de `R∪V` a `S`. Una arista `x–y` con
`λ(x)<i<λ(y)` ofrece `ds[x]+1+dt[y]` para todos los índices
estrictamente entre sus niveles: una oferta de intervalo.

En el otro caso `x` pertenece a `V`, y su prefijo mínimo ordinario
podría usar el vértice eliminado. Calcular un prefijo corregido
`detour`: para cada vértice `v` fuera de `P`, sembrar el mínimo de
`ds[u]+1` entre vecinos de nivel inferior. Dijkstra multifuente propaga
solo entre vértices fuera de `P` del mismo nivel. Las regiones de
niveles son disjuntas. Una arista de tal `x` a `y` de nivel mayor ofrece
`detour[x]+1+dt[y]` únicamente para el fallo `λ(x)`.

El prefijo corregido es exacto: en cualquier camino restringido a `R∪V`,
tomar su última entrada de `R` a `V`. El prefijo no es menor que la
semilla correspondiente y el resto permanece en `V`. Recíprocamente,
todo camino de Dijkstra sembrado tiene un prefijo válido en `R` y evita
el vértice borrado. Toda ruta de reemplazo cruza hacia `S`, y ambos
casos agotan ese cruce. Su mínimo es la distancia correcta; si no hay
oferta, existe desconexión.

Ordenar intervalos por extremo izquierdo y barrer los índices del camino
con un montículo de `(coste,extremo derecho)`. Insertar los intervalos
iniciados y descartar mínimos caducados. Combinar el menor intervalo
activo con las ofertas puntuales. Elegir la casilla de mayor distancia
resultante.

Se emplea la reducción para evitar un vértice de [Lee y Lu, sección
2.2](https://arxiv.org/html/1310.8062#S2.SS2), con Dijkstra y montículos
ordinarios, sin el procedimiento lineal de mínimos de matriz. Con
`N=n·m` hay como máximo `2N` aristas no dirigidas: tiempo `O(N log N)`,
memoria `O(N)`. Un arreglo plano con borde simplifica vecinos; los
componentes inalcanzables no participan.

La fórmula para eliminar una arista no basta para eliminar un vértice:
los desvíos del mismo nivel son esenciales. Los intervalos excluyen
ambos niveles extremos; la oferta puntual inferior excluye el propio
vértice del camino. No bloquear los extremos. Desconectar supera toda
longitud finita. Con extremos adyacentes la tercera casilla puede estar
inicialmente aislada. Contar movimientos, no vértices, y mantener fila
antes que columna.

## Notas por lenguaje

Todos los programas usan BFS iterativo, cuadrícula plana con borde,
registros de aristas entre niveles y montículos, sin recursión profunda
en corredores. Distancias e infinito nombrado caben en enteros con signo
de 32 bits. Rust comprueba marcadores sin signo de nivel ausente antes
de comparar. Python solo imprime coordenadas. Se miden recursos de cada
programa completo antes de publicar su disponibilidad.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2006_graphs_shortest_paths.cpp](2006_graphs_shortest_paths.cpp) | G++ 13.2 x64 | graphs, shortest_paths | O(N log N) | AC | 0.031 s | 5332 KB |
| [2006_graphs_shortest_paths.go](2006_graphs_shortest_paths.go) | Go 1.14 x64 | graphs, shortest_paths | O(N log N) | AC | 0.062 s | 19532 KB |
| [2006_graphs_shortest_paths.java](2006_graphs_shortest_paths.java) | Java 1.8 | graphs, shortest_paths | O(N log N) | AC | 0.218 s | 11892 KB |
| [2006_graphs_shortest_paths.py](2006_graphs_shortest_paths.py) | Python 3.12 x64 | graphs, shortest_paths | O(N log N) | AC | 0.578 s | 33312 KB |
| [2006_graphs_shortest_paths.rs](2006_graphs_shortest_paths.rs) | Rust 1.75 x64 | graphs, shortest_paths | O(N log N) | AC | 0.031 s | 9068 KB |
