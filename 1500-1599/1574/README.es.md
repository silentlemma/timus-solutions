# 1574. Matemáticos y paréntesis

[Timus 1574](https://acm.timus.ru/problem.aspx?space=1&num=1574) · dificultad 353 · strings

Problema original de Alexander Toropov, del USU Junior Contest (XIV Campeonato Abierto por Equipos de Programación para Escolares de la Región de Sverdlovsk), octubre de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dada una línea no vacía de hasta 100000 paréntesis, hay que contar los
desplazamientos cíclicos, de 0 a n − 1 caracteres, que la convierten en
una secuencia correcta de paréntesis. Los desplazamientos de distinta
cantidad cuentan por separado aunque den la misma línea.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

La línea de paréntesis.

## Salida

El número de esos desplazamientos.

## Ejemplos

### Ejemplo 1

Entrada:

```
)(()
```

Salida:

```
1
```

### Ejemplo 2

Entrada:

```
)()(
```

Salida:

```
2
```

### Ejemplo 3

Entrada:

```
()
```

Salida:

```
1
```

## Solución

Si los números de paréntesis de apertura y de cierre difieren, ningún
desplazamiento sirve. Si no, se toma el balance tras cada prefijo:
aperturas menos cierres. Un desplazamiento que empieza justo tras la
posición i cambia cada balance en −p(i), donde p(i) es el balance ahí,
así que nunca baja de cero exactamente cuando p(i) es el menor de todos
los balances. La respuesta es el número de prefijos cuyo balance es ese
mínimo. `O(n)`.

Detalles a tener en cuenta:

- una línea como `)()(` da la misma línea correcta con dos
  desplazamientos distintos, y ambos cuentan (el segundo ejemplo);
- el desplazamiento por cero también cuenta (el tercer ejemplo);
- una línea desequilibrada solo tiene la respuesta 0, aunque algún
  desplazamiento mantenga todos los balances no negativos
  (pruebas 04, 05).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1574_strings.cpp](1574_strings.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.031 s | 500 KB |
| [1574_strings.go](1574_strings.go) | Go 1.14 x64 | strings | O(n) | AC | 0.031 s | 1768 KB |
| [1574_strings.java](1574_strings.java) | Java 1.8 | strings | O(n) | AC | 0.125 s | 1196 KB |
| [1574_strings.py](1574_strings.py) | Python 3.12 x64 | strings | O(n) | AC | 0.093 s | 5252 KB |
| [1574_strings.rs](1574_strings.rs) | Rust 1.75 x64 | strings | O(n) | AC | 0.046 s | 2068 KB |
