# 1294. Satélites marcianos

[Timus 1294](https://acm.timus.ru/problem.aspx?space=1&num=1294) · dificultad 316 · geometry

Problema original de Vladimir Yakovlev, de la Novena Competición Abierta por Equipos de Programación para Escolares, 13 de marzo de 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cuatro satélites A, B, C y D están en una misma órbita circular, en
este orden. Se conocen las distancias AD, AC, BD y BC en miles de
kilómetros (enteros de 1 a 10 000); el radio de la órbita no. Hay que
hallar la distancia CD en kilómetros, redondeada a entero, o indicar
que no se puede determinar de forma única.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

AD, AC, BD y BC.

## Salida

`Distance is X km.` o `Impossible.`

## Ejemplos

### Ejemplo 1

Entrada:

```
4 7 5 7
```

Salida:

```
Distance is 5385 km.
```

## Solución

Sean a = AD, b = AC, c = BD, d = BC y x = CD. Los puntos A y B están en
el mismo arco que corta la cuerda CD, así que la ven con el mismo
ángulo inscrito t. El teorema del coseno en los triángulos ACD y BCD da

x² = a² + b² − 2ab cos t = c² + d² − 2cd cos t,

dos ecuaciones en x² y cos t. Por tanto

cos t = (a² + b² − c² − d²) / (2 (ab − cd)),

x² = (ab (c² + d²) − cd (a² + b²)) / (ab − cd).

- Si ab = cd, las ecuaciones o se contradicen o no dicen nada sobre t.
  En el segundo caso, por ejemplo un trapecio isósceles, CD de verdad
  puede tomar muchos valores (prueba 02). En ambos casos la respuesta es
  `Impossible.` (pruebas 02 y 03).
- Si |a² + b² − c² − d²| > 2 |ab − cd|, el coseno saldría de [−1, 1] y
  no existe tal órbita, así que la respuesta vuelve a ser
  `Impossible.` (prueba 04).
- Si no, x = 1000 · √x² kilómetros, redondeado.

Las dos comprobaciones usan enteros exactos de 64 bits (todos los
productos quedan por debajo de 2 · 10¹⁶). Solo la última raíz cuadrada
se calcula en coma flotante. `O(1)`.

La fórmula se comprobó en 100 000 cuadriláteros cíclicos aleatorios,
en ambas orientaciones: reprodujo CD con un error relativo de 10⁻¹⁰.

Detalles a tener en cuenta:

- los datos están en miles de kilómetros y la respuesta en kilómetros
  (prueba 01);
- AD · AC = BD · BC no siempre significa datos contradictorios: a veces
  significa muchas respuestas (pruebas 02 y 03).

## Notas por lenguaje

- El `round` de Python lleva las mitades al par más cercano, así que la
  solución en Python usa floor(x + 0.5), que redondea las mitades hacia
  arriba como hacen los otros cuatro lenguajes con números positivos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1294_geometry.cpp](1294_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 148 KB |
| [1294_geometry.go](1294_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.015 s | 1088 KB |
| [1294_geometry.java](1294_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.109 s | 1632 KB |
| [1294_geometry.py](1294_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.093 s | 472 KB |
| [1294_geometry.rs](1294_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.015 s | 236 KB |
