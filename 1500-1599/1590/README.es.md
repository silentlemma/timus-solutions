# 1590. El cifrado de Bacon

[Timus 1590](https://acm.timus.ru/problem.aspx?space=1&num=1590) · dificultad 187 · strings

Problema original de Alexey Zhevak, de la subregión oriental del NEERC del ACM ICPC 2007–2008, Ekaterimburgo, 27 de octubre de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay que contar las subcadenas no vacías distintas de una cadena de como
mucho 5000 letras latinas minúsculas.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

La cadena.

## Salida

El número de subcadenas distintas.

## Ejemplos

### Ejemplo 1

Entrada:

```
aaba
```

Salida:

```
8
```

## Solución

Se construye el autómata de sufijos de la cadena. Cada estado representa
las subcadenas que terminan en el mismo conjunto de posiciones; sus
longitudes van de len(link) + 1 a len, así que el estado contiene
len − len(link) subcadenas distintas, y ninguna subcadena está en dos
estados. La respuesta es la suma de len − len(link) sobre todos los
estados salvo el inicial. El autómata tiene menos de 2n estados y se
construye en `O(n·26)` de tiempo y memoria. Los resultados se
contrastaron con meter todas las subcadenas en un conjunto para cadenas
cortas.

Detalles a tener en cuenta:

- una cadena aleatoria de 5000 letras tiene unos 12,5 millones de
  subcadenas distintas, así que guardarlas en 64 MB es imposible;
- al partir un estado, el clon hereda todas las transiciones del estado
  viejo y su enlace de sufijo.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1590_strings.cpp](1590_strings.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.015 s | 1428 KB |
| [1590_strings.go](1590_strings.go) | Go 1.14 x64 | strings | O(n) | AC | 0.015 s | 2328 KB |
| [1590_strings.java](1590_strings.java) | Java 1.8 | strings | O(n) | AC | 0.093 s | 2412 KB |
| [1590_strings.py](1590_strings.py) | Python 3.12 x64 | strings | O(n) | AC | 0.109 s | 3132 KB |
| [1590_strings.rs](1590_strings.rs) | Rust 1.75 x64 | strings | O(n) | AC | 0.015 s | 2272 KB |
