# 1084. La parte de un huerto cuadrado que alcanza una cabra atada

[Timus 1084](https://acm.timus.ru/problem.aspx?space=1&num=1084) · dificultad 150 · geometry

Problema original de Irina Danilina, de la Tercera Competición por Equipos de Programación para Escolares de la Región de Sverdlovsk, 4 de marzo de 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una cabra está atada con una cuerda de longitud `r` a una estaca en el
centro de un huerto cuadrado de lado `a` (ambos enteros de 1 a 100). Se
come todo lo que alcanza sin salir del huerto. Halla el área comida con
tres cifras tras el punto decimal.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`a` y `r`.

## Salida

El área comida.

## Evaluación

Los números se comparan con un error absoluto de 0.0011: las respuestas
se imprimen con tres decimales, así que la última cifra puede diferir en
uno.

## Ejemplos

### Ejemplo 1

Entrada:

```
10 6
```

Salida:

```
95.091
```

## Solución

La parte comida es la intersección del cuadrado con un círculo de radio
`r` alrededor de su centro. Sea `h = a/2`.

- `r ≤ h`: el círculo cabe dentro, y el área es `πr²`.
- `r² ≥ 2h²`: la cuerda llega a las esquinas, y se come todo el cuadrado
  `a²`.
- Si no, cada lado corta un segmento circular del círculo. Un segmento a
  distancia `h` del centro tiene área `r²·arccos(h/r) − h·√(r² − h²)`, y
  los cuatro segmentos no se solapan porque el círculo no llega a las
  esquinas. El área es `πr² − 4·segmento`.

`O(1)`.

Detalles a tener en cuenta:

- el caso intermedio necesita ambas cotas: con `r` al menos la mitad de la
  diagonal los segmentos se solaparían y la fórmula restaría de más;
- la prueba `r² ≥ 2h²` compara cuadrados y evita la raíz de 2.

Las respuestas se comprobaron con una integración numérica de la altura
comida `min(a, 2√(r² − x²))` sobre `x` con la regla de Simpson, partida
donde cambia la fórmula.

## Notas por lenguaje

- C++ toma `π` como `acos(-1)`, ya que `M_PI` no forma parte del C++
  estándar.
- Java da formato a la respuesta con `Locale.US` para obtener un punto
  decimal.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1084_geometry.cpp](1084_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 148 KB |
| [1084_geometry.go](1084_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1088 KB |
| [1084_geometry.java](1084_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.125 s | 1792 KB |
| [1084_geometry.py](1084_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.062 s | 376 KB |
| [1084_geometry.rs](1084_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.031 s | 268 KB |
