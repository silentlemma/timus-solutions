# 1587. El cerdo volador

[Timus 1587](https://acm.timus.ru/problem.aspx?space=1&num=1587) · dificultad 819 · greedy

Problema original de Sergey Pupyrev, de la subregión oriental del NEERC del ACM ICPC 2007–2008, Ekaterimburgo, 27 de octubre de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

El público pone a un cerdo n notas (1 ≤ n ≤ 50000), cada una un entero
de −3 a 3. Hay que hallar el mayor producto de un tramo no vacío de
notas consecutivas.

Límite de tiempo: 0.75 segundos. Límite de memoria: 64 MB.

## Entrada

n y luego las n notas.

## Salida

El mayor producto, escrito completo.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
1 2 -1
```

Salida:

```
2
```

## Solución

Los ceros cortan las notas en bloques. Dentro de un bloque cada nota vale
al menos 1 en valor absoluto, así que un tramo más largo nunca tiene un
producto menor en valor absoluto, y el producto es ±2ᵃ·3ᵇ, donde a y b
cuentan las notas ±2 y ±3. Con un número par de notas negativas el
bloque entero es positivo. Con un número impar, el mejor tramo positivo
descarta o todo hasta la primera nota negativa o todo desde la última.
Los conteos prefijos dan a y b de cada candidato, y los candidatos se
comparan por a·ln 2 + b·ln 3; pares (a, b) distintos nunca quedan tan
cerca como para que los dobles los confundan. Solo el ganador se
convierte en un número grande.

Si no hay ningún tramo positivo, cada bloque es una sola nota negativa:
la respuesta es 0 si hay un cero y, si no, la propia nota (entonces
n = 1). `O(n + B(n))`, donde B(n) es el coste de construir e imprimir
el entero grande (`O(n²)` en C++/Rust). Los resultados se
contrastaron con probar todos los tramos con productos exactos en
entradas pequeñas.

Detalles a tener en cuenta:

- la respuesta llega a 3⁵⁰⁰⁰⁰, casi 24000 cifras; C++ y Rust multiplican
  a mano en base 10⁹, y Python 3.12 tiene que quitar su límite para
  convertir enteros largos en texto;
- multiplicar números grandes bloque a bloque es demasiado lento; se
  comparan los exponentes y solo se construye la respuesta;
- una sola nota negativa es su propia respuesta, mientras que −1 0 −1
  da 0.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1587_greedy.cpp](1587_greedy.cpp) | G++ 13.2 x64 | greedy | O(n + B(n)) | AC | 0.046 s | 844 KB |
| [1587_greedy.go](1587_greedy.go) | Go 1.14 x64 | greedy | O(n + B(n)) | AC | 0.031 s | 4040 KB |
| [1587_greedy.java](1587_greedy.java) | Java 1.8 | greedy | O(n + B(n)) | AC | 0.125 s | 4860 KB |
| [1587_greedy.py](1587_greedy.py) | Python 3.12 x64 | greedy | O(n + B(n)) | AC | 0.109 s | 7880 KB |
| [1587_greedy.rs](1587_greedy.rs) | Rust 1.75 x64 | greedy | O(n + B(n)) | AC | 0.031 s | 1336 KB |
