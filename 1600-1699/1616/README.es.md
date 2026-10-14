# 1616. País Cuadrado 4

[Timus 1616](https://acm.timus.ru/problem.aspx?space=1&num=1616) · dificultad 3806 · geometry

Problema original de Vladimir Yakovlev (idea de Stanislav Vasilyev), del XII Campeonato de los Urales de Programación Competitiva, 29 de marzo de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un mapa del cuadrado [−n, n] × [−n, n] (1 ≤ n ≤ 30) muestra el dueño de
cada celda unitaria: una letra latina minúscula por dueño, `.` para el
Estado. Todas las tierras privadas están dentro de este cuadrado.
El eje x va a la derecha y el eje y hacia arriba. Luego los ejes de
coordenadas giran en sentido horario alrededor de (0, 0) α grados
(0 ≤ α ≤ 90, real), y cada celda unitaria de la nueva cuadrícula pasa al
dueño que tenía más de la mitad de su área antes del giro, o al Estado si
no hay ninguno. Imprime el nuevo mapa de [−2n, 2n] × [−2n, 2n] en el
mismo formato.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

n y α, luego 2n filas de 2n caracteres.

## Salida

4n filas de 4n caracteres.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 45.0
aaaa
aaaa
bb.x
bbx.
```

Salida:

```
........
........
...aa...
..aa.x..
..a..x..
...bb...
........
........
```

## Solución

Girar los ejes en sentido horario gira la tierra en sentido antihorario
en las nuevas coordenadas. Cada celda con dueño se convierte en un
cuadrado girado α; solo toca unas pocas celdas nuevas dentro de su
rectángulo envolvente. Recortar el cuadrado girado contra cada una de
esas celdas (cuatro semiplanos, como en el método de Sutherland–Hodgman)
da el polígono de intersección, y la fórmula del área de Gauss da su
área, que se suma a la parte de ese dueño en la celda. Una celda pasa al
dueño cuya parte supera 1/2 en más de 10⁻⁹. Con a lo sumo 3 600 celdas
con dueño esto es instantáneo. `O(n²)`.

Detalles a tener en cuenta:

- una parte de exactamente la mitad no es más de la mitad: esas celdas
  pasan al Estado (las celdas cortadas del ejemplo a 45 grados);
- con α = 0 y α = 90 las celdas caen exactamente sobre celdas, y los
  bordes que solo se tocan no deben sumar área (pruebas 02, 03);
- los radianes se calculan como α · π / 180 en todos los lenguajes; Rust
  usa `sin_cos`, mientras que las otras soluciones llaman al seno y al
  coseno por separado.

Las salidas coinciden con una implementación aceptada independiente en
150 mapas aleatorios.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1616_geometry.cpp](1616_geometry.cpp) | G++ 13.2 x64 | geometry | O(n²) | AC | 0.031 s | 3564 KB |
| [1616_geometry.go](1616_geometry.go) | Go 1.14 x64 | geometry | O(n²) | AC | 0.046 s | 8724 KB |
| [1616_geometry.java](1616_geometry.java) | Java 1.8 | geometry | O(n²) | AC | 0.187 s | 9704 KB |
| [1616_geometry.py](1616_geometry.py) | Python 3.12 x64 | geometry | O(n²) | AC | 0.359 s | 5252 KB |
| [1616_geometry.rs](1616_geometry.rs) | Rust 1.75 x64 | geometry | O(n²) | AC | 0.031 s | 3040 KB |
