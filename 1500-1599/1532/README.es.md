# 1532. Perdido en la traducción

[Timus 1532](https://acm.timus.ru/problem.aspx?space=1&num=1532) · dificultad 1976 · hashing

Problema original de Sergey Pupyrev, del Octavo Campeonato Personal Abierto de la Universidad Estatal de los Urales, 3 de marzo de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una lista contiene K palabras distintas (1 ≤ K ≤ 5000) de 1 a 15 letras
minúsculas inglesas. Algunas son faltas de ortografía de otras: una palabra mal
escrita tiene como mucho dos errores, cada uno una letra que falta, una
letra de más o una letra equivocada, y la forma correcta de cada palabra
está en la lista. Hay que escribir, en orden lexicográfico, cada palabra
que aparece más de una vez contando sus faltas de ortografía.

Límite de tiempo: 4 segundos. Límite de memoria: 64 MB.

## Entrada

K y luego las K palabras, una por línea.

## Salida

El número de esas palabras y luego las palabras, una por línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
7
lomba
pella
palpa
papa
moina
morna
sin
```

Salida:

```
5
moina
morna
palpa
papa
pella
```

## Solución

Como todas las formas correctas están en la lista, una palabra entra en
la respuesta exactamente cuando otra palabra está a dos ediciones o
menos de ella. Tomemos una alineación óptima de dos de esas palabras:
cada sustitución borra una letra de ambas palabras, cada letra de más
borra una letra de una de ellas, y lo que queda es la misma cadena, el
resto. Así que cada palabra borra como mucho dos letras. A la inversa,
si al borrar letras de dos palabras queda el mismo resto, se anota para
cada letra borrada su hueco: el número de letras del resto que hay antes
de ella. Dentro de un hueco, las letras borradas de las dos palabras se
emparejan con sustituciones y las sobrantes se insertan, así que las
palabras están a lo sumo a la suma, sobre los huecos, de la mayor de
las dos cantidades.

Para dos palabras con el mismo resto, que han perdido c y d letras, esa
suma es como mucho dos en estos casos:

- c + d ≤ 2;
- c = 2 y d = 1, con el hueco único igual a uno de los dos huecos;
- c = d = 2, con los mismos dos huecos.

Cada palabra da como mucho 1 + 15 + 105 = 121 claves: el resto,
empaquetado en un entero con 5 bits por letra (Python toma sus bytes), el número de la palabra,
cuántas letras se borraron y sus huecos. Una palabra nunca da los mismos
huecos dos veces. Tras ordenar, cada grupo con el mismo resto se revisa:
si el resto es una palabra, todo el grupo está cerca
de ella; dos palabras que perdieron una letra cada una están cerca; una
palabra que perdió dos letras está cerca de otra que perdió dos en los
mismos huecos o una en uno de sus huecos. Al empaquetar con 5 bits por
letra, un resto ocupa hasta 75 bits, así que C++ y Rust usan claves de
128 bits, Go usa dos campos de 64 bits y Java sustituye las primeras
12 letras por su posición entre todos los comienzos.
`O(K·L²·(L + log(K·L)))` con L ≤ 15.

Detalles a tener en cuenta:

- compartir el resto no basta: abcde y bcdxy dan bcd tras dos borrados,
  pero en huecos distintos, y están a tres ediciones (prueba 05);
- intercambiar dos letras vecinas son dos ediciones (prueba 03);
- las longitudes que difieren en tres o más nunca coinciden (prueba 07);
- la respuesta puede estar vacía; se escribe 0 (pruebas 02, 04).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1532_hashing.cpp](1532_hashing.cpp) | G++ 13.2 x64 | hashing | O(K * L^2 * (L + log(K * L))) | AC | 0.109 s | 17484 KB |
| [1532_hashing.go](1532_hashing.go) | Go 1.14 x64 | hashing | O(K * L^2 * (L + log(K * L))) | AC | 0.375 s | 35180 KB |
| [1532_hashing.java](1532_hashing.java) | Java 1.8 | hashing | O(K * L^2 * (L + log(K * L))) | AC | 0.421 s | 27344 KB |
| [1532_hashing.py](1532_hashing.py) | Python 3.12 x64 | hashing | O(K * L^2 * (L + log(K * L))) | AC | 1.953 s | 39528 KB |
| [1532_hashing.rs](1532_hashing.rs) | Rust 1.75 x64 | hashing | O(K * L^2 * (L + log(K * L))) | AC | 0.093 s | 17732 KB |
