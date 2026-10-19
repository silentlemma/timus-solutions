# 2118. Cortar una cadena de bits de un código prefijo en trozos indescifrables

[Timus 2118](https://acm.timus.ru/problem.aspx?space=1&num=2118) · dificultad 1366 · greedy, strings

Problema original de Alexey Danilyuk, del concurso t.me/umnik_team, campamento de Petrozavodsk, verano de 2018.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un mensaje sobre un alfabeto de k letras se codifica con un código
prefijo binario, lo que da una cadena de bits T. Cortar T en el mayor
número de trozos de modo que ningún trozo pueda descifrarse con el mismo
código, o indicar que es imposible. Los límites son 1 segundo y 64 MB.

## Entrada

k, 1 ≤ k ≤ 52, el mensaje de hasta 10⁶ letras de las primeras k de
A–Z a–z, y luego las k palabras del código, cada una de longitud a lo
sumo k.

## Salida

El mayor número de trozos, o −1.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
CACB
011
1
001
```

Salida:

```
2
```

### Ejemplo 2

Entrada:

```
3
ACBABCAACABCAACC
0
10
110
```

Salida:

```
-1
```

## Solución

Descifrar con un código prefijo es determinista: en cada posición encaja
a lo sumo una palabra. La respuesta depende de las palabras de un bit.

- Ninguna: un bit suelto nunca se descifra, así que cada bit es un trozo
  y la respuesta es la longitud de T.
- 0 y 1: toda cadena se descifra, así que la respuesta es −1.
- Exactamente una, llamada g, y b el otro bit. Entonces todas las demás
  palabras empiezan por b. Un trozo hecho solo de g se descifra, así que
  cada trozo contiene una b y hay a lo sumo tantos trozos como bits b.

En el último caso un trozo g…g b nunca se descifra: los bits g se
descifran uno a uno y la b final sola no es una palabra. Sea p la última
posición de T tal que ninguna palabra es prefijo del sufijo que empieza
en p. Cada sufijo posterior empieza por una palabra y, por inducción, se
descifra, así que el último trozo no puede empezar después de p; y el
sufijo desde p no se descifra. Cortar justo después de cada b anterior a
p y dejar el resto como último trozo da (número de b antes de p) + 1
trozos, que es lo máximo. Si no existe tal p, o T no tiene ninguna b, la
respuesta es −1.

T puede tener 5 · 10⁷ bits, así que no se construye. Los sufijos se
recorren desde el final con un autómata de Aho–Corasick de las palabras
invertidas: un estado es de aceptación cuando alguna palabra es prefijo
del sufijo leído. La transición por una letra entera desde un estado se
calcula bit a bit una vez y se guarda, así que el recorrido cuesta O(|s|)
más O(k²) por estado, con a lo sumo k² estados.

En el primer ejemplo T = 0010110011 y g = 1. El sufijo 0011 empieza por
la palabra 001, pero ninguna palabra empieza el sufijo 010110011, así que
p es el segundo bit, hay un 0 antes y la respuesta es 2.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2118_greedy_strings.cpp](2118_greedy_strings.cpp) | G++ 13.2 x64 | greedy, strings | O(L + k^4) | AC | 0.031 s | 2016 KB |
| [2118_greedy_strings.go](2118_greedy_strings.go) | Go 1.14 x64 | greedy, strings | O(L + k^4) | AC | 0.031 s | 3340 KB |
| [2118_greedy_strings.java](2118_greedy_strings.java) | Java 1.8 | greedy, strings | O(L + k^4) | AC | 0.125 s | 7440 KB |
| [2118_greedy_strings.py](2118_greedy_strings.py) | Python 3.12 x64 | greedy, strings | O(L + k^4) | AC | 0.265 s | 4020 KB |
| [2118_greedy_strings.rs](2118_greedy_strings.rs) | Rust 1.75 x64 | greedy, strings | O(L + k^4) | AC | 0.031 s | 2140 KB |
