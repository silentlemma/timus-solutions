# 1466. Cuadrado mágico

[Timus 1466](https://acm.timus.ru/problem.aspx?space=1&num=1466) · dificultad 3125 · backtracking

Problema original de Alexander Ipatov, del concurso de la Universidad Estatal de los Urales en el campus de invierno de Petrozavodsk, enero de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un cuadrado de n² × n² casillas (1 ≤ n ≤ 3) se divide en n² bloques de
n × n. Es mágico si contiene los números de 0 a n² − 1 con 0 en la
casilla superior izquierda, ningún número se repite en una fila, una
columna o un bloque, y estas reglas de no repetición siguen cumpliéndose
tras intercambiar dos bloques cualesquiera que comparten un lado. Hay k casillas ya
rellenas. Hay que decidir si el cuadrado puede completarse hasta uno
mágico.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

n y k, y luego k tríos a, b, c: la columna a, la fila b y el número c.

## Salida

«YES» o «NO».

## Ejemplos

### Ejemplo 1

Entrada:

```
2 4
0 0 0
1 2 1
2 1 2
3 3 3
```

Salida:

```
NO
```

### Ejemplo 2

Entrada:

```
2 0
```

Salida:

```
YES
```

## Solución

La regla de los intercambios fija la estructura. Intercambiar dos
bloques vecinos en horizontal deja intactas las filas, y las columnas
siguen siendo válidas solo si, en cada desplazamiento c dentro de un
bloque, ambos bloques tienen el mismo conjunto de números en esa
columna: los conjuntos de una columna de bloques reparten todos los
números, así que el conjunto del vecino debe encajar justo en el de su
pareja. Por tanto, en una fila de bloques todos comparten sus conjuntos
por columnas, y del mismo modo, por intercambios verticales, en una
columna de bloques todos comparten sus conjuntos por filas. Así cada
número v tiene un desplazamiento de fila π_v(J) que ocupa en todos los
bloques de la columna de bloques J, y un desplazamiento de columna
σ_v(I) en todos los bloques de la fila de bloques I, y π_v, σ_v son
permutaciones porque el número aparece una vez por fila y columna del
cuadrado entero. Las reglas de no repetición y de intercambio se cumplen
justo cuando, para cada par (I, J), los números ocupan las n × n posiciones
(π_v(J), σ_v(I)) una vez cada una; y a la inversa, cualquier familia así
cumple esas reglas.

Salvo los nombres de los números, una familia así es un conjunto de n²
pares (π, σ), y una búsqueda breve las encuentra todas: una para n ≤ 2 y
28 para n = 3. Para cada una, una casilla rellena (a, b, c) señala el
único par que cae en ella, así que el número c debe tomar ese par. El
cuadrado puede completarse justo cuando, para alguna familia, ningún
número queda atado a dos pares y ningún par a dos números; los números
libres toman los pares restantes en cualquier orden. La esquina con 0
cuenta como una casilla rellena más.

Detalles a tener en cuenta:

- un sudoku válido corriente casi nunca es mágico (prueba 09);
- 0 debe estar en la esquina (prueba 06) y no repetirse en su fila
  (prueba 15).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1466_backtracking.cpp](1466_backtracking.cpp) | G++ 13.2 x64 | backtracking | O(1) with 28 structures | AC | 0.031 s | 256 KB |
| [1466_backtracking.go](1466_backtracking.go) | Go 1.14 x64 | backtracking | O(1) with 28 structures | AC | 0.031 s | 1136 KB |
| [1466_backtracking.java](1466_backtracking.java) | Java 1.8 | backtracking | O(1) with 28 structures | AC | 0.140 s | 4352 KB |
| [1466_backtracking.py](1466_backtracking.py) | Python 3.12 x64 | backtracking | O(1) with 28 structures | AC | 0.328 s | 704 KB |
| [1466_backtracking.rs](1466_backtracking.rs) | Rust 1.75 x64 | backtracking | O(1) with 28 structures | AC | 0.062 s | 436 KB |
