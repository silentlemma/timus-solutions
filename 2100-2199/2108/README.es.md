# 2108. Clausura de un conjunto de figuras bajo reglas de deseos

[Timus 2108](https://acm.timus.ru/problem.aspx?space=1&num=2108) · dificultad 461 · bitmask

Problema original de Kirill Borozdin, del Campeonato Juvenil de la UrFU 2016.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay n figuras de colección. Cada uno de los m deseos dice: en cuanto se
tienen todas las figuras de un conjunto A, también se quieren todas las
de un conjunto B. A partir de las figuras ya obtenidas, hallar el menor
conjunto que satisface todos los deseos, es decir, el que se alcanza
cumpliendo deseos hasta que no se quiere nada nuevo. Los límites son 0.9
segundos y 64 MB.

## Entrada

n y m, 1 ≤ n ≤ 1000, 0 ≤ m ≤ 4000, luego m líneas con los conjuntos A y
B como cadenas de n ceros y unos, y el conjunto obtenido con el mismo
formato.

## Salida

El conjunto final con el mismo formato.

## Ejemplos

### Ejemplo 1

Entrada:

```
6 4
111000 101000
110000 111000
010000 100000
000010 000001
010100
```

Salida:

```
111100
```

## Solución

Un conjunto que satisface todos los deseos y contiene las figuras
obtenidas tiene que contener cada figura a la que lleva alguna cadena de
deseos, y el conjunto de exactamente esas figuras satisface todos los
deseos. Así que se repiten pasadas sobre los deseos: un deseo cuyo A está
dentro del conjunto obtenido añade B. Una pasada que no añade nada
termina el proceso, y cualquier otra añade al menos una figura, así que
hay a lo sumo n + 1 pasadas.

Los conjuntos son bitsets de palabras de 64 bits: "A dentro del conjunto
obtenido" es A AND NOT owned = 0, y añadir B es un OR, ambas n / 64
operaciones de palabra. El trabajo total es O(n · m · n / 64), unas
6 · 10⁷ operaciones de palabra.

En el ejemplo las figuras obtenidas 2 y 4 activan el tercer deseo, que
añade 1; luego el segundo deseo añade 3, y el resultado es 111100.

## Notas por lenguaje

La solución en Python traspone el problema, porque las pasadas son
demasiado lentas allí cuando una cadena de deseos aparece en orden
inverso. Para cada figura construye el conjunto de deseos que la
necesitan como un único entero grande (una columna de la matriz de
cadenas A). Un árbol de segmentos sobre las figuras guarda la unión de
esos conjuntos sobre las figuras que aún faltan, que es exactamente el
conjunto de deseos todavía no activados. Cada ronda cumple todos los
deseos recién activados y pone a cero las hojas de las figuras recién
obtenidas. Cada deseo se cumple como máximo una vez y la hoja de cada
figura se pone a cero como máximo una vez.

Sea w el número de bits por dígito de un entero de Python,
N = ceil(n / w), M = ceil(m / w) y L = 1 + ceil(log2 n). Para m > 0,
el tiempo es O(nm + (nL + m)M + nN): leer y trasponer cuesta O(nm),
actualizar el árbol y comprobar la activación cuesta O(nLM), enumerar
los deseos activados cuesta O(mM) y enumerar las figuras nuevas cuesta
O(nN). Unir los resultados cuesta O(mN), ya incluido en O(nm).
Para m = 0, el tiempo es O(n).

Trampa (prueba 15, resultados vacíos): un deseo que no añade nada aún
debe procesarse. Enumerar bits activos en Python no cuesta tiempo
constante por bit: `mask & -mask` y `mask ^= low` recorren los dígitos
del entero. Con n = 1 y m = 4000 deseos A = B = 0, la respuesta sigue
siendo 0, pero enumerar los deseos activados requiere Θ(m² / w)
operaciones sobre dígitos. Por eso, la cota O(n^2 m / 64) de las pasadas
repetidas no describe la solución en Python.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2108_bitmask.cpp](2108_bitmask.cpp) | G++ 13.2 x64 | bitmask | O(n^2 m / 64) | AC | 0.046 s | 1808 KB |
| [2108_bitmask.go](2108_bitmask.go) | Go 1.14 x64 | bitmask | O(n^2 m / 64) | AC | 0.062 s | 18712 KB |
| [2108_bitmask.java](2108_bitmask.java) | Java 1.8 | bitmask | O(n^2 m / 64) | AC | 0.234 s | 1792 KB |
| [2108_bitmask.py](2108_bitmask.py) | Python 3.12 x64 | bitmask | O(nm + (nL + m)M + nN) | AC | 0.171 s | 17336 KB |
| [2108_bitmask.rs](2108_bitmask.rs) | Rust 1.75 x64 | bitmask | O(n^2 m / 64) | AC | 0.062 s | 9312 KB |
