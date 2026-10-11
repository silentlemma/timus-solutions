# 1261. Propinas

[Timus 1261](https://acm.timus.ru/problem.aspx?space=1&num=1261) · dificultad 330 · number_theory

Problema original de Alexander Ipatov, de la Competición Abierta por Equipos de Programación para Escolares de la Región de Sverdlovsk, 11 de octubre de 2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay billetes de 1, 3, 9, 27, … trits, y el cliente tiene exactamente un
billete de cada valor. La cuenta es de N trits (1 ≤ N ≤ 10⁷). El
cliente paga una cantidad y el camarero se queda el cambio como
propina. El camarero se ofende salvo que la propina sea positiva y
pueda pagarse con billetes distintos. Hay que dar un pago y una
propina; el pago no puede superar 4 294 967 291. Se acepta cualquier
pareja válida; si no hay ninguna, se imprime 0.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N.

## Salida

El pago y la propina.

## Evaluación

Valen muchas parejas, así que el evaluador acepta cualquiera: el pago
menos la propina debe ser N, la propina positiva, el pago dentro del
límite, y ambos escritos en base 3 solo con los dígitos 0 y 1.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
```

Salida:

```
9 4
```

## Solución

Tanto el pago P como la propina T son sumas de potencias de 3 distintas,
y P − T = N. Se escribe N en ternario equilibrado, con dígitos −1, 0 y
1: los dígitos 1 forman P y los −1 forman T. Desde la cifra más baja, un
resto 1 da un dígito 1 y un resto 2 da un dígito −1 con acarreo a la
siguiente posición.

Si N no tiene ningún 2 en base 3, queda T = 0. Entonces se toma la menor
potencia de 3 que falta en P y se suma a ambos: P sigue con billetes
distintos y T es ese único billete. Así que siempre hay respuesta y
nunca se imprime 0. P queda por debajo de 3¹⁶ ≈ 4,3 · 10⁷, muy lejos del
límite. `O(log N)`.

Detalles a tener en cuenta:

- la propina debe ser positiva: N = 1 no puede pagarse como 1 con
  propina 0, y 4 3 es una respuesta (prueba 02);
- el pago puede necesitar un billete mayor que N: N = 10⁷ se paga con
  14 960 143 y una propina de 4 960 143 (prueba 03);
- el pago y la propina pueden compartir un billete: la propina es solo
  una suma que podría pagarse, no billetes del cliente.

Todos los N de 1 a 3000 y los dos mayores se pasaron por el evaluador.

## Notas por lenguaje

- Todos los lenguajes obtienen los dígitos del ternario equilibrado en
  un solo bucle.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1261_number_theory.cpp](1261_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(log N) | AC | 0.015 s | 128 KB |
| [1261_number_theory.go](1261_number_theory.go) | Go 1.14 x64 | number_theory | O(log N) | AC | 0.031 s | 1068 KB |
| [1261_number_theory.java](1261_number_theory.java) | Java 1.8 | number_theory | O(log N) | AC | 0.125 s | 1612 KB |
| [1261_number_theory.py](1261_number_theory.py) | Python 3.12 x64 | number_theory | O(log N) | AC | 0.078 s | 432 KB |
| [1261_number_theory.rs](1261_number_theory.rs) | Rust 1.75 x64 | number_theory | O(log N) | AC | 0.046 s | 232 KB |
