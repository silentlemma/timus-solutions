# 1879. Prácticas en GOV 2

[Timus 1879](https://acm.timus.ru/problem.aspx?space=1&num=1879) · dificultad 1456 · greedy

Problema original de Mikhail Rubinchik, del Concurso Regional Escolar de Programación de los Urales 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

La distancia de una cadena cíclica s a una cadena más corta t es la
suma de las distancias de Hamming de t a cada subcadena de s de la
longitud de t, incluidas las que dan la vuelta por el final de s. Ambas
cadenas pueden tener signos de interrogación. Hay que cambiar cada
signo por una letra para que la distancia sea mínima, y escribirla. Las
letras son números de 1 a 100 000, y 0 es un signo de interrogación.

## Entrada

La longitud n de s (1 ≤ n ≤ 100 000) y sus n números, luego la longitud
m de t y sus m números.

## Salida

La menor distancia.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
2 1 1 0 2
4
3 0 3 0
```

Salida:

```
14
```

## Solución

Una cadena cíclica de longitud n tiene n subcadenas de longitud m, una
desde cada posición. Para una posición fija j de t, los inicios
recorren las n posiciones de s, así que cada pareja (posición de s,
posición de t) se compara exactamente una vez. La distancia es por
tanto n·m menos el número de parejas con letras iguales,
Σ a(c)·b(c) sobre las letras c, donde a(c) y b(c) cuentan c en s y en
t. El orden de las letras no importa en absoluto.

Ahora x(c) signos de s e y(c) signos de t pasan a ser la letra c. Las
parejas iguales crecen en Σ (x(c)·b(c) + y(c)·a(c) + x(c)·y(c)). Con y
fijo esto es lineal en x, así que lo mejor es poner los p signos de s
en una sola letra. Del mismo modo los q signos de t van a una sola
letra. Con una misma letra para ambas la ganancia es
p·b(c) + q·a(c) + p·q, y con dos letras distintas es como mucho
p·max b + q·max a. Esa cota se alcanza cuando los dos máximos están en
letras distintas, y si no el primer caso la iguala o supera. La respuesta es
n·m − Σ a(c)b(c) menos la mayor ganancia. `O(n + m + letters)`.

En el ejemplo los recuentos son a: 2 → 2, 1 → 2 con un signo, y
b: 3 → 2 con dos. No hay letras comunes, y la mejor ganancia es 6, por
ejemplo convirtiendo todos los signos en 2. La respuesta es
20 − 6 = 14.

Trampas:

- las subcadenas cíclicas hacen que cada pareja se encuentre
  exactamente una vez, así que ni las posiciones ni el orden de las
  letras importan;
- repartir los signos de una cadena entre varias letras nunca ayuda;
- la distancia llega a 10¹⁰, así que hacen falta enteros de 64 bits.

Las respuestas coinciden con una búsqueda sobre todos los reemplazos y
todas las subcadenas cíclicas en 3000 casos pequeños aleatorios, y con
una implementación aceptada independiente en 90 casos grandes.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1879_greedy.cpp](1879_greedy.cpp) | G++ 13.2 x64 | greedy | O(n + m + L) | AC | 0.125 s | 1752 KB |
| [1879_greedy.go](1879_greedy.go) | Go 1.14 x64 | greedy | O(n + m + L) | AC | 0.031 s | 3796 KB |
| [1879_greedy.java](1879_greedy.java) | Java 1.8 | greedy | O(n + m + L) | AC | 0.125 s | 2108 KB |
| [1879_greedy.py](1879_greedy.py) | Python 3.12 x64 | greedy | O(n + m + L) | AC | 0.156 s | 20668 KB |
| [1879_greedy.rs](1879_greedy.rs) | Rust 1.75 x64 | greedy | O(n + m + L) | AC | 0.046 s | 4716 KB |
