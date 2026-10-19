# 1849. Caza de conejos 2

[Timus 1849](https://acm.timus.ru/problem.aspx?space=1&num=1849) · dificultad 2490 · sorting

Problema original de Alexey Samsonov, del Ural SU Contest en la sesión de verano de Petrozavodsk, agosto de 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

n conejos están en puntos distintos del plano. Un programa genera q
disparos, cada uno una posición del cazador y una dirección; un disparo
mata a todos los conejos del rayo que sale del cazador en esa
dirección, incluido un conejo en el mismo punto que el cazador. El
disparo 1 está dado, y cada siguiente sale del anterior con
x′ = (aₓ·(x + 10000) + bₓ) mod 20001 − 10000, lo mismo para y con a_y,
b_y, y v′ = (a_v·(v + 10) + b_v) mod 21 − 10 para cada parte de la
dirección con su propio par de números. Hallar el disparo que mata más
conejos y cuántos mata.

## Entrada

n (1 ≤ n ≤ 10 000) y los conejos, enteros de valor absoluto hasta
10 000; luego q (1 ≤ q ≤ 10⁶); luego x₁, y₁, vx₁, vy₁
(|x₁|, |y₁| ≤ 10 000, |vx₁|, |vy₁| ≤ 10); luego aₓ, bₓ, a_y, b_y, a_vx,
b_vx, a_vy, b_vy, de 0 a 10⁵. Ninguna dirección de los primeros q
disparos es nula.

## Salida

El número del mejor disparo y cuántos conejos mata. Entre disparos
igual de buenos las soluciones imprimen el último.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
0 0
2 0
3 0
2 2
3
-1 -1 1 0
1 0 1 1 1 0 1 0
```

Salida:

```
2 3
```

## Solución

Una dirección (vx, vy) solo importa por su vector primitivo
(dx, dy) = (vx, vy) / mcd(vx, vy), y de esos hay solo unos cientos. Se
generan primero todos los disparos y se ordenan por vector primitivo
con un ordenamiento por conteo. Luego se toman los vectores de uno en
uno. A lo largo de (dx, dy) un punto (x, y) está en la recta
x·dy − y·dx y en el lugar x·dx + y·dy de esa recta. Se ordenan los
conejos por recta y luego por lugar; un disparo alcanza a los conejos
de su recta cuyo lugar es al menos el suyo, y dos búsquedas binarias
los cuentan. Cada vector cuesta `O(n log n)` una vez y cada disparo
`O(log n)`.

Las partes de la dirección siguen una aplicación v → a·v + b sobre 21
valores, así que pronto se repiten con un periodo de como mucho 42
pares, y en la práctica solo se usan unas decenas de vectores.

En el ejemplo el segundo disparo está en (−1, 0) y mira según (1, 0):
su recta contiene (0, 0), (2, 0) y (3, 0), todos delante, así que
mata 3. El primer y el tercer disparo miran por y = −1 e y = 1, donde no hay
conejos.

Trampas:

- (2, 0) y (1, 0) son la misma dirección; hay que dividir por el mcd;
- un conejo en el punto del cazador cuenta, uno detrás no;
- los disparos son muchos, así que se generan una vez y se guardan de
  forma compacta.

Las respuestas coinciden con una implementación aceptada independiente
en trescientos casos pequeños y en las pruebas grandes, empates
incluidos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1849_sorting.cpp](1849_sorting.cpp) | G++ 13.2 x64 | sorting | O(D n log n + q log n) | AC | 0.171 s | 15560 KB |
| [1849_sorting.go](1849_sorting.go) | Go 1.14 x64 | sorting | O(D n log n + q log n) | AC | 0.296 s | 18392 KB |
| [1849_sorting.java](1849_sorting.java) | Java 1.8 | sorting | O(D n log n + q log n) | AC | 0.281 s | 17612 KB |
| [1849_sorting.py](1849_sorting.py) | Python 3.12 x64 | sorting | O(D n log n + q log n) | AC | 2.265 s | 20952 KB |
| [1849_sorting.rs](1849_sorting.rs) | Rust 1.75 x64 | sorting | O(D n log n + q log n) | AC | 0.187 s | 31916 KB |
