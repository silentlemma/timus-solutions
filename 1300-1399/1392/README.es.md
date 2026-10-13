# 1392. Soñando con las estrellas

[Timus 1392](https://acm.timus.ru/problem.aspx?space=1&num=1392) · dificultad 763 · graphs

Problema original de Fedor Fominykh, del Primer Concurso de Programación por Equipos para Estudiantes de Secundaria de Novouralsk, abril de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

K ≤ 1000 planetas son bolas con centros y radios enteros de valor
absoluto hasta 1000. Dos planetas están pegados si comparten al menos
dos puntos, y un archipiélago es un grupo de planetas unidos por
cadenas de pares pegados al que no se pega ningún otro planeta. Hay que
imprimir los archipiélagos.

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

K y luego K líneas con x, y, z y R.

## Salida

Una línea por archipiélago con los números de sus planetas desde 0, en
orden creciente y separados por una coma y un espacio; los
archipiélagos van ordenados por su planeta menor.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
1 1 1 1
1 3 1 1
```

Salida:

```
0
1
```

### Ejemplo 2

Entrada:

```
3
1 1 1 1
1 3 1 1
1 4 1 1
```

Salida:

```
0
1, 2
```

### Ejemplo 3

Entrada:

```
3
1000 1000 1000 1
 999 1000 1000 1
   1    1    1 1
```

Salida:

```
0, 1
2
```

## Solución

Dos bolas macizas comparten más de un punto justo cuando se solapan, es
decir, cuando la distancia entre los centros es menor que r₁ + r₂; si es
igual, solo se tocan. En enteros es dx² + dy² + dz² < (r₁ + r₂)², sin
ningún redondeo. Los archipiélagos son las componentes conexas de esta
relación: se revisan todos los pares y se unen los que se solapan en
una estructura de conjuntos disjuntos. Luego se agrupan los planetas
por su raíz en orden creciente y se ordenan los grupos por su primer
planeta. `O(K²)`.

Detalles a tener en cuenta:

- las bolas que se tocan en un punto no están pegadas (ejemplos 1 y 2,
  prueba 06);
- una bola dentro de otra, aunque la toque por dentro, está pegada a
  ella (prueba 05);
- una cadena dada en desorden sigue siendo un solo archipiélago (prueba
  04);
- el separador es una coma y un espacio, sin ninguno tras el último
  planeta.

Las pruebas se juzgan por comparación exacta.

## Notas por lenguaje

- Python se ejecuta con PyPy: CPython excede el límite de 0,5 s en la
  prueba 10 del juez, y PyPy tarda unos 0,2 s.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1392_graphs.cpp](1392_graphs.cpp) | G++ 13.2 x64 | graphs | O(K^2) | AC | 0.015 s | 264 KB |
| [1392_graphs.go](1392_graphs.go) | Go 1.14 x64 | graphs | O(K^2) | AC | 0.031 s | 1224 KB |
| [1392_graphs.java](1392_graphs.java) | Java 1.8 | graphs | O(K^2) | AC | 0.171 s | 2964 KB |
| [1392_graphs.py](1392_graphs.py) | PyPy 3.10 x64 | graphs | O(K^2) | AC | 0.203 s | 5736 KB |
| [1392_graphs.rs](1392_graphs.rs) | Rust 1.75 x64 | graphs | O(K^2) | AC | 0.031 s | 320 KB |
