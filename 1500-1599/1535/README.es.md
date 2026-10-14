# 1535. El hobbit, o Historia de una ida y de una vuelta

[Timus 1535](https://acm.timus.ru/problem.aspx?space=1&num=1535) · dificultad 496 · constructive

Problema original de Alexander Ipatov, del Octavo Campeonato Personal Abierto de la Universidad Estatal de los Urales, 3 de marzo de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Bilbo sale de la ciudad 1, visita una vez cada una de las ciudades
2 … N y vuelve a la ciudad 1 (2 ≤ N ≤ 50000). Entrar en la ciudad P
desde la ciudad Q cuesta P·Q monedas de oro. Hay que escribir un orden
de visita de coste total mínimo y otro de coste total máximo.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N.

## Salida

Dos líneas con N números cada una, empezando por 1: el orden más barato
y el más caro. Se acepta cualquier orden óptimo.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
```

Salida:

```
1 4 2 3
1 3 4 2
```

## Solución

El coste es la suma de los productos de vecinos en un ciclo por todos
los números 1 … N, así que ambas líneas son disposiciones en círculo.

La más cara pone cada número junto a los dos más cercanos en tamaño:
1, 3, 5, … hasta N y de vuelta por los pares hasta 2. Es la disposición
clásica en «tubos de órgano», que maximiza esa suma circular.

La más barata junta números grandes con pequeños. Leído el ciclo desde
N, un lado va 2, N − 2, 4, N − 4, 6, … y el otro 1, N − 1, 3, N − 3,
5, …; en el paso k los dos lados toman k + 1 y k para k impar y N − k y
N − k + 1 para k par, hasta que un par repetiría un número. Si queda un
número, va donde se encuentran los dos lados. Una búsqueda exhaustiva
para N ≤ 10 muestra que es el único ciclo más barato salvo reflexión, y
el juez lo acepta para todo N; no tenemos una demostración. Girar el
ciclo para que empiece en 1 da la primera línea. `O(N)`.

Detalles a tener en cuenta:

- la alternancia simple 1, N, 2, N − 1, … no es óptima: para N = 5 cuesta
  38, y 1, 5, 2, 3, 4 cuesta 37 (prueba 04);
- los dos lados pueden encontrarse dejando una ciudad (prueba 05) o
  ninguna (prueba 06);
- ambas líneas deben empezar por la ciudad 1 (todas las pruebas).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1535_constructive.cpp](1535_constructive.cpp) | G++ 13.2 x64 | constructive | O(N) | AC | 0.015 s | 1700 KB |
| [1535_constructive.go](1535_constructive.go) | Go 1.14 x64 | constructive | O(N) | AC | 0.015 s | 7060 KB |
| [1535_constructive.java](1535_constructive.java) | Java 1.8 | constructive | O(N) | AC | 0.140 s | 11176 KB |
| [1535_constructive.py](1535_constructive.py) | Python 3.12 x64 | constructive | O(N) | AC | 0.109 s | 8752 KB |
| [1535_constructive.rs](1535_constructive.rs) | Rust 1.75 x64 | constructive | O(N) | AC | 0.031 s | 4376 KB |
