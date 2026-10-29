# 1136. Pasar el orden izquierda-derecha-raíz de un árbol de búsqueda al orden derecha-izquierda-raíz

[Timus 1136](https://acm.timus.ru/problem.aspx?space=1&num=1136) · dificultad 100 · trees

Problema original del cuarto de final de la región central de Rusia, Rybinsk, 17–18 de octubre de 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Los miembros de un parlamento, con números positivos distintos, se
sientan como en un árbol binario de búsqueda: el primero es el
presidente, y cada siguiente va a la izquierda si su número es menor que
el del presidente actual y a la derecha en otro caso, hasta encontrar un
asiento libre. En las sesiones impares hablan en el orden ala izquierda,
ala derecha, presidente, de forma recursiva; en las pares, ala derecha,
ala izquierda, presidente. Dado el orden de la sesión impar de `N ≤ 3000`
miembros con números hasta 65535, imprime el orden de la sesión par.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y luego los `N` números en el orden de la sesión impar.

## Salida

Los números en el orden de la sesión par, uno por línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
9
1
7
5
21
22
27
25
20
10
```

Salida:

```
27
21
22
25
20
7
1
5
10
```

## Solución

El orden de la sesión impar es el recorrido en postorden del árbol de
búsqueda: ala izquierda, ala derecha, presidente. Leído al revés, cada
presidente aparece antes que todos los miembros de sus alas. Por eso,
insertar los números en un árbol binario de búsqueda vacío en ese orden
invertido pone a cada miembro exactamente donde estaba: su presidente ya
está en su sitio cuando llega. El orden de la sesión par es entonces un
recorrido recursivo: ala derecha, ala izquierda, presidente.

Cada inserción baja desde la raíz. En una cadena de 3000 miembros son
hasta 3000 pasos, unos 4,5 millones en total: `O(N^2)`, aún rápido.

Detalles a tener en cuenta:

- el árbol puede ser una cadena de profundidad 3000, y la recursión del
  recorrido también; Python sube su límite de recursión;
- puede haber varios números por línea; se leen como palabras;
- con un solo miembro, ambos órdenes coinciden.

Las respuestas de ambos métodos se compararon en todas las pruebas y en
300 parlamentos aleatorios, lo que además comprobó que cada entrada es un
orden válido de sesión impar.

## Soluciones optimizadas

Las soluciones optimizadas reconstruyen el árbol en una pasada, `O(N)`.
Leído al revés, el orden de la sesión impar da cada presidente, luego toda
el ala derecha y luego toda el ala izquierda. Se mantiene una pila de
presidentes a los que aún puede llegar el ala izquierda:

- si el siguiente número es mayor que la cima de la pila, es el hijo
  derecho de esa cima;
- si no, se sacan todos los presidentes mayores que él; el último sacado
  es el presidente cuya ala izquierda empieza él, y el número pasa a ser su
  hijo izquierdo.

Cada número entra en la pila una vez y sale como mucho una vez. El orden de
la sesión par es el orden normal raíz, izquierda, derecha leído al revés,
que una segunda pila explícita produce sin recursión. Los hijos se indexan
por la posición en la entrada; Go además analiza la entrada a mano. C++
ocupa 188 KB en lugar de 348 KB y Go 1052 KB en lugar de 2200 KB, ambos
con el mismo tiempo; Python tarda 0.078 s en lugar de 0.500 s y ocupa
1028 KB en lugar de 1508 KB. Java y Rust solo tienen las soluciones
sencillas.

## Notas por lenguaje

- Las soluciones simples recorren el árbol de forma recursiva, hasta 3000
  llamadas de profundidad: ningún lenguaje necesita una pila mayor para
  eso, y Python solo sube su límite de recursión.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1136_trees.cpp](1136_trees.cpp) | G++ 13.2 x64 | trees | O(N^2) | AC | 0.015 s | 348 KB | 11303079 |
| [1136_trees.go](1136_trees.go) | Go 1.14 x64 | trees | O(N^2) | AC | 0.031 s | 2200 KB | 11303083 |
| [1136_trees.java](1136_trees.java) | Java 1.8 | trees | O(N^2) | AC | 0.109 s | 640 KB | 11303090 |
| [1136_trees.py](1136_trees.py) | Python 3.12 x64 | trees | O(N^2) | AC | 0.500 s | 1508 KB | 11303091 |
| [1136_trees.rs](1136_trees.rs) | Rust 1.75 x64 | trees | O(N^2) | AC | 0.031 s | 804 KB | 11303094 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1136_trees_optimized.cpp](1136_trees_optimized.cpp) | G++ 13.2 x64 | trees | O(N) | AC | 0.015 s | 188 KB | 11303566 |
| [1136_trees_optimized.go](1136_trees_optimized.go) | Go 1.14 x64 | trees | O(N) | AC | 0.031 s | 1052 KB | 11303567 |
| [1136_trees_optimized.py](1136_trees_optimized.py) | Python 3.12 x64 | trees | O(N) | AC | 0.078 s | 1028 KB | 11303568 |
