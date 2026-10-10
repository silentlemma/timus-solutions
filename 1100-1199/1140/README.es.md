# 1140. El camino más corto de vuelta al centro de una cuadrícula hexagonal tras un paseo

[Timus 1140](https://acm.timus.ru/problem.aspx?space=1&num=1140) · dificultad 381 · geometry

Problema original del cuarto de final de la región central de Rusia, Rybinsk, 17–18 de octubre de 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un pantano está dividido en celdas hexagonales, y tres de las seis
direcciones entre celdas vecinas se llaman `X`, `Y` y `Z`, con `Y` entre
`X` y `Z`. Un estudiante empieza en la celda central y recorre hasta 32000
tramos rectos, cada uno dado por una dirección y una longitud con signo
no nula; una longitud negativa va en sentido contrario. El estudiante
nunca se aleja más de 100 celdas del centro. Describe un camino de vuelta
al centro por el menor número de celdas, en el mismo formato.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`n` y luego `n` líneas con la letra de la dirección y una longitud con
signo.

## Salida

El número de tramos `m ≥ 0` del camino de vuelta y luego los tramos.

## Evaluación

Se acepta cualquier camino más corto. El comprobador verifica el formato,
que el camino acaba en el centro y que su longitud total es igual a la
distancia hexagonal desde la última celda.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
Z -2
Y 3
Z 3
X -1
```

Salida:

```
2
Y -2
Z -2
```

## Solución

En una cuadrícula hexagonal la dirección del medio es la suma de las otras
dos: un paso por `Y` lleva a la misma celda que un paso por `X` seguido de
uno por `Z`. Así que se suman las longitudes por dirección y el final del
paseo se escribe como `a·X + b·Z`, con `a = X + Y` y `b = Z + Y`. Un camino
de vuelta con `m` pasos por `Y` necesita además `a − m` por `X` y `b − m`
por `Z`, hacia atrás, y tiene `|a − m| + |m| + |b − m|` pasos. Una suma de
distancias de `m` a los puntos `a`, `0` y `b` es mínima en su mediana, así
que se toma `m` como la mediana de `a`, `0` y `b` y se imprimen las partes
no nulas de `X −(a − m)`, `Y −m`, `Z −(b − m)`. `O(n)`.

Detalles a tener en cuenta:

- cuando `a` y `b` tienen el mismo signo, parte del camino va por `Y`;
  cuando los signos difieren, `m = 0` y `Y` no se usa;
- no se permiten tramos de longitud cero, así que se descartan, y la
  respuesta puede tener `0` tramos;
- puede haber varios caminos más cortos; se acepta cualquiera.

Las respuestas se comprobaron con el comprobador en todas las pruebas y en
200 paseos aleatorios; la fórmula de distancia del comprobador se comparó
con una búsqueda en anchura sobre todas las celdas a 100 o menos del
centro.

## Notas por lenguaje

- Todos los lenguajes suman las longitudes y toman la misma mediana.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1140_geometry.cpp](1140_geometry.cpp) | G++ 13.2 x64 | geometry | O(n) | AC | 0.015 s | 188 KB |
| [1140_geometry.go](1140_geometry.go) | Go 1.14 x64 | geometry | O(n) | AC | 0.031 s | 1348 KB |
| [1140_geometry.java](1140_geometry.java) | Java 1.8 | geometry | O(n) | AC | 0.093 s | 828 KB |
| [1140_geometry.py](1140_geometry.py) | Python 3.12 x64 | geometry | O(n) | AC | 0.125 s | 776 KB |
| [1140_geometry.rs](1140_geometry.rs) | Rust 1.75 x64 | geometry | O(n) | AC | 0.015 s | 344 KB |
