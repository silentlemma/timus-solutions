# 1766. Humpty Dumpty

[Timus 1766](https://acm.timus.ru/problem.aspx?space=1&num=1766) · dificultad 1373 · math

Problema original de Sergey Pupyrev (preparado por Eugene Krokhalev), del XIV Campeonato de los Urales de Programación Competitiva, 10 de abril de 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada casilla de un tablero de 8 × 8 tiene un número de 1 a 1000. Un
caminante pasa cada segundo a una de las hasta ocho casillas que
comparten un lado o una esquina con la suya, eligiendo cada una con
probabilidad proporcional a su número. Tras un tiempo enorme (100100100
días), hallar la probabilidad de encontrar al caminante en cada
casilla.

## Entrada

Ocho líneas de ocho números, empezando por la primera fila.

## Salida

Ocho líneas de ocho probabilidades en el mismo orden, con un error de
a lo sumo 10⁻¹². La respuesta del ejemplo está impresa a propósito con
demasiado poca precisión.

## Ejemplos

### Ejemplo 1

Entrada:

```
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
```

Salida:

```
0.007 0.012 0.012 0.012 0.012 0.012 0.012 0.007
0.012 0.019 0.019 0.019 0.019 0.019 0.019 0.012
0.012 0.019 0.019 0.019 0.019 0.019 0.019 0.012
0.012 0.019 0.019 0.019 0.019 0.019 0.019 0.012
0.012 0.019 0.019 0.019 0.019 0.019 0.019 0.012
0.012 0.019 0.019 0.019 0.019 0.019 0.019 0.012
0.012 0.019 0.019 0.019 0.019 0.019 0.019 0.012
0.007 0.012 0.012 0.012 0.012 0.012 0.012 0.007
```

## Solución

Sea w(u) el número de la casilla u y W(u) la suma de los números a su
alrededor. El caminante va de u a una vecina v con probabilidad
w(v)/W(u). Dar a cada casilla el peso π(u) = w(u)·W(u) equilibra cada
par de vecinas: π(u)·w(v)/W(u) = w(u)·w(v) = π(v)·w(u)/W(v). Así estos
pesos, normalizados para sumar 1, forman una distribución que un paso
deja igual. Desde cada casilla se llega a cualquier otra, y tres
casillas vecinas entre sí hacen el paseo aperiódico, así que desde
cualquier inicio se asienta en esta única distribución, y tras tanto
tiempo no queda otra cosa. Los pesos son enteros y solo se divide al
final. `O(64)`.

Con todos los números iguales, π es proporcional al número de vecinas:
3 en una esquina, 5 en un borde y 8 dentro, 420 en total, así que una
esquina recibe 3/420 ≈ 0,00714 y una casilla interior 8/420 ≈ 0,01905.

Trampas:

- la casilla inicial no importa, una vez asentado el paseo;
- 15 cifras decimales mantienen el error muy por debajo de 10⁻¹²;
- simular el paseo paso a paso converge despacio cuando se mezclan
  números 1 y 1000.

El verificador calcula la distribución exacta a partir de la entrada
con fracciones. Resolver exactamente las ecuaciones de equilibrio con
fracciones da la misma distribución en seis tableros aleatorios, y
20000 pasos del paseo coinciden en tableros con números aleatorios.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1766_math.cpp](1766_math.cpp) | G++ 13.2 x64 | math | O(64) | AC | 0.015 s | 140 KB |
| [1766_math.go](1766_math.go) | Go 1.14 x64 | math | O(64) | AC | 0.031 s | 1128 KB |
| [1766_math.java](1766_math.java) | Java 1.8 | math | O(64) | AC | 0.140 s | 1944 KB |
| [1766_math.py](1766_math.py) | Python 3.12 x64 | math | O(64) | AC | 0.078 s | 504 KB |
| [1766_math.rs](1766_math.rs) | Rust 1.75 x64 | math | O(64) | AC | 0.046 s | 276 KB |
