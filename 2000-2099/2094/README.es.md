# 2094. Cuándo ir al asiento en una fila que se llena

[Timus 2094](https://acm.timus.ru/problem.aspx?space=1&num=2094) · dificultad 5142 · dp, probability

Problema original de Denis Dublennykh, del Concurso Individual Abierto de la UrFU 2014.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una fila de cine tiene n asientos; algunos están ocupados, uno es el de
Alex, y cada asiento libre sigue libre hasta que empieza la película con
probabilidad p %, de forma independiente. Los demás espectadores entran
de uno en uno en orden aleatorio, y todos llegan a su asiento desde el
extremo izquierdo de la fila. Alex puede esperar en el pasillo y elegir
cuándo ir; si aún espera al empezar, va entonces. Minimizar el número
esperado de espectadores por delante de los que pasa Alex más el de los
que pasan por delante de Alex. Los límites son 1 segundo y 64 MB.

## Entrada

Enteros n y p (1 ≤ n ≤ 1000, 0 ≤ p ≤ 100), y después una cadena de n
caracteres: 0 libre, 1 ocupado, 2 el asiento de Alex. La cadena contiene
exactamente un 2.

## Salida

El valor esperado con error absoluto o relativo de a lo sumo 10⁻⁶.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 0
01120
```

Salida:

```
2.500
```

### Ejemplo 2

Entrada:

```
3 50
020
```

Salida:

```
0.375
```

## Solución

Los asientos ocupados a la izquierda se pasan haga lo que haga Alex, así
que aportan una constante. Lo que importa son los asientos libres: l a
la izquierda y r a la derecha, v = l + r en total. Cada uno se llenará
con probabilidad 1 − p/100, así que el número de llegadas es binomial;
tras ver algunas llegadas, la probabilidad de que llegue alguien más y
el número esperado de los que aún faltan solo dependen de cuántos
asientos libres quedan, y ambos salen de una recurrencia corta sobre ese
número. Cada llegada siguiente ocupa cualquier asiento aún libre con la
misma probabilidad.

Una DP sobre (l, r) compara entonces dos opciones. Ir ahora cuesta el
número esperado de llegadas posteriores a la derecha, r por las
llegadas esperadas que faltan dividido entre l + r. Esperar a la
siguiente llegada no cuesta nada si ya no viene nadie; si no, el recién
llegado se sienta a la izquierda con probabilidad l / (l + r) (Alex
tendrá que pasar por delante: 1 más el valor en (l − 1, r)) o a la
derecha (el valor en (l, r − 1)). Sin asientos libres a la izquierda
Alex puede esperar sin más, y sin asientos a la derecha puede ir: ambos
cuestan 0. La respuesta son los asientos ocupados a la izquierda más el
valor inicial, O(n²) en total.

En el primer ejemplo vienen todos (p = 0); esperar al espectador de la
derecha cuesta 2 o 3 según quién llegue primero, así que la respuesta es
2.5.

Trampa (prueba 03): con un solo asiento la respuesta es 0. Tanto `0`
como `0.000` son válidos; la evaluación debe comparar valores numéricos
con la tolerancia indicada, sin exigir textos idénticos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2094_dp_probability.cpp](2094_dp_probability.cpp) | G++ 13.2 x64 | dp, probability | O(n^2) | AC | 0.015 s | 468 KB |
| [2094_dp_probability.go](2094_dp_probability.go) | Go 1.14 x64 | dp, probability | O(n^2) | AC | 0.031 s | 1132 KB |
| [2094_dp_probability.java](2094_dp_probability.java) | Java 1.8 | dp, probability | O(n^2) | AC | 0.109 s | 544 KB |
| [2094_dp_probability.py](2094_dp_probability.py) | Python 3.12 x64 | dp, probability | O(n^2) | AC | 0.125 s | 740 KB |
| [2094_dp_probability.rs](2094_dp_probability.rs) | Rust 1.75 x64 | dp, probability | O(n^2) | AC | 0.015 s | 256 KB |
