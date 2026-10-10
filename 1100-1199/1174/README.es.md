# 1174. La posición de una permutación en el orden de intercambios vecinos

[Timus 1174](https://acm.timus.ru/problem.aspx?space=1&num=1174) · dificultad 716 · math

Problema original de Mugurel Ionut Andreica, del Romanian Open Contest de diciembre de 2001; el programa generador del enunciado se basa en programas de Frank Ruskey.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un programa dado lista las `N!` permutaciones de `1..N` (`N ≤ 100`),
empezando por `1 2 … N` e intercambiando cada vez dos vecinos. Lo hace de
forma recursiva: el elemento `k` recorre paso a paso la disposición de los
elementos menores, alternando su sentido, y entre sus pasos los elementos
mayores hacen todos sus movimientos. Dada una permutación, hay que hallar
su número de línea en esa lista.

Límite de tiempo: 0.5 segundos. Límite de memoria: 64 MB.

## Entrada

`N` y luego la permutación.

## Salida

La posición, contando desde 1; puede tener más de 150 dígitos.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 
2 3 1 4
```

Salida:

```
17
```

## Solución

Se miran solo los elementos `1..k` y se ignoran los mayores. Su orden
relativo cambia solo cuando se mueve `k` o uno menor, así que la lista de
esos órdenes es la misma lista para `k` elementos. En ella, el elemento
`k` hace una pasada de `k` posiciones por cada orden de `1..k−1`, y las
pasadas se alternan: la primera va del extremo derecho a la izquierda, la
siguiente de izquierda a derecha, y así sucesivamente.

Así que si `rank(k−1)` es la posición desde 0 del orden de `1..k−1`, el
orden de `1..k` está en la pasada número `rank(k−1)`, con desplazamiento
`s` dentro de ella, donde `s` es el número de elementos menores a la
izquierda de `k` cuando la pasada va a la derecha (pasadas impares), y
`k − 1` menos ese número cuando va a la izquierda (pares). Entonces
`rank(k) = rank(k−1)·k + s`, y la respuesta es `rank(N) + 1`. `O(N²)` para
las cuentas más los pasos con números grandes.

Detalles a tener en cuenta:

- el sentido depende de la paridad de `rank(k−1)`, un número grande, pero
  solo hace falta su última cifra;
- el programa empieza con el elemento `k` en el extremo derecho
  moviéndose a la izquierda, lo que hace que las pasadas pares vayan a la
  izquierda;
- `100!` tiene 158 dígitos, así que 64 bits no bastan ni de lejos.

Las respuestas se comprobaron ejecutando directamente el programa que
genera la lista para cada permutación con `N ≤ 6`, y se compararon con una
solución escrita aparte en permutaciones aleatorias de hasta 100
elementos.

## Notas por lenguaje

- Python, Go y Java usan sus enteros grandes; C++ y Rust guardan la
  posición en dígitos de base 10⁹ con una sola operación: multiplicar y
  sumar un número pequeño.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1174_math.cpp](1174_math.cpp) | G++ 13.2 x64 | math | O(N²) | AC | 0.015 s | 196 KB |
| [1174_math.go](1174_math.go) | Go 1.14 x64 | math | O(N²) | AC | 0.015 s | 1176 KB |
| [1174_math.java](1174_math.java) | Java 1.8 | math | O(N²) | AC | 0.140 s | 1832 KB |
| [1174_math.py](1174_math.py) | Python 3.12 x64 | math | O(N²) | AC | 0.062 s | 408 KB |
| [1174_math.rs](1174_math.rs) | Rust 1.75 x64 | math | O(N²) | AC | 0.015 s | 236 KB |
