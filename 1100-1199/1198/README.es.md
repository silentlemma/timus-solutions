# 1198. Qué senadores pueden aprobar una ley por su cuenta

[Timus 1198](https://acm.timus.ru/problem.aspx?space=1&num=1198) · dificultad 488 · graphs

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
invertidas. `O(N + M)` para `M` expedientes, hasta unos `4·10⁶`.

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

## Notas por lenguaje

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

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1198_graphs.cpp](1198_graphs.cpp) | G++ 13.2 x64 | graphs | O(N + M) | AC | 0.140 s | 32064 KB |
| [1198_graphs.go](1198_graphs.go) | Go 1.14 x64 | graphs | O(N + M) | AC | 0.296 s | 50472 KB |
| [1198_graphs.java](1198_graphs.java) | Java 1.8 | graphs | O(N + M) | AC | 0.250 s | 37092 KB |
| [1198_graphs.py](1198_graphs.py) | Python 3.12 x64 | graphs | O(N + M) | AC | 1.281 s | 36148 KB |
| [1198_graphs.rs](1198_graphs.rs) | Rust 1.75 x64 | graphs | O(N + M) | AC | 0.281 s | 64220 KB |
