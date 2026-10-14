# 1577. Correo electrónico

[Timus 1577](https://acm.timus.ru/problem.aspx?space=1&num=1577) · dificultad 470 · dp

Problema original de Igor Chevdar, del USU Junior Contest (XIV Campeonato Abierto por Equipos de Programación para Escolares de la Región de Sverdlovsk), octubre de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un servidor acepta una cadena escrita si la contraseña real es una
subsecuencia suya. Vasya tiene dos contraseñas de letras minúsculas, de
hasta 2000 letras cada una, y quiere una cadena que acepten ambos
servidores. Hay que contar las cadenas distintas de la menor longitud
posible que contienen ambas contraseñas como subsecuencias, módulo
10⁹ + 7.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Las dos contraseñas, una por línea.

## Salida

El número de cadenas comunes más cortas módulo 10⁹ + 7.

## Ejemplos

### Ejemplo 1

Entrada:

```
b
ab
```

Salida:

```
1
```

### Ejemplo 2

Entrada:

```
abcab
cba
```

Salida:

```
4
```

## Solución

Son las supersecuencias comunes más cortas de las contraseñas a y b.
Para los sufijos a[i:] y b[j:] se guardan su menor longitud L(i, j) y el
número C(i, j) de cadenas distintas de esa longitud. Si a[i] = b[j],
toda cadena así empieza por esa letra, y el resto es una de las más
cortas para a[i+1:] y b[j+1:]. Si no, empieza por a[i] o por b[j], y el
resto es una de las más cortas para a[i+1:], b[j:] o para a[i:],
b[j+1:]. Las cadenas con primera letra distinta son distintas, así que
los números de las ramas que alcanzan la menor longitud simplemente se
suman; nada se cuenta dos veces.

Cuando un sufijo está vacío, la única respuesta es el otro sufijo. Las
filas se rellenan desde el final de las contraseñas hacia atrás, y la
fila i solo necesita la fila i + 1, así que bastan dos filas.
`O(|a|·|b|)`, unos 4·10⁶ pasos. Los resultados se contrastaron con
enumerar todas las cadenas de la menor longitud en 250 pares aleatorios
de contraseñas cortas.

Detalles a tener en cuenta:

- distintas maneras de intercalar pueden dar la misma cadena, como `aa`
  a partir de `a` y `a`, así que se cuentan cadenas y no maneras
  (pruebas 03, 05);
- contraseñas sin letras comunes dan todos los intercalados,
  C(|a| + |b|, |a|), lo que necesita el módulo (prueba gen4);
- Python se ejecuta con PyPy: las pruebas más grandes tardan unos
  1–2.5 s con CPython frente a un límite de 1 s, y unos 0.15 s con
  PyPy.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1577_dp.cpp](1577_dp.cpp) | G++ 13.2 x64 | dp | O(len(a) · len(b)) | AC | 0.031 s | 424 KB |
| [1577_dp.go](1577_dp.go) | Go 1.14 x64 | dp | O(len(a) · len(b)) | AC | 0.046 s | 1180 KB |
| [1577_dp.java](1577_dp.java) | Java 1.8 | dp | O(len(a) · len(b)) | AC | 0.187 s | 632 KB |
| [1577_dp.py](1577_dp.py) | PyPy 3.10 x64 | dp | O(len(a) · len(b)) | AC | 0.218 s | 8184 KB |
| [1577_dp.rs](1577_dp.rs) | Rust 1.75 x64 | dp | O(len(a) · len(b)) | AC | 0.031 s | 280 KB |
