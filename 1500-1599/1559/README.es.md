# 1559. Lingüística de los TruCoders

[Timus 1559](https://acm.timus.ru/problem.aspx?space=1&num=1559) · dificultad 4082 · parsing

Problema original del Novosibirsk SU Contest en el campus de Petrozavodsk, septiembre de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un lenguaje viene dado por una expresión de como mucho 10000 caracteres
formada por letras minúsculas (una palabra de una letra), 0 (el
conjunto vacío), paréntesis, concatenación, unión `|` y estrella `*`
(cualquier número de repeticiones, incluido ninguno, que da la palabra
vacía). Tres personas pueden aprender como mucho 10¹⁰⁰⁰⁰⁰ palabras cada
una. Hay que imprimir F si entre las tres pueden aprender todo el
lenguaje y N en caso contrario.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Una línea con la expresión.

## Salida

F o N.

## Ejemplos

### Ejemplo 1

Entrada:

```
((a|b)(c|d))
```

Salida:

```
F
```

## Solución

La respuesta es N exactamente cuando el lenguaje es infinito. Un
lenguaje finito dado por una expresión de longitud L tiene como mucho
2^L palabras: una letra o 0 tiene como mucho 1, una unión suma tamaños,
una concatenación los multiplica, y una estrella sobre un lenguaje
finito sin palabras no vacías da solo la palabra vacía, así que cada
carácter como mucho duplica la cota. Y 2^10000 ronda 10³⁰¹¹, muy por
debajo de 3·10¹⁰⁰⁰⁰⁰.

Para cada subexpresión basta saber cuatro cosas: si el conjunto es no
vacío, si contiene la palabra vacía, si contiene una palabra no vacía y
si es infinito. Una unión los combina con «o». Una concatenación es
vacía si alguna parte lo es y, si no, contiene la palabra vacía si
ambas partes la contienen, una palabra no vacía si alguna la contiene,
y es infinita si alguna lo es. Una estrella nunca es vacía, siempre
contiene la palabra vacía y es infinita exactamente cuando su argumento
contiene una palabra no vacía.

Los paréntesis pueden anidarse unos 5000 niveles, así que la expresión
se lee con una pila explícita en lugar de recursión. Cada nivel de
paréntesis guarda la unión hasta el momento, la concatenación hasta el
momento y su último símbolo, al que aún puede aplicarse una estrella
siguiente. Esto tarda O(L). Los resultados se contrastaron con una
fuerza bruta que enumera las palabras hasta una longitud fija en
expresiones aleatorias.

Detalles a tener en cuenta:

- una estrella no siempre da infinitas palabras: 0* y (0|(0)*)* son solo
  la palabra vacía (pruebas 03, 05);
- un factor vacío vacía toda la concatenación, estrella incluida: a*0
  no tiene palabras (prueba 04);
- el límite 10¹⁰⁰⁰⁰⁰ solo parece un número con el que comparar: incluso
  2000 elecciones entre dos letras dan solo 2^2000 palabras
  (prueba gen7);
- la recursión sobre 5000 paréntesis anidados puede desbordar la pila
  (prueba gen1).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1559_parsing.cpp](1559_parsing.cpp) | G++ 13.2 x64 | parsing | O(L) | AC | 0.015 s | 520 KB |
| [1559_parsing.go](1559_parsing.go) | Go 1.14 x64 | parsing | O(L) | AC | 0.046 s | 1308 KB |
| [1559_parsing.java](1559_parsing.java) | Java 1.8 | parsing | O(L) | AC | 0.125 s | 680 KB |
| [1559_parsing.py](1559_parsing.py) | Python 3.12 x64 | parsing | O(L) | AC | 0.093 s | 1152 KB |
| [1559_parsing.rs](1559_parsing.rs) | Rust 1.75 x64 | parsing | O(L) | AC | 0.046 s | 380 KB |
