# 1412. Temporada de otoño

[Timus 1412](https://acm.timus.ru/problem.aspx?space=1&num=1412) · dificultad 1505 · geometry

Problema original de Pavel Egorov, del Campeonato de la Universidad Estatal de los Urales, 29 de octubre de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

La lluvia cae en vertical, 1 mm por minuto, sobre un campo rectangular
con esquinas (0, 0), (0, W), (L, 0) y (L, W) (1 ≤ W, L ≤ 10 000). N
personas (1 ≤ N ≤ 1000) están en puntos dados (|X|, |Y| ≤ 10 000), cada una
bajo un paraguas con forma de semiesfera superior de radio 1 m. El agua
de un paraguas baja por el camino más corto sobre la semiesfera y cae
desde el borde. Los paraguas no se solapan, y unos postes altos en las
esquinas del campo impiden que un paraguas cubra una esquina. Hay que
imprimir la cantidad de lluvia que llega al campo por minuto, con 3
cifras tras el punto.

Límite de tiempo: 0.5 segundos. Límite de memoria: 64 MB.

## Entrada

W y L, luego N, luego N líneas con X e Y.

## Salida

La cantidad de lluvia sobre el campo.

## Ejemplos

### Ejemplo 1

Entrada:

```
10 10
2
0.5 2
2 10.1
```

Salida:

```
99.666
```

## Solución

El camino más corto de un punto de la semiesfera a su borde sigue el
meridiano, así que la lluvia que cae sobre el disco del paraguas en el
ángulo θ sale del borde en el mismo ángulo θ: las π unidades que recoge
un paraguas se reparten por igual a lo largo del borde. Sin paraguas el
campo recibe W·L, y cada paraguas lo cambia en π por la parte de su
borde sobre el campo menos el área de su disco sobre el campo.

El área del disco unidad dentro del rectángulo es la suma, sobre los
cuatro lados, del área con signo del disco dentro del triángulo que va
del centro al lado: el lado se corta donde toca la circunferencia, un
trozo dentro del círculo suma su triángulo y uno fuera suma su sector.
La parte del borde sale de cortar la circunferencia en los ángulos donde
toca las cuatro rectas del contorno y comprobar el punto medio de cada
arco. `O(N)`.

Detalles a tener en cuenta:

- pese a la palabra «promedio» del enunciado, el número esperado es el
  total sobre el campo, W·L si nada interfiere (pruebas 03, 05);
- X va a lo largo de L, el segundo número, e Y a lo largo de W; un caso
  del foro solo cuadra con esta lectura (pruebas 02, 10);
- los puntos de tangencia cortan los arcos del borde, y la prueba del
  punto medio de cada segmento en el disco es estricta (pruebas 11, 12);
- un paraguas fuera del campo puede dejar caer agua dentro (prueba 08).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1412_geometry.cpp](1412_geometry.cpp) | G++ 13.2 x64 | geometry | O(N) | AC | 0.031 s | 236 KB |
| [1412_geometry.go](1412_geometry.go) | Go 1.14 x64 | geometry | O(N) | AC | 0.031 s | 1404 KB |
| [1412_geometry.java](1412_geometry.java) | Java 1.8 | geometry | O(N) | AC | 0.125 s | 2164 KB |
| [1412_geometry.py](1412_geometry.py) | Python 3.12 x64 | geometry | O(N) | AC | 0.078 s | 796 KB |
| [1412_geometry.rs](1412_geometry.rs) | Rust 1.75 x64 | geometry | O(N) | AC | 0.046 s | 280 KB |
