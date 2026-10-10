# 1210. El ascenso más barato por niveles de planetas

[Timus 1210](https://acm.timus.ru/problem.aspx?space=1&num=1210) · dificultad 170 · dp

Problema original de Leonid Volkov, del USU Open Collegiate Programming Contest, octubre de 2002, Junior Session.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Los planetas están en niveles de 0 a `N < 30`, como mucho 30 por nivel,
y el nivel 0 tiene un único planeta, la casa del viajero. Los pasos solo
llevan de un planeta de un nivel a planetas del siguiente, y cada uno
cuesta un entero de `−32768` a `32767`; un coste negativo significa que
el espíritu que lo guarda paga al viajero. Hay que hallar la ruta más
barata de casa a cualquier planeta del nivel `N`; puede ser negativa. Se
sabe que existe una ruta.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y luego `N` bloques separados por líneas con `*`. El bloque `i`
empieza con el número de planetas del nivel `i`; después, para cada uno,
una línea de pares «planeta del nivel `i − 1`, coste» terminada en `0`.

## Salida

El menor coste total.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
2
1 15 0
1 5 0
*
3
1 -5 2 10 0
1 3 0
2 40 0
*
2
1 1 2 5 3 -5 0
2 -19 3 -20 0
```

Salida:

```
-1
```

## Solución

El mapa está por capas y cada paso sube un nivel, así que no hay ciclos
y los costes negativos no estorban: el camino más barato a un planeta es
el más barato a uno de los planetas que llevan a él más ese paso. Se
guarda el menor coste de cada planeta del nivel actual, empezando con 0
para la casa, y se construyen los costes del nivel siguiente a partir de
los pasos de entrada listados en su bloque. La respuesta es el menor
coste del nivel `N`. `O(L)` para `L` pasos.

Detalles a tener en cuenta:

- un planeta puede no tener ningún paso de entrada, o solo pasos desde
  planetas inalcanzables; ese planeta debe seguir siendo inalcanzable en
  vez de transmitir un paso generoso que salga de él;
- las líneas `*` son solo separadores y se pueden saltar al leer números;
- el total queda por debajo de `30 · 32768` en valor absoluto, así que
  bastan enteros de 32 bits.

Las respuestas se compararon con una solución escrita aparte en 300
mapas aleatorios, la mitad con planetas inalcanzables.

## Notas por lenguaje

- Python y Rust filtran los `*` del flujo de entrada; los demás lenguajes
  los saltan en su lector de números.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1210_dp.cpp](1210_dp.cpp) | G++ 13.2 x64 | dp | O(L) | AC | 0.031 s | 384 KB |
| [1210_dp.go](1210_dp.go) | Go 1.14 x64 | dp | O(L) | AC | 0.031 s | 1220 KB |
| [1210_dp.java](1210_dp.java) | Java 1.8 | dp | O(L) | AC | 0.140 s | 5668 KB |
| [1210_dp.py](1210_dp.py) | Python 3.12 x64 | dp | O(L) | AC | 0.125 s | 3276 KB |
| [1210_dp.rs](1210_dp.rs) | Rust 1.75 x64 | dp | O(L) | AC | 0.046 s | 732 KB |
