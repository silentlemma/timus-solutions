# 1807. Cartuchos para la Maxim

[Timus 1807](https://acm.timus.ru/problem.aspx?space=1&num=1807) · dificultad 1474 · number_theory

Problema original de Daniil Ayzenshteyn (idea de Alex Samsonov), de la subregión oriental del NEERC 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

n cartuchos llegaron en al menos dos cajas iguales de al menos 100
cada una. Repartirlos en dos o más bolsillos de modo que el mcd de las
cantidades sea lo mayor posible y, entre esos repartos, el mcm también
lo sea. Imprimir cualquier reparto óptimo.

## Entrada

n (200 ≤ n ≤ 10⁹).

## Salida

Las cantidades de los bolsillos.

## Ejemplos

### Ejemplo 1

Entrada:

```
200
```

Salida:

```
100 100
```

### Ejemplo 2

Entrada:

```
625
```

Salida:

```
375 250
```

## Solución

Sea p el menor factor primo de n; n es compuesto, así que p ≤ 31622.
Un mcd g de al menos dos bolsillos divide a n y deja n/g ≥ 2, así que
el mayor mcd es n/p. Todo reparto óptimo es entonces n/p por partes que
suman p, y su mcm es n/p por el mcm de las partes. Entre partes menores
que p que suman p, el mayor mcm lo dan potencias de primos distintos
completadas con unos, una variante de la función de Landau. Se halla con una mochila: para
cada primo q se elige como mucho una potencia de q menor que p, con
peso la potencia y valor su logaritmo, maximizando el valor con peso
como mucho p. Una tabla de elecciones por primo reconstruye las partes.
Una búsqueda completa con todos los primos mostró una vez que la mejor
elección para cualquier primo p < 31623 nunca necesita un primo mayor
que 700, así que solo entran los primos menores que 1000. Las partes
son menores que p, así que siempre hay al menos dos bolsillos.
`O(p · π(1000) · log p)`.

En el segundo ejemplo p = 5 y n/p = 125; 5 = 2 + 3 tiene mcm 6, el
mayor posible, así que los bolsillos llevan 250 y 375.

Trampas:

- un n par da p = 2, y el único reparto son dos mitades;
- p mismo no puede ser una parte, ya que hacen falta dos bolsillos;
- el mcm puede superar los enteros de 64 bits, así que se compara su
  logaritmo.

El verificador compara el mcm exacto con el de la respuesta esperada y
comprueba la suma, el mcd y el número de bolsillos. Las respuestas
coinciden con una implementación aceptada independiente en los
cuadrados de todos los primos de 11 a 400, en el cuadrado del mayor
primo menor que 31623 y en totales aleatorios.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1807_number_theory.cpp](1807_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(p pi(1000) log p) | AC | 0.015 s | 5504 KB |
| [1807_number_theory.go](1807_number_theory.go) | Go 1.14 x64 | number_theory | O(p pi(1000) log p) | AC | 0.046 s | 14608 KB |
| [1807_number_theory.java](1807_number_theory.java) | Java 1.8 | number_theory | O(p pi(1000) log p) | AC | 0.171 s | 12444 KB |
| [1807_number_theory.py](1807_number_theory.py) | PyPy 3.10 x64 | number_theory | O(p pi(1000) log p) | AC | 0.187 s | 15384 KB |
| [1807_number_theory.rs](1807_number_theory.rs) | Rust 1.75 x64 | number_theory | O(p pi(1000) log p) | AC | 0.046 s | 5784 KB |
