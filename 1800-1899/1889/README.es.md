# 1889. Avisos del aeropuerto

[Timus 1889](https://acm.timus.ru/problem.aspx?space=1&num=1889) · dificultad 308 · bruteforce

Problema original de Denis Dublennykh, de la subregión oriental del NEERC 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Igor oyó n frases de un aviso y conoce el idioma de algunas; las demás
son "unknown". El aviso se leyó en varios idiomas, cada uno como mucho
una vez y con el mismo número de frases en cada uno. ¿En cuántos
idiomas pudo leerse? Hay que listar todas las posibilidades en orden
creciente, o escribir "Igor is wrong." si no hay ninguna.

## Entrada

n (2 ≤ n ≤ 1000) y luego n líneas con el nombre de un idioma (de 4 a 20
letras minúsculas) o "unknown"; al menos una frase es conocida.

## Salida

Todos los números de idiomas posibles en orden creciente, o
"Igor is wrong.".

## Ejemplos

### Ejemplo 1

Entrada:

```
6
english
unknown
unknown
unknown
german
unknown
```

Salida:

```
2 3 6
```

### Ejemplo 2

Entrada:

```
4
english
french
unknown
english
```

Salida:

```
Igor is wrong.
```

### Ejemplo 3

Entrada:

```
3
zulu
zulu
zulu
```

Salida:

```
1
```

## Solución

Si el aviso se leyó en k idiomas, k divide a n y las frases se reparten
en k bloques consecutivos de n/k, un bloque por idioma. Para cada
divisor k se comprueban dos cosas. Las frases conocidas de un bloque
deben estar todas en un mismo idioma. Ningún idioma puede aparecer en
dos bloques distintos. Los bloques sin frases conocidas pueden ser de
cualquier idioma nuevo. Hay pocos divisores y cada comprobación es
lineal, así que cuesta `O(n·d(n))`.

En el primer ejemplo un solo bloque tendría inglés y alemán, así que 1
falla. Con 2 los bloques son "english ? ?" y "? german ?", con 3 son
parejas con el inglés en la primera y el alemán en la tercera, y 6
siempre es posible aquí: la respuesta es 2 3 6.

Trampas:

- el mismo idioma en dos bloques descarta k, como en el tercer ejemplo
  con 3 idiomas;
- un bloque solo con frases desconocidas es válido;
- la línea de salida es "Igor is wrong." con el punto.

Las respuestas coinciden con una implementación aceptada independiente
en 125 avisos aleatorios.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1889_bruteforce.cpp](1889_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(n d(n)) | AC | 0.015 s | 532 KB |
| [1889_bruteforce.go](1889_bruteforce.go) | Go 1.14 x64 | bruteforce | O(n d(n)) | AC | 0.031 s | 1236 KB |
| [1889_bruteforce.java](1889_bruteforce.java) | Java 1.8 | bruteforce | O(n d(n)) | AC | 0.125 s | 684 KB |
| [1889_bruteforce.py](1889_bruteforce.py) | Python 3.12 x64 | bruteforce | O(n d(n)) | AC | 0.093 s | 476 KB |
| [1889_bruteforce.rs](1889_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(n d(n)) | AC | 0.015 s | 452 KB |
