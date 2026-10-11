# 1306. Mediana de una sucesión

[Timus 1306](https://acm.timus.ru/problem.aspx?space=1&num=1306) · dificultad 145 · sorting

Problema original del Segundo Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 3–4 de abril de 1998.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay que hallar la mediana de N ≤ 250 000 enteros de 0 a 2³¹ − 1: el
elemento central de la sucesión ordenada si N es impar, y la media de
los dos centrales si N es par. Se imprime con un decimal.

Límite de tiempo: 1 segundo. Límite de memoria: 1 MB. El enunciado
admite C, C++ y Pascal; el formulario de envío ofrece además Rust.

## Entrada

N y luego los N números, uno por línea.

## Salida

La mediana con un decimal.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
3
6
4
5
```

Salida:

```
4.5
```

## Solución

La sucesión entera ocupa 250 000 · 4 bytes, alrededor de 1 MB, que es
todo el límite de memoria. Pero solo importa la mitad menor: la mediana
es el mayor, o la media de los dos mayores, de los ⌊N/2⌋ + 1 números más
pequeños.

Así que un montículo de máximo guarda los ⌊N/2⌋ + 1 números más
pequeños vistos hasta ahora, unos 500 KB. Cada número nuevo entra
mientras el montículo no está lleno, o sustituye a la cima si es menor
que ella. Al final:

- con N impar la cima es la mediana;
- con N par la cima y, tras sacarla, la nueva cima son los dos
  elementos centrales.

`O(N log N)` en tiempo y `O(N / 2)` en memoria.

Detalles a tener en cuenta:

- dos números cerca de 2³¹ − 1 desbordan incluso una suma sin signo de
  32 bits, así que la suma se hace en 64 bits (pruebas 03 y 04);
- la media es entera o termina en .5, así que se imprime exacta, sin
  coma flotante (pruebas 01 y 08);
- aquí los flujos de C++ gastan demasiada memoria, así que el programa
  lee con `scanf`.

## Notas por lenguaje

- El enunciado solo admite C, C++ y Pascal, pero el formulario de envío
  de Timus ofrece además Rust 1.75, así que hay soluciones en C++ y Rust;
  Go, Python y Java no se pueden enviar.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1306_sorting.cpp](1306_sorting.cpp) | G++ 13.2 x64 | sorting | O(N log N) | AC | 0.203 s | 624 KB |
| [1306_sorting.rs](1306_sorting.rs) | Rust 1.75 x64 | sorting | O(N log N) | AC | 0.031 s | 696 KB |
