# 1444. Alimentar al elefpótamo

[Timus 1444](https://acm.timus.ru/problem.aspx?space=1&num=1444) · dificultad 263 · geometry

Problema original de Ekaterina Vasilyeva (idea y texto) y Alexander Mironenko, Alexey Lakhtin y Den Raskovalov (programación), del Décimo Campeonato Universitario de Programación por Equipos de los Urales, 24–25 de marzo de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N calabazas (3 ≤ N ≤ 30000) están en puntos enteros distintos con
coordenadas de −1000 a 1000, no todas en una recta. Un elefpótamo empieza
en la calabaza 1 y se la come; tras cada calabaza se le puede mandar en
línea recta hacia cualquier calabaza restante. El animal se detiene para
siempre en cuanto pisa sus propias huellas, así que el recorrido nunca
debe tocarse a sí mismo. Hay que hallar el mayor número K de calabazas
que puede comer y el orden del recorrido, empezando por la 1.

Límite de tiempo: 0.5 segundos. Límite de memoria: 64 MB.

## Entrada

N y luego las coordenadas de las calabazas 1 a N.

## Salida

K y luego los números de las calabazas en el orden en que se comen, uno
por línea. Se acepta cualquier recorrido válido.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
0 0
10 10
0 10
10 0
```

Salida:

```
4
1
3
2
4
```

## Solución

Siempre se pueden comer las N calabazas. Las demás se ordenan por el
ángulo de la dirección desde la calabaza 1 y, en un mismo rayo, por la
distancia, las cercanas primero; las comparaciones usan productos
vectoriales enteros, así que son exactas. Recorrerlas en ese orden barre
alrededor de la calabaza 1 como un abanico: cada paso avanza más lejos
por el mismo rayo o pasa a la dirección siguiente, de modo que el
recorrido está en cada momento dentro de un sector estrecho y nunca
vuelve atrás.

El único peligro es el comienzo del círculo. Si dos direcciones vecinas
distan media vuelta o más, el paso entre ellas podría pasar por la
calabaza 1 o cortar pasos anteriores, así que el círculo se corta justo
después de ese hueco; solo puede haber uno, porque no todas las
calabazas están en una recta. Sin un hueco así, cualquier comienzo vale.
`O(N log N)`.

Detalles a tener en cuenta:

- varias calabazas en un mismo rayo se comen de la más cercana a la más
  lejana (pruebas 03, 06, gen2);
- un hueco de exactamente media vuelta, con calabazas a ambos lados de
  la calabaza 1 sobre una recta (pruebas 03, 09);
- la calabaza 1 en una esquina deja un hueco de más de media vuelta
  (pruebas 04, gen3, gen4).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1444_geometry.cpp](1444_geometry.cpp) | G++ 13.2 x64 | geometry | O(N log N) | AC | 0.062 s | 444 KB |
| [1444_geometry.go](1444_geometry.go) | Go 1.14 x64 | geometry | O(N log N) | AC | 0.078 s | 2336 KB |
| [1444_geometry.java](1444_geometry.java) | Java 1.8 | geometry | O(N log N) | AC | 0.187 s | 6232 KB |
| [1444_geometry.py](1444_geometry.py) | Python 3.12 x64 | geometry | O(N log N) | AC | 0.453 s | 11600 KB |
| [1444_geometry.rs](1444_geometry.rs) | Rust 1.75 x64 | geometry | O(N log N) | AC | 0.031 s | 2104 KB |
