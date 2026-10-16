# 1780. Código Gray

[Timus 1780](https://acm.timus.ru/problem.aspx?space=1&num=1780) · dificultad 912 · dp

Problema original de Dmitry Poletaev, del XV Campeonato Abierto por Equipos de Programación de la Universidad Estatal de los Urales.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

El código Gray binario reflejado de longitud n enumera todas las
cadenas binarias de n cifras; en la posición k está el código Gray de
k. Un papel tiene k y su código x en binario, de igual longitud, con
algunas cifras borradas y mostradas como `?`. Restaurar ambos números
si se puede hacer de exactamente una manera.

## Entrada

k y x, cadenas de 0, 1 y ? de la misma longitud, a lo sumo 10⁵,
posiblemente con ceros a la izquierda.

## Salida

k y x restaurados, o `Ambiguity` si hay varias maneras, o `Impossible`
si no hay ninguna.

## Ejemplos

### Ejemplo 1

Entrada:

```
0?1
0?0
```

Salida:

```
011
010
```

### Ejemplo 2

Entrada:

```
?00
??0
```

Salida:

```
Ambiguity
```

### Ejemplo 3

Entrada:

```
100
100
```

Salida:

```
Impossible
```

## Solución

La lista construida reflejando y anteponiendo pone en la posición k el
número k xor (k desplazado una posición a la derecha), así que la cifra
i de x, contando desde la izquierda, es la cifra i de k xor la cifra
i − 1 de k, con un 0 antes de la primera. De izquierda a derecha, las
lecturas de las primeras cifras se cuentan según la última cifra de k:
una lectura que acaba en k(i) = b prolonga una que acaba en
k(i − 1) = c cuando el papel admite k(i) = b y x(i) = b xor c. Los
recuentos se limitan a 2, que es todo lo que necesita la respuesta.

Si hay exactamente una lectura, se recupera desde el final: en cada
paso solo una cifra anterior con lectura propia lleva adelante, y las
cifras del código salen de k. `O(n)`.

En el primer ejemplo la cifra central de k debe ser 1, pues un 0 daría
un 1 al final del código, que acaba en 0: k = 011, x = 010.

Trampas:

- la primera cifra del código es la primera cifra de k;
- los recuentos pueden crecer como 2ⁿ, así que se limitan;
- los ceros a la izquierda forman parte de las cadenas y se conservan.

Las respuestas coinciden con una búsqueda sobre todo k de hasta 10
cifras en 600 papeles aleatorios y con una implementación aceptada
independiente en 60 papeles de hasta 10⁵ cifras.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1780_dp.cpp](1780_dp.cpp) | G++ 13.2 x64 | dp | O(n) | AC | 0.015 s | 1404 KB |
| [1780_dp.go](1780_dp.go) | Go 1.14 x64 | dp | O(n) | AC | 0.046 s | 3692 KB |
| [1780_dp.java](1780_dp.java) | Java 1.8 | dp | O(n) | AC | 0.140 s | 5852 KB |
| [1780_dp.py](1780_dp.py) | Python 3.12 x64 | dp | O(n) | AC | 0.234 s | 11024 KB |
| [1780_dp.rs](1780_dp.rs) | Rust 1.75 x64 | dp | O(n) | AC | 0.046 s | 1496 KB |
