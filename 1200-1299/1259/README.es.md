# 1259. Cómo convertirse en estrella

[Timus 1259](https://acm.timus.ru/problem.aspx?space=1&num=1259) · dificultad 398 · math

Problema original de Pavel Egorov, de la Competición Abierta por Equipos de Programación para Escolares de la Región de Sverdlovsk, 11 de octubre de 2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se fija un ángulo α con 0 < α < π. Una poligonal empieza con el
segmento de (0, 0) a (1, 0); cada segmento siguiente es el anterior
girado α en sentido antihorario alrededor de su extremo libre. La
construcción para en cuanto la poligonal se cierra, y el resultado es
una estrella con tantos vértices como segmentos. ¿Cuántas estrellas
distintas tienen exactamente N vértices (3 ≤ N ≤ 100 000)?

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N.

## Salida

El número de estrellas con N vértices.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
```

Salida:

```
2
```

### Ejemplo 2

Entrada:

```
9
```

Salida:

```
3
```

## Solución

Girar un segmento α alrededor de su extremo lejano da un segmento que
apunta como el anterior girado β = α + π. Así que los segmentos son
vectores unitarios con ángulos 0, β, 2β, …, y la poligonal se cierra
tras k segmentos justo cuando su suma es cero:

```text
1 + e^{iβ} + … + e^{i(k−1)β} = 0  ⇔  e^{ikβ} = 1 y e^{iβ} ≠ 1
```

Cerrarse por primera vez tras N segmentos significa β = 2πm / N con
mcd(m, N) = 1. Como π < β < 2π, m recorre N/2 < m < N. Los números
coprimos con N van en parejas m y N − m, una a cada lado de N/2 (para
N ≥ 3 ninguno es igual a N/2), así que la respuesta es φ(N) / 2, con la
función φ de Euler calculada por división de prueba. `O(√N)`.

Detalles a tener en cuenta:

- solo valen giros entre π y 2π, así que la respuesta es la mitad de
  φ(N), no φ(N) entera (una estrella y su imagen especular son
  poligonales distintas, pero solo una gira en sentido antihorario un
  α < π);
- la estrella debe cerrarse por primera vez en N: los ángulos con
  mcd(m, N) > 1 se cierran antes y dan estrellas con menos vértices.

La fórmula se comparó para cada N de 3 a 299 con sumar los pasos
unitarios para cada ángulo candidato y ver cuándo la suma vuelve a cero
por primera vez.

## Notas por lenguaje

- Todos los lenguajes calculan la función de Euler por división de
  prueba.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1259_math.cpp](1259_math.cpp) | G++ 13.2 x64 | math | O(√N) | AC | 0.015 s | 128 KB |
| [1259_math.go](1259_math.go) | Go 1.14 x64 | math | O(√N) | AC | 0.031 s | 1076 KB |
| [1259_math.java](1259_math.java) | Java 1.8 | math | O(√N) | AC | 0.125 s | 1580 KB |
| [1259_math.py](1259_math.py) | Python 3.12 x64 | math | O(√N) | AC | 0.062 s | 424 KB |
| [1259_math.rs](1259_math.rs) | Rust 1.75 x64 | math | O(√N) | AC | 0.015 s | 224 KB |
