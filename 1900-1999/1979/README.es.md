# 1979. Etiquetas con sumas iguales en los ciclos del cubo

[Timus 1979](https://acm.timus.ru/problem.aspx?space=1&num=1979) · dificultad 1361 · constructive

Problema original de Denis Dublennykh, del Campeonato de Programación Deportiva de los Urales 2013.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada cara de un cubo se divide en una cuadrícula `n×n`. Al entrar en una
celda por un lado, el recorrido debe salir por el opuesto y no puede
pasar por vértices. Un ciclo completo visita `4n` celdas. Coloque cada
entero de `1` a `6n²` exactamente una vez para que la suma de cualquier
ciclo sea independiente del inicio y del sentido.

`1≤n≤100`. Tiempo: 1 segundo; memoria: 64 MB.

## Entrada

Un entero `n`.

## Salida

Imprima el desarrollo en T con las caras nombradas como se muestra
abajo. Las primeras `n` líneas contienen `n` etiquetas de `U`; las
siguientes `n` contienen `4n` etiquetas de `A,B,C,D`; las últimas `n`
contienen `n` etiquetas de `V`.

```text
U
A B C D
V
```

## Evaluación

Un comprobador verifica las filas y la permutación y recorre cada camino
cerrado en el cubo plegado; se acepta cualquier disposición válida.

## Ejemplos

Entrada:

```
2
```

Salida:

```
20 13
11 8
3 15 19 4 12 24 18 5
1 7 9 23 21 17 6 16
10 22
14 2
```

## Solución

Sean `a=n²` y `M=6a+1`. Numere tres caras con la mitad inferior de las
etiquetas, por filas. Con índices `r,c` desde cero, defina
`A(r,c)=rn+c+1`, `B(r,c)=a+rn+c+1` y `U(r,c)=2a+rn+c+1`.

Las caras opuestas reciben los complementos hasta `M`. En este
desarrollo, los pares `A,C` y `B,D` invierten las columnas; `U,V`
invierten las filas. Por tanto, `C(r,c)=M−A(r,n−1−c)`,
`D(r,c)=M−B(r,n−1−c)` y `V(r,c)=M−U(n−1−r,c)`.

Las primeras tres caras contienen exactamente `1,…,3a`; sus complementos
contienen `3a+1,…,6a`. Cada etiqueta requerida aparece una vez.

Considere las coordenadas físicas de una celda. Continuar por lados
opuestos conserva una coordenada tangencial y forma un cinturón que
atraviesa cuatro caras. Las franjas de caras opuestas se emparejan
mediante reflexión en el plano medio del cubo. Las inversiones indicadas
mantienen las mismas coordenadas tangenciales, y cada pareja suma `M`.
Hay `2n` parejas por cinturón, así que la suma común es `2nM`. El
argumento incluye tamaños pares, impares y `n=1`.

En el ejemplo, `n=2` y la suma común es `4·25=100`. La primera fila de
la banda central forma un ciclo de ocho celdas que suma 100; los demás
sentidos tienen el mismo total.

Cada etiqueta se calcula directamente a partir de su posición de salida.
El tiempo es `O(n²)`, óptimo para imprimir `6n²` números. La memoria de
trabajo adicional es `O(n)` o menor.

Trampas:

- Invierta columnas para `A,C` y `B,D`, y filas para `U,V`.
- Use reflexión en un plano medio; la simetría central cambia la
  coordenada fija del cinturón.
- Cada fila central contiene cuatro caras; las superiores e inferiores
  contienen una.
- La celda inicial se cuenta una sola vez en el ciclo completo.

## Notas por lenguaje

Todas las versiones usan fórmulas directas. Python construye una fila
cada vez y Java escribe una fila mediante un búfer. C++, Go y Rust
imprimen las etiquetas secuencialmente con salida almacenada en búfer.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1979_constructive.cpp](1979_constructive.cpp) | G++ 13.2 x64 | constructive | O(n^2) | AC | 0.015 s | 424 KB |
| [1979_constructive.go](1979_constructive.go) | Go 1.14 x64 | constructive | O(n^2) | AC | 0.031 s | 1372 KB |
| [1979_constructive.java](1979_constructive.java) | Java 1.8 | constructive | O(n^2) | AC | 0.125 s | 3008 KB |
| [1979_constructive.py](1979_constructive.py) | Python 3.12 x64 | constructive | O(n^2) | AC | 0.125 s | 564 KB |
| [1979_constructive.rs](1979_constructive.rs) | Rust 1.75 x64 | constructive | O(n^2) | AC | 0.062 s | 244 KB |
