# 1907. Repartos iguales de dos cuadrículas

[Timus 1907](https://acm.timus.ru/problem.aspx?space=1&num=1907) · difficulty 1323 · number_theory

Problema original de Ivan Burmistrov, Ural Championship 2012.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dos cuadrículas cuadradas tienen lados enteros a y b. Entre ambas hay
a²+b² celdas unitarias y 4(a+b) segmentos unitarios de borde exterior.
Hay que repartir ambas colecciones entre los mismos c≥2 grupos, de modo
que todos reciban igual cantidad de celdas e igual cantidad de segmentos.
No se exige conectividad. Dados a y n, cuenta los enteros b con 1≤b≤n
que permiten el reparto. Límites: 1 segundo y 64 MB.

## Entrada

Dos enteros a,n, con 1≤a≤10¹² y 1≤n≤10¹⁸.

## Salida

Imprime la cantidad de valores admisibles de b.

## Evaluación

Un único entero exacto, comparado por tokens.

## Ejemplos

```
3 6
```

```
4
```

## Solución

Existe un número de grupos c exactamente cuando
gcd(a²+b²,4(a+b))>1: los totales deben compartir un primo.
Si a y b tienen la misma paridad, ambos totales son pares y basta c=2.

Con paridades distintas, el total de celdas es impar. Un primo común p
debe ser impar y dividir a+b. Sustituir b≡−a (mod p) da
a²+b²≡2a². Como p es impar, esto se anula exactamente si p divide a,
y entonces también b. A la inversa, cualquier primo impar común a ambos
lados divide los dos totales. Por tanto, son válidos los b de la misma
paridad que a o que comparten con a algún factor primo impar.

Factoriza solamente a mediante divisiones de prueba y conserva los primos
impares distintos. Cuenta los valores inválidos: de paridad opuesta y sin
ninguno de esos factores. Si a es impar, escribe b=2t y cuenta los
t≤floor(n/2) coprimos con los factores. Si a es par, cuenta los b impares
hasta n que evitan los factores.

Sea F(x,i) la cantidad del tipo elegido hasta x que evita los primos
de índices i,…,r−1. Sin primos pendientes, el caso base es x para todos
los enteros, o floor((x+1)/2) para los impares. En otro caso,
F(x,i)=F(x,i+1)−F(floor(x/pᵢ),i+1). El segundo término elimina los múltiplos
de pᵢ. Dividir por este primo impar conserva la paridad y la divisibilidad
por los demás primos, lo que demuestra la recurrencia. Si x=0, devuelve cero.
La respuesta final es n menos la cantidad inválida.

Hay como máximo diez factores primos impares distintos: el producto de los
primeros once es 3 710 369 067 405>10¹². Tiempo O(√a+2ʳ), espacio O(r).
En el ejemplo sirven los impares 1,3,5 y el tamaño 6, que comparte el primo 3.

## Notas por lenguaje

C++, Go 1.14, Java 8 y Rust 1.75 usan enteros con signo de 64 bits.
No calcules a²+b² directamente: puede acercarse a 10³⁶. Cada resultado
recursivo cuenta un subconjunto y queda entre cero y su cota; por ello
las restas intermedias también son seguras. La respuesta no supera 10¹⁸.
Los cuadrados de los divisores de prueba solo alcanzan aproximadamente 10¹²,
sin depender de n². Python 3.12 usa enteros normales. La profundidad máxima
es once. Elimina cada potencia prima completa para no duplicar factores.

Las respuestas coinciden con el cálculo directo del mcd de los totales
en 90 208 casos, y las grandes con una suma de inclusión-exclusión
sencilla en precisión arbitraria.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1907_number_theory.cpp](1907_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(sqrt(a) + 2^r) | AC | 0.015 s | 424 KB |
| [1907_number_theory.go](1907_number_theory.go) | Go 1.14 x64 | number_theory | O(sqrt(a) + 2^r) | AC | 0.046 s | 1088 KB |
| [1907_number_theory.java](1907_number_theory.java) | Java 1.8 | number_theory | O(sqrt(a) + 2^r) | AC | 0.140 s | 1660 KB |
| [1907_number_theory.py](1907_number_theory.py) | Python 3.12 x64 | number_theory | O(sqrt(a) + 2^r) | AC | 0.140 s | 500 KB |
| [1907_number_theory.rs](1907_number_theory.rs) | Rust 1.75 x64 | number_theory | O(sqrt(a) + 2^r) | AC | 0.046 s | 232 KB |
