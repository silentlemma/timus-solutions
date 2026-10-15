# 1653. Cinta de la Muerte

[Timus 1653](https://acm.timus.ru/problem.aspx?space=1&num=1653) · dificultad 5743 · geometry

Problema original de Pavel Atnashev, del cuarto de final de la subregión oriental del NEERC 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una estación espacial es un poliedro regular (uno de los cinco sólidos
platónicos) centrado en el origen, con un cañón en cada vértice que
apunta hacia fuera. Al principio un cañón apunta según Oz y una arista
suya está en el semiplano x ≥ 0 de Oxz. En cada ataque la estación gira
para que el cañón más cercano al atacante le apunte de lleno, y se queda
así hasta el siguiente ataque. Hay que hallar el ángulo total girado.

## Entrada

El nombre del sólido (tetrahedron, hexahedron, octahedron, dodecahedron
o icosahedron), luego n (1 ≤ n ≤ 100) y n vectores de ataque, las
direcciones en que las naves vuelan hacia el centro. El cañón más
cercano nunca es ambiguo.

## Salida

El ángulo total en radianes con 5 cifras tras el punto decimal.

## Ejemplos

### Ejemplo 1

Entrada:

```
tetrahedron
5
0.00000 0.00000 -1.00000
-1.00000 0.00000 1.00000
0.00000 0.00000 -1.00000
-1.00000 0.00000 1.00000
0.00000 0.00000 -1.00000
```

Salida:

```
1.78225
```

## Solución

Una nave que vuela según v hacia el centro llega desde la dirección −v.
Los vértices de cada sólido salen de sus coordenadas clásicas (esquinas
del cubo, rectángulos áureos para el icosaedro y el dodecaedro) y se
normalizan. Para la posición inicial, un vértice pasa a ser el nuevo eje
z y un vértice vecino, sin su componente z, el nuevo eje x; cualquier
elección de vértice y vecino da la misma estación, porque las rotaciones
del sólido los llevan unos en otros.

La orientación de la estación se guarda como matriz de rotación. En cada
ataque, el cañón con mayor producto escalar con el objetivo es el más
cercano. La rotación más pequeña que lo lleva al objetivo gira el ángulo
entre ambos alrededor del eje cañón × objetivo; ese ángulo se suma al
total y la rotación, construida con la fórmula de Rodrigues, se compone
con la orientación. Un cañón que ya apunta no necesita giro. `O(V² + n · V)`
para V vértices.

Detalles a tener en cuenta:

- el vector de ataque apunta hacia el centro, así que el objetivo es el
  opuesto;
- el giro cambia la orientación para todos los ataques siguientes, así
  que hay que componer las rotaciones, no solo sumar sus ángulos;
- los vectores no tienen por qué ser unitarios (prueba 02).

Las respuestas coinciden con una implementación aceptada independiente
en 120 pruebas aleatorias, todas con un cañón más cercano claro.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1653_geometry.cpp](1653_geometry.cpp) | G++ 13.2 x64 | geometry | O(V² + n · V) | AC | 0.015 s | 484 KB |
| [1653_geometry.go](1653_geometry.go) | Go 1.14 x64 | geometry | O(V² + n · V) | AC | 0.031 s | 1152 KB |
| [1653_geometry.java](1653_geometry.java) | Java 1.8 | geometry | O(V² + n · V) | AC | 0.187 s | 5208 KB |
| [1653_geometry.py](1653_geometry.py) | Python 3.12 x64 | geometry | O(V² + n · V) | AC | 0.078 s | 1176 KB |
| [1653_geometry.rs](1653_geometry.rs) | Rust 1.75 x64 | geometry | O(V² + n · V) | AC | 0.046 s | 280 KB |
