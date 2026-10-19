# 2001. Mathematicians and Berries

[Timus 2001](https://acm.timus.ru/problem.aspx?space=1&num=2001) · dificultad 22 · math

Problema original de Oleg Merkurev. (Prepared by Kirill Devyatkin), del Concurso Regional Escolar de Programación de los Urales 2013.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se pesan dos cestas tres veces. Al principio cada una contiene sus
propias bayas. Después se pasan todas las bayas de la segunda a la
primera y se pesan ambas. Finalmente se pasa todo el contenido de la
primera a la segunda y se repite. Recuperar las masas iniciales de
bayas, con masas constantes de las cestas.

## Entrada

Tres parejas cronológicas `a1 b1`, `a2 b2`, `a3 b3`, con lecturas
enteras de 0 a 10000 que corresponden a las transferencias. Tiempo 0,5
segundos y memoria 64 MB.

## Salida

Las masas iniciales de bayas de la primera y segunda cesta, en ese orden.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
1 2
2 1
0 3
```

```
1 1
```

La primera cesta está vacía en la última lectura, pesando 0. La segunda
está vacía en la intermedia, pesando 1. Restar esas masas de las
lecturas iniciales 1 y 2 da 1 y 1.

## Solución

Sean `c,d` las masas vacías y `x,y` las bayas iniciales. Entonces
`a1=c+x`, `b1=d+y`. Al vaciar la segunda, `b2=d`; al vaciar la primera,
`a3=c`. La respuesta única es `x=a1−a3`, `y=b1−b2`.

Sustituir demuestra que ambas diferencias son exactamente los contenidos
iniciales. Las otras lecturas cumplen `a2=c+x+y`, `b3=d+x+y`: se
consumen de la entrada pero no hacen falta para recuperar. No hay
división, búsqueda ni redondeo.

Tiempo `O(1)` y memoria `O(1)` para seis lecturas fijas. Las diferencias
válidas están entre 0 y 10000, dentro de 32 bits con signo.

Restar la misma cesta vacía: `a3` para la primera y `b2` para la
segunda. Las lecturas combinadas `a2,b3` aún incluyen una cesta.
Mantener el orden de salida y aceptar masas nulas sin casos especiales.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2001_math.cpp](2001_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 396 KB |
| [2001_math.go](2001_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1088 KB |
| [2001_math.java](2001_math.java) | Java 1.8 | math | O(1) | AC | 0.156 s | 388 KB |
| [2001_math.py](2001_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.093 s | 384 KB |
| [2001_math.rs](2001_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 228 KB |
