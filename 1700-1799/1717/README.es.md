# 1717. Reglas de admisión

[Timus 1717](https://acm.timus.ru/problem.aspx?space=1&num=1717) · dificultad 2215 · segment_tree

Problema original de Sergey Pupyrev, preparado por Alex Samsonov, de la subregión oriental del NEERC 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada uno de los n equipos tiene una edad media a, un número de
concursos f y una satisfacción s. Elegir un rango de edades y un rango
de concursos de modo que al menos dos equipos caigan en ambos y la
satisfacción total de esos equipos sea la mayor posible.

## Entrada

n (2 ≤ n ≤ 1500) y luego n líneas a f s con 4·10⁸ ≤ a ≤ 10⁹,
0 ≤ f ≤ 10⁹ y |s| ≤ 10⁹.

## Salida

El rango de edades en la primera línea y el de concursos en la segunda,
enteros de 0 a 10⁹. Se acepta cualquier par óptimo de rangos.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
500000000 1 1
510000000 3 -10
600000000 3 2
700000000 4 3
```

Salida:

```
550000000 750000000
2 5
```

## Solución

Es un rectángulo de peso máximo sobre puntos del plano, con al menos
dos puntos dentro. Solo importan los valores distintos de a y de f. Se
fija por turnos la edad menor y se sube paso a paso la mayor, añadiendo
los equipos de cada edad nueva a un árbol de segmentos sobre los
valores distintos de f.

Un nodo guarda su total, su número de equipos limitado a 2, y el mejor
prefijo y el mejor sufijo para cada cantidad exacta 0, 1 y «2 o más»,
además de su mejor rango con dos o más equipos. Aquí los prefijos y
sufijos nunca son vacíos. Dos hijos se combinan como de costumbre para
el subarreglo máximo, sumando y limitando las cantidades. Un rango que
cruza el medio une un sufijo del hijo izquierdo y un prefijo del
derecho cuyas cantidades suman al menos 2. Tras cada edad nueva, la
raíz da el mejor rango de concursos para esas edades. En total,
`O(n² log n)`.

El árbol solo halla el mejor valor y su par de edades. El rango de
concursos para ese par se vuelve a hallar con sumas prefijas en una
sola pasada. Para cada extremo derecho, el mejor izquierdo tiene la
menor suma prefija entre los que dejan al menos dos equipos dentro.

Trampas:

- un solo equipo nunca puede ser la respuesta, aunque todos los demás
  empeoren la suma (test 02);
- los equipos con la misma edad deben añadirse todos antes de leer la
  raíz, y los equipos con el mismo f comparten una hoja;
- los totales llegan a 1,5 · 10¹², así que necesitan 64 bits;
- la solución en Python corre en PyPy con el árbol en cuatro arreglos
  planos: en lugar de los tres recuentos exactos guarda solo el mejor
  prefijo y el mejor sufijo con al menos un equipo, así que un rango que
  cruza el centro de un nodo ya contiene dos equipos, y solo las hojas
  distinguen uno de dos. CPython necesita unos 5 s con 1500 equipos. Con
  PyPy tarda 0,75 s en el juez; una versión anterior con nueve arreglos
  de recuentos se quedaba sin tiempo en la prueba 5 del juez.

Un comprobador acepta cualquier par óptimo de rangos. Revisa los
límites, que se admitan al menos dos equipos y el total. Las respuestas
coinciden con una implementación aceptada independiente en 300 casos
pequeños aleatorios y en otros grandes.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1717_segment_tree.cpp](1717_segment_tree.cpp) | G++ 13.2 x64 | segment_tree | O(n² log n) | AC | 0.578 s | 308 KB |
| [1717_segment_tree.go](1717_segment_tree.go) | Go 1.14 x64 | segment_tree | O(n² log n) | AC | 0.828 s | 1656 KB |
| [1717_segment_tree.java](1717_segment_tree.java) | Java 1.8 | segment_tree | O(n² log n) | AC | 1.718 s | 5904 KB |
| [1717_segment_tree.py](1717_segment_tree.py) | PyPy 3.10 x64 | segment_tree | O(n² log n) | AC | 0.750 s | 9680 KB |
| [1717_segment_tree.rs](1717_segment_tree.rs) | Rust 1.75 x64 | segment_tree | O(n² log n) | AC | 0.781 s | 952 KB |
