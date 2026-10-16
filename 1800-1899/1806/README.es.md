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
números del primero al último.

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

En el primer ejemplo la ruta intercambia la primera y la séptima cifra
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
pequeños aleatorios y con 50000 telégrafos en disposiciones densas,
dispersas, en cadena e inalcanzables, frente a una implementación
aceptada independiente.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1806_graphs.cpp](1806_graphs.cpp) | G++ 13.2 x64 | graphs | O(135 n log n) | AC | 0.312 s | 4760 KB |
| [1806_graphs.go](1806_graphs.go) | Go 1.14 x64 | graphs | O(135 n log n) | AC | 0.328 s | 8788 KB |
| [1806_graphs.java](1806_graphs.java) | Java 1.8 | graphs | O(135 n log n) | AC | 0.531 s | 12700 KB |
| [1806_graphs.py](1806_graphs.py) | Python 3.12 x64 | graphs | O(135 n log n) | AC | 2.343 s | 16128 KB |
| [1806_graphs.rs](1806_graphs.rs) | Rust 1.75 x64 | graphs | O(135 n log n) | AC | 0.218 s | 6672 KB |
