# 1260. El fotógrafo quisquilloso

[Timus 1260](https://acm.timus.ru/problem.aspx?space=1&num=1260) · dificultad 111 · dp

Problema original de Alexander Ipatov, de la Competición Abierta por Equipos de Programación para Escolares de la Región de Sverdlovsk, 11 de octubre de 2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N estudiantes de 1, 2, …, N años (1 ≤ N ≤ 55) se sientan en fila. Quien
tiene 1 año se sienta en el extremo izquierdo, y las edades de dos
vecinos cualesquiera difieren como mucho en 2. ¿Cuántas filas así hay?

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N.

## Salida

El número de filas.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
```

Salida:

```
4
```

## Solución

Sea a(k) el número de filas para las edades 1..k. Se mira quién se
sienta en segundo lugar:

- la edad 2: el resto es una fila de 2..k que empieza en 2, el mismo
  problema desplazado en uno, a(k − 1) formas;
- la edad 3 y luego la 2: después debe ir el 4, y el resto es una fila
  de 4..k que empieza en 4, a(k − 3) formas;
- la edad 3, pero el 2 más tarde: los vecinos del 2 solo pueden ser 1, 3
  y 4, y 1 y 3 ya están juntos, así que el 2 va en el extremo derecho
  junto al 4. Esto obliga al zigzag 1, 3, 5, … subiendo por las edades
  impares y bajando por las pares hasta 4, 2: exactamente una fila.

Así, a(k) = a(k − 1) + a(k − 3) + 1, con a(1) = a(2) = 1 y a(3) = 2.
Aplicar la regla hacia atrás da a(0) = 0 y a(−1) = −1, lo que permite
empezar el bucle en k = 1 sin casos especiales. a(55) = 1 388 937 263
aún cabe en 32 bits, pero las soluciones usan 64. `O(N)`.

Detalles a tener en cuenta:

- el tercer caso es fácil de olvidar: para N = 5 es la fila
  1, 3, 5, 4, 2 (prueba 05);
- con N = 1 y N = 2 hay una sola fila (pruebas 02, 03).

La recurrencia se comparó con listar todas las permutaciones para N
hasta 10.

## Notas por lenguaje

- Todos los lenguajes guardan los tres últimos valores en tres
  variables.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1260_dp.cpp](1260_dp.cpp) | G++ 13.2 x64 | dp | O(N) | AC | 0.015 s | 128 KB |
| [1260_dp.go](1260_dp.go) | Go 1.14 x64 | dp | O(N) | AC | 0.046 s | 1076 KB |
| [1260_dp.java](1260_dp.java) | Java 1.8 | dp | O(N) | AC | 0.093 s | 1568 KB |
| [1260_dp.py](1260_dp.py) | Python 3.12 x64 | dp | O(N) | AC | 0.109 s | 404 KB |
| [1260_dp.rs](1260_dp.rs) | Rust 1.75 x64 | dp | O(N) | AC | 0.015 s | 232 KB |
