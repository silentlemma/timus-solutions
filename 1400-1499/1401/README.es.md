# 1401. Jugadores

[Timus 1401](https://acm.timus.ru/problem.aspx?space=1&num=1401) · dificultad 159 · constructive

Problema original de Alex Samsonov, del Duodécimo Campeonato por Equipos de Programación para Escolares de la Región de Sverdlovsk, 15 de octubre de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay que cubrir un tablero de 2ⁿ × 2ⁿ, n ≤ 9, al que le falta una
casilla, con piezas en forma de L de tres casillas. Se imprime el
tablero con 0 en la casilla quitada y el número de la pieza en cada una
de las demás, con las piezas numeradas de 1 a (4ⁿ − 1) / 3, o -1 si no
hay forma de cubrirlo.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

n y luego la fila y la columna de la casilla quitada.

## Salida

2ⁿ líneas de 2ⁿ números. Se acepta cualquier recubrimiento.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
1 1
```

Salida:

```
0 1 3 3
1 1 4 3
2 4 4 5
2 2 5 5
```

## Solución

Siempre se puede, partiendo por la mitad. Se divide el tablero en cuatro
cuartos; la casilla quitada está en uno de ellos. Se coloca una pieza en
las tres casillas junto al centro del tablero que pertenecen a los otros
tres cuartos. Ahora cada cuarto es un tablero de 2ⁿ⁻¹ × 2ⁿ⁻¹ con
exactamente una casilla ocupada, que es la misma tarea, y un tablero de
1 × 1 no necesita nada. Las soluciones guardan los cuadrados pendientes
en una pila en lugar de usar recursión, cada uno con su casilla ocupada,
y numeran las piezas en el orden en que se colocan. `O(4ⁿ)`.

Detalles a tener en cuenta:

- la respuesta nunca es -1;
- un tablero de 512 × 512 imprime 262 144 números, así que la salida se
  almacena en búfer (pruebas generadas).

Las pruebas se juzgan con un verificador que exige 0 solo en la casilla
quitada y cada número de 1 a (4ⁿ − 1) / 3 en tres casillas que formen
una L dentro de un cuadrado de 2 × 2.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1401_constructive.cpp](1401_constructive.cpp) | G++ 13.2 x64 | constructive | O(4^n) | AC | 0.031 s | 3760 KB |
| [1401_constructive.go](1401_constructive.go) | Go 1.14 x64 | constructive | O(4^n) | AC | 0.031 s | 4732 KB |
| [1401_constructive.java](1401_constructive.java) | Java 1.8 | constructive | O(4^n) | AC | 0.203 s | 13044 KB |
| [1401_constructive.py](1401_constructive.py) | Python 3.12 x64 | constructive | O(4^n) | AC | 0.375 s | 10628 KB |
| [1401_constructive.rs](1401_constructive.rs) | Rust 1.75 x64 | constructive | O(4^n) | AC | 0.031 s | 4276 KB |
