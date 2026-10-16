# 1805. Chapáev y la rejilla de cifrado

[Timus 1805](https://acm.timus.ru/problem.aspx?space=1&num=1805) · dificultad 1010 · combinatorics

Problema original de Alexander Ipatov, de la subregión oriental del NEERC 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una rejilla de cifrado es un cuadrado de n × n con n²/4 ventanas tales
que, en sus cuatro posiciones giradas por cuartos de vuelta, las
ventanas cubren cada celda exactamente una vez. Escritas como matriz de
0 y 1 leída por filas, las rejillas se ordenan lexicográficamente.
Imprimir la k-ésima.

## Entrada

n y k (4 ≤ n ≤ 10, n par, 1 ≤ k ≤ 10¹⁸); k no supera el número de
rejillas.

## Salida

La rejilla como n filas de n dígitos.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 15
```

Salida:

```
0000
0000
1101
0001
```

## Solución

Un cuarto de vuelta mueve cada celda por una órbita de cuatro celdas, y
una rejilla abre exactamente una celda de cada órbita, así que hay
4^(n²/4) rejillas, como mucho 4²⁵. Se recorren las celdas en orden y se
prueba primero 0. Con esta celda cerrada, cada órbita sin ventana aún
puede abrir cualquiera de sus celdas no recorridas, así que el número
de tales rejillas es el producto de esas cantidades. Si k no supera ese
número la celda queda en 0; si no, k baja en él y la celda pasa a ser
la ventana de su órbita. Una celda cuya órbita ya tiene ventana es 0, y
la última celda de una órbita sin ventana es 1 a la fuerza, pues el
producto con un factor cero es 0. `O(n⁴)`.

En el ejemplo las rejillas con las dos filas superiores cerradas son
2⁴ = 16 ≥ 15, ya que cada órbita conserva sus dos celdas inferiores,
así que esas filas quedan cerradas y la elección ocurre en la mitad
inferior.

Trampas:

- las cantidades llegan a 4²⁵, unos 10¹⁵, así que hacen falta enteros
  de 64 bits;
- una órbita que ya tiene ventana deja de ser factor del producto;
- 0 va antes que 1, así que la opción cerrada se cuenta primero.

Las respuestas coinciden con una implementación aceptada independiente
en la primera, la última y rejillas aleatorias de cada tamaño, y con la
lista completa de las 256 rejillas de lado 4.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1805_combinatorics.cpp](1805_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(n^4) | AC | 0.015 s | 388 KB |
| [1805_combinatorics.go](1805_combinatorics.go) | Go 1.14 x64 | combinatorics | O(n^4) | AC | 0.031 s | 1096 KB |
| [1805_combinatorics.java](1805_combinatorics.java) | Java 1.8 | combinatorics | O(n^4) | AC | 0.109 s | 1660 KB |
| [1805_combinatorics.py](1805_combinatorics.py) | Python 3.12 x64 | combinatorics | O(n^4) | AC | 0.109 s | 596 KB |
| [1805_combinatorics.rs](1805_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(n^4) | AC | 0.031 s | 240 KB |
