# 1305. Envolvente convexa

[Timus 1305](https://acm.timus.ru/problem.aspx?space=1&num=1305) · dificultad 704 · geometry

Problema original del Segundo Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 3–4 de abril de 1998.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dados hasta 100 000 puntos con coordenadas enteras de 0 a 1000 (los
puntos pueden repetirse), hay que construir su «envolvente convexa
regular»: el menor conjunto convexo que los contiene cuyo borde es una
poligonal cerrada con cada lado paralelo a un eje o a 45° de los ejes.
Se imprimen sus vértices en sentido antihorario, cada uno una vez,
desde cualquier vértice, sin tres vértices consecutivos (de forma
cíclica) en una recta.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y luego N líneas con un punto cada una.

## Salida

Los vértices de la envolvente, uno por línea.

## Evaluación

La envolvente es única, pero su recorrido puede empezar en cualquier
vértice. El verificador acepta la lista esperada de vértices girada
hasta cualquier punto de inicio.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
3 3
3 1
2 2
4 2
```

Salida:

```
3 1
4 2
3 3
2 2
```

## Solución

Un lado de la envolvente solo puede ir en una de ocho direcciones, así
que su normal exterior es una de (1, 0), (1, 1), (0, 1), (−1, 1) y sus
opuestas. El menor conjunto convexo con esos lados es la intersección
del semiplano más ajustado para cada normal:

minX ≤ x ≤ maxX, minY ≤ y ≤ maxY, minS ≤ x + y ≤ maxS, minD ≤ x − y ≤ maxD.

Una pasada por los puntos halla estos ocho extremos. Yendo en sentido
antihorario desde el lado inferior, cada vértice es donde una recta
paralela a un eje se cruza con una diagonal, por ejemplo
(minS − minY, minY) y (maxD + minY, minY) en los extremos del lado
inferior. Los ocho vértices tienen coordenadas enteras. Cada una de las
ocho rectas toca un punto real, así que los vértices siempre salen en
este orden, pero un lado puede tener longitud cero, y entonces sus dos
vértices coinciden. Los vecinos iguales (también al dar la vuelta) se
funden, y no hace falta limpiar más: los lados que quedan apuntan en
direcciones distintas de las ocho, cada uno girando a la izquierda
respecto al anterior, así que ningún vértice queda en medio de un lado
recto. Un punto o un segmento es lo que queda cuando desaparecen todos
los lados menos ninguno o dos.

`O(N)`.

Detalles a tener en cuenta:

- un solo punto, aunque se repita, se imprime una vez (pruebas 02 y
  03);
- puntos en una recta en una de las ocho direcciones dan un segmento de
  dos vértices (pruebas 04 y 05), pero cualquier otra pendiente se
  ensancha en un polígono de verdad (prueba 06);
- varios vértices seguidos pueden coincidir, como en cada punta del
  rombo del ejemplo, donde los lados paralelos a los ejes miden 0
  (prueba 01).

La salida se comprobó en 300 conjuntos de puntos aleatorios:
estrictamente convexa y antihoraria, lados solo en las ocho
direcciones, cada lado en su recta más ajustada y todos los puntos
dentro.

## Notas por lenguaje

- C++, Go y Java guardan solo los ocho extremos al leer; Python y Rust
  leen primero todos los puntos, lo que también cabe de sobra.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1305_geometry.cpp](1305_geometry.cpp) | G++ 13.2 x64 | geometry | O(N) | AC | 0.109 s | 196 KB |
| [1305_geometry.go](1305_geometry.go) | Go 1.14 x64 | geometry | O(N) | AC | 0.015 s | 1680 KB |
| [1305_geometry.java](1305_geometry.java) | Java 1.8 | geometry | O(N) | AC | 0.125 s | 544 KB |
| [1305_geometry.py](1305_geometry.py) | Python 3.12 x64 | geometry | O(N) | AC | 0.078 s | 26160 KB |
| [1305_geometry.rs](1305_geometry.rs) | Rust 1.75 x64 | geometry | O(N) | AC | 0.015 s | 3716 KB |
