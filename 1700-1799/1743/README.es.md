# 1743. Ordenar dominós

[Timus 1743](https://acm.timus.ru/problem.aspx?space=1&num=1743) · dificultad 991 · greedy

Problema original de Artyom Ripatti y Petr Lezhankin, del concurso de la USATU de Ufá en el campus de entrenamiento de verano de Petrozavodsk, agosto de 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Colocar n fichas de dominó en una columna, una por fila, dando la vuelta
a las que se quiera, de modo que los números de la izquierda suban (no
estrictamente) y los de la derecha bajen. Imprimir esa disposición o
indicar que no existe.

## Entrada

n (1 ≤ n ≤ 10⁵) y luego los dos números de cada ficha (de 0 a 10⁶).

## Salida

`YES` y las fichas en orden, o `NO`. Se acepta cualquier disposición
válida.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
5 2
6 1
3 4
```

Salida:

```
YES
1 6
2 5
3 4
```

### Ejemplo 2

Entrada:

```
4
1 5
7 1
3 8
5 6
```

Salida:

```
YES
1 7
1 5
6 5
8 3
```

### Ejemplo 3

Entrada:

```
2
1 2
3 4
```

Salida:

```
NO
```

## Solución

Se lee cada ficha como un intervalo [low, high]. Va derecha como (low,
high) o volteada como (high, low). Cada dos filas deben estar en orden:
dos fichas derechas encajan cuando sus intervalos están anidados, dos
volteadas igual, y una derecha con una volteada cuando sus intervalos
se cortan. Así las fichas derechas forman una cadena de intervalos
anidados, las volteadas otra, y el intervalo más interior de una cadena
debe cortar al más interior de la otra; entonces cada intervalo derecho
corta a cada volteado.

Se ordenan los intervalos por su extremo izquierdo, los más largos
primero en caso de empate. Una cadena anidada es entonces una
subsecuencia cuyos extremos derechos nunca suben, y repartir la lista
en dos subsecuencias así se hace de forma voraz: un intervalo va a la
primera cadena si cabe, si no a la segunda, y si no tampoco, no hay
disposición. El último extremo derecho de la primera cadena siempre
queda por debajo del de la segunda, así que esto equivale a poner cada
intervalo en la cadena más ajustada, lo que nunca falla si existe un
reparto.

Si se usan las dos cadenas, sus últimos intervalos, los más interiores,
deben cortarse. Si ninguno contiene al otro, todo reparto tiene el mismo
par interior; si no, todos los intervalos contienen su intersección.
Así la comprobación decide. La primera cadena se imprime derecha y la
segunda volteada y al revés.
`O(n log n)`.

En el segundo ejemplo las cadenas son [1, 7] ⊃ [1, 5] y [3, 8] ⊃
[5, 6], cuyos intervalos interiores se tocan en 5.

Trampas:

- intervalos que solo se tocan en un número se cortan;
- fichas iguales están anidadas en ambos sentidos, así que los empates
  no necesitan más cuidado que el orden de la ordenación;
- un intervalo grande alrededor de dos pequeños separados no tiene
  disposición: los pequeños serían los interiores y no se cortan.

El comprobador verifica que se imprimen las mismas fichas y que ambas
columnas están ordenadas. Los veredictos coinciden con una búsqueda
sobre todas las formas de voltear las fichas en 500 conjuntos
aleatorios de hasta 8, y con una implementación aceptada independiente
en las pruebas grandes.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1743_greedy.cpp](1743_greedy.cpp) | G++ 13.2 x64 | greedy | O(n log n) | AC | 0.187 s | 2348 KB |
| [1743_greedy.go](1743_greedy.go) | Go 1.14 x64 | greedy | O(n log n) | AC | 0.203 s | 13216 KB |
| [1743_greedy.java](1743_greedy.java) | Java 1.8 | greedy | O(n log n) | AC | 0.218 s | 10432 KB |
| [1743_greedy.py](1743_greedy.py) | Python 3.12 x64 | greedy | O(n log n) | AC | 0.437 s | 40804 KB |
| [1743_greedy.rs](1743_greedy.rs) | Rust 1.75 x64 | greedy | O(n log n) | AC | 0.046 s | 7688 KB |
