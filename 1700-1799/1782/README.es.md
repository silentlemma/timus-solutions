# 1782. La nueva palabra de Jack

[Timus 1782](https://acm.timus.ru/problem.aspx?space=1&num=1782) · dificultad 2126 · strings

Problema original de Alex Samsonov, del XV Campeonato Abierto por Equipos de Programación de la Universidad Estatal de los Urales.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una palabra binaria no tiene ningún factor no vacío xyxyx con
|y| ≤ 2|x|. Partiendo de la palabra vacía, se permiten tres frases:
añadir una letra al principio, añadir una letra al final, o cambiar
cada 0 por 01 y cada 1 por 10 (duplicar). Construir la palabra con a lo
sumo 100 frases, o informar de que necesita más.

## Entrada

La palabra, no vacía, de a lo sumo 10⁵ letras.

## Salida

El número de frases k (1 ≤ k ≤ 100) y las frases `front c`, `back c` o
`double` en orden, o −1. Se acepta cualquier descripción válida.

## Ejemplos

### Ejemplo 1

Entrada:

```
011010011
```

Salida:

```
5
back 1
front 0
double
double
back 1
```

## Solución

Leída al revés, una descripción quita algunas letras de los extremos
de la palabra, deshace una duplicación, vuelve a quitar letras, y así
sucesivamente. Una palabra puede desduplicarse cuando sus letras se
emparejan como 01 y 10, y entonces la primera letra de cada par da la
palabra más corta. Las palabras sin las repeticiones prohibidas tienen
una estructura conocida: salvo a lo sumo dos letras en cada extremo,
son la duplicación de una palabra más corta del mismo tipo. Así que las
menos frases para una palabra s se hallan probando todas las formas de
quitar hasta cinco letras de cada extremo (bastarían dos; cinco es un
margen) y deshacer la duplicación del resto, frente a añadir sin más
todas las letras de s una a una, quedándose con lo más barato; los
resultados se recuerdan por palabra. Las palabras de cada nivel son
trozos unas de otras, así que solo se prueban unas pocas decenas, y
dividir a la mitad deja unos log₂ n niveles. `O(n log n)`.

Después la descripción se escribe hacia delante: la palabra más corta,
la duplicación, las letras del principio en orden inverso y las del
final. Si ni siquiera las menos frases bastan con 100, la respuesta es
−1.

En el ejemplo 01101001 es la duplicación de 0110, que es la de 01: dos
letras, dos duplicaciones y un 1 al final, cinco frases.

Trampas:

- las letras añadidas al principio salen en orden inverso;
- un par 00 u 11 significa que la parte central no es una palabra
  duplicada;
- la respuesta no es única, así que el verificador reproduce las
  frases.

El número de frases es el mínimo hallado por una implementación
aceptada independiente, que busca todas las descripciones en anchura,
en 310 palabras: palabras cortas construidas con frases al azar y
trozos de la palabra de Thue–Morse de hasta 10⁵ letras.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1782_strings.cpp](1782_strings.cpp) | G++ 13.2 x64 | strings | O(n log n) | AC | 0.046 s | 2120 KB |
| [1782_strings.go](1782_strings.go) | Go 1.14 x64 | strings | O(n log n) | AC | 0.062 s | 8736 KB |
| [1782_strings.java](1782_strings.java) | Java 1.8 | strings | O(n log n) | AC | 0.171 s | 8444 KB |
| [1782_strings.py](1782_strings.py) | Python 3.12 x64 | strings | O(n log n) | AC | 0.156 s | 2592 KB |
| [1782_strings.rs](1782_strings.rs) | Rust 1.75 x64 | strings | O(n log n) | AC | 0.046 s | 2208 KB |
