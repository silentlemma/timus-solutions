# 1198. Qué senadores pueden aprobar una ley por su cuenta

[Timus 1198](https://acm.timus.ru/problem.aspx?space=1&num=1198) · dificultad 489 · graphs

Problema original de Nikita Rybak.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada uno de los `N ≤ 2000` senadores guarda expedientes comprometedores
sobre algunos de los demás. Quien quiere una ley llama a todas las
personas de las que tiene expediente y les pide que la apoyen y que hagan
a su vez las mismas llamadas. Una ley se aprueba cuando la apoyan todos
los senadores. Hay que hallar a todos los senadores que pueden conseguir
así que se apruebe una ley por su cuenta.

Límite de tiempo: 1.5 segundos. Límite de memoria: 96 MB.

## Entrada

`N` y luego una línea por senador con los senadores de los que guarda
expediente, terminada en `0`.

## Salida

Los números de esos senadores en orden creciente en una línea, seguidos
de `0`; solo `0` si no hay ninguno.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
3 2 0
0
4 5 0
1 5 0
2 0
```

Salida:

```
1 3 4 0
```

## Solución

Se traza una arista de cada senador a cada persona de la que guarda
expediente; la respuesta es el conjunto de vértices desde los que se
alcanzan todos los vértices.

Se lanza una búsqueda desde cada vértice aún sin marcar, y cada búsqueda
marca solo vértices sin marcar. Nada marcado antes puede alcanzar la raíz
de una búsqueda posterior, porque entonces ya estaría marcada, así que la
raíz de la última búsqueda está en una componente fuertemente conexa a la
que no llega ninguna otra componente. Si esa raíz no alcanza a todos,
nadie lo hace: quien alcanza a todos alcanza la raíz y, por tanto, está en
su componente. Si los alcanza, la respuesta son exactamente los vértices
que alcanzan la raíz, que se hallan con una búsqueda más por las aristas
invertidas. `O(N + M)` (`O(N² + M)` en Python) para `M` expedientes, hasta unos `4·10⁶`.

Detalles a tener en cuenta:

- la entrada puede rondar los 20 MB, así que una lectura lenta cuesta más
  que el trabajo con el grafo;
- las listas de adyacencia de `4·10⁶` entradas deben guardarse de forma
  compacta, como números de 32 bits en arreglos planos, para quedar con
  holgura dentro del límite de memoria;
- un senador puede aparecer en su propia lista o dos veces en la misma
  lista;
- si nadie cumple la condición, la salida es un solo `0`.

Las respuestas se compararon con una solución escrita aparte, basada en
el cierre transitivo con conjuntos de bits, en 300 grafos pequeños
aleatorios y en todas las pruebas.

La versión didáctica en C++ guarda una matriz booleana de adyacencia. El recorrido directo lee una fila y el inverso lee una columna de la misma matriz. Una arista repetida vuelve a marcar la misma entrada. Se comprueba la última raíz mediante un recorrido directo y luego se buscan en sentido inverso todos los vértices que la alcanzan. En cada pasada cada vértice entra en la cola como máximo una vez y se examinan N entradas. Tiempo O(N² + M), espacio O(N²).

## Soluciones optimizadas

C++, Go y Rust comprimen filas de ambos grafos en palabras64. Duplicados y bucles solo vuelven a poner el mismo bit. Se intersecta con no visitados y se borran bits antes de encolar: cada vértice entra una vez. Se toma la última raíz, se verifica que llega a todos y se recorre el grafo inverso. Si existe una fuente universal, la última raíz llega a todos; verificada esta, otro vértice es universal exactamente si llega a ella. Tres recorridos cuestan O(N⌈N/64⌉) palabras, más lectura O(M). Con N=2000 las matrices ocupan 1024000 bytes; IDs16 bastan. Se conservan bases CSR; Java/Python reutilizan las admitidas.

Las implementaciones base aceptadas [1198_graphs.java](1198_graphs.java), [1198_graphs.py](1198_graphs.py) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Notas por lenguaje

Estas notas describen las implementaciones sencillas.

- C++, Go, Java y Rust guardan ambos grafos como arreglos planos con
  desplazamientos y construyen el invertido contando.
- Python guarda la lista de cada senador como un entero grande con un
  byte por senador, rellenado mediante un `bytearray`, de modo que todo
  el trabajo por expediente ocurre dentro de funciones integradas; las
  búsquedas cuestan unas pocas operaciones sobre conjuntos enteros por
  senador, y el grafo invertido sale de un `zip` sobre las filas. Lee
  toda la entrada de una vez, lo que aquí es mucho más rápido que leer
  línea a línea.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1198_graphs.cpp](1198_graphs.cpp) | G++ 13.2 x64 | graphs | O(N + M) | AC | 0.140 s | 32064 KB | 11283511 |
| [1198_graphs.go](1198_graphs.go) | Go 1.14 x64 | graphs | O(N + M) | AC | 0.296 s | 50472 KB | 11283512 |
| [1198_graphs.java](1198_graphs.java) \* | Java 1.8 | graphs | O(N + M) | AC | 0.250 s | 37092 KB | 11283514 |
| [1198_graphs.py](1198_graphs.py) \* | Python 3.12 x64 | graphs | O(N² + M) | AC | 1.281 s | 36148 KB | 11283513 |
| [1198_graphs.rs](1198_graphs.rs) | Rust 1.75 x64 | graphs | O(N + M) | AC | 0.281 s | 64220 KB | 11283517 |
| [1198_bfs.cpp](1198_bfs.cpp) | G++ 13.2 x64 | bfs | O(N² + M) | AC | 0.609 s | 4228 KB | 11315851 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1198_graphs_bitmask.cpp](1198_graphs_bitmask.cpp) | G++ 13.2 x64 | graphs, bitmask | O(M + N⌈N/64⌉) | AC | 0.078 s | 1092 KB | 11315333 |
| [1198_graphs_bitmask.go](1198_graphs_bitmask.go) | Go 1.14 x64 | graphs, bitmask | O(M + N⌈N/64⌉) | AC | 0.062 s | 1320 KB | 11315339 |
| [1198_graphs_bitmask.rs](1198_graphs_bitmask.rs) | Rust 1.75 x64 | graphs, bitmask | O(M + N⌈N/64⌉) | AC | 0.062 s | 1092 KB | 11315334 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
