# 1656. El ejército del Reino Lejano

[Timus 1656](https://acm.timus.ru/problem.aspx?space=1&num=1656) · dificultad 206 · constructive

Problema original de Vladimir Yakovlev (idea de Magaz Asanov), del cuarto de final de la subregión oriental del NEERC 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay que colocar n² soldados de alturas dadas en un cuadrado de n × n de
modo que en cada fila y cada columna el más alto esté en el medio y las
alturas no crezcan del medio hacia ningún extremo.

## Entrada

Un n impar de 3 a 9 y luego n² alturas de 170 a 200.

## Salida

El cuadrado, n filas de n alturas. Se acepta cualquier disposición
válida.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
170
170
180
175
170
175
175
170
175
```

Salida:

```
170 175 170
175 180 175
170 175 170
```

## Solución

Se ordenan las casillas por el par (menor, mayor) de sus distancias a la
fila central y a la columna central, y los soldados más altos van a los
rangos más bajos. En una fila a distancia a del centro, una casilla a
distancia b tiene rango (b, a) mientras b < a y (a, b) desde ahí: de
cualquier modo el rango crece con b, así que a cada lado del medio las
alturas no aumentan hacia fuera. Las columnas, igual por simetría. Las
casillas de igual rango son imágenes especulares y nunca quedan del mismo
lado de una misma línea. `O(n² log n)`.

Detalles a tener en cuenta:

- «no crecer hacia los extremos» permite alturas iguales (prueba 02);
- hay muchas disposiciones válidas, así que un verificador comprueba las
  reglas y el conjunto de alturas.

Los cuadrados del programa pasan el verificador en 90 ejércitos
aleatorios.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1656_constructive.cpp](1656_constructive.cpp) | G++ 13.2 x64 | constructive | O(n² log n) | AC | 0.015 s | 200 KB |
| [1656_constructive.go](1656_constructive.go) | Go 1.14 x64 | constructive | O(n² log n) | AC | 0.031 s | 1152 KB |
| [1656_constructive.java](1656_constructive.java) | Java 1.8 | constructive | O(n² log n) | AC | 0.156 s | 4188 KB |
| [1656_constructive.py](1656_constructive.py) | Python 3.12 x64 | constructive | O(n² log n) | AC | 0.078 s | 448 KB |
| [1656_constructive.rs](1656_constructive.rs) | Rust 1.75 x64 | constructive | O(n² log n) | AC | 0.015 s | 240 KB |
