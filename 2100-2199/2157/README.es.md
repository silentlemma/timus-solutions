# 2157. La caída más larga a través de nubes que detienen al paracaidista

[Timus 2157](https://acm.timus.ru/problem.aspx?space=1&num=2157) · dificultad 1301 · dp

Problema original de Valentin Zuev, del Concurso Escolar de Programación de los Urales 2020.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un paracaidista cae desde (x, y) con aceleración 10 m/s², empezando con
velocidad vertical cero, y puede fijar en cualquier momento cualquier
velocidad horizontal entre −1 y 1 m/s. Llegar al punto de la nube i
detiene la caída durante cᵢ segundos, tras los cuales vuelve a caer desde
el reposo. Hallar el mayor tiempo posible hasta llegar al suelo y = 0,
con error absoluto o relativo a lo sumo 10⁻⁴. Los límites son 3 segundos
y 256 MB.

## Entrada

n, 0 ≤ n ≤ 50 000, el inicio, y luego las nubes xᵢ, yᵢ, cᵢ con
|xᵢ| ≤ 10 000, 0 < yᵢ < y ≤ 10 000 y 1 ≤ cᵢ ≤ 10 000.

## Salida

El mayor tiempo de caída.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
0 80
-1 30 2
-1 60 1
0 40 10
1 20 1
1 50 1
```

Salida:

```
20.863703305
```

### Ejemplo 2

Entrada:

```
0
100 100
```

Salida:

```
4.472135955
```

## Solución

Una caída de altura h desde el reposo dura √(h / 5) segundos, y en ella
la posición horizontal puede cambiar a lo sumo eso mismo. Así que desde
la altura Y una nube en (x′, y′) es alcanzable exactamente cuando
5 (x′ − x)² ≤ Y − y′, es decir, a lo sumo ⌊√(Y / 5)⌋ ≤ 44 columnas a cada
lado.

Sea best(p) el mayor tiempo restante desde una nube p tras su parada, o
desde el inicio: caer directamente al suelo, √(h / 5) para su altura h, o caer a una nube
alcanzable q y sumar su densidad y best(q). Dentro de una columna solo
importa la nube alcanzable más alta. Pasar por ella de camino a una nube
más baja de la misma columna es posible y más largo, porque
√a + √b ≥ √(a + b) y la parada añade tiempo.

Así que se procesan las nubes y el inicio por altura creciente. Cada
columna guarda las alturas de sus nubes procesadas en orden creciente
con sus valores; para un punto, una búsqueda binaria en cada una de las a
lo sumo 89 columnas halla la nube más alta lo bastante baja, y best del
punto es el máximo sobre ellas. El inicio va al final y su valor es la
respuesta. El trabajo es O(n · 89 · log n).

En el segundo ejemplo no hay nubes, y la caída desde 100 m dura
√20 ≈ 4.472 segundos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2157_dp.cpp](2157_dp.cpp) | G++ 13.2 x64 | dp | O(89 n log n) | AC | 0.125 s | 3052 KB |
| [2157_dp.go](2157_dp.go) | Go 1.14 x64 | dp | O(89 n log n) | AC | 0.390 s | 6320 KB |
| [2157_dp.java](2157_dp.java) | Java 1.8 | dp | O(89 n log n) | AC | 0.718 s | 7852 KB |
| [2157_dp.py](2157_dp.py) | Python 3.12 x64 | dp | O(89 n log n) | AC | 2.453 s | 23964 KB |
| [2157_dp.rs](2157_dp.rs) | Rust 1.75 x64 | dp | O(89 n log n) | AC | 0.250 s | 4032 KB |
