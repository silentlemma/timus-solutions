# 2066. El menor valor con tres números

[Timus 2066](https://acm.timus.ru/problem.aspx?space=1&num=2066) · dificultad 28 · bruteforce

Problema original de Kirill Borozdin, del Concurso Regional Escolar de Programación de los Urales 2015.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Tres enteros no negativos pueden escribirse en cualquier orden con uno
de los signos +, − o × entre cada dos vecinos; la multiplicación va
primero y no hay paréntesis ni menos unario. Hallar el menor valor
posible de una expresión así. Los límites son 1 segundo y 64 MB.

## Entrada

Los números a ≤ b ≤ c, 0 ≤ a, cada uno en su línea, c ≤ 100.

## Salida

El menor valor.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

### Ejemplo 1

Entrada:

```
1
2
3
```

Salida:

```
-5
```

## Solución

Solo hay 6 órdenes y 9 pares de signos, así que los programas prueban
las 54 expresiones. Se evalúa x op₁ y op₂ z con la precedencia usual: si
solo el segundo signo es ×, primero se calcula y × z; si no, se va de
izquierda a derecha.

La búsqueda siempre termina con la misma forma: el menor número menos el
mayor de b + c y b × c, es decir, a − max(b + c, b × c). Restar al menor
número tanto como sea posible es lo mejor, y b + c supera a b × c solo
cuando uno de ellos es 0 o 1. Comprobar las 176 851 entradas confirma la
fórmula, pero la búsqueda directa no necesita ninguna demostración.

En el ejemplo 1 − 2 × 3 = −5.

## Notas por lenguaje

Ningún lenguaje necesita nada especial.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2066_bruteforce.cpp](2066_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(1) | AC | 0.015 s | 184 KB |
| [2066_bruteforce.go](2066_bruteforce.go) | Go 1.14 x64 | bruteforce | O(1) | AC | 0.031 s | 1080 KB |
| [2066_bruteforce.java](2066_bruteforce.java) | Java 1.8 | bruteforce | O(1) | AC | 0.140 s | 1632 KB |
| [2066_bruteforce.py](2066_bruteforce.py) | Python 3.12 x64 | bruteforce | O(1) | AC | 0.078 s | 532 KB |
| [2066_bruteforce.rs](2066_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(1) | AC | 0.062 s | 224 KB |
