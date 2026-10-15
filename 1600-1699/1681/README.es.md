# 1681. El huerto del Hermano Oso

[Timus 1681](https://acm.timus.ru/problem.aspx?space=1&num=1681) · dificultad 3703 · geometry

Problema original de Pavel Egorov, del X Campeonato Abierto Individual de la Universidad Estatal de los Urales, 28 de febrero de 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un huerto es un polígono estrictamente convexo de n postes, dados en
sentido antihorario. Desde cada poste sale una cuerda hasta el poste k
pasos más allá en sentido antihorario. Un conejo entra saltando la
valla y nunca cruza una cuerda. Hallar la fracción del área del huerto
a la que no puede llegar.

## Entrada

n y k (3 ≤ n ≤ 300; 1 ≤ k < n), y luego los n postes, coordenadas
enteras de valor absoluto a lo sumo 10000.

## Salida

La razón entre el área salvada y el área total, con un error de a lo
sumo 10⁻⁴.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 3
0 0
20 0
20 20
10 30
0 20
```

Salida:

```
0.466666667
```

### Ejemplo 2

Entrada:

```
6 2
0 2
-2 1
-2 -1
0 -2
2 -1
2 1
```

Salida:

```
0.666666667
```

## Solución

Las cuerdas para k y para n − k son las mismas cuerdas geométricas, así
que tomamos k = min(k, n − k). Con k = 1 todas las cuerdas van a lo
largo de la valla y el conejo no puede entrar: la respuesta es 1.

Si no, cada cuerda corta el huerto en dos, así que dos puntos están en
el mismo trozo exactamente cuando ninguna cuerda los separa, y cada
trozo es el huerto intersecado con un semiplano por cuerda. El conejo
llega justo a los trozos que contienen un tramo de valla. El trozo
junto al lado i (del poste i al poste i + 1) es el huerto recortado,
para cada cuerda, al semiplano que contiene el punto medio del lado.
Dos lados nunca comparten trozo: las cuerdas desde los postes i + 1 − k
e i bordean ambas el lado i y entre las dos lo separan de cualquier
otro lado. Así, la respuesta es 1 − Σ área(trozo del lado i) / área.

Basta aplicar las k cuerdas que pasan sobre el lado i, desde los postes
i + 1 − k, …, i. La parte del huerto del lado de i respecto a cualquier
otra cuerda es la envolvente de n − k + 1 postes consecutivos alrededor
del lado i, y como 2k ≤ n esos postes incluyen los k + 1 postes de
alguna cuerda sobre el lado i. Esa cuerda ya corta al menos igual de
hondo.

Recortar un polígono convexo por un semiplano es lineal en su tamaño.
Primero se aplican las dos cuerdas desde los extremos del lado, que
dejan un triángulo pequeño, y luego las demás.
`O(n² + n · k · s)`, donde s es el tamaño de un trozo, unos pocos
vértices.

Trampas:

- k = 1 y k = n − 1 dan 1, no 0: las cuerdas son la propia valla;
- un trozo que toca la valla solo en un poste, como una punta de
  pentagrama (test 05), queda salvado;
- cuando 2k = n cada cuerda aparece dos veces, lo que no molesta.

Las respuestas coinciden con el recorte por las n cuerdas en 500
polígonos aleatorios y con una implementación aceptada independiente en
polígonos aleatorios, casi circulares e irregulares.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1681_geometry.cpp](1681_geometry.cpp) | G++ 13.2 x64 | geometry | O(n² + n · k · s) | AC | 0.015 s | 252 KB |
| [1681_geometry.go](1681_geometry.go) | Go 1.14 x64 | geometry | O(n² + n · k · s) | AC | 0.031 s | 5624 KB |
| [1681_geometry.java](1681_geometry.java) | Java 1.8 | geometry | O(n² + n · k · s) | AC | 0.125 s | 4932 KB |
| [1681_geometry.py](1681_geometry.py) | Python 3.12 x64 | geometry | O(n² + n · k · s) | AC | 0.265 s | 756 KB |
| [1681_geometry.rs](1681_geometry.rs) | Rust 1.75 x64 | geometry | O(n² + n · k · s) | AC | 0.031 s | 312 KB |
