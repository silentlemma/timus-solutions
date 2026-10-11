# 1294. Satélites marcianos

[Timus 1294](https://acm.timus.ru/problem.aspx?space=1&num=1294) · dificultad 317 · geometry

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
- Si |a² + b² − c² − d²| ≥ 2 |ab − cd|, no existe un triángulo no
  degenerado: la igualdad también falla, porque tres puntos distintos
  de una circunferencia no pueden ser colineales (pruebas 04 y 07).
- El teorema de Ptolomeo exige AB · CD = bc − ad > 0 para el orden dado.
  Si bc ≤ ad, la respuesta es `Impossible.` (pruebas 05 y 07). Junto con
  la cota estricta del coseno, esta comprobación garantiza el orden
  correcto de los puntos reconstruidos.
- Si no, x = 1000 · √x² kilómetros, redondeado.

Todas las comprobaciones de existencia usan enteros exactos de 64 bits
(los productos originales son menores que 2 · 10¹⁶). Se normalizan el
numerador y el denominador para que sean positivos. Una raíz cuadrada
en coma flotante estima la parte entera m de la distancia en kilómetros;
se redondea hacia arriba exactamente si
(2m + 1)² ≤ floor(4 · 1000² · num / den). Para evitar desbordamientos,
se calcula la cota como s · (num div den) + (s · (num mod den)) div den,
donde s = 4 · 1000². Los nuevos valores intermedios son menores que
2 · 10¹⁵. El tiempo y el espacio auxiliar son `O(1)`.

Las comprobaciones corregidas y los resultados redondeados se verifican
con un oráculo exacto independiente basado en el teorema de Ptolomeo,
los ángulos opuestos y las desigualdades estrictas del triángulo.

Detalles a tener en cuenta:

- los datos están en miles de kilómetros y la respuesta en kilómetros
  (prueba 01);
- AD · AC = BD · BC no siempre significa datos contradictorios: a veces
  significa muchas respuestas (pruebas 02 y 03);
- un coseno en [−1, 1] no basta: hay que excluir los triángulos
  degenerados y comprobar el orden cíclico (prueba 07).

## Notas por lenguaje

- El `round` de Python lleva las mitades al par más cercano. Las cinco
  soluciones comparan el cuadrado del límite de medio kilómetro con
  enteros exactos, por lo que las mitades se redondean hacia arriba igual.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1294_geometry.cpp](1294_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 124 KB |
| [1294_geometry.go](1294_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1084 KB |
| [1294_geometry.java](1294_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.109 s | 1648 KB |
| [1294_geometry.py](1294_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 448 KB |
| [1294_geometry.rs](1294_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.015 s | 236 KB |
