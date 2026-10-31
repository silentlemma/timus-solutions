# 1846. MCD 2010

[Timus 1846](https://acm.timus.ru/problem.aspx?space=1&num=1846) · dificultad 155 · segment_tree

Problema original de Alexey Samsonov, del Ural SU Contest en la sesión de verano de Petrozavodsk, agosto de 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un multiconjunto de enteros positivos empieza vacío. Cada operación
añade un número o quita una copia de un número que está. Tras cada
operación imprimir el máximo común divisor de todo el multiconjunto; el
mcd del multiconjunto vacío se declara igual a 1.

## Entrada

q (1 ≤ q ≤ 10⁵), luego q líneas "+ x" o "- x" con 1 ≤ x ≤ 10⁹. Solo se
quitan números presentes.

## Salida

El mcd tras cada operación, uno por línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
+ 8
+ 6
+ 8
- 8
- 8
```

Salida:

```
8
2
2
2
6
```

## Solución

Un mcd no se puede deshacer, así que quitar un número necesita una
estructura. Cada adición recibe su propia hoja en un árbol de segmentos
sobre las operaciones, y para cada valor se guarda una pila de las hojas
que lo contienen. Añadir x escribe x en la hoja de esa operación; quitar
x vacía la hoja de la cima de su pila escribiendo 0, lo que no cambia
ningún mcd porque mcd(a, 0) = a. Cada nodo interno guarda el mcd de sus
hijos, así que la raíz es el mcd del multiconjunto, y una raíz 0
significa que está vacío: se imprime 1. Actualizar una hoja recalcula
sus antepasados, y la subida puede parar en el primer nodo cuyo valor no
cambia, porque entonces nada por encima cambia. `O(q log q log x)`.

En el ejemplo las hojas guardan 8, 6 y 8, así que el mcd es 2. Quitar
los dos 8 vacía dos hojas y deja el 6.

Trampas:

- el multiconjunto vacío imprime 1, no 0;
- números iguales pueden añadirse varias veces y quitarse de uno en
  uno;
- con medio segundo importan tanto parar pronto la subida como leer
  rápido; la solución sencilla en Python corre en PyPy.

Las respuestas coinciden con una implementación aceptada independiente
en treinta archivos aleatorios de hasta 10⁵ operaciones.

## Soluciones optimizadas

La solución optimizada en C++ lee primero todas las operaciones, ordena
sus valores y quita los repetidos, y da a cada valor distinto una hoja
con un contador de sus copias en lugar de una hoja por cada adición y
una tabla hash de pilas de hojas. La hoja guarda x mientras el contador
es positivo y 0 si no, así que el árbol cambia solo cuando un valor
aparece o desaparece. Cada operación se guarda como un único `int` con
signo, +x o −x, que cabe porque x ≤ 10⁹; la hoja de un valor se halla
con búsqueda binaria. Los números se analizan a mano desde un búfer de
4 KB que se rellena con `fread`: {1846_segment_tree_optimized.cpp}.

La solución optimizada en Go lee primero todas las operaciones, ordena
sus valores y quita los repetidos, y da a cada valor distinto una hoja
con un contador de sus copias en lugar de una hoja por cada adición y un
`map` de slices de hojas. La hoja guarda x mientras el contador es
positivo y 0 si no, así que el árbol cambia solo cuando un valor aparece
o desaparece. Cada operación se guarda como un único `int32`, +x o −x,
que cabe porque x ≤ 10⁹, y el árbol y los contadores son slices de
`int32`; la hoja de un valor se halla con búsqueda binaria. Los números
se analizan a mano desde un lector `bufio` en lugar de partir la entrada
en palabras: {1846_segment_tree_optimized.go}.

La solución optimizada en Java lee primero todas las operaciones
analizándolas a mano desde un búfer de 64 KB en lugar de
`StreamTokenizer`. Numera los valores con búsqueda binaria en una copia
ordenada y guarda las hojas de cada valor como pilas enlazadas en dos
arreglos de `int`, la hoja de arriba de cada valor y la hoja de debajo
de cada hoja, en lugar de un `HashMap` de `ArrayDeque<Integer>`, así que
ningún número se envuelve en un objeto; cada adición sigue teniendo su
propia hoja: {1846_segment_tree_optimized.java}.

La solución optimizada en Python lee toda la entrada y la divide en líneas,
evitando una llamada al flujo con búfer por operación. Cada valor distinto
tiene una hoja y un contador de multiplicidad, así que las copias repetidas
no actualizan el árbol. El árbol y los contadores son listas de enteros en
lugar de `array("I")`, para evitar convertir sus celdas en cada acceso del
bucle de actualización. Cada valor se busca una sola vez en el diccionario;
las respuestas siguen escribiéndose en lotes de 1024. Se usa PyPy 3.10: la
versión anterior con lectura línea a línea excedió el tiempo en CPython:
{1846_segment_tree_optimized.py}.

La solución optimizada en Rust lee primero todas las operaciones y
libera el texto de la entrada, ordena los valores y quita los repetidos,
y da a cada valor distinto una hoja con un contador de sus copias en
lugar de una hoja por cada adición y un `HashMap` de pilas `Vec`. La
hoja guarda x mientras el contador es positivo y 0 si no, así que el
árbol cambia solo cuando un valor aparece o desaparece. Cada operación
se guarda como un único `i32`, +x o −x, que cabe porque x ≤ 10⁹, y el
árbol y los contadores son `u32`; las respuestas se escriben mediante un
`BufWriter` en lugar de juntarse en un `String`:
{1846_segment_tree_optimized.rs}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1846_segment_tree_optimized.cpp`: reducción de tiempo +61.58%;
  reducción de memoria +75.57%; base: `1846_segment_tree.cpp`.

- `1846_segment_tree_optimized.go`: reducción de tiempo -19.23%;
  reducción de memoria +75.57%; base: `1846_segment_tree.go`.

- `1846_segment_tree_optimized.java`: reducción de tiempo +46.58%;
  reducción de memoria +50.17%; base: `1846_segment_tree.java`.

- `1846_segment_tree_optimized.py`: reducción de tiempo -6.00%;
  reducción de memoria +39.87%; base: `1846_segment_tree.py`.

- `1846_segment_tree_optimized.rs`: reducción de tiempo -69.57%;
  reducción de memoria +74.46%; base: `1846_segment_tree.rs`.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1846_segment_tree.cpp](1846_segment_tree.cpp) | G++ 13.2 x64 | segment_tree | O(q log q log x) | AC | 0.203 s | 8612 KB | 11304079 |
| [1846_segment_tree.go](1846_segment_tree.go) | Go 1.14 x64 | segment_tree | O(q log q log x) | AC | 0.078 s | 14000 KB | 11290662 |
| [1846_segment_tree.java](1846_segment_tree.java) | Java 1.8 | segment_tree | O(q log q log x) | AC | 0.234 s | 20164 KB | 11305869 |
| [1846_segment_tree.py](1846_segment_tree.py) | PyPy 3.10 x64 | segment_tree | O(q log q log x) | AC | 0.250 s | 37060 KB | 11290667 |
| [1846_segment_tree.rs](1846_segment_tree.rs) | Rust 1.75 x64 | segment_tree | O(q log q log x) | AC | 0.046 s | 12328 KB | 11290670 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1846_segment_tree_optimized.cpp](1846_segment_tree_optimized.cpp) | G++ 13.2 x64 | segment_tree | O(q log q log x) | AC | 0.078 s | 2104 KB | 11305870 |
| [1846_segment_tree_optimized.go](1846_segment_tree_optimized.go) | Go 1.14 x64 | segment_tree | O(q log q log x) | AC | 0.093 s | 3420 KB | 11305877 |
| [1846_segment_tree_optimized.java](1846_segment_tree_optimized.java) | Java 1.8 | segment_tree | O(q log q log x) | AC | 0.125 s | 10048 KB | 11307314 |
| [1846_segment_tree_optimized.py](1846_segment_tree_optimized.py) | PyPy 3.10 x64 | segment_tree | O(q log q log x) | AC | 0.265 s | 22284 KB | 11307371 |
| [1846_segment_tree_optimized.rs](1846_segment_tree_optimized.rs) | Rust 1.75 x64 | segment_tree | O(q log q log x) | AC | 0.078 s | 3148 KB | 11305885 |
