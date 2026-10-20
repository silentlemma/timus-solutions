# 2161. Un caballero que gana cada duelo compren lo que compren los demás

[Timus 2161](https://acm.timus.ru/problem.aspx?space=1&num=2161) · dificultad 772 · greedy

Problema original de Aleksey Bykov, del Concurso Escolar de Programación de los Urales 2021.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada uno de los n caballeros tiene ataque aᵢ, escudo dᵢ y gᵢ monedas;
una moneda añade un punto al ataque o al escudo, y nadie sabe cómo
gastarán las suyas los demás. Cada par de caballeros combate una vez; un
caballero queda aplastado cuando el ataque del rival es al menos su
escudo, y gana cuando el rival queda aplastado y el propio caballero no. Hallar un
caballero que pueda comprar un equipo que gane todos los combates haga lo
que haga el resto, o imprimir −1. Los límites son 1.5 segundos y 256 MB.

## Entrada

n, 1 ≤ n ≤ 10⁵, y luego las ternas aᵢ, dᵢ, gᵢ, cada una entre 0 y 10⁹.

## Salida

El número de ese caballero, o −1.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
100 4 5
1 2 8
```

Salida:

```
-1
```

### Ejemplo 2

Entrada:

```
3
5 2 2
4 1 10
10 4 0
```

Salida:

```
2
```

## Solución

El rival j puede llegar a ataque aⱼ + gⱼ o a escudo dⱼ + gⱼ, y el
caballero i debe estar a salvo frente a ambos extremos. Así que i
necesita un escudo mayor que A = max sobre j ≠ i de (aⱼ + gⱼ) y un ataque
de al menos D = max sobre j ≠ i de (dⱼ + gⱼ). El caballero i lo consigue
exactamente cuando

max(0, A + 1 − dᵢ) + max(0, D − aᵢ) ≤ gᵢ.

Los máximos sobre todos menos i salen de los dos mayores valores de
cada tipo y de la posición del mayor. Como mucho un caballero puede
cumplirlo, porque un caballero así vence a todos los demás. Sin rivales
no hay máximos y un caballero solo gana. El trabajo es O(n), con sumas
de 64 bits.

En el primer ejemplo el caballero 1 solo puede subir el escudo hasta 9,
y el caballero 2 puede subir también el ataque hasta 9, así que el
caballero 1 no está a salvo; el caballero 2 no puede conseguir un escudo
mayor que 105.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2161_greedy.cpp](2161_greedy.cpp) | G++ 13.2 x64 | greedy | O(n) | AC | 0.203 s | 2556 KB |
| [2161_greedy.go](2161_greedy.go) | Go 1.14 x64 | greedy | O(n) | AC | 0.203 s | 6900 KB |
| [2161_greedy.java](2161_greedy.java) | Java 1.8 | greedy | O(n) | AC | 0.156 s | 7484 KB |
| [2161_greedy.py](2161_greedy.py) | Python 3.12 x64 | greedy | O(n) | AC | 0.265 s | 32468 KB |
| [2161_greedy.rs](2161_greedy.rs) | Rust 1.75 x64 | greedy | O(n) | AC | 0.015 s | 8320 KB |
