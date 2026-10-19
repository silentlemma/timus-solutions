# 1847. Zamkadye

[Timus 1847](https://acm.timus.ru/problem.aspx?space=1&num=1847) · dificultad 3831 · dp

Problema original de Alexander Ipatov, del Ural SU Contest en la sesión de verano de Petrozavodsk, agosto de 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

n ciudades del plano están unidas por n − 1 caminos rectos de longitud
total mínima. Un rey salió de la ciudad 1 y viajó en profundidad: desde
la ciudad actual iba por cualquier camino a una ciudad aún no vista, y
si no había ninguna volvía por donde había llegado la primera vez; cada
ciudad nueva entraba en su diario. Su hijo vuela en línea recta entre
ciudades, las visita en el orden del diario y vuelve a la ciudad 1. No
se sabe en qué orden eligió el rey los caminos: hallar el vuelo más
corto posible.

## Entrada

n (2 ≤ n ≤ 1000), las coordenadas de las n ciudades (enteros de valor
absoluto hasta 10 000, todos los puntos distintos), una línea vacía y
los n − 1 caminos como pares de ciudades.

## Salida

El vuelo más corto, con error relativo de como mucho 10⁻⁹.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
0 0
1 0
1 1
0 1

1 2
1 4
4 3
```

Salida:

```
4.000
```

## Solución

El diario es un recorrido en preorden del árbol con raíz en la ciudad
1, con los hijos de cada ciudad en cualquier orden. El vuelo por un
subárbol empieza en su raíz y, como el subárbol de cada hijo termina
antes de que empiece el siguiente, acaba en una de sus hojas. Así, para
cada ciudad u y cada hoja e debajo de ella, sea cost(u, e) el vuelo más
corto por el subárbol de u que termina en e.

Dentro de u los hijos se recorren en algún orden. Entrar en el hijo b
justo después de terminar el hijo a cuesta link(a, b) = mínimo sobre
las hojas e de a de cost(a, e) + |e b|, que no depende de lo anterior.
Por tanto el orden de los hijos es un problema de camino mínimo sobre
subconjuntos: enter(m, b) es lo más barato para terminar los hijos del
conjunto m con b el último, partiendo de enter({b}, b) = |u b| y
creciendo con enter(m, a) + link(a, b). Entonces
cost(u, e) = enter(todos, b) + cost(b, e) para una hoja e del hijo b, y
la respuesta es el menor cost(1, e) + |e 1|.

Los caminos forman un árbol generador mínimo de puntos del plano, donde
dos aristas de una ciudad forman un ángulo de al menos 60°, así que una
ciudad tiene como mucho seis vecinos y el paso por subconjuntos cuesta
como mucho 2⁶·6² por ciudad. Calcular los link recorre cada hoja bajo
una ciudad como mucho seis veces, y una hoja está bajo como mucho n
ciudades, así que esta parte es `O(n²)`. Las ciudades se procesan de
hijos a padres, en orden inverso de anchura, para evitar una recursión
profunda.

En el ejemplo el árbol es 1 – 2 y 1 – 4 – 3. Visitar primero 2 da 1, 2,
4, 3 y un vuelo de 1 + √2 + 1 + 1; visitar primero 4 da 1, 4, 3, 2 y
cuatro pasos unidad, 4.

Trampas:

- el vuelo por un subárbol siempre empieza en su raíz, y por eso
  link(a, b) no depende del resto del orden;
- la cota del grado viene de que el árbol es mínimo; con un árbol
  cualquiera el paso por subconjuntos sería exponencial.

Las respuestas coinciden con una implementación aceptada independiente
en sesenta conjuntos aleatorios de hasta 1000 ciudades, incluidas
rejillas con muchos caminos iguales, espinas largas y estrellas de cinco
brazos anidadas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1847_dp.cpp](1847_dp.cpp) | G++ 13.2 x64 | dp | O(n^2) | AC | 0.015 s | 596 KB |
| [1847_dp.go](1847_dp.go) | Go 1.14 x64 | dp | O(n^2) | AC | 0.031 s | 2312 KB |
| [1847_dp.java](1847_dp.java) | Java 1.8 | dp | O(n^2) | AC | 0.156 s | 2764 KB |
| [1847_dp.py](1847_dp.py) | Python 3.12 x64 | dp | O(n^2) | AC | 0.109 s | 1196 KB |
| [1847_dp.rs](1847_dp.rs) | Rust 1.75 x64 | dp | O(n^2) | AC | 0.046 s | 532 KB |
