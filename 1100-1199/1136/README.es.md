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
búsqueda, y el postorden de un árbol binario de búsqueda con claves
distintas determina el árbol. Leído al revés, da cada presidente, luego
toda el ala derecha y luego toda el ala izquierda. El árbol se reconstruye
en una pasada por esa lista invertida con una pila de presidentes a los
que aún puede llegar el ala izquierda:

- si el siguiente número es mayor que la cima de la pila, es el hijo
  derecho de esa cima;
- si no, se sacan todos los presidentes mayores que él; el último sacado
  es el presidente cuya ala izquierda empieza, y el número pasa a ser su
  hijo izquierdo.

Cada número entra en la pila una vez y sale como mucho una vez, así que
es `O(N)`. El orden de la sesión par es el orden normal raíz, izquierda,
derecha leído al revés, que una pila explícita produce sin recursión.

Detalles a tener en cuenta:

- el árbol puede ser una cadena de profundidad 3000, así que se evita la
  recursión;
- puede haber varios números por línea; se leen como palabras;
- con un solo miembro, ambos órdenes coinciden.

Las respuestas se compararon en todas las pruebas y en 300 parlamentos
aleatorios con una reconstrucción por inserción simple y recorridos
recursivos, que además comprobó que cada entrada es un orden válido de
sesión impar.

## Notas por lenguaje

- Todos los lenguajes usan las mismas dos pilas, con los hijos en arrays
  indexados por el número del miembro.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1136_trees.cpp](1136_trees.cpp) | G++ 13.2 x64 | trees | O(N) | AC | 0.015 s | 776 KB |
| [1136_trees.go](1136_trees.go) | Go 1.14 x64 | trees | O(N) | AC | 0.046 s | 2396 KB |
| [1136_trees.java](1136_trees.java) | Java 1.8 | trees | O(N) | AC | 0.093 s | 1524 KB |
| [1136_trees.py](1136_trees.py) | Python 3.12 x64 | trees | O(N) | AC | 0.078 s | 1336 KB |
| [1136_trees.rs](1136_trees.rs) | Rust 1.75 x64 | trees | O(N) | AC | 0.046 s | 1296 KB |
