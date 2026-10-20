# 2184. El mayor tamaño de montón cuando uno se repartió entre dos cofres

[Timus 2184](https://acm.timus.ru/problem.aspx?space=1&num=2184) · dificultad 1216 · number_theory

Problema original de Artyom Stepanov, del Concurso Escolar de Programación de los Urales 2024.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Las monedas se repartieron en montones de d en n cofres, cada montón
entero en un cofre, salvo el último, que se dividió de cualquier manera
entre dos cofres. Dado el contenido aᵢ de los cofres, hallar el mayor d
posible. Los límites son 1 segundo y 256 MB.

## Entrada

n, 2 ≤ n ≤ 10⁵, y luego a₁ … a_n con 0 ≤ aᵢ ≤ 10¹², no todos cero.

## Salida

El mayor d.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
5 8 7 100
```

Salida:

```
5
```

### Ejemplo 2

Entrada:

```
5
9 4 6 5 12
```

Salida:

```
3
```

### Ejemplo 3

Entrada:

```
6
4 8 16 24 12 40
```

Salida:

```
8
```

## Solución

Los cofres guardan un número entero de montones en total, así que d
divide la suma S, y cada cofre salvo los dos que compartieron el último
montón tiene un múltiplo de d. Al revés, si d divide S y todos los aᵢ
salvo dos, los dos restos suman 0 o d, que es un montón dividido. Así
que la respuesta es el mayor mcd de S con todos los valores salvo a lo
sumo dos.

Quitar un valor solo ayuda donde cambia un mcd acumulado. Sean i < j los
quitados. Si el mcd de S y los valores antes de i ya divide aᵢ,
conservar aᵢ no cambia nada, y lo mismo para j con los valores después.
Así que i se puede buscar entre las posiciones donde cambia el mcd de
prefijo (empezado en S), y j entre las que cambia el de sufijo. Cada
cambio al menos divide a la mitad un número de hasta 10¹⁷, así que hay
menos de 60 de cada tipo.

La solución marca esas posiciones, junta todos los demás valores en un
solo mcd con S y prueba cada par de valores marcados con mcd de sufijo
sobre la lista marcada. No quitar nada lo cubre el mcd de todo.

En el primer ejemplo S = 120 y d = 5 conserva 5 y 100, mientras que 8 y
7 dejan restos 3 y 2 que forman un montón de 5.

El recorrido cuesta O(n log S), y los pares unos 120² pasos de mcd.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2184_number_theory.cpp](2184_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(n log S) | AC | 0.046 s | 1032 KB |
| [2184_number_theory.go](2184_number_theory.go) | Go 1.14 x64 | number_theory | O(n log S) | AC | 0.062 s | 5676 KB |
| [2184_number_theory.java](2184_number_theory.java) | Java 1.8 | number_theory | O(n log S) | AC | 0.125 s | 1244 KB |
| [2184_number_theory.py](2184_number_theory.py) | Python 3.12 x64 | number_theory | O(n log S) | AC | 0.187 s | 10604 KB |
| [2184_number_theory.rs](2184_number_theory.rs) | Rust 1.75 x64 | number_theory | O(n log S) | AC | 0.031 s | 3736 KB |
