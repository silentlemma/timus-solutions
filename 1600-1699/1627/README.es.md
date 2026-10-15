# 1627. Unir

[Timus 1627](https://acm.timus.ru/problem.aspx?space=1&num=1627) · dificultad 1093 · math

Problema original del SPbSU ITMO Contest en el campus de Petrozavodsk, invierno de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una casa es una cuadrícula de n × m habitaciones (1 ≤ n, m ≤ 9), cada
una dormitorio `.` o despensa `*`, con al menos un dormitorio. Las
puertas pueden unir dormitorios que comparten pared. Cuenta las maneras
de poner puertas para que entre dos dormitorios cualesquiera haya
exactamente un camino, módulo 10⁹.

Límite de tiempo: 4 segundos. Límite de memoria: 64 MB.

## Entrada

n y m, luego las n filas del mapa.

## Salida

El número de maneras módulo 10⁹.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 2
..
..
```

Salida:

```
4
```

### Ejemplo 2

Entrada:

```
2 2
*.
.*
```

Salida:

```
0
```

## Solución

Exactamente un camino entre dos dormitorios cualesquiera significa que
las puertas forman un árbol generador del grafo de dormitorios. Por el
teorema de la matriz y el árbol de Kirchhoff, el número de árboles
generadores es el determinante del laplaciano (grados en la diagonal, −1
por cada par de vecinos) sin una fila y una columna; para un grafo no
conexo vale 0. Con hasta 81 dormitorios es un determinante de 80 × 80.

El conteo se pide módulo 10⁹, que no es primo, así que la eliminación
ordinaria módulo 10⁹ no puede dividir por un pivote. El algoritmo de
Euclides sobre filas sí: para anular una entrada bajo el pivote, se resta
de la fila del pivote el múltiplo adecuado de esa fila y se intercambian
ambas, como en un mcd, hasta que la entrada sea 0. Solo se usan resta,
multiplicación e intercambios, así que todo vale módulo 10⁹; cada
intercambio cambia el signo. `O(v³ log M)` para v dormitorios. Python usa
en su lugar Bareiss: `O(v³)` operaciones con enteros grandes y divisiones
exactas, y luego toma el resto.

Detalles a tener en cuenta:

- los dormitorios que solo se tocan en una esquina no están unidos: 0
  (el segundo ejemplo);
- un solo dormitorio tiene una manera, el conjunto vacío de puertas
  (prueba 03).

Las respuestas coinciden con una implementación aceptada independiente
en 160 casas aleatorias.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1627_math.cpp](1627_math.cpp) | G++ 13.2 x64 | math | O(v³ log M) | AC | 0.015 s | 460 KB |
| [1627_math.go](1627_math.go) | Go 1.14 x64 | math | O(v³ log M) | AC | 0.015 s | 1200 KB |
| [1627_math.java](1627_math.java) | Java 1.8 | math | O(v³ log M) | AC | 0.125 s | 1744 KB |
| [1627_math.py](1627_math.py) | Python 3.12 x64 | math | O(v³) | AC | 0.125 s | 660 KB |
| [1627_math.rs](1627_math.rs) | Rust 1.75 x64 | math | O(v³ log M) | AC | 0.046 s | 292 KB |
