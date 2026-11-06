# 1261. Propinas

[Timus 1261](https://acm.timus.ru/problem.aspx?space=1&num=1261) · dificultad 329 · number_theory

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

## Soluciones optimizadas

Go recorre los dígitos ternarios equilibrados conservando solo el importe restante, la potencia actual, el pago y la propina. Un uno añade el billete al pago. Un dos lo añade a la propina y lleva uno a la siguiente cifra. Recuerda el menor billete sin usar para añadirlo a ambas sumas cuando la propina sea cero. La entrada y la salida decimal usan búferes fijos de bytes, sin un analizador ni un formateador numérico general. Go accede directamente a los descriptores de entrada y salida estándar.

Las implementaciones base aceptadas [1261_number_theory.cpp](1261_number_theory.cpp), [1261_number_theory.java](1261_number_theory.java), [1261_number_theory.py](1261_number_theory.py), [1261_number_theory.rs](1261_number_theory.rs) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Notas por lenguaje

Estas notas describen las implementaciones sencillas.

- Todos los lenguajes obtienen los dígitos del ternario equilibrado en
  un solo bucle.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1261_number_theory.cpp](1261_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(log N) | AC | 0.015 s | 128 KB | 11284132 |
| [1261_number_theory.go](1261_number_theory.go) | Go 1.14 x64 | number_theory | O(log N) | AC | 0.031 s | 1068 KB | 11284133 |
| [1261_number_theory.java](1261_number_theory.java) \* | Java 1.8 | number_theory | O(log N) | AC | 0.125 s | 1612 KB | 11284139 |
| [1261_number_theory.py](1261_number_theory.py) \* | Python 3.12 x64 | number_theory | O(log N) | AC | 0.078 s | 432 KB | 11284137 |
| [1261_number_theory.rs](1261_number_theory.rs) \* | Rust 1.75 x64 | number_theory | O(log N) | AC | 0.046 s | 232 KB | 11284140 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1261_number_theory_optimized.go](1261_number_theory_optimized.go) \* | Go 1.14 x64 | number_theory | O(log N) | AC | 0.031 s | 308 KB | 11311230 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
