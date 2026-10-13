# 1418. Historia militar

[Timus 1418](https://acm.timus.ru/problem.aspx?space=1&num=1418) · dificultad 1491 · geometry

Problema original de Alexey Lakhtin, del Campeonato de la Universidad Estatal de los Urales, 29 de octubre de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay N postes distintos en puntos enteros (3 ≤ N ≤ 4000, coordenadas de
0 a 10 000). Las vallas son polígonos simples de área no nula con
esquinas en postes; no deben tocarse ni cruzarse, y cada una debe estar
dentro de la siguiente. Hay que hallar el mayor número de vallas.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

N, luego N líneas con las coordenadas.

## Salida

El mayor número de vallas.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
100 100
200 100
100 200
300 300
```

Salida:

```
1
```

## Solución

Un poste en el borde de la envolvente convexa, en una esquina o en
medio de un lado, nunca puede quedar estrictamente dentro de un
polígono con esquinas en postes, porque ese polígono está dentro de la
envolvente. Así que solo la valla exterior puede usar esos postes, las
interiores usan solo postes estrictamente dentro de la envolvente, y
por inducción el número de vallas es como mucho el número de capas: se
quita todo el borde de la envolvente, luego el borde de la envolvente
del resto, y así mientras los postes que quedan tengan área positiva.
Las propias envolventes alcanzan esta cota, cada una estrictamente
dentro de la anterior.

Los postes se ordenan una vez; cada capa se halla luego con la cadena
monótona de Andrew en tiempo lineal, sacando de la pila solo en un giro
estricto a la derecha para que los postes de los lados sigan en la
cadena. Se para cuando quedan menos de tres postes o todos están en una
recta. `O(N²)` en el peor caso, que son N / 3 triángulos anidados.

Detalles a tener en cuenta:

- los postes en medio de los lados de la envolvente son de la capa
  exterior (prueba 09);
- los postes que quedan en una recta, o uno o dos postes sueltos, no
  forman valla (pruebas 02, 07, 08, gen4);
- en una cuadrícula densa cada lado de la envolvente tiene muchos postes
  (pruebas 06, 07, gen3).

## Notas por lenguaje

- Python se ejecuta con PyPy: 1333 triángulos anidados tardan unos 1,3 s
  con CPython y unos 0,2 s con PyPy.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1418_geometry.cpp](1418_geometry.cpp) | G++ 13.2 x64 | geometry | O(N^2) | AC | 0.062 s | 472 KB |
| [1418_geometry.go](1418_geometry.go) | Go 1.14 x64 | geometry | O(N^2) | AC | 0.093 s | 9556 KB |
| [1418_geometry.java](1418_geometry.java) | Java 1.8 | geometry | O(N^2) | AC | 0.234 s | 6280 KB |
| [1418_geometry.py](1418_geometry.py) | PyPy 3.10 x64 | geometry | O(N^2) | AC | 0.562 s | 7684 KB |
| [1418_geometry.rs](1418_geometry.rs) | Rust 1.75 x64 | geometry | O(N^2) | AC | 0.062 s | 552 KB |
