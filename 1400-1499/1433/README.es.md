# 1433. Tetraedros

[Timus 1433](https://acm.timus.ru/problem.aspx?space=1&num=1433) · dificultad 264 · bruteforce

Problema original de Pavel Egorov y Stanislav Vasiliev, del Séptimo Campeonato Personal Abierto de la Universidad Estatal de los Urales, 25 de febrero de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dos tetraedros regulares del mismo tamaño tienen cada cara pintada de
R, G, B o Y. Los colores se dan en el mismo orden para ambos: la base,
la cara delantera izquierda, la delantera derecha y la trasera. Hay que
imprimir «equal» si un tetraedro puede girarse hasta verse exactamente
como el otro, y «different» si no.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Dos líneas de cuatro letras.

## Salida

«equal» o «different».

## Ejemplos

### Ejemplo 1

Entrada:

```
RGRB
GRRB
```

Salida:

```
equal
```

## Solución

Un giro del tetraedro permuta sus cuatro caras, y los giros dan
exactamente las 12 permutaciones pares: un giro sobre un eje que pasa
por un vértice mueve tres caras en ciclo, medio giro sobre un eje que
pasa por dos aristas opuestas intercambia dos pares, y una permutación
impar, como un solo intercambio, sería una imagen especular. Así que se
prueban los 24 órdenes de las caras, se conservan los que tienen un
número par de inversiones y se mira si alguno convierte la primera
coloración en la segunda. `O(1)`.

Detalles a tener en cuenta:

- las imágenes especulares son distintas: con cuatro colores distintos,
  intercambiar dos caras no es un giro (pruebas 03, 11);
- con un color repetido, cualquier disposición de los mismos colores es
  igual, porque intercambiar las dos caras iguales corrige la paridad
  (pruebas 05, 07, 08, 12).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1433_bruteforce.cpp](1433_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(1) | AC | 0.015 s | 360 KB |
| [1433_bruteforce.go](1433_bruteforce.go) | Go 1.14 x64 | bruteforce | O(1) | AC | 0.031 s | 1084 KB |
| [1433_bruteforce.java](1433_bruteforce.java) | Java 1.8 | bruteforce | O(1) | AC | 0.125 s | 1568 KB |
| [1433_bruteforce.py](1433_bruteforce.py) | Python 3.12 x64 | bruteforce | O(1) | AC | 0.078 s | 440 KB |
| [1433_bruteforce.rs](1433_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(1) | AC | 0.031 s | 224 KB |
