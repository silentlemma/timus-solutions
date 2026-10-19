# 1842. Raíces locales

[Timus 1842](https://acm.timus.ru/problem.aspx?space=1&num=1842) · dificultad 5538 · strings

Problema original de Ivan Burmistrov, del Ural SU Contest en la sesión de verano de Petrozavodsk, agosto de 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se corta una palabra w de n letras en un punto i (1 ≤ i ≤ n − 1) en un
prefijo p y un sufijo s. La raíz local en i es la palabra no vacía más
corta r tal que p y r terminan igual (una es sufijo de la otra) y s y r
empiezan igual (una es prefijo de la otra). Hallar un punto donde la
raíz local sea la más larga, y su longitud.

## Entrada

Una palabra de letras latinas minúsculas, de 2 a 300 000 letras.

## Salida

El punto y la longitud de la raíz local en él. Se acepta cualquier
punto con la raíz más larga.

## Ejemplos

### Ejemplo 1

Entrada:

```
aababaaa
```

Salida:

```
5 6
```

## Solución

Una longitud L sirve en el punto i exactamente cuando w[k] = w[k + L]
para todo k con i − L ≤ k < i y ambos índices dentro de la palabra: r escrita
dos veces, la primera copia terminando en el corte y la segunda
empezando allí, coincide con w donde las copias caen dentro de ella. El
periodo P de w siempre sirve, así que ninguna raíz local es más larga
que P. El teorema de factorización crítica dice que en algún punto la
raíz local mide exactamente P, y la construcción de Crochemore–Perrin
encuentra uno en tiempo lineal.

Se toma dos veces el mayor sufijo lexicográfico de w: con el orden
habitual de las letras y con el orden inverso, contando en ambos casos
como menor una palabra que es prefijo de otra más larga. El más tardío
de los dos inicios es un punto crítico. Solo en una palabra de una
única letra repetida ambos sufijos son la palabra entera; entonces
sirve cualquier punto, y se toma 1. El mayor sufijo se halla con el
bucle de comparación de la búsqueda Two-Way: un inicio candidato, un
desplazamiento en curso y el periodo de la parte que coincide, y cada
discrepancia adelanta el candidato o el recorrido. El periodo es n
menos el borde más largo, por la función de prefijos. `O(n)`.

En el ejemplo el periodo es 6, porque el borde más largo es "aa". Con
a < b el mayor sufijo es "babaaa", tras 2 letras; con b < a es
"aaa", tras 5 letras. La respuesta es el punto 5, donde la raíz
local es "aaabab".

Trampas:

- la raíz puede sobresalir por ambos extremos de la palabra, así que un
  lado corto no la limita;
- el límite de tiempo es medio segundo, así que se usa un algoritmo
  lineal; la solución en Python corre en PyPy.

Las respuestas pasan un verificador que recalcula el periodo y confirma
que ninguna raíz más corta sirve en el punto impreso. En todas las
palabras de hasta 8 letras sobre tres letras y de hasta 12 sobre dos,
los puntos son críticos por búsqueda directa.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1842_strings.cpp](1842_strings.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.031 s | 1652 KB |
| [1842_strings.go](1842_strings.go) | Go 1.14 x64 | strings | O(n) | AC | 0.031 s | 7380 KB |
| [1842_strings.java](1842_strings.java) | Java 1.8 | strings | O(n) | AC | 0.140 s | 4904 KB |
| [1842_strings.py](1842_strings.py) | PyPy 3.10 x64 | strings | O(n) | AC | 0.296 s | 4344 KB |
| [1842_strings.rs](1842_strings.rs) | Rust 1.75 x64 | strings | O(n) | AC | 0.031 s | 3444 KB |
