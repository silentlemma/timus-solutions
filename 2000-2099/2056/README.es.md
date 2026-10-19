# 2056. Determinar la categoría de beca

[Timus 2056](https://acm.timus.ru/problem.aspx?space=1&num=2056) · difficulty 41 · implementation

Problema popular, del Campeonato de Programación Deportiva de los Urales 2015.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un estudiante aprobó n exámenes con notas de 3 a 5. Indicar la beca:
`None` si hay algún 3; si no, `Named` si todas las notas son 5; si no,
`High` si la media es al menos 4,5; y `Common` en los demás casos. Los
límites son 1 segundo y 64 MB.

## Entrada

El número de exámenes n, 1 ≤ n ≤ 10, y después n líneas con una nota
cada una.

## Salida

Una palabra, respetando mayúsculas.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
3
5
5
4
```

```
High
```

```
3
3
3
3
```

```
None
```

En el primero la suma es catorce y `2·14≥9·3`, por lo que el promedio
supera 4,5. No hay tres, pero tampoco son todas cinco: corresponde
`High`. En el segundo hay tres y la regla prioritaria determina `None`.

## Solución

Recorremos las notas guardando suma `S` y mínimo `q`, inicialmente cero
y cinco. Tras cada prefijo son exactamente su suma y mínimo: añadimos la
nueva nota y la comparamos con el mínimo previo. Al terminar, `q=3`
equivale a que exista un tres. En ese caso imprimimos `None` antes de
examinar el promedio.

Si no, `q=5` equivale a que todas sean cinco, pues cinco es el máximo
permitido, y se imprime `Named`. Si ninguna prueba se cumple, solo
quedan cuatros y cincos, con al menos un cuatro. Como `n>0`, `S/n≥4.5`
equivale a la comparación entera exacta `2S≥9n`. Si se cumple imprimimos
`High`; en otro caso, `Common`. Las condiciones reproducen las cuatro
reglas en el orden requerido, son excluyentes y exhaustivas, demostrando
corrección.

Un tres anula la beca incluso con promedio alto. Todas cinco requieren
`Named`, no `High`. El umbral incluye igualdad: cuatro y cinco dan
`High`. No truncar el promedio mediante división entera. Con un solo
examen, tres, cuatro y cinco corresponden a `None`, `Common` y `Named`.
Mantener las mayúsculas exactas.

## Notas por lenguaje

Un recorrido cuesta `O(n)` tiempo y `O(1)` estado de trabajo. Python y
Rust conservan además `O(n)` texto o tokens de entrada; los demás leen
con buffer. Toda la aritmética es entera: `S≤50`, `2S≤100`, `9n≤90`. Los
cinco usan las mismas tres estadísticas; Python se ejecuta en CPython
3.12. No se necesita división flotante.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2056_implementation.cpp](2056_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 420 KB |
| [2056_implementation.go](2056_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.046 s | 1096 KB |
| [2056_implementation.java](2056_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.109 s | 452 KB |
| [2056_implementation.py](2056_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.078 s | 472 KB |
| [2056_implementation.rs](2056_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.015 s | 224 KB |
