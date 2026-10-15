# 1708. Suma de dígitos 2

[Timus 1708](https://acm.timus.ru/problem.aspx?space=1&num=1708) · dificultad 11130 · math

Problema original de Vladimir Yakovlev, del XIII Campeonato de los Urales de Programación Competitiva, 4 de abril de 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un número positivo en base b es mínimo si ningún número menor tiene la
misma suma de dígitos y la misma suma de cuadrados de los dígitos. Hay
que describir todos los números mínimos con la lista de patrones más
corta. Un patrón se forma con dígitos y asteriscos, y un asterisco deja
que el dígito anterior se repita cualquier número de veces, incluso
ninguna. Todo número que encaje en algún patrón debe ser mínimo, y todo
número mínimo debe encajar en algún patrón.

## Entrada

La base b, 2 ≤ b ≤ 36.

## Salida

Los patrones ordenados como cadenas, uno por línea, con los dígitos
1 … 9, A, B, … y sin partes sobrantes: 12*3 y no 12*2*3. Un patrón
también puede encajar con la cadena vacía.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
```

Salida:

```
1*2*
112*3*
12*3*
2*3*
```

## Solución

Ninguna de las dos sumas depende del orden de los dígitos, así que un
número mínimo no tiene ceros y sus dígitos no decrecen: es un
multiconjunto de los dígitos 1 … b − 1, un vector de conteos. De dos
vectores con sumas iguales, es menor el que tiene menos dígitos. Con la
misma longitud, se mira el primer dígito cuyos conteos difieren: es
menor el vector con más copias de él. La comparación depende solo de la
diferencia de los vectores, así que añadir los mismos dígitos a ambos
nunca la cambia.

Quitar dígitos de un número mínimo deja un número mínimo, de modo que
los vectores mínimos son justo los que no están por encima de ninguno
de los vectores no mínimos minimales, llamados prohibidos más abajo.
Para hallarlos, se calcula para cada par (suma, suma de cuadrados)
alcanzable con a lo sumo 15 dígitos su vector mínimo. Se añaden los
dígitos en orden creciente y se guarda solo la mejor palabra de cada
par: por la observación anterior, la mejor sigue siéndolo tras
cualquier extensión. Un vector prohibido sin su dígito mayor es mínimo,
así que sale de alargar una palabra mínima con un dígito al final. La
palabra alargada está prohibida si no es la mínima de su par, mientras
que toda palabra con un dígito menos sí lo es. La base 36 tiene unos
720000 pares y 25000 vectores prohibidos. Ninguno pasa de 15 dígitos, y
subir el tope a 17 no encuentra otros.

Los patrones salen de una recursión sobre el último dígito. Sea G un
conjunto de vectores prohibidos sobre los dígitos 1 … n y t el mayor
conteo del dígito n en G. Con k < t copias, un prefijo debe evitar los
vectores de G con a lo sumo k copias, quitando el dígito n y dejando
solo los minimales. Con t copias o más, el prefijo debe evitarlos todos,
y ese caso se vuelve un asterisco. Así, los patrones son los del caso
del asterisco seguidos de n*, y para cada k < t los de su caso seguidos
de k copias. Ahí se descartan los patrones de prefijo que ya lo evitan
todo, pues el asterisco los cubre. Estos conjuntos crecen con k. Como G
solo tiene vectores minimales, un recién llegado nunca está por encima
de uno anterior, así que cada paso solo descarta los anteriores que
están por encima de algún recién llegado. Los mismos conjuntos se
repiten a menudo, así que los resultados se memorizan. Los patrones se
guardan en un trie de nodos (padre, conteo), y el resultado de un
conjunto son unos pocos tramos de nodos consecutivos. La base 36 acaba
con unos 2,1 millones de nodos y 47062 patrones.

Trampas:

- el límite de memoria es 64 MB: las palabras mínimas se guardan de forma
  compacta en una tabla de direccionamiento abierto, que se libera antes
  de construir los patrones;
- la prueba más frecuente es si un vector está por encima de uno de
  muchos otros: estos se agrupan por sus conjuntos de conteos no nulos,
  y solo se revisan los grupos dentro del conjunto del vector probado;
- la base 2 tiene un único patrón, 1*, y la base 36 imprime unos
  325 KB;
- Java y Python construyen los mismos patrones de otra forma, que cabe
  en los límites del juez: allí Java tarda 0,27 s y Python, con PyPy,
  1,75 s, mientras que versiones anteriores con la recursión descrita
  arriba se quedaban sin tiempo en las pruebas 30 y 22. Enumeran las
  palabras mínimas por niveles en orden lexicográfico, de modo que la
  primera palabra que llega a un par de sumas es su mínima, en una tabla
  indexada directamente por el par: para cada suma, las sumas de
  cuadrados forman un intervalo de una misma paridad. Una palabra solo
  se extiende con los dígitos que admiten todas las palabras con un
  dígito menos, lo que omite las palabras prohibidas no minimales. Cada
  patrón es una palabra mínima con a lo sumo dos asteriscos, sobre un
  dígito o sobre dos dígitos vecinos: borrar todas las copias de un
  dígito, o de dos dígitos vecinos, de una palabra prohibida da una
  palabra finita que bloquea ese asterisco, y un asterisco bloqueado
  pasa de cada palabra a sus extensiones. `O(P · (b + L))` para P pares
  de sumas y palabras de a lo sumo L = 15 dígitos.

Para cada base de 2 a 36 la salida es idéntica a la de una
implementación aceptada independiente.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1708_math.cpp](1708_math.cpp) | G++ 13.2 x64 | math | O(b⁴ · L² + N · b) | AC | 2.375 s | 29376 KB |
| [1708_math.go](1708_math.go) | Go 1.14 x64 | math | O(b⁴ · L² + N · b) | AC | 3.828 s | 39212 KB |
| [1708_math.java](1708_math.java) | Java 1.8 | math | O(P · (b + L)) | AC | 0.265 s | 25728 KB |
| [1708_math.py](1708_math.py) | PyPy 3.10 x64 | math | O(P · (b + L)) | AC | 1.750 s | 29456 KB |
| [1708_math.rs](1708_math.rs) | Rust 1.75 x64 | math | O(b⁴ · L² + N · b) | AC | 2.671 s | 35628 KB |
