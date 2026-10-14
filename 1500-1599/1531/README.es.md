# 1531. Zonas en un plano

[Timus 1531](https://acm.timus.ru/problem.aspx?space=1&num=1531) · dificultad 1427 · math

Problema original de Dmitry Gozman, del Dmitry Gozman Contest 1 en el campus de invierno de Petrozavodsk, enero de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

La zona 1 es un cuadrado formado por dos triángulos rectángulos
isósceles. La zona n + 1 sale de la zona n: sobre cada cateto de cada
uno de sus triángulos, como hipotenusa, se construyen dos triángulos
rectángulos isósceles, y luego se quita todo triángulo que forme parte
de una zona anterior. Hay que contar cuántos polígonos simples forman
la zona n (1 ≤ n ≤ 2000).

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

n.

## Salida

El número de polígonos.

## Ejemplos

### Ejemplo 1

Entrada:

```
1
```

Salida:

```
1
```

### Ejemplo 2

Entrada:

```
2
```

Salida:

```
4
```

### Ejemplo 3

Entrada:

```
3
```

Salida:

```
8
```

### Ejemplo 4

Entrada:

```
4
```

Salida:

```
12
```

## Solución

Las primeras 16 zonas pueden construirse exactamente en una red: se escala
el cuadrado por 2^16 para que todas las coordenadas de los vértices sigan
siendo enteras, se conservan los triángulos nuevos cuyo centro no está
cubierto por un triángulo anterior, y se unen los triángulos de una zona
que comparten un lado. Para las primeras 16 zonas esto da 1, 4, 8, 12,
20, 28, 44, 60, 92, 124, 188, 252, 380, 508, 764, 1020. Desde la zona 3
los incrementos son 4, 4, 8, 8, 16, 16, …, duplicándose cada dos
zonas, así que para n ≥ 2

- un n par = 2k da 2^(k+2) − 4;
- un n impar = 2k + 1 da 3·2^(k+1) − 4.

Las soluciones escriben estos números, que llegan a unos 10³⁰¹, así que
C++ y Rust duplican un número decimal cifra a cifra y Go y Java usan sus
enteros grandes. Como mucho `O(n²)` operaciones con cifras.

Detalles a tener en cuenta:

- la zona 1 es la única excepción: la fórmula impar daría 2, pero el
  cuadrado es un solo polígono (prueba 01);
- para n = 2000, 1999 las respuestas superan las 300 cifras (pruebas 06, 07);
- la fórmula se apoya en las cuentas de las primeras 16 zonas y la ha
  comprobado el juez; el razonamiento de arriba no la demuestra.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1531_math.cpp](1531_math.cpp) | G++ 13.2 x64 | math | O(n^2) | AC | 0.015 s | 188 KB |
| [1531_math.go](1531_math.go) | Go 1.14 x64 | math | O(n^2) | AC | 0.015 s | 1160 KB |
| [1531_math.java](1531_math.java) | Java 1.8 | math | O(n^2) | AC | 0.093 s | 1700 KB |
| [1531_math.py](1531_math.py) | Python 3.12 x64 | math | O(n^2) | AC | 0.093 s | 380 KB |
| [1531_math.rs](1531_math.rs) | Rust 1.75 x64 | math | O(n^2) | AC | 0.046 s | 232 KB |
