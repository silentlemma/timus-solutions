# 1271. Práctico

[Timus 1271](https://acm.timus.ru/problem.aspx?space=1&num=1271) · dificultad 4551 · geometry

Problema original de Alexey Lakhtin, del Campeonato de la Universidad Estatal de los Urales, 25 de octubre de 2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un petrolero triangular navega por un puerto rectangular 0 ≤ x ≤ DX,
0 ≤ y ≤ DY (DX, DY < 10⁸) entre N ≤ 40 barcos triangulares fondeados.
Solo puede desplazarse, nunca girar. Hay que hallar la longitud de la
ruta más corta que lleva su primera esquina a un punto dado, con tres
decimales, o −1 si es imposible. El petrolero puede tocar los barcos y
los bordes del puerto, pero no solaparse con ellos; los barcos no se
solapan entre sí.

Límite de tiempo: 3 segundos. Límite de memoria: 64 MB.

## Entrada

DX y DY, las tres esquinas del petrolero, el destino de su primera
esquina, N y luego las tres esquinas de cada barco. Todas las
coordenadas son enteras.

## Salida

La longitud de la ruta, o −1.

## Ejemplos

### Ejemplo 1

Entrada:

```
2003 2003
20 50
10 30
30 30
140 60
1
80 1000
100 20
60 20
```

Salida:

```
146.569
```

## Solución

Se sigue solo la primera esquina A del petrolero; las demás están a
desplazamientos fijos d₁, d₂, d₃ de ella (uno es cero).

- El petrolero queda dentro del puerto justo cuando A queda en un
  rectángulo menor, metido hacia dentro según los desplazamientos menor
  y mayor.
- El petrolero se solapa con un barco justo cuando A está estrictamente
  dentro de la envolvente convexa de los nueve puntos (esquina del barco
  − desplazamiento del petrolero). Son las sumas de Minkowski, polígonos
  convexos abiertos de como mucho seis esquinas.

Así, un punto se mueve en un rectángulo entre obstáculos convexos
abiertos. Un camino más corto solo dobla en esquinas de los obstáculos.
Por eso los vértices del grafo son el inicio, el destino y cada esquina
de obstáculo que está en el rectángulo y no estrictamente dentro de otro
obstáculo. Dos de ellos se unen cuando el segmento entre ellos no entra
en ningún obstáculo. El algoritmo de Dijkstra da la ruta.

Todo es exacto en enteros de 64 bits: las esquinas son enteras, de
valor absoluto menor que 3 · 10⁸. Un segmento no toca el interior de un
polígono convexo abierto justo cuando algún eje los separa, como mucho
tocándose. Los ejes que hay que probar son las normales de las aristas
del polígono y la normal del propio segmento. Cada prueba compara
productos escalares del orden de 10¹⁷. Con V ≤ 242 vértices y N
polígonos es `O(V² · N)`.

Detalles a tener en cuenta:

- tocar está permitido: el petrolero puede deslizarse junto a un barco,
  pasar un hueco justo de su anchura o acabar tocando un barco
  (pruebas 06, 07, 09);
- el destino puede ser inalcanzable porque el petrolero no cabe allí,
  dentro del puerto o entre los barcos (prueba 03);
- las pruebas en coma flotante pueden fallar con 10⁸, donde una astilla de una
  unidad de grosor debe seguir cerrando el paso (prueba 05);
- un obstáculo puede sobresalir del rectángulo reducido; sus esquinas de
  fuera no sirven, pero lo que queda dentro sigue estorbando;
- si el destino es el inicio, la respuesta es 0 (prueba 04).

Las respuestas se compararon con una implementación independiente en
240 puertos aleatorios, con 40 barcos, coordenadas de 10⁸ y muros con
huecos estrechos.

## Notas por lenguaje

- Todos los lenguajes usan las mismas pruebas exactas con enteros y un
  Dijkstra sencillo en O(V²).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1271_geometry.cpp](1271_geometry.cpp) | G++ 13.2 x64 | geometry | O(V² · N) | AC | 0.015 s | 280 KB |
| [1271_geometry.go](1271_geometry.go) | Go 1.14 x64 | geometry | O(V² · N) | AC | 0.031 s | 1260 KB |
| [1271_geometry.java](1271_geometry.java) | Java 1.8 | geometry | O(V² · N) | AC | 0.171 s | 5508 KB |
| [1271_geometry.py](1271_geometry.py) | Python 3.12 x64 | geometry | O(V² · N) | AC | 0.390 s | 1200 KB |
| [1271_geometry.rs](1271_geometry.rs) | Rust 1.75 x64 | geometry | O(V² · N) | AC | 0.062 s | 500 KB |
