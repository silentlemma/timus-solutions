# 1827. Guerras indígenas

[Timus 1827](https://acm.timus.ru/problem.aspx?space=1&num=1827) · dificultad 1188 · hashing

Problema original de Dmitry Ivankov, del XII Concurso Individual Abierto de la Universidad Estatal de los Urales, 19 de marzo de 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Los indígenas distinguen los días por el número de estrellas del cielo
nocturno. Su libro anota cada guerra como x, las estrellas de su primer
día, y, las de su último día, y d, su duración en días. Dadas las
estrellas vistas hace i días para cada uno de los últimos n días,
marcar todos los días en que pudo estar en curso alguna guerra anotada.

## Entrada

n (2 ≤ n ≤ 10⁵), luego a₁, …, aₙ, donde aᵢ es el número de estrellas de
hace i días (0 ≤ aᵢ ≤ 2·10⁸), luego m (1 ≤ m ≤ 10⁵) y m líneas x, y, d
(0 ≤ x, y ≤ 2·10⁸, 2 ≤ d ≤ 50).

## Salida

Una cadena de n dígitos: el i-ésimo es 1 si hace i días pudo haber
guerra, y 0 si no.

## Ejemplos

### Ejemplo 1

Entrada:

```
6
6 5 4 3 2 1
3
2 4 3
4 5 2
1 6 5
```

Salida:

```
011110
```

## Solución

Una guerra de d días que terminó hace k días empezó hace k + d − 1
días, así que encaja ahí exactamente cuando a en k + d − 1 vale x y a
en k vale y. Las duraciones no pasan de 50, así que para cada duración
d que aparece en el libro se meten los pares (x, y) de sus guerras en
un conjunto hash y se recorren todos los k consultando (a en k + d − 1,
a en k). Cada acierto cubre los días k … k + d − 1: se guarda, para
cada k, el día más antiguo cubierto por una guerra que termina ahí, y
un barrido marca todos los días hasta el máximo acumulado inclusive. Son
como mucho 49·n consultas, `O(50·n + m)`.

Python hace las consultas de una duración de una vez con `map` sobre
dos listas desplazadas, empaqueta los aciertos en una máscara de bits
de entero grande y la extiende a d días con O(log d) desplazamientos y
operaciones «o».

En el ejemplo la guerra (2, 4, 3) encaja hace 5 a 3 días y (4, 5, 2)
hace 3 a 2 días, mientras que (1, 6, 5) necesitaría 6 estrellas hace 2
días.

Trampas:

- el primer día de una guerra está más en el pasado, así que x se
  compara con el mayor número de días atrás;
- si todos los números son iguales, cada guerra encaja en todas partes,
  así que buscar guerras posición a posición desde su primer día es
  cuadrático;
- una guerra puede ser más larga que todo el registro.

Las respuestas coinciden con una implementación aceptada independiente
en unos cientos de registros aleatorios y en los de tamaño máximo de
las pruebas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1827_hashing.cpp](1827_hashing.cpp) | G++ 13.2 x64 | hashing | O(50 n + m) | AC | 0.484 s | 5944 KB |
| [1827_hashing.go](1827_hashing.go) | Go 1.14 x64 | hashing | O(50 n + m) | AC | 0.187 s | 10820 KB |
| [1827_hashing.java](1827_hashing.java) | Java 1.8 | hashing | O(50 n + m) | AC | 0.234 s | 6812 KB |
| [1827_hashing.py](1827_hashing.py) | Python 3.12 x64 | hashing | O(50 n + m) | AC | 0.828 s | 42112 KB |
| [1827_hashing.rs](1827_hashing.rs) | Rust 1.75 x64 | hashing | O(50 n + m) | AC | 0.093 s | 8892 KB |
