# 1697. Disparo de francotirador

[Timus 1697](https://acm.timus.ru/problem.aspx?space=1&num=1697) · dificultad 5057 · geometry

Problema original de Alex Samsonov, del Ural SU Contest en el campus de invierno de Petrozavodsk, febrero de 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un francotirador en S = (sx, sy, sz) vigila un objetivo que va por el
suelo de A a B. Las balas vuelan en línea recta; pueden rozar un
rascacielos (una caja de lados paralelos a los ejes apoyada en el
suelo), pero no atravesarlo. Hallar el primer punto del camino al que
el francotirador puede acertar, o informar de que no lo hay.

## Entrada

S, luego A y B en el suelo, luego n (0 ≤ n ≤ 100) edificios
lx ly rx ry h. Todos los valores son enteros de valor absoluto a lo sumo
100, sz ≥ 0. Los edificios no comparten puntos, S está fuera de todos y
el segmento AB no toca ninguno.

## Salida

Las coordenadas de ese punto con un error de a lo sumo 10⁻⁷, o
Impossible.

## Ejemplos

### Ejemplo 1

Entrada:

```
0 0 2
-4 4 4 4
2
-3 2 -1 3 10
1 -1 4 2 20
```

Salida:

```
-1.3333333333 4.0000000000
```

### Ejemplo 2

Entrada:

```
0 0 2
4 1 4 -1
1
1 -1 3 1 10
```

Salida:

```
Impossible
```

## Solución

Sea P(t) = A + t(B − A). Un punto del disparo hacia P(t) es
S + u(P(t) − S) = S + u(A − S) + v(B − A) con v = u·t, lineal en
(u, v). Así, el interior de un edificio se convierte en un polígono
convexo abierto del plano (u, v), recortado por dos franjas (en x y en
y) y por el rango de alturas de u, donde sz·(1 − u) debe quedar por
debajo de h. Los tiempos t que bloquea son los valores v / u sobre ese
polígono, un intervalo abierto (lᵢ, rᵢ). Dos rectas más, −1 ≤ t ≤ 2,
lo mantienen acotado sin tocar los tiempos que importan.

Todas las rectas del borde tienen coeficientes enteros pequeños, así
que los vértices del polígono se hallan exactamente como las
intersecciones de pares de rectas que cumplen todas las restricciones,
y lᵢ y rᵢ son los cocientes v / u extremos sobre ellos. El polígono
tiene interior, y el edificio bloquea algo, exactamente cuando tiene
tres vértices distintos: un polígono que solo roza es un segmento o un
punto. La única excepción es un plano de disparos que contiene una
pared, como cuando S, A y B tienen todos x = lx: el polígono tiene
interior, pero cada disparo solo se desliza a lo largo de la pared.
Entonces una recta de franja tiene ambos coeficientes nulos, y ese
edificio no bloquea nada. Un francotirador en el suelo (sz = 0) solo
pierde la restricción de altura.

Los tiempos libres forman un conjunto cerrado, así que su primer punto
es 0 o el extremo derecho rᵢ de algún intervalo. Se prueban esos
candidatos en orden contra todos los intervalos abiertos y se imprime
el primero libre. Toda comparación es una multiplicación cruzada de
enteros menores que 10¹⁰. `O(n²)`.

Trampas:

- rozar una pared, una arista o un tejado está permitido, así que los
  intervalos son abiertos y un tiempo libre puede quedar justo entre
  dos de ellos;
- un disparo que se desliza a lo largo de un tejado o una pared no está
  bloqueado, y las pruebas en coma flotante fallan fácilmente aquí;
- todos los disparos pueden estar en el plano de una pared (tests 10 y
  11), y entonces el interior del polígono no significa un disparo
  bloqueado;
- con A = B solo hay un tiempo, 0.

Las respuestas coinciden con una implementación aceptada independiente
en 330 casos aleatorios, la mayoría con coordenadas pequeñas donde los
disparos rozan aristas y esquinas, y en 400 casos con todos los
disparos en el plano de paredes.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1697_geometry.cpp](1697_geometry.cpp) | G++ 13.2 x64 | geometry | O(n²) | AC | 0.015 s | 216 KB |
| [1697_geometry.go](1697_geometry.go) | Go 1.14 x64 | geometry | O(n²) | AC | 0.031 s | 1204 KB |
| [1697_geometry.java](1697_geometry.java) | Java 1.8 | geometry | O(n²) | AC | 0.156 s | 3560 KB |
| [1697_geometry.py](1697_geometry.py) | Python 3.12 x64 | geometry | O(n²) | AC | 0.093 s | 944 KB |
| [1697_geometry.rs](1697_geometry.rs) | Rust 1.75 x64 | geometry | O(n²) | AC | 0.046 s | 272 KB |
