# 1920. Todas las longitudes pares de ciclos en una cuadrícula

[Timus 1920](https://acm.timus.ru/problem.aspx?space=1&num=1920) · difficulty 727 · constructive

Problema original de Alexey Samsonov, preparado por Dmitry Ivankov; subregión oriental del NEERC 2012.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Construir un ciclo simple de exactamente L nodos en una cuadrícula n×n.
Nodos consecutivos, incluidos el último y el primero, deben estar a una
unidad de distancia. Ningún nodo puede usarse dos veces. Las coordenadas
son enteras de 1 a n. Dar cualquier ciclo válido o declarar que no existe.
Límites: 1 segundo y 64 MB.

## Entrada

Dos enteros n,L con 2≤n≤100 y 4≤L≤20 000.

## Salida

Si es imposible, imprimir `Unsuitable device`. En otro caso imprimir
`Overwhelming power of magic`, seguido de L pares de coordenadas,
uno por línea en orden de recorrido. No repetir el primer nodo al final.
Se acepta cualquier ciclo válido, punto de inicio y dirección.

## Evaluación

Un comprobador propio valida la cabecera, cantidad, coordenadas enteras
dentro del rango, vértices distintos y distancia Manhattan uno para
cada arista, incluida la de cierre. Rechaza declaraciones falsas de
imposibilidad. El camino esperado no es canónico y no se compara por tokens.

## Ejemplos

```
2 6
```

```
Unsuitable device
```

```
3 6
```

```
Overwhelming power of magic
1 1
2 1
3 1
3 2
2 2
1 2
```

## Solución

Coloreamos (r,c) según la paridad de r+c. Cada arista cambia de color,
así que todo ciclo tiene longitud par. La unicidad exige además L≤n².
Construiremos todos los pares desde 4 hasta M=n²−(n mod 2), demostrando
que esas condiciones también son suficientes.

Partimos del contorno de un cuadrado 2×2, de longitud 4. Una extensión
sustituye una arista u—v por u—a—b—v usando dos nodos nuevos adyacentes
al otro lado de la arista. Añade dos vértices y conserva las aristas
unitarias y un único ciclo simple.

Sea W=n−(n mod 2), un número par. Seguimos este orden fijo:

1. Extender el rectángulo de dos filas hasta anchura W, columna a columna,
   desviando la arista vertical derecha por los dos nodos de la nueva columna.
2. Añadir filas 3 a n. En cada fila procesar columnas por pares (1,2),
   (3,4), …, (W−1,W), desviando la arista horizontal superior por el par nuevo.
3. Si n es impar, añadir la última columna por pares de filas (1,2),
   (3,4), …, (n−2,n−1), usando las aristas verticales a su izquierda.

Las aristas necesarias siempre existen. La primera etapa conserva el
borde inferior completo. Cada desvío de la segunda crea la arista de par
para la siguiente fila y conserva el borde vertical derecho. La tercera
usa aristas disjuntas de ese borde. Los nodos añadidos siempre son nuevos;
por ello también se puede parar a mitad de una fila.

Si n es par, la segunda etapa cubre los n² nodos. Si es impar, la tercera
deja solo la esquina inferior derecha, obteniendo n²−1. Como cada paso
añade dos, detenerse tras (L−4)/2 extensiones produce cualquier longitud
par hasta M. Esto prueba la construcción y el criterio de imposibilidad.

Codificamos coordenadas desde cero como r·n+c y guardamos cada arista
dirigida en un arreglo de sucesores. Si la arista elegida está invertida,
invertimos tanto los extremos viejos como los nuevos. Modificamos tres
enlaces y, al terminar, recorremos exactamente L vértices desde la esquina
superior izquierda, convirtiendo las coordenadas a índices desde uno.

O(n²+L) tiempo y espacio, incluidos inicialización del arreglo y salida
almacenada. Cada extensión de dos vértices cambia O(1) enlaces.
Una entrada imposible se rechaza en O(1).

Una cuadrícula impar no permite todos sus nodos, pero sí n²−1,
no solo n(n−1). No omitir la última columna. Al invertir una arista,
intercambiar ambos pares de extremos. Parar tras el número exacto de
extensiones, permitir la última fila parcial y cerrar el ciclo sin
volver a imprimir el primer nodo.

## Notas por lenguaje

Índices y longitudes caben en enteros ordinarios. C++, Go, Java y Rust
usan arreglos planos y bucles explícitos. Python genera el mismo orden
de extensiones de forma perezosa. Java, Python y Rust almacenan la salida;
Go usa E/S con búfer y C++ desactiva sincronización de flujos.
Los enlaces evitan desplazar una lista con cada inserción.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1920_constructive.cpp](1920_constructive.cpp) | G++ 13.2 x64 | constructive | O(n^2 + L) | AC | 0.031 s | 472 KB |
| [1920_constructive.go](1920_constructive.go) | Go 1.14 x64 | constructive | O(n^2 + L) | AC | 0.031 s | 1408 KB |
| [1920_constructive.java](1920_constructive.java) | Java 1.8 | constructive | O(n^2 + L) | AC | 0.125 s | 948 KB |
| [1920_constructive.py](1920_constructive.py) | Python 3.12 x64 | constructive | O(n^2 + L) | AC | 0.093 s | 2028 KB |
| [1920_constructive.rs](1920_constructive.rs) | Rust 1.75 x64 | constructive | O(n^2 + L) | AC | 0.031 s | 296 KB |
