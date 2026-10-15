# 1661. Dodecaedro

[Timus 1661](https://acm.timus.ru/problem.aspx?space=1&num=1661) · dificultad 3526 · combinatorics

Problema original de Igor Chevdar, del Ural SU Contest en el campus de invierno de Petrozavodsk, enero de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Treinta varillas de igual longitud, cada una de algún color, se usan
como aristas de un dodecaedro. Hay que contar cuántos dodecaedros
distintos se pueden armar, considerando iguales los que solo difieren en
una rotación.

## Entrada

Treinta enteros de 1 a 30, los colores de las varillas.

## Salida

La cantidad de dodecaedros distintos.

## Ejemplos

### Ejemplo 1

Entrada:

```
1 1 2 2 2 2 2 2 2 2
2 2 2 2 2 2 2 2 2 2
2 2 2 2 2 2 2 2 2 2
```

Salida:

```
11
```

## Solución

Por el lema de Burnside, el número de coloraciones salvo rotación es el
promedio, sobre las 60 rotaciones del dodecaedro, del número de
coloraciones que cada rotación deja fijas. Una rotación reparte las 30
aristas en ciclos, y una coloración queda fija exactamente cuando cada
ciclo es de un solo color. Las rotaciones son de cuatro tipos:

- la identidad: 30 ciclos de longitud 1;
- 24 giros alrededor de ejes por los centros de caras opuestas: 6 ciclos
  de longitud 5;
- 20 giros alrededor de ejes por vértices opuestos: 10 ciclos de
  longitud 3;
- 15 medias vueltas alrededor de ejes por los puntos medios de aristas
  opuestas: esas 2 aristas quedan en su sitio y las otras 28 forman 14
  ciclos de longitud 2.

Con todos los ciclos de longitud L, el color c debe ocupar exactamente
count(c) / L ciclos, lo que es imposible si L no divide todas las
cantidades y, si no, da el coeficiente multinomial
(30 / L)! / ∏ (count(c) / L)!. En una media vuelta se eligen en orden
colores disponibles para las dos aristas fijas, se retiran esas varillas
y el resto se cuenta con L = 2. Se pondera por las rotaciones y se divide
entre 60. `O(C³)` para C = 30 colores.

Detalles a tener en cuenta:

- la respuesta llega a 30! / 60, unos 4,4 · 10³⁰ (prueba 03), más de 64
  bits; todos los valores intermedios son como máximo 30! < 2¹²⁸,
  así que C++ y Rust usan enteros de 128 bits y los demás, enteros
  grandes;
- un multinomial armado como producto de binomiales, con un factor
  exacto cada vez, nunca necesita un valor mayor que unas 30 · 30!.

Los tipos de ciclo de arriba salen del grupo de rotaciones real,
construido a partir de las coordenadas de un dodecaedro, y la fórmula
coincide con un recuento de órbitas por fuerza bruta en coloraciones
pequeñas. Las respuestas también coinciden con una implementación
aceptada independiente en entradas aleatorias.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1661_combinatorics.cpp](1661_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(C^3) | AC | 0.015 s | 192 KB |
| [1661_combinatorics.go](1661_combinatorics.go) | Go 1.14 x64 | combinatorics | O(C^3) | AC | 0.015 s | 1280 KB |
| [1661_combinatorics.java](1661_combinatorics.java) | Java 1.8 | combinatorics | O(C^3) | AC | 0.140 s | 932 KB |
| [1661_combinatorics.py](1661_combinatorics.py) | Python 3.12 x64 | combinatorics | O(C^3) | AC | 0.093 s | 548 KB |
| [1661_combinatorics.rs](1661_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(C^3) | AC | 0.031 s | 240 KB |
