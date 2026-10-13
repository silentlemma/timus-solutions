# 1442. Polvos flu

[Timus 1442](https://acm.timus.ru/problem.aspx?space=1&num=1442) · dificultad 3019 · geometry

Problema original de Anton Botov (autor) y Stanislav Vasiliev (texto), del Décimo Campeonato Universitario de Programación por Equipos de los Urales, 24–25 de marzo de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Los polvos flu se echaron en un baúl de 1 m de largo, 50 cm de ancho y
50 cm de alto por un agujero en el centro de la tapa, y formaron un cono
circular recto de radio r y altura h (1 ≤ r ≤ 25, 1 ≤ h ≤ 50). Una
rendija recta y fina cruza el fondo a distancia d del centro de la base
(1 ≤ d ≤ 25). Donde la base toca la rendija, los polvos se escapan y
dejan a lo largo de ella pendientes planas con el mismo ángulo de reposo
que el cono. Hay que hallar, en centímetros cúbicos y con cuatro cifras
tras el punto, cuántos polvos quedan.

Límite de tiempo: 0.5 segundos. Límite de memoria: 64 MB.

## Entrada

r, d y h, uno por línea, en centímetros.

## Salida

El volumen que queda.

## Ejemplos

### Ejemplo 1

Entrada:

```
10
5
2
```

Salida:

```
151.704483
```

## Solución

Se pone el centro de la base en el origen y la rendija en la recta
x = d. Con la pendiente k = h / r, la superficie del cono sobre un punto
a distancia ρ del centro tiene altura k (r − ρ), y las pendientes junto a
la rendija tienen altura k |x − d|; los polvos que quedan están bajo la
menor de las dos. Si d ≥ r la rendija no toca la base y la respuesta es
el cono entero π r² h / 3. Si no, se resta el volumen perdido, la
integral de k ((r − ρ) − |x − d|) donde es positiva.

Se corta la base en rebanadas paralelas a la rendija. Para un x fijo sea
a = r − |x − d|; la pérdida es positiva donde ρ < a, es decir
|y| < Y = √(a² − x²), y la integral en y tiene forma cerrada, así que la
rebanada pierde k (a Y − x² ln((a + Y) / |x|)). Solo hay rebanadas para
(d − r) / 2 < x < (d + r) / 2. La integral restante en x se calcula con
la regla de Simpson adaptativa, partida en x = 0 y x = d, donde la
función de la rebanada tiene quiebros; la raíz cuadrada en los extremos
es lo que hace útiles los pasos adaptativos. En la práctica
`O(log(1/ε))` pasos por tramo liso.

Detalles a tener en cuenta:

- si la rendija toca la base o pasa de largo, no se pierde nada
  (pruebas 02, 06, 10);
- la rendija junto al centro es la que más se lleva (pruebas 03, 09);
- se esperan cuatro decimales exactos, así que Simpson simple con unos
  cientos de pasos no basta del todo cerca de los extremos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1442_geometry.cpp](1442_geometry.cpp) | G++ 13.2 x64 | geometry | O(log(1/ε)) | AC | 0.015 s | 156 KB |
| [1442_geometry.go](1442_geometry.go) | Go 1.14 x64 | geometry | O(log(1/ε)) | AC | 0.015 s | 1100 KB |
| [1442_geometry.java](1442_geometry.java) | Java 1.8 | geometry | O(log(1/ε)) | AC | 0.140 s | 1772 KB |
| [1442_geometry.py](1442_geometry.py) | Python 3.12 x64 | geometry | O(log(1/ε)) | AC | 0.078 s | 700 KB |
| [1442_geometry.rs](1442_geometry.rs) | Rust 1.75 x64 | geometry | O(log(1/ε)) | AC | 0.015 s | 252 KB |
