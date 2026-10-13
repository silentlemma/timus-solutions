# 1429. Galletas

[Timus 1429](https://acm.timus.ru/problem.aspx?space=1&num=1429) · dificultad 2591 · geometry

Problema original de Nikita Rybak, Ilya Grebnov y Dmitry Kovalioff, de Timus Top Coders: First Challenge.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

La masa se extiende en un disco de radio 32 000 centrado en el origen,
y se hacen en ella N cortes circulares (0 ≤ N ≤ 500), cada uno con centro
(|X|, |Y| ≤ 10 000) y radio (1 ≤ R ≤ 10 000) enteros, así que todos
quedan muy dentro de la masa. Hay que contar los trozos en que queda la
masa; los trozos pueden tener agujeros, y lo que sobra alrededor de
todos los cortes también es un trozo. Los puntos de cruce o de contacto
distintos de los cortes distan al menos 10⁻³.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N, luego N líneas X Y R.

## Salida

El número de trozos.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
-1 0 2
1 0 2
0 0 3
```

Salida:

```
6
```

## Solución

Los cortes forman un grafo plano: los puntos de cruce y de contacto son
vértices y los arcos entre ellos son aristas. La fórmula de Euler para
un grafo plano con C componentes conexas dice V − E + F = 1 + C, donde
F cuenta también la cara exterior, y aquí la cara exterior es la masa
sobrante, que también es un trozo. Así que la respuesta es E − V + C + 1.
Una circunferencia sin cruces se toma como un vértice y una arista, lo
que no cambia E − V pero forma su propia componente.

Los cortes repetidos son un solo corte, así que primero se juntan las
circunferencias iguales. El número de puntos comunes de dos
circunferencias se decide exactamente con enteros a partir de d²,
(r₁ − r₂)² y (r₁ + r₂)². Los puntos son
p₁ + (m·(dx, dy) ± √K·(−dy, dx)) / (2d²) con m = d² + r₁² − r₂² y
K = 4d²r₁² − m², donde K se calcula exactamente con enteros antes de
evaluar las coordenadas en coma flotante. Los puntos de pares distintos
se juntan con una tabla hash de celdas de 10⁻³: las estimaciones de un
mismo punto difieren mucho menos de 10⁻⁴, y los puntos distintos distan
al menos 10⁻³. Cada circunferencia con puntos comunes tiene tantos arcos
como puntos distintos sobre ella, y una unión-búsqueda sobre los pares que se cruzan o se tocan
da C. `O(N²)` pares, hasta unos 250 000 puntos.

Detalles a tener en cuenta:

- la masa sobrante cuenta, así que un solo corte da 2 (prueba 03);
- los cortes iguales deben juntarse (pruebas 06, 09);
- varias circunferencias pueden encontrarse en un punto, que sigue
  siendo un único vértice (pruebas 07, gen4);
- las tangencias y las circunferencias casi tangentes requieren pruebas
  exactas y un redondeo cuidadoso (pruebas 04, 05, 08).

## Notas por lenguaje

- C++ y Rust guardan un único hash de rejilla con todos los puntos, como
  se describe arriba. En Go, Java y Python esa tabla de hasta 250 000
  puntos superaba el límite de 64 MB, así que guardan solo las
  estimaciones de cada circunferencia y las agrupan circunferencia por
  circunferencia. Un grupo de s estimaciones en una circunferencia es un
  punto sobre s + 1 circunferencias, así que suma 1 / (s + 1) al número
  de vértices, y cada punto suma 1 en total. Go y Python agrupan con un
  pequeño hash de rejilla por circunferencia; Java ordena los ángulos de
  las estimaciones alrededor del centro, donde las de un mismo punto
  quedan juntas en orden circular, ya que puntos distintos difieren al
  menos 10⁻³ / r en ángulo.
- Python se ejecuta con PyPy; con CPython, según la máquina, las pruebas
  más grandes de aquí pueden superar el límite de 1 s.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1429_geometry.cpp](1429_geometry.cpp) | G++ 13.2 x64 | geometry | O(N^2 log N) | AC | 0.265 s | 24972 KB |
| [1429_geometry.go](1429_geometry.go) | Go 1.14 x64 | geometry | O(N^2) | AC | 0.359 s | 19352 KB |
| [1429_geometry.java](1429_geometry.java) | Java 1.8 | geometry | O(N^2 log N) | AC | 0.187 s | 9948 KB |
| [1429_geometry.py](1429_geometry.py) | PyPy 3.10 x64 | geometry | O(N^2) | AC | 0.750 s | 22356 KB |
| [1429_geometry.rs](1429_geometry.rs) | Rust 1.75 x64 | geometry | O(N^2 log N) | AC | 0.265 s | 51048 KB |
