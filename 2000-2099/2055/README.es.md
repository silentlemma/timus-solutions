# 2055. Conservar conexiones con el menor intervalo de precios

[Timus 2055](https://acm.timus.ru/problem.aspx?space=1&num=2055) · difficulty 1468 · trees, dsu, two_pointers

Problema original de Nikita Burlakov, del Campeonato de Programación Deportiva de los Urales 2015.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un multigrafo conexo tiene n vértices y m carreteras con precios.
Conservar un árbol generador, para quitar tantas carreteras como sea
posible, y entre los árboles generadores minimizar la diferencia entre
el precio mayor y el menor conservados. Los límites son 1,5 segundos y
128 MB.

## Entrada

La primera línea tiene n y m, 2 ≤ n ≤ 50 000, n − 1 ≤ m ≤ 50 000. Cada
una de las m líneas siguientes describe una carretera `a b c`: dos
extremos distintos y un precio 1 ≤ c ≤ 10⁹. Las carreteras paralelas son
distintas.

## Salida

Los números de las carreteras conservadas, en una línea y en cualquier
orden.

## Evaluación

Un comprobador verifica que las carreteras forman un árbol generador y
que su rango de precios es óptimo; se acepta cualquier árbol óptimo.

## Ejemplos

```
3 3
1 2 1
2 3 3
3 1 4
```

```
2 3
```

```
4 5
1 2 1
2 3 1
1 3 2
1 4 2
2 4 1
```

```
1 2 5
```

En el primero, los tres árboles tienen diferencias `3−1=2`, `4−1=3` y
`4−3=1`; las carreteras 2 y 3 logran el mínimo uno. En el segundo, 1, 2
y 5 conectan los cuatro vértices y cuestan uno, por lo que alcanzan la
cota absoluta cero.

## Solución

### Bosque generador máximo de cada prefijo

La conexión requiere al menos `n−1` aristas y un árbol alcanza esa cota;
el primer objetivo exige un árbol. Ordenamos por precio, extremos e
identificador original, asignando rangos distintos `0,…,m−1`. Mantenemos
el bosque generador de máxima suma de rangos del prefijo procesado.

Un DSU ordinario registra la conexión de todo el grafo procesado. Si una
arista nueva une componentes distintas, se incluye y se fusionan. Si no,
cierra un ciclo en el bosque: se elimina la arista de menor rango del
camino anterior entre sus extremos y se añade la nueva, cuyo rango
supera todos los anteriores. Un arreglo booleano marca rangos
conservados y un puntero avanza hasta el primero activo. Los eliminados
nunca reaparecen; el avance total cuesta `O(m)`.

Con `n−1` aristas el bosque es árbol. La carretera más reciente siempre
está incluida y tiene el precio máximo. Guardamos la mejor diferencia y
su intervalo de rangos; cero permite terminar. Al final un DSU nuevo
recorre ese intervalo y conserva `n−1` uniones. Así no copiamos un árbol
entero tras cada mejora.

### Bosque dinámico y reutilización del nodo de arista

Un link-cut tree representa cada vértice y cada carretera conservada
mediante nodos. Los vértices tienen clave centinela `m+1`; una arista
tiene su rango actual. Cada splay auxiliar guarda el nodo de clave
mínima. El splay iterativo propaga inversiones pendientes antes de
rotar. `makeroot(u); access(v)` expone en orden todo el camino `u–v`; su
agregado encuentra la arista mínima.

Un nodo de arista tiene grado físico dos. Tras exponer el camino,
hacemos splay del mínimo `e`. El subárbol izquierdo es `u…a` y el
derecho `b…v`; la carretera anterior unía `a,b`. Invertimos **ambos**
subárboles y actualizamos la clave de `e` al nuevo rango. El orden pasa
a ser `a…u,e,v…b`: se elimina la conexión anterior y el nodo reciclado
une exactamente los extremos nuevos `u,v`. Las demás carreteras y ramas
virtuales se conservan. Invertir no altera el agregado mínimo;
recalculamos `e` al cambiar la clave. La operación cambia la topología,
no solo el precio anterior.

Solo se asigna un nodo nuevo cuando el DSU fusiona componentes: como
máximo `n−1`, por lo que bastan como máximo `2n` posiciones incluyendo
el cero sin usar. Tras reciclar, el índice del nodo deja de ser el rango
de la carretera; se consulta su clave. Las operaciones de camino cuestan
`O(log n)` amortizado.

### Por qué el rango obtenido es óptimo

La actualización mantiene un bosque máximo. Al unir componentes
anteriores, la nueva arista es su única conexión recién disponible.
Dentro de una componente, sean `T` el árbol máximo anterior, `e` la
nueva arista y `f` el mínimo del ciclo. Un competidor sin `e` no mejora
`T+e−f`. Si contiene `e`, al eliminarla aparece un corte cruzado por
alguna arista `g` del camino anterior. Sustituir `e` por `g` produce un
árbol del prefijo anterior, con suma de rangos a lo sumo `T`. Como
`rank(g)≥rank(f)`, el competidor no supera `T+e−f`. El bosque sigue
siendo máximo.

Ese árbol también maximiza el precio mínimo del prefijo. En caso
contrario, eliminemos una arista demasiado barata del árbol: un
competidor con todos sus precios mayores cruza ese corte mediante una
arista de precio y rango mayores. El intercambio aumentaría la suma de
rangos, contradicción. Los empates no perjudican, pues un aumento
estricto de precio implica aumento estricto de rango.

Tomemos un árbol globalmente óptimo y el prefijo que termina en su
arista de mayor rango. El árbol mantenido no tiene máximo mayor ni
mínimo menor, por lo que su diferencia no supera la óptima. Todos los
árboles registrados son factibles; la mejor diferencia es exactamente la
óptima. El intervalo guardado es conexo y cualquier árbol reconstruido
dentro de él tiene diferencia a lo sumo óptima; tampoco puede ser menor.
La reconstrucción es correcta.

## Notas por lenguaje

Ordenar cuesta `O(m log m)`, actualizar `O(m log n)` amortizado y
reconstruir `O(m)`: total `O(m log m+m log n)` tiempo y `O(n+m)`
espacio. DSU y bosque ocupan `O(n)`; carreteras y actividad, `O(m)`. Las
sumas de rangos solo aparecen en la prueba, no se calculan. Precios y
diferencias caben en enteros de 32 bits con signo.

C++, Go, Java y Rust usan splay/DSU iterativos, entrada con buffer y la
misma reutilización con métodos auxiliares. No se necesita recursión del
grafo ni recorrer linealmente un camino.

No confundir la conexión del prefijo en el DSU con las eliminaciones del
árbol. Los empates siguen siendo rangos separados; conservar IDs
originales y comparar claves en vez de índices reciclados. Propagar
inversiones antes del splay, invertir ambos lados al reutilizar y
actualizar agregados al cambiar la clave. Solo evaluar árboles
completos. El mínimo precio total y el mínimo intervalo son objetivos
distintos: Kruskal ordinario resuelve únicamente el primero.

Python no usa un árbol link-cut. Mueve dos punteros sobre las carreteras
ordenadas por precio: el derecho añade carreteras a un DSU con deshacer,
y mientras la ventana conecta el grafo el izquierdo quita su carretera
más barata. Un DSU no puede quitar directamente su carretera más
antigua, así que la ventana se guarda como una cola de dos pilas: cuando
la pila delantera está vacía, las carreteras de la ventana se deshacen y
se vuelven a añadir en un orden que deja las más antiguas arriba, y cada
carretera se mueve O(log m) veces en total. La ventana conexa más barata
da la respuesta, y Kruskal sobre sus carreteras construye el árbol. `O(m
log m log n)` con unión por tamaño y sin compresión de caminos. Corre en
CPython, 1,34 s de los 1,5 s en el juez; la versión anterior con el
bosque splay superaba el límite de tiempo en la prueba 11 del juez
incluso con PyPy.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2055_dsu_two_pointers.py](2055_dsu_two_pointers.py) | Python 3.12 x64 | dsu, two_pointers | O(m log m log n) | AC | 1.343 s | 12480 KB |
| [2055_trees.cpp](2055_trees.cpp) | G++ 13.2 x64 | trees | O(m log m+m log n) | AC | 0.125 s | 3596 KB |
| [2055_trees.go](2055_trees.go) | Go 1.14 x64 | trees | O(m log m+m log n) | AC | 0.250 s | 9376 KB |
| [2055_trees.java](2055_trees.java) | Java 1.8 | trees | O(m log m+m log n) | AC | 0.312 s | 8148 KB |
| [2055_trees.rs](2055_trees.rs) | Rust 1.75 x64 | trees | O(m log m+m log n) | AC | 0.125 s | 9020 KB |
