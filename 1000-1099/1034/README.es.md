# 1034. Mover tres reinas entre posiciones pacíficas

[Timus 1034](https://acm.timus.ru/problem.aspx?space=1&num=1034) · dificultad 810 · bruteforce

Problema original de Dmitry Filimonenkov, del III Campeonato Universitario por Equipos de Programación de los Urales, 1999.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

`N` reinas (`4 ≤ N ≤ 50`) están en un tablero `N × N` en una posición
pacífica: ninguna reina ataca a otra. Cuenta las posiciones pacíficas que
se obtienen de la dada moviendo exactamente tres reinas. Las reinas no se
distinguen: una posición es el conjunto de casillas ocupadas, así que
intercambiar reinas entre casillas ocupadas da la misma posición.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y luego `N` líneas con las coordenadas `X Y` (`1 ≤ X, Y ≤ N`) de las
reinas.

## Salida

El número de posiciones pacíficas alcanzables moviendo exactamente tres
reinas.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
2 1
1 3
3 4
4 2
```

Salida:

```
0
```

### Ejemplo 2

Entrada:

```
9
2 5
3 8
7 1
8 7
9 4
6 6
1 3
5 9
4 2
```

Salida:

```
4
```

## Solución

En una posición pacífica cada fila y cada columna tiene exactamente una
reina, así que una posición es una permutación: fila `r` → columna
`col[r]`. Mover exactamente tres reinas significa que la nueva posición
difiere de la antigua en exactamente tres casillas. Las otras `N − 3`
reinas se quedan y conservan sus filas y columnas, de modo que las tres
reinas movidas deben ocupar las mismas tres filas y las mismas tres
columnas, emparejadas de otra forma. De los 6 emparejamientos de tres
filas con tres columnas, uno es la posición antigua y tres dejan una reina
en su sitio (solo se mueven dos); quedan los dos desplazamientos cíclicos
de las columnas. Ternas o desplazamientos distintos dan posiciones
distintas.

Por tanto: para cada terna de filas `a < b < c` y ambos desplazamientos
cíclicos, se colocan las tres reinas en las casillas nuevas y se revisan
las diagonales. Se llevan contadores de reinas en cada diagonal `r + c` y
`r − c`; se quitan las tres reinas antiguas y luego cada casilla nueva debe
encontrar vacías sus dos diagonales (esto también detecta dos reinas nuevas
que se atacan entre sí). Son `2 · C(N, 3) ≈ 39 000` comprobaciones de
tiempo constante, `O(N^3)` en total.

Detalles a tener en cuenta:

- intercambiar solo dos reinas es mover dos reinas, no tres, y no se
  cuenta;
- no cuentes un desplazamiento dos veces: los dos desplazamientos cíclicos
  de una terna son dos posiciones distintas, los otros cuatro
  emparejamientos no interesan;
- una reina nueva puede atacar a otra reina nueva, no solo a las que se
  quedan.

## Notas por lenguaje

- **C++**, **Go**, **Java**, **Rust**: contadores de diagonales modificados
  en el sitio y restaurados después de cada comprobación.
- **Python**: conjuntos de diagonales ocupadas; para cada terna se quitan
  las tres diagonales antiguas de una copia de los conjuntos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1034_bruteforce.cpp](1034_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(N^3) | AC | 0.015 s | 196 KB |
| [1034_bruteforce.go](1034_bruteforce.go) | Go 1.14 x64 | bruteforce | O(N^3) | AC | 0.015 s | 1104 KB |
| [1034_bruteforce.java](1034_bruteforce.java) | Java 1.8 | bruteforce | O(N^3) | AC | 0.093 s | 1016 KB |
| [1034_bruteforce.py](1034_bruteforce.py) | Python 3.12 x64 | bruteforce | O(N^3) | AC | 0.187 s | 604 KB |
| [1034_bruteforce.rs](1034_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(N^3) | AC | 0.031 s | 216 KB |
