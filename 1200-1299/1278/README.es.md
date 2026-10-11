# 1278. "… Connecting people"

[Timus 1278](https://acm.timus.ru/problem.aspx?space=1&num=1278) · dificultad 983 · constructive

Problema original de Sergey Volchenkov, Vladimir Pinaev y Michael Kopachev, del cuarto de final de la región central de Rusia del ACM ICPC 2003–2004, Rybinsk, 15–16 de octubre de 2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un procesador de sonido conoce dos órdenes, una por celda de memoria.
`CALL X` apila la dirección de la celda siguiente en una pila de 100
celdas y salta a la celda X. `BELL&RET` suena una vez y vuelve a la
dirección de la cima de la pila, o se detiene si la pila está vacía. La
ejecución empieza en la celda 0. Hay que escribir un programa de como
mucho 100 órdenes, con un único `BELL&RET` al final, que suene
exactamente K veces (1 ≤ K ≤ 10⁹).

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

K.

## Salida

El programa, una orden por línea, empezando por la celda 0.

## Evaluación

Sirven muchos programas, así que el evaluador acepta cualquiera:
comprueba la forma de cada línea y que cada llamada apunte hacia
delante. Luego cuenta los sonidos desde cada celda, de la última hacia
arriba, y comprueba la profundidad de la pila y el total.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
```

Salida:

```
CALL 1
CALL 2
BELL&RET
```

### Ejemplo 2

Entrada:

```
1
```

Salida:

```
BELL&RET
```

## Solución

Sea bells(i) el número de sonidos que se producen cuando el procesador
ejecuta desde la celda i hasta que esa ejecución vuelve. La última celda
da bells = 1. Una orden `CALL X` en la celda i ejecuta primero desde X y
luego desde i + 1, así que bells(i) = bells(X) + bells(i + 1). Bastan
dos elecciones de X:

- `CALL i+1` duplica: bells(i) = 2 · bells(i + 1);
- una llamada a la última celda suma uno: bells(i) = bells(i + 1) + 1.

Subiendo desde la última celda, se empieza en 1 y se recorren los
dígitos binarios de K tras el uno inicial: se duplica en cada dígito y,
en cada 1, se suma uno más. Para K menor que 2³⁰ hacen falta como mucho
29 duplicaciones y 29 sumas, 59 celdas con la campana. Todas las
llamadas apuntan hacia delante, así que la pila guarda como mucho una
dirección por celda. `O(log K)`.

Detalles a tener en cuenta:

- con K = 1 el programa es solo `BELL&RET` (prueba 02);
- una llamada a la misma celda o a una anterior se llama a sí misma sin
  fin y desborda la pila, así que ninguna llamada puede apuntar atrás;
- el programa se lee desde la celda 0, así que las celdas construidas de
  abajo arriba se imprimen al revés.

Además, todos los K hasta 299 se ejecutaron en un modelo literal del
procesador, y las respuestas de todas las pruebas pasan el evaluador.

## Notas por lenguaje

- Todos los lenguajes recorren los dígitos binarios de K de la misma
  manera.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1278_constructive.cpp](1278_constructive.cpp) | G++ 13.2 x64 | constructive | O(log K) | AC | 0.015 s | 192 KB |
| [1278_constructive.go](1278_constructive.go) | Go 1.14 x64 | constructive | O(log K) | AC | 0.031 s | 1096 KB |
| [1278_constructive.java](1278_constructive.java) | Java 1.8 | constructive | O(log K) | AC | 0.109 s | 1656 KB |
| [1278_constructive.py](1278_constructive.py) | Python 3.12 x64 | constructive | O(log K) | AC | 0.093 s | 448 KB |
| [1278_constructive.rs](1278_constructive.rs) | Rust 1.75 x64 | constructive | O(log K) | AC | 0.015 s | 244 KB |
