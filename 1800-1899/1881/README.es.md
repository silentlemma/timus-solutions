# 1881. Enunciado largo

[Timus 1881](https://acm.timus.ru/problem.aspx?space=1&num=1881) · dificultad 62 · simulation

Problema original de Fedor Fominykh, del Concurso Regional Escolar de Programación de los Urales 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una página tiene h líneas de w caracteres. Las palabras de una línea se
separan con un solo espacio, y una palabra que no cabe en la línea
actual empieza otra; las palabras nunca se parten. ¿Cuántas páginas
ocupa un texto de n palabras?

## Entrada

h, w y n (1 ≤ h, w ≤ 100, 1 ≤ n ≤ 10 000), luego n palabras, una por
línea, cada una de como mucho w caracteres; su longitud total es como
mucho 10 000.
Las palabras no están vacías y solo contienen letras inglesas mayúsculas
y minúsculas y los signos de puntuación `.,!?`.

## Salida

El número de páginas.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 5 6
To
be
or
not
to
be
```

Salida:

```
2
```

## Solución

Se llenan las líneas de forma voraz. Se guarda cuántos caracteres van
usados en la línea actual; una palabra necesita su longitud más un
espacio salvo si empieza la línea. Si no cabe, empieza una línea nueva.
Empezar la cuenta en −1 hace que la primera palabra de una línea no
necesite espacio. La respuesta es el número de líneas dividido entre h
y redondeado hacia arriba. `O(n)`.

En el ejemplo las líneas son "To be", "or", "not" y "to be": "or not" y
"not to" tienen un carácter de más. Cuatro líneas en páginas de tres
ocupan dos páginas.

Trampas:

- una palabra que llena justo el resto de la línea, espacio incluido,
  todavía cabe;
- el espacio solo va entre palabras, nunca al principio de una línea;
- el número de páginas se redondea hacia arriba.

Los recuentos coinciden con una implementación aceptada independiente
en 100 textos aleatorios.

## Soluciones optimizadas

La solución optimizada en C++ nunca guarda una palabra: lee cada palabra
carácter a carácter con `getchar` y conserva solo su longitud, que es
todo lo que necesita el reparto en líneas. Ocupa 128 KB en lugar de
404 KB, con el mismo tiempo.

La solución optimizada en Java lee la entrada en bloques de 1 KB y solo
mide cada palabra, byte a byte, en lugar de unir las líneas y dividirlas
en cadenas: 408 KB en lugar de 1336 KB, con el mismo tiempo.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1881_simulation.cpp](1881_simulation.cpp) | G++ 13.2 x64 | simulation | O(n) | AC | 0.015 s | 404 KB | 11291031 |
| [1881_simulation.go](1881_simulation.go) | Go 1.14 x64 | simulation | O(n) | AC | 0.031 s | 1236 KB | 11291032 |
| [1881_simulation.java](1881_simulation.java) | Java 1.8 | simulation | O(n) | AC | 0.109 s | 1336 KB | 11291035 |
| [1881_simulation.py](1881_simulation.py) | Python 3.12 x64 | simulation | O(n) | AC | 0.078 s | 656 KB | 11291034 |
| [1881_simulation.rs](1881_simulation.rs) | Rust 1.75 x64 | simulation | O(n) | AC | 0.031 s | 256 KB | 11291036 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1881_simulation_optimized.cpp](1881_simulation_optimized.cpp) \* | G++ 13.2 x64 | simulation | O(n) | AC | 0.031 s | 128 KB | 11303646 |
| [1881_simulation_optimized.java](1881_simulation_optimized.java) | Java 1.8 | simulation | O(n) | AC | 0.125 s | 408 KB | 11303783 |

\* No está entre las 10 mejores ni en el 15% mejor de las soluciones de
su lenguaje en el juez actual; quizá se pueda optimizar más.
