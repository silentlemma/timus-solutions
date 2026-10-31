# 1210. El ascenso más barato por niveles de planetas

[Timus 1210](https://acm.timus.ru/problem.aspx?space=1&num=1210) · dificultad 169 · dp

Problema original de Leonid Volkov, del USU Open Collegiate Programming Contest, octubre de 2002, Junior Session.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Los planetas están en niveles de 0 a `N`, `0 < N < 30`, como mucho 30
por nivel, y el nivel 0 tiene un único planeta, la casa del viajero. Los
pasos solo llevan de un planeta de un nivel a planetas del siguiente, y
cada uno cuesta un entero de `−32768` a `32767`; un coste negativo
significa que el espíritu que lo guarda paga al viajero. Hay que hallar
la ruta más barata de casa a cualquier planeta del nivel `N`; puede ser
negativa. Se sabe que existe una ruta.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y luego `N` bloques separados por líneas con `*`. El bloque `i`
empieza con el número `K_i` de planetas del nivel `i`, numerados de 1 a
`K_i`; después, para cada uno en ese orden, una línea de pares «planeta
del nivel `i − 1`, coste» terminada en `0`.

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

## Soluciones optimizadas

La solución optimizada en C++ analiza a mano los números con signo desde
un búfer de 4 KB que se rellena con `fread`, saltándose los separadores
`*` junto con los demás caracteres que no forman parte de un número, en
lugar de leer cada token en un `std::string` y convertirlo con
`std::stoi`; imprime con `printf`, así que no usa `iostream` en
absoluto. Su marca de planeta inalcanzable es 1 000 000, mayor que el
coste de cualquier ruta, ya que una ruta tiene menos de 30 enlaces de
como mucho 32 768 en valor absoluto: {1210_dp_optimized.cpp}.

La solución optimizada en Java lee la entrada en bloques de 4 KB y
analiza a mano los números con signo, saltándose los separadores `*`, en
lugar de partir las líneas en cadenas con `StringTokenizer`, y halla el
mínimo con un bucle simple en lugar de `Arrays.stream`. Su marca de
planeta inalcanzable es 1 000 000, mayor que el coste de cualquier ruta,
ya que una ruta tiene menos de 30 enlaces de como mucho 32 768 en valor
absoluto: {1210_dp_optimized.java}.

La solución optimizada en Python lee la entrada en trozos de 4 KB y
parte cada trozo en tokens, pasando al trozo siguiente solo un token
inacabado, en lugar de leer y partir toda la entrada de golpe, así que
la entrada nunca está entera en memoria; los tokens `*` se descartan
sobre la marcha: {1210_dp_optimized.py}.

La solución optimizada en Rust analiza a mano los números con signo
desde un búfer de 4 KB que se rellena desde la entrada estándar,
saltándose los separadores `*`, en lugar de leer toda la entrada en un
`String`, así que aparte de los costes de dos niveles solo ocupa memoria
ese búfer. Su marca de planeta inalcanzable es 1 000 000, mayor que el
coste de cualquier ruta, ya que una ruta tiene menos de 30 enlaces de
como mucho 32 768 en valor absoluto: {1210_dp_optimized.rs}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1210_dp_optimized.cpp`: reducción de tiempo +51.61%; reducción de
  memoria +65.62%; base: `1210_dp.cpp`.

- `1210_dp_optimized.java`: reducción de tiempo +22.14%; reducción de
  memoria +92.73%; base: `1210_dp.java`.

- `1210_dp_optimized.py`: reducción de tiempo +25.60%; reducción de
  memoria +83.15%; base: `1210_dp.py`.

- `1210_dp_optimized.rs`: reducción de tiempo +0.00%; reducción de
  memoria +74.86%; base: `1210_dp.rs`.

## Notas por lenguaje

En la clasificación del 2026-10-31, las siguientes implementaciones
básicas ya alcanzan los objetivos de tiempo y memoria. Se conservan sus
archivos en el conjunto básico; estos lenguajes no necesitan otra
implementación para alcanzar el objetivo.

- [1210_dp.go](1210_dp.go).

- Python y Rust filtran los `*` del flujo de entrada; los demás lenguajes
  los saltan en su lector de números.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1210_dp.cpp](1210_dp.cpp) | G++ 13.2 x64 | dp | O(L) | AC | 0.031 s | 384 KB | 11283629 |
| [1210_dp.go](1210_dp.go) | Go 1.14 x64 | dp | O(L) | AC | 0.031 s | 1220 KB | 11283633 |
| [1210_dp.java](1210_dp.java) | Java 1.8 | dp | O(L) | AC | 0.140 s | 5668 KB | 11283635 |
| [1210_dp.py](1210_dp.py) | Python 3.12 x64 | dp | O(L) | AC | 0.125 s | 3276 KB | 11283634 |
| [1210_dp.rs](1210_dp.rs) | Rust 1.75 x64 | dp | O(L) | AC | 0.046 s | 732 KB | 11283636 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1210_dp_optimized.cpp](1210_dp_optimized.cpp) | G++ 13.2 x64 | dp | O(L) | AC | 0.001 s | 132 KB | 11307238 |
| [1210_dp_optimized.java](1210_dp_optimized.java) | Java 1.8 | dp | O(L) | AC | 0.109 s | 412 KB | 11307239 |
| [1210_dp_optimized.py](1210_dp_optimized.py) \* | Python 3.12 x64 | dp | O(L) | AC | 0.093 s | 552 KB | 11307241 |
| [1210_dp_optimized.rs](1210_dp_optimized.rs) | Rust 1.75 x64 | dp | O(L) | AC | 0.046 s | 184 KB | 11307240 |

\* Aceptada; aún no cumple el objetivo de clasificación. Puede optimizarse más.
