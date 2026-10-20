# 2149. Girar palomas ASCII hasta un patrón ordenado

[Timus 2149](https://acm.timus.ru/problem.aspx?space=1&num=2149) · dificultad 148 · implementation

Problema original de Kirill Borozdin, del Concurso de Programación por Equipos de los Urales 2019.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

n palomas están en fila, con n par, cada una mirando a la izquierda o a
la derecha, dibujadas en ASCII. La fila está ordenada cuando la mitad
izquierda mira hacia un lado y la derecha hacia el otro, o cuando las
palomas en posiciones pares miran hacia un lado y las de posiciones
impares hacia el otro. Hallar el menor número de palomas que hay que
girar. Los límites son 0.5 segundos y 256 MB.

## Entrada

n, 2 ≤ n ≤ 100, y luego tres líneas de 5n − 1 caracteres con las
palomas: `<@..`, `.OO=`, `./\.` para una paloma que mira a la izquierda
y `..@>`, `=OO.`, `./\.` para una que mira a la derecha, separadas por
columnas de puntos.

## Salida

El menor número de giros.

## Ejemplos

### Ejemplo 1

Entrada:

```
8
..@>.<@...<@.....@>...@>...@>.<@...<@..
=OO...OO=..OO=.=OO..=OO..=OO...OO=..OO=
./\.../\.../\.../\.../\.../\.../\.../\.
```

Salida:

```
4
```

### Ejemplo 2

Entrada:

```
4
..@>...@>.<@.....@>
=OO..=OO...OO=.=OO.
./\.../\.../\.../\.
```

Salida:

```
1
```

## Solución

Solo hace falta la primera línea: con índices desde cero, la paloma i
mira a la izquierda exactamente cuando el carácter de la posición 5i es
`<`. Se prueban cuatro patrones candidatos, en dos pares de opuestos. Se
cuentan las palomas que difieren de "la mitad izquierda mira a la
izquierda y la derecha a la derecha"; su patrón opuesto difiere justo en
las demás palomas, así que necesita n menos esa cuenta. Lo mismo vale
para "las posiciones pares miran a la izquierda y las impares a la
derecha". La respuesta es el menor de los cuatro números, hallado en
O(n).

En el segundo ejemplo solo la primera paloma rompe la alternancia, así
que basta un giro.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2149_implementation.cpp](2149_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.031 s | 400 KB |
| [2149_implementation.go](2149_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.015 s | 1100 KB |
| [2149_implementation.java](2149_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.125 s | 1612 KB |
| [2149_implementation.py](2149_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.078 s | 412 KB |
| [2149_implementation.rs](2149_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.046 s | 240 KB |
