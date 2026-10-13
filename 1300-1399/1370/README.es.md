# 1370. Mago

[Timus 1370](https://acm.timus.ru/problem.aspx?space=1&num=1370) · dificultad 88 · implementation

Problema original de Stanislav Vasiliev, del Noveno Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 19–24 de abril de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una rueda lleva N cifras en el borde, 11 ≤ N ≤ 1000, y una ventanilla
muestra 10 seguidas, al principio de la 1.ª a la 10.ª. Cada chasquido
gira la rueda una cifra, así que tras un chasquido la ventanilla muestra
de la 2.ª a la 11.ª. Dados M ≤ 32 767 chasquidos, hay que imprimir las
10 cifras de la ventanilla.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y M, luego las N cifras, una por línea.

## Salida

Las 10 cifras de la ventanilla, con sus ceros a la izquierda.

## Ejemplos

### Ejemplo 1

Entrada:

```
12 7
1
2
3
4
5
6
7
8
9
0
7
7
```

Salida:

```
8907712345
```

## Solución

Tras M chasquidos la ventanilla empieza en la cifra M (contando desde
0), y la rueda da la vuelta, así que la respuesta son las cifras
(M + i) mod N para i = 0 … 9. `O(1)` tras leer la entrada.

Detalles a tener en cuenta:

- M puede ser muchas veces mayor que N (prueba 05);
- la ventanilla puede pasar de la última cifra a la primera (ejemplo);
- la respuesta se imprime como cifras, con sus ceros a la izquierda
  (prueba 03).

## Notas por lenguaje

- Las cinco soluciones guardan las cifras como texto y unen las diez de
  la ventanilla.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1370_implementation.cpp](1370_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.015 s | 196 KB |
| [1370_implementation.go](1370_implementation.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.015 s | 1108 KB |
| [1370_implementation.java](1370_implementation.java) | Java 1.8 | implementation | O(1) | AC | 0.125 s | 1892 KB |
| [1370_implementation.py](1370_implementation.py) | Python 3.12 x64 | implementation | O(1) | AC | 0.062 s | 404 KB |
| [1370_implementation.rs](1370_implementation.rs) | Rust 1.75 x64 | implementation | O(1) | AC | 0.015 s | 244 KB |
