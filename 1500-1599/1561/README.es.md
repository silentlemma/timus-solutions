# 1561. Winnie the Pooh

[Timus 1561](https://acm.timus.ru/problem.aspx?space=1&num=1561) · dificultad 2838 · math

Problema original del Novosibirsk SU Contest en el campus de Petrozavodsk, septiembre de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Winnie come cada barril de una misma clase de miel en el mismo número
entero de días, desconocido para cada clase. Llegan en orden hasta 1000
consultas: `Add` trae una clase nueva, `Learn A0 … Ak S E` dice que comer
A0 barriles de la clase 0, …, Ak de la clase k desde el día de la semana
S termina el día E, y `Eat A0 … Ak S` pregunta qué día termina una comida
así empezada en S (0 ≤ Ai ≤ 10⁶). Cada `Eat` se responde con el día si
los hechos hasta ahora lo fijan, `Don't know` si permiten varios y
`Already crazy` si los hechos hasta ahora se contradicen.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

El número de consultas y luego una consulta por línea, con los días
escritos como Monday … Sunday.

## Salida

Una línea por cada consulta `Eat`.

## Ejemplos

### Ejemplo 1

Entrada:

```
9
Add
Add
Learn 5 2 Saturday Monday
Eat 3 3 Tuesday
Add
Learn 0 9 4 Friday Thursday
Eat 3 0 6 Sunday
Learn 3 2 10 Saturday Friday
Eat 3 4 11 Monday
```

Salida:

```
Don't know
Saturday
Already crazy
```

## Solución

Para el día de la semana solo importa el número de días módulo 7, y
cualquier resto es posible, ya que una clase puede tardar 7 días. Así
que las incógnitas x₀, x₁, … están en el cuerpo de los restos módulo 7,
un hecho es la ecuación lineal A0·x₀ + … + Ak·xk = E − S, y una comida
empezada en S termina en S + A0·x₀ + … + Ak·xk.

Los hechos se guardan como una base escalonada: cada fila tiene un 1 en
su primer lugar no nulo, su pivote, y no hay dos filas con el mismo
pivote. Un vector nuevo se reduce restando múltiplos de las filas en
orden creciente de pivote, junto con sus lados derechos. Un hecho que
se reduce a cero es redundante o, con lado derecho no nulo, una
contradicción, tras la cual toda comida se responde `Already crazy`; si
no, pasa a ser una fila nueva. Una comida queda fijada exactamente
cuando su vector se reduce a cero, y entonces el lado derecho acumulado
por el camino es su duración. Cada reducción tarda O(R·K) para R filas
y K clases, unos 2·10⁷ pasos en el peor caso. Los resultados se
contrastaron con probar todos los restos en pruebas pequeñas
aleatorias.

Detalles a tener en cuenta:

- un hecho sobre una comida de cero barriles es una contradicción salvo
  que S = E (prueba 03);
- los múltiplos de 7 barriles no dicen nada de los días por barril
  (prueba 04);
- en cuanto los hechos se contradicen, toda comida posterior se
  responde `Already crazy`, pero las anteriores conservan su respuesta
  (prueba 05);
- pueden aparecer clases después de conocerse un hecho, así que las
  filas guardadas son más cortas que los vectores posteriores;
- Python se ejecuta con PyPy: las pruebas más grandes tardan unos 1.1 s
  con CPython frente a un límite de 2 s, y unos 0.3 s con PyPy.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1561_math.cpp](1561_math.cpp) | G++ 13.2 x64 | math | O(N^2 K) | AC | 0.328 s | 1076 KB |
| [1561_math.go](1561_math.go) | Go 1.14 x64 | math | O(N^2 K) | AC | 0.171 s | 5804 KB |
| [1561_math.java](1561_math.java) | Java 1.8 | math | O(N^2 K) | AC | 0.421 s | 8276 KB |
| [1561_math.py](1561_math.py) | PyPy 3.10 x64 | math | O(N^2 K) | AC | 0.750 s | 29076 KB |
| [1561_math.rs](1561_math.rs) | Rust 1.75 x64 | math | O(N^2 K) | AC | 0.125 s | 2880 KB |
