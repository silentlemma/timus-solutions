# 1223. El menor número de lanzamientos de huevos que halla el piso crítico

[Timus 1223](https://acm.timus.ru/problem.aspx?space=1&num=1223) · dificultad 291 · dp

Problema original del folclore, propuesto por Alexander Klepinin, del séptimo concurso universitario de programación de la Universidad Estatal de los Urales.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Todos los huevos son igual de resistentes: un huevo aguanta una caída
desde el piso `E` o más abajo y se rompe desde cualquier piso más alto.
Con un número dado de huevos y de pisos, ambos hasta 1000, hay que hallar
el menor número de lanzamientos que determina `E` con seguridad en el
peor caso; los huevos que no se rompen se pueden volver a lanzar. Hasta
1000 consultas, terminadas en `0 0`.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Una consulta por línea: el número de huevos y el número de pisos.

## Salida

Para cada consulta, el menor número de lanzamientos en el peor caso.

## Ejemplos

### Ejemplo 1

Entrada:

```
1 10
2 5
0 0
```

Salida:

```
10
3
```

## Solución

Se da la vuelta a la pregunta: con `d` lanzamientos y `k` huevos,
¿cuántos pisos se pueden distinguir? El primer lanzamiento se hace desde
algún piso; si el huevo se rompe, quedan los pisos de abajo con `d − 1`
lanzamientos y `k − 1` huevos, y si aguanta, los de arriba con `d − 1`
lanzamientos y `k` huevos. Así

`reach(d, k) = reach(d − 1, k − 1) + reach(d − 1, k) + 1`,

con `reach(0, k) = reach(d, 0) = 0`. La respuesta para `n` pisos es el
menor `d` con `reach(d, k) ≥ n`. Diez huevos ya permiten una búsqueda
binaria normal sobre 1000 pisos, así que más huevos no ayudan y `k` se
limita a 10. Rellenar para cada `k` las respuestas de todos los `n` según
crece `d` cuesta `O(10 · 1000)` una vez, y cada consulta es después una
consulta a la tabla.

Detalles a tener en cuenta:

- con un solo huevo lo único seguro es ir piso a piso, así que la
  respuesta es el número de pisos;
- cualquier número de huevos por encima de 10 se comporta como 10, así
  que se limita antes de mirar la tabla;
- los números de pisos crecen como coeficientes binomiales, así que
  también se limitan a 1000, o se desbordarían mucho antes de completar
  la tabla.

Las respuestas se comprobaron con la recurrencia minimax directa para
hasta 5 huevos y 60 pisos, y se compararon con una solución escrita
aparte en todas las pruebas.

## Notas por lenguaje

- Todos los lenguajes construyen la misma tabla y responden con ella.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1223_dp.cpp](1223_dp.cpp) | G++ 13.2 x64 | dp | O(10 · 1000) once, O(1) per query | AC | 0.015 s | 172 KB |
| [1223_dp.go](1223_dp.go) | Go 1.14 x64 | dp | O(10 · 1000) once, O(1) per query | AC | 0.031 s | 1216 KB |
| [1223_dp.java](1223_dp.java) | Java 1.8 | dp | O(10 · 1000) once, O(1) per query | AC | 0.078 s | 668 KB |
| [1223_dp.py](1223_dp.py) | Python 3.12 x64 | dp | O(10 · 1000) once, O(1) per query | AC | 0.078 s | 812 KB |
| [1223_dp.rs](1223_dp.rs) | Rust 1.75 x64 | dp | O(10 · 1000) once, O(1) per query | AC | 0.015 s | 376 KB |
