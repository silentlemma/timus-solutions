# 1511. Operaciones fiscales

[Timus 1511](https://acm.timus.ru/problem.aspx?space=1&num=1511) · dificultad 1212 · dp

Problema original de Nikita Rybak, Ilya Grebnov y Dmitry Kovalioff, de Timus Top Coders: Third Challenge.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una declaración de impuestos da tres números positivos A, B y C (cada
uno menor que 10¹⁰⁰⁰), pero A + B ≠ C. Una cifra puede cambiarse por
otra con una multa igual al valor absoluto de la diferencia de ambas;
la longitud de un número no puede cambiar y su primera cifra no puede
pasar a ser 0. Hay que hallar la menor multa total que logre
A + B = C, o escribir -1.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

A, B y C, uno por línea.

## Salida

La menor multa total, o -1.

## Ejemplos

### Ejemplo 1

Entrada:

```
123
554
345
```

Salida:

```
8
```

## Solución

A y B no pueden ser más largos que C, porque su suma también lo sería.
Si no, se suma columna a columna desde la cifra más baja, como en
papel, con el acarreo como estado: cost[carry] es el arreglo más barato
de las columnas ya hechas que pasa ese acarreo. En cada columna se
prueba cada cifra x para A e y para B (solo 0 fuera de la longitud del
número, y no 0 en su primera cifra); la cifra de C es entonces
(x + y + carry) mod 10, que no puede ser 0 en la primera cifra de C, y
la multa es la suma de las tres diferencias. La respuesta es cost[0]
tras la última columna de C. Como mucho 2 · 100 transiciones por
columna, `O(len(C))` con un factor de 200.

Detalles a tener en cuenta:

- la primera cifra no puede pasar a 0, así que 1 + 1 = 1 obliga a
  cambiar C por 2 (prueba 02);
- C más corto que A, o dos cifras más largo que cualquier suma, da -1
  (pruebas 03, 04, gen3);
- cuando C tiene una cifra más, las columnas altas de A y B deben
  llevarse una (prueba 06, gen2);
- los números tienen hasta 1000 cifras, así que se tratan como cadenas
  de cifras (gen1, gen5).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1511_dp.cpp](1511_dp.cpp) | G++ 13.2 x64 | dp | O(len(C)) | AC | 0.031 s | 388 KB |
| [1511_dp.go](1511_dp.go) | Go 1.14 x64 | dp | O(len(C)) | AC | 0.031 s | 1080 KB |
| [1511_dp.java](1511_dp.java) | Java 1.8 | dp | O(len(C)) | AC | 0.125 s | 636 KB |
| [1511_dp.py](1511_dp.py) | Python 3.12 x64 | dp | O(len(C)) | AC | 0.171 s | 768 KB |
| [1511_dp.rs](1511_dp.rs) | Rust 1.75 x64 | dp | O(len(C)) | AC | 0.046 s | 228 KB |
