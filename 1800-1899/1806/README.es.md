# 1806. Telégrafos móviles

[Timus 1806](https://acm.timus.ru/problem.aspx?space=1&num=1806) · dificultad 178 · graphs

Problema original de Pavel Atnashev, de la subregión oriental del NEERC 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada uno de n telégrafos tiene un número distinto de diez cifras. Un
mensaje puede ir de a a b si b difiere de a en exactamente una cifra o
por un intercambio de dos cifras; tarda cost[l], donde l es la longitud
de su prefijo común. Hallar la ruta más rápida del primer telégrafo al
último, o indicar que no existe.

## Entrada

n (2 ≤ n ≤ 50000), luego los diez costes de 1 a 10000 en orden no
creciente, luego los n números; el primero es el de Anka y el último
el de Chapáev.

## Salida

"-1", o el menor tiempo, el número de telégrafos de la ruta y sus
índices del primero al último.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
100 10 10 10 1 1 1 1 1 1
9123493342
3123493942
9223433942
3223493942
9223433945
```

Salida:

```
211
5
1 2 4 3 5
```

### Ejemplo 2

Entrada:

```
2
1 1 1 1 1 1 1 1 1 1
0123493342
0223433945
```

Salida:

```
-1
```

## Solución

Se ejecuta el algoritmo de Dijkstra desde el primer telégrafo,
construyendo las aristas sobre la marcha. Un telégrafo tiene como mucho
90 números a una cifra cambiada y 45 a un intercambio, y un mapa hash
de números a telégrafos dice cuáles existen. Para un cambio en la cifra
p, o un intercambio de las cifras p < q, el prefijo común es
exactamente p, así que su coste es cost[p]. Con los números guardados
como enteros, un vecino es el número más un múltiplo de una potencia de
diez. La búsqueda se detiene cuando el último telégrafo sale de la
cola, y la ruta se reconstruye por los predecesores.
`O(135·n log n)`.

En el primer ejemplo la ruta intercambia la primera y la octava cifra
(100), cambia la segunda (10), intercambia la primera y la sexta (100)
y cambia la última (1): 211.

Trampas:

- los números de diez cifras no caben en 32 bits, y los ceros iniciales
  solo importan para las posiciones de las cifras;
- intercambiar dos cifras iguales no cambia nada y no es una arista;
- se acepta cualquier ruta más rápida.

El verificador suma los costes a lo largo de la ruta impresa, exige que
cada paso sea un cambio de una cifra o un intercambio, y compara el
total con el menor tiempo. Todas las soluciones lo superan en casos
pequeños aleatorios y con hasta 50000 telégrafos en disposiciones densas,
dispersas, en cadena e inalcanzables, frente a una implementación
aceptada independiente.

## Soluciones optimizadas

La solución optimizada en C++ sustituye `std::unordered_map` por una
tabla plana de direccionamiento abierto cuyo tamaño es una potencia de
dos, al menos `2n`, y cuyas casillas guardan el índice del telégrafo más
uno, y cero si están vacías; la casilla se elige por hash multiplicativo
del número, una colisión pasa a la casilla siguiente y, como la tabla
está como mucho medio llena, una búsqueda suele terminar tras pocos
sondeos. Las distancias son `int`: una ruta más rápida tiene como mucho
`n − 1 ≤ 49 999` pasos de como mucho 10000 cada uno, menos de
`5 · 10^8 < 2^31`. La cola es un montículo binario indexado con
disminución de clave, así que cada telégrafo ocupa como mucho una
casilla del montículo en lugar de entradas repetidas, y el arreglo del
montículo se reutiliza para imprimir la ruta. Los números se analizan a
mano desde bloques de 4 KB en lugar de leerlos como cadenas con `scanf`
y convertirlos: {1806_graphs_optimized.cpp}.

La solución optimizada en Go sustituye el mapa por una tabla plana de
direccionamiento abierto de índices `int32` cuyo tamaño es una potencia
de dos, al menos `2n`, donde cero marca una casilla vacía; la casilla se
elige por hash multiplicativo del número, una colisión pasa a la casilla
siguiente y la tabla medio vacía suele mantener cortos los sondeos. Las
distancias son `int32`: una ruta más rápida tiene como mucho
`n − 1 ≤ 49 999` pasos de como mucho 10000 cada uno, menos de
`5 · 10^8 < 2^31`. La cola es un montículo binario indexado de `int32`
con disminución de clave en lugar de `container/heap` con sus llamadas
por interfaz y entradas repetidas. Los números se analizan a mano desde
el lector con búfer en lugar de con `fmt.Fscan`, y la ruta se escribe
directamente en la salida: {1806_graphs_optimized.go}.

La solución optimizada en Java sustituye el `HashMap` de claves `Long`
empaquetadas por una tabla plana de direccionamiento abierto de índices
`int` cuyo tamaño es una potencia de dos, al menos `2n`, donde cero
marca una casilla vacía; la casilla se elige por hash multiplicativo del
número, una colisión pasa a la casilla siguiente y la tabla medio vacía
suele mantener cortos los sondeos. Las distancias son `int`: una ruta
más rápida tiene como mucho `n − 1 ≤ 49 999` pasos de como mucho
10000 cada uno, menos de `5 · 10^8 < 2^31`. La cola es un montículo
binario indexado con disminución de clave en lugar de una
`PriorityQueue` de pares `long[]` con un comparador lambda, así que no
se crea ningún objeto por entrada de la cola. Los números se analizan a
mano desde bloques de bytes de 4 KB: {1806_graphs_optimized.java}.

La solución optimizada en Python anota, para cada posición, qué dígitos
aparecen en ella en algún número de telégrafo, y se salta los cambios e
intercambios que pondrían allí otro dígito, porque ningún telégrafo
puede tener ese número vecino. Un telégrafo sale del diccionario de
números en cuanto se extrae de la cola, porque con costes positivos ya
no puede mejorar, así que las búsquedas posteriores encuentran menos
números, y la lista de tokens de la entrada se libera antes de la
búsqueda. Se ejecuta con PyPy, cuyos bucles enteros compilados son aquí
más rápidos: {1806_graphs_optimized.py}.

La solución optimizada en Rust sustituye el `HashMap` por una tabla
plana de direccionamiento abierto de índices `u32` cuyo tamaño es una
potencia de dos, al menos `2n`, donde cero marca una casilla vacía; la
casilla se elige por hash multiplicativo del número, una colisión pasa a
la casilla siguiente y la tabla medio vacía suele mantener cortos los
sondeos. Las distancias son `i32` y los vértices del montículo `u32`, la
mitad de `i64` y `usize`: una ruta más rápida tiene como mucho
`n − 1 ≤ 49 999` pasos de como mucho 10000 cada uno, menos de
`5 · 10^8 < 2^31`. Los dígitos de un número van a un arreglo fijo en
lugar de a un vector nuevo por cada telégrafo, y la ruta se escribe
directamente en la salida en lugar de reunirse en cadenas:
{1806_graphs_optimized.rs}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1806_graphs_optimized.cpp`: reducción de tiempo +65.06%; reducción de
  memoria +70.82%; base: `1806_graphs.cpp`.

- `1806_graphs_optimized.go`: reducción de tiempo +38.11%; reducción de
  memoria +65.91%; base: `1806_graphs.go`.

- `1806_graphs_optimized.java`: reducción de tiempo +46.02%; reducción
  de memoria +69.51%; base: `1806_graphs.java`.

- `1806_graphs_optimized.py`: reducción de tiempo +58.00%; reducción de
  memoria +16.30%; base: `1806_graphs.py`.

- `1806_graphs_optimized.rs`: reducción de tiempo +35.78%; reducción de
  memoria +50.36%; base: `1806_graphs.rs`.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1806_graphs.cpp](1806_graphs.cpp) | G++ 13.2 x64 | graphs | O(135 n log n) | AC | 0.312 s | 4756 KB | 11304248 |
| [1806_graphs.go](1806_graphs.go) | Go 1.14 x64 | graphs | O(135 n log n) | AC | 0.328 s | 8788 KB | 11290019 |
| [1806_graphs.java](1806_graphs.java) | Java 1.8 | graphs | O(135 n log n) | AC | 0.578 s | 12740 KB | 11304250 |
| [1806_graphs.py](1806_graphs.py) | Python 3.12 x64 | graphs | O(135 n log n) | AC | 2.343 s | 16464 KB | 11304252 |
| [1806_graphs.rs](1806_graphs.rs) | Rust 1.75 x64 | graphs | O(135 n log n) | AC | 0.218 s | 6680 KB | 11304254 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1806_graphs_optimized.cpp](1806_graphs_optimized.cpp) | G++ 13.2 x64 | graphs | O(135 n log n) | AC | 0.109 s | 1388 KB | 11307284 |
| [1806_graphs_optimized.go](1806_graphs_optimized.go) | Go 1.14 x64 | graphs | O(135 n log n) | AC | 0.203 s | 2996 KB | 11307288 |
| [1806_graphs_optimized.java](1806_graphs_optimized.java) | Java 1.8 | graphs | O(135 n log n) | AC | 0.312 s | 3884 KB | 11307286 |
| [1806_graphs_optimized.py](1806_graphs_optimized.py) | PyPy 3.10 x64 | graphs | O(135 n log n) | AC | 0.984 s | 13780 KB | 11307367 |
| [1806_graphs_optimized.rs](1806_graphs_optimized.rs) | Rust 1.75 x64 | graphs | O(135 n log n) | AC | 0.140 s | 3316 KB | 11307327 |
