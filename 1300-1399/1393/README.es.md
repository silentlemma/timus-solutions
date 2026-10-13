# 1393. Prefijo común medio

[Timus 1393](https://acm.timus.ru/problem.aspx?space=1&num=1393) · dificultad 1161 · strings

Problema original de Ilya Grebnov.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

T es una cadena de n letras mayúsculas, 1 < n ≤ 250 000. Hay que
ordenar sus n desplazamientos cíclicos, incluidos los iguales, e
imprimir la longitud media del prefijo común más largo de los
desplazamientos vecinos en ese orden, con al menos tres cifras
decimales. Dos desplazamientos iguales comparten las n letras.

Límite de tiempo: 1,5 segundos. Límite de memoria: 16 MB.

## Entrada

n y luego T.

## Salida

El prefijo común medio.

## Ejemplos

### Ejemplo 1

Entrada:

```
11
MISSISSIPPI
```

Salida:

```
1.300
```

## Solución

Los desplazamientos iguales hacen ambiguo el orden y estropean la forma
habitual de hallar prefijos comunes, así que primero se quitan. Sea p el
periodo más corto de T como cadena cíclica, hallado con la función
prefijo: T es una palabra u de p letras repetida n / p veces (p = n si no
hay tal periodo). Entonces cada desplazamiento de T aparece n / p veces
seguidas, lo que da p·(n / p − 1) pares de vecinos con prefijo común n.
Dos desplazamientos distintos de u difieren dentro de p letras, así que
su prefijo común en T es el mismo que en u.

Las p rotaciones de u son todas distintas. Se ordenan por duplicación de
prefijos con ordenación por conteo: rotaciones ordenadas por sus
primeras 2ᵏ letras y luego por pares de clases. Después, el recorrido de
Kasai da el prefijo común de cada rotación con la anterior: al pasar de
la rotación i a la i + 1 se pierde a lo sumo una letra, así que el
trabajo total es lineal. La respuesta es la suma de ambas partes entre
n − 1, con la suma en 64 bits. `O(n log n)`.

Detalles a tener en cuenta:

- los desplazamientos iguales tienen prefijo común n, no más: para AAAAA
  la respuesta es 5.000 (prueba 02 y prueba generada 2);
- la suma llega a 6,25·10¹⁰ y necesita 64 bits (prueba generada 2);
- una cadena de una sola letra salvo la última necesita unos log n pasos
  de duplicación (prueba generada 3);
- el límite de memoria es de 16 MB, así que los arreglos usan números de
  32 bits.

Las respuestas se compararon en 1 500 cadenas cortas aleatorias, un
tercio de ellas periódicas, ordenando todos los desplazamientos y
comparándolos letra a letra.

## Notas por lenguaje

- No se espera que Python pase: en las pruebas más grandes necesita unos
  1,2 s y más de 50 MB con CPython y más de 150 MB con PyPy, frente a un
  límite de 16 MB; da respuestas correctas en todas las pruebas de aquí.
  En el juez excede el límite de memoria en la prueba 30 y se mantiene
  marcada MLE.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1393_strings.cpp](1393_strings.cpp) | G++ 13.2 x64 | strings | O(n log n) | AC | 0.109 s | 4928 KB |
| [1393_strings.go](1393_strings.go) | Go 1.14 x64 | strings | O(n log n) | AC | 0.218 s | 9364 KB |
| [1393_strings.java](1393_strings.java) | Java 1.8 | strings | O(n log n) | AC | 0.218 s | 7948 KB |
| [1393_strings.py](1393_strings.py) | Python 3.12 x64 | strings | O(n log n) | MLE (test 30) | 0.218 s | 18088 KB |
| [1393_strings.rs](1393_strings.rs) | Rust 1.75 x64 | strings | O(n log n) | AC | 0.109 s | 5504 KB |
