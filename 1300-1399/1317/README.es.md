# 1317. Granizo

[Timus 1317](https://acm.timus.ru/problem.aspx?space=1&num=1317) · dificultad 1055 · geometry

Problema original con idea de Pavel Atnashev, preparado por Pavel Atnashev y Alexey Lakhtin, del Octavo Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 11–16 de marzo de 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un aparcamiento es un polígono convexo de 3 a 10 vértices, rodeado por
una valla de altura h (1 ≤ h ≤ 100). Un láser está en el suelo
estrictamente dentro del aparcamiento y destruye un granizo si está a
una distancia de d como mucho (h < d < 1000). Los granizos caen en
vertical.

El alcance siempre basta para los granizos que caen sobre el propio
aparcamiento, y el láser también derriba los que caen fuera, siempre
que pueda verlos por encima de la valla y alcanzarlos. Dados hasta 100
puntos donde caen granizos, hay que contar cuántos se derriban en el
aire. Todas las coordenadas valen como mucho 1000 en valor absoluto.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

La primera línea tiene n y h, luego n líneas con los vértices en orden
alrededor del polígono, luego una línea con d y las coordenadas del
láser, y después k y k líneas con los puntos de caída.

## Salida

El número de granizos derribados.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 10.00
1.00 0.00
0.00 1.00
-1.00 0.00
0.00 -1.00
50.00 0.00 0.00
5
0.00 0.00
1.00 1.00
2.00 2.00
3.00 3.00
4.00 4.00
```

Salida:

```
3
```

## Solución

Sea un granizo que cae fuera del aparcamiento a una distancia
horizontal r del láser. El rayo sale del aparcamiento a una distancia
horizontal a, donde el rayo desde el láser hacia el punto de caída
cruza la valla. Un haz que alcanza el granizo a altura z pasa sobre la
valla a altura z · a / r, así que solo la supera si z ≥ h · r / a. Al
láser le conviene disparar lo más bajo posible, y el granizo se derriba
si ese punto más bajo está al alcance:

r² + (h · r / a)² ≤ d², es decir r² · (a² + h²) ≤ d² · a².

Para hallar a, el polígono se orienta en sentido antihorario (por el
signo de su área) y cada lado se escribe como una normal exterior n con
un desplazamiento c, de modo que el aparcamiento es n · p ≤ c en todos
los lados. El rayo L + t · u cruza los lados hacia los que avanza
(n · u > 0) en t = (c − n · L) / (n · u), y como el aparcamiento es
convexo, sale de él en el menor de esos valores. Un granizo con
n · p ≤ c en todos los lados cae sobre el aparcamiento o sobre la valla
y siempre cuenta. `O(n · k)`.

Detalles a tener en cuenta:

- los granizos sobre la valla cuentan como caídos en el aparcamiento
  (prueba 02);
- los vértices pueden venir en sentido horario (prueba 05), así que
  primero hay que hallar la orientación;
- las comparaciones necesitan una pequeña tolerancia relativa: con
  h = 100, un cuadrado de semilado 1 y un granizo a distancia 2, hace
  falta d² ≥ 40004, así que d = 200 se queda corto y d = 201 alcanza
  (pruebas 06 y 07).

Las respuestas se compararon con una comprobación directa que busca la
altura visible más baja por bisección y prueba el haz contra cada lado
de la valla, en 400 aparcamientos aleatorios.

## Notas por lenguaje

- Las cinco soluciones siguen los mismos pasos; Python toma la mínima
  distancia de salida directamente y las demás empiezan en infinito.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1317_geometry.cpp](1317_geometry.cpp) | G++ 13.2 x64 | geometry | O(n k) | AC | 0.001 s | 220 KB |
| [1317_geometry.go](1317_geometry.go) | Go 1.14 x64 | geometry | O(n k) | AC | 0.031 s | 1084 KB |
| [1317_geometry.java](1317_geometry.java) | Java 1.8 | geometry | O(n k) | AC | 0.093 s | 600 KB |
| [1317_geometry.py](1317_geometry.py) | Python 3.12 x64 | geometry | O(n k) | AC | 0.078 s | 628 KB |
| [1317_geometry.rs](1317_geometry.rs) | Rust 1.75 x64 | geometry | O(n k) | AC | 0.015 s | 228 KB |
