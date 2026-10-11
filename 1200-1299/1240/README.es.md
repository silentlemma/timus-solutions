# 1240. Un mago contra una manada de monstruos

[Timus 1240](https://acm.timus.ru/problem.aspx?space=1&num=1240) · dificultad 1414 · games

Problema original de Andrew Stankevich, del concurso regional ACM ICPC del noreste de Europa 2002–2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un héroe está en la casilla 0 de una franja de casillas 0 a N (N ≤ 10)
con HP_H puntos de vida (≤ 100) y MP_H de maná (≤ 50). Una manada de N_M
monstruos de HP_M puntos cada uno (N_M, HP_M ≤ 10) empieza en la casilla
N y actúa como un solo cuerpo: con H puntos restantes tiene ⌈H/HP_M⌉
monstruos. Cada turno el héroe gasta un punto de maná en un hechizo y
luego la manada se mueve:

- **Rayo** quita L_P puntos a la manada, donde P es su casilla;
- **Teletransporte** pone la manada en cualquier casilla de 1 a N;
- **Curación** da al héroe dH puntos, sin pasar de HP_H.

Después la manada avanza min(V, P − 1) casillas hacia el héroe y, si
termina en la casilla 1, golpea con tantos puntos como monstruos tiene.
El héroe pierde con cero puntos de vida, o sin maná con monstruos vivos.
Hay que hallar una secuencia de hechizos ganadora o decir que no existe.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N, HP_H, MP_H, HP_M, N_M, V, dH y luego L_1 … L_N.

## Salida

`DEFEATED`, o `VICTORIOUS` seguido de un hechizo por línea: `L`, `H` o
`T p`.

## Evaluación

Se acepta cualquier secuencia ganadora. El verificador compara el
veredicto con la respuesta esperada y juega los hechizos: cada uno
necesita maná, el héroe debe sobrevivir a cada golpe, la manada debe
morir con el último hechizo y no puede venir nada después.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 3 2 1 2 1 1
1 1
```

Salida:

```
VICTORIOUS
L
L
```

### Ejemplo 2

Entrada:

```
2 3 2 3 1 1 1
1 1
```

Salida:

```
DEFEATED
```

### Ejemplo 3

Entrada:

```
4 4 3 1 4 1 1
3 1 1 1
```

Salida:

```
VICTORIOUS
L
T 2
L
```

### Ejemplo 4

Entrada:

```
1 6 5 1 4 1 3
1
```

Salida:

```
VICTORIOUS
L
L
H
L
L
```

## Solución

Cada hechizo cuesta un punto de maná, así que el juego siempre termina y
un estado se resuelve a partir de estados con menos maná. Un estado son
los puntos del héroe, el maná, los puntos de la manada y su casilla:
hasta 100 × 50 × 100 × 10. Pero más puntos de vida nunca perjudican al
héroe: los mismos hechizos siguen sirviendo. Así que para cada maná m,
puntos de la manada h y casilla p basta saber `need[m][h][p]`, los menos
puntos con los que el héroe aún gana, y son solo 50 × 100 × 10 números.

Para un hechizo, se sigue a la manada hasta su siguiente casilla q y se
suma el golpe `s` que da allí:

- un rayo que mata a la manada necesita solo 1 punto; si no, necesita
  `s + need[m−1][h − L_p][q]`;
- un teletransporte a t necesita `s + need[m−1][h][q]`, con q la casilla
  tras moverse desde t;
- una curación necesita el mismo `s + need[m−1][h][q]` tras curarse, lo
  que es imposible si supera HP_H y si no pide dH menos.

`need` es el mínimo entre los hechizos, e infinito sin maná. El héroe
gana cuando `need[MP_H][N_M·HP_M][N] ≤ HP_H`; entonces los hechizos se
reconstruyen hacia delante, tomando cada vez cualquiera cuyo requisito
cumplan los puntos actuales. `O(MP_H · N_M·HP_M · N²)`.

Detalles a tener en cuenta:

- tras un teletransporte la manada se mueve en seguida, así que nunca
  está en la casilla elegida en el siguiente turno del héroe: la prueba
  05 la manda a la casilla 10 para que quede en la 9, la única fuerte;
- una manada que ya está en la casilla 1 avanza cero casillas y golpea
  cada turno;
- el golpe cuenta los monstruos que quedan, ⌈H/HP_M⌉, no sus puntos.

Los veredictos se compararon con una búsqueda exhaustiva sobre estados
completos en 800 batallas pequeñas aleatorias, y cada victoria se jugó
con el verificador.

## Notas por lenguaje

- Rust nombra los hechizos con un enum, Go y Python con letras, y C++ y
  Java con números: -1 para el rayo, 0 para la curación y la casilla de
  destino para el teletransporte.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1240_games.cpp](1240_games.cpp) | G++ 13.2 x64 | games | O(MP_H · N_M·HP_M · N²) | AC | 0.015 s | 448 KB |
| [1240_games.go](1240_games.go) | Go 1.14 x64 | games | O(MP_H · N_M·HP_M · N²) | AC | 0.031 s | 1740 KB |
| [1240_games.java](1240_games.java) | Java 1.8 | games | O(MP_H · N_M·HP_M · N²) | AC | 0.093 s | 876 KB |
| [1240_games.py](1240_games.py) | Python 3.12 x64 | games | O(MP_H · N_M·HP_M · N²) | AC | 0.578 s | 1372 KB |
| [1240_games.rs](1240_games.rs) | Rust 1.75 x64 | games | O(MP_H · N_M·HP_M · N²) | AC | 0.015 s | 592 KB |
