# 1846. MCD 2010

[Timus 1846](https://acm.timus.ru/problem.aspx?space=1&num=1846) · dificultad 155 · segment_tree

Problema original de Alexey Samsonov, del Ural SU Contest en la sesión de verano de Petrozavodsk, agosto de 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un multiconjunto de enteros positivos empieza vacío. Cada operación
añade un número o quita una copia de un número que está. Tras cada
operación imprimir el máximo común divisor de todo el multiconjunto; el
mcd del multiconjunto vacío se declara igual a 1.

## Entrada

q (1 ≤ q ≤ 10⁵), luego q líneas "+ x" o "- x" con 1 ≤ x ≤ 10⁹. Solo se
quitan números presentes.

## Salida

El mcd tras cada operación, uno por línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
+ 8
+ 6
+ 8
- 8
- 8
```

Salida:

```
8
2
2
2
6
```

## Solución

Un mcd no se puede deshacer, así que quitar un número necesita una
estructura. Cada adición recibe su propia hoja en un árbol de segmentos
sobre las operaciones, y para cada valor se guarda una pila de las hojas
que lo contienen. Añadir x escribe x en la hoja de esa operación; quitar
x vacía la hoja de la cima de su pila escribiendo 0, lo que no cambia
ningún mcd porque mcd(a, 0) = a. Cada nodo interno guarda el mcd de sus
hijos, así que la raíz es el mcd del multiconjunto, y una raíz 0
significa que está vacío: se imprime 1. Actualizar una hoja recalcula
sus antepasados, y la subida puede parar en el primer nodo cuyo valor no
cambia, porque entonces nada por encima cambia. `O(q log q log x)`.

En el ejemplo las hojas guardan 8, 6 y 8, así que el mcd es 2. Quitar
los dos 8 vacía dos hojas y deja el 6.

Trampas:

- el multiconjunto vacío imprime 1, no 0;
- números iguales pueden añadirse varias veces y quitarse de uno en
  uno;
- con medio segundo importan tanto parar pronto la subida como leer
  rápido; la solución en Python corre en PyPy.

Las respuestas coinciden con una implementación aceptada independiente
en treinta archivos aleatorios de hasta 10⁵ operaciones.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1846_segment_tree.cpp](1846_segment_tree.cpp) | G++ 13.2 x64 | segment_tree | O(q log q log x) | AC | 0.171 s | 8616 KB |
| [1846_segment_tree.go](1846_segment_tree.go) | Go 1.14 x64 | segment_tree | O(q log q log x) | AC | 0.078 s | 14000 KB |
| [1846_segment_tree.java](1846_segment_tree.java) | Java 1.8 | segment_tree | O(q log q log x) | AC | 0.140 s | 10080 KB |
| [1846_segment_tree.py](1846_segment_tree.py) | PyPy 3.10 x64 | segment_tree | O(q log q log x) | AC | 0.250 s | 37060 KB |
| [1846_segment_tree.rs](1846_segment_tree.rs) | Rust 1.75 x64 | segment_tree | O(q log q log x) | AC | 0.046 s | 12328 KB |
