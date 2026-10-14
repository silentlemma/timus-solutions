# 1543. Revolución del baile

[Timus 1543](https://acm.timus.ru/problem.aspx?space=1&num=1543) · dificultad 2151 · simulation

Problema original de Denis Musin, del XI Campeonato Universitario por Equipos de Programación de los Urales, Ekaterimburgo, 21 de abril de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una canción es una fila de compases, cada uno vacío (N) o que pide una
de las teclas U, D, L, R. Un compás dura 1000, 500 o 250 ms en Easy,
Medium y Hard (Diff = 1, 2, 3). Dado el registro de pulsaciones del
jugador, se califica cada compás no vacío (un paso) por la primera
pulsación dentro de él:

- sin pulsación: Boo; una tecla equivocada: Miss;
- la tecla correcta antes del 40 % del compás desde su inicio: Perfect,
  antes del 70 %: Great, y si no Good.

Las pulsaciones después de la primera en un compás y las de compases
vacíos no cuentan. Luego se calculan

- la puntuación de baile: el n-ésimo paso da p·n·⌊B / S⌋ con p = 10 para
  Perfect, 5 para Great y 0 en otro caso, B = 10⁶·Diff y
  S = N(N + 1)/2 para N pasos;
- el bonus de combo: en una racha de pasos Perfect, Great y Good el
  c-ésimo paso da 55·c por Perfect, 33·c por Great y 0 por Good; Boo y
  Miss cortan la racha;
- el bonus de nivel según los puntos de baile (Perfect +2, Great +1,
  Good 0, Boo −4, Miss −5): 0 si los puntos bajaron alguna vez de cero;
  si no, 10⁷ si todos los pasos fueron Perfect, 10⁶ si todos fueron
  Perfect o Great, y en otro caso 10⁵, 10⁴, 10³ o 100 para al menos el
  80 %, 64 %, 50 % o menos del máximo posible, 2N.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

La duración de la canción (m:ss) y el nivel, los compases y luego
líneas «tiempo tecla» con las pulsaciones, en milisegundos desde el
inicio.

## Salida

Los cinco recuentos, una línea de 20 guiones y las cuatro
puntuaciones, como en el ejemplo.

## Ejemplos

### Ejemplo 1

Entrada:

```
0:30 Easy
NNNNNLNNRNUNNUNNNDDDNNUNNNNRNU
5201 L
8475 R
8735 L
10000 U
13200 U
17284 D
18355 D
19124 D
22222 U
27543 R
29923 U
```

Salida:

```
Perfect: 7
Great: 2
Good: 1
Boo: 0
Miss: 0
--------------------
Stage Score: 7181495
Combo Bonus: 2233
Dance Level Bonus: 100000
Total Score: 7283728
```

## Solución

El compás i cubre los tiempos [i·T, (i + 1)·T) para el periodo T. Se
ordenan las pulsaciones por tiempo y se recorren con un puntero:
antes de cada compás se saltan las anteriores a su inicio; la
pulsación bajo el puntero es la primera del compás si es anterior a
su fin. Los umbrales se comparan con enteros, 10·elapsed < 4·T y
10·elapsed < 7·T, y también las proporciones, 100·puntos ≥ 80·2N,
etc. La duración de la canción no hace falta: los compases están
dados. Las puntuaciones caben en 64 bits.
`O(L + P log P)` para L compases y P pulsaciones.

El enunciado admite varias lecturas. Estas siguen el enunciado; las dos
primeras también se confirman en el foro del juez, y la tercera es
nuestra lectura de «al menos el 80 %»:

- un compás incluye su inicio y excluye su fin;
- el bonus de nivel es 0 en cuanto los puntos bajan de cero, aunque el
  total final sea bueno (prueba 03);
- las proporciones se comparan exactamente: 4 puntos de 6 quedan por
  debajo del 80 % (4,8), así que la prueba 02 recibe 10⁴, no 10⁵.

Detalles a tener en cuenta:

- las pulsaciones justo al 40 % y al 70 % del compás son Great y Good
  (prueba 06);
- una primera pulsación equivocada es un Miss aunque luego llegue la
  tecla correcta (prueba 07);
- una pulsación en un compás vacío justo antes de un paso no cuenta
  para él (prueba 07);
- Good alarga el combo sin dar puntos de combo (prueba gen3).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1543_simulation.cpp](1543_simulation.cpp) | G++ 13.2 x64 | simulation | O(L + P log P) | AC | 0.031 s | 528 KB |
| [1543_simulation.go](1543_simulation.go) | Go 1.14 x64 | simulation | O(L + P log P) | AC | 0.031 s | 1776 KB |
| [1543_simulation.java](1543_simulation.java) | Java 1.8 | simulation | O(L + P log P) | AC | 0.171 s | 4360 KB |
| [1543_simulation.py](1543_simulation.py) | Python 3.12 x64 | simulation | O(L + P log P) | AC | 0.078 s | 1676 KB |
| [1543_simulation.rs](1543_simulation.rs) | Rust 1.75 x64 | simulation | O(L + P log P) | AC | 0.015 s | 644 KB |
