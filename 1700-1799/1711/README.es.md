# 1711. Nombres en clave

[Timus 1711](https://acm.timus.ru/problem.aspx?space=1&num=1711) · dificultad 135 · greedy

Problema original de Alex Samsonov, preparado por Igor Chevdar, de la subregión oriental del NEERC 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada uno de los n problemas tiene tres nombres en clave candidatos, y
los problemas de un conjunto van en orden alfabético de sus nombres.
Hay que elegir un nombre por problema para que los problemas queden en
un orden dado, o informar de que no se puede.

## Entrada

n (1 ≤ n ≤ 16), luego n líneas con los tres nombres de cada problema:
letras minúsculas, a lo sumo 20, todos los nombres distintos. La última
línea es el orden pedido, una permutación de 1 … n.

## Salida

Los nombres elegidos en el orden pedido, uno por línea, o IMPOSSIBLE.
Se acepta cualquier elección válida.

## Ejemplos

### Ejemplo 1

Entrada:

```
11
cipher grille kamkohob
names codenames codes
newtests rejudge timus
size volume summit
watchmen braineater twosides
solution random yesorno
keywords subversion commands
bosses shooting shaitan
game strategy playgame
mnemonic palindromes bestname
eligibility rectangle rules
2 1 7 10 9 6 11 3 8 4 5
```

Salida:

```
codenames
grille
keywords
mnemonic
playgame
random
rectangle
rejudge
shaitan
volume
watchmen
```

### Ejemplo 2

Entrada:

```
3
problems in the
first sample are
ordered not randomly
1 2 3
```

Salida:

```
IMPOSSIBLE
```

## Solución

Se recorre el orden pedido y a cada problema se le da el menor de sus
nombres que va después del nombre elegido anterior. Si no hay ninguno,
la respuesta es IMPOSSIBLE.

Esta elección voraz es segura. Supongamos que existe una elección
válida y comparémosla con la voraz problema a problema. Por inducción,
el nombre voraz nunca va después del válido: el nombre válido del
siguiente problema va después del válido anterior, y por tanto también
después del voraz anterior. Así que es un candidato, y la elección
voraz no es mayor que él. Por eso el recorrido voraz nunca se atasca.
`O(n)` comparaciones de cadenas cortas.

Trampas:

- los nombres se comparan como cadenas, así que un prefijo va antes:
  «code» antes de «codenames»;
- la línea del orden da los números de problema según su lugar en el
  conjunto, no el lugar de cada problema;
- se acepta cualquier respuesta válida, así que las pruebas usan un
  comprobador.

El comprobador verifica que cada nombre pertenezca a su problema y que
los nombres crezcan. Las respuestas coinciden con una implementación
aceptada independiente en 600 conjuntos aleatorios.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1711_greedy.cpp](1711_greedy.cpp) | G++ 13.2 x64 | greedy | O(n) | AC | 0.015 s | 400 KB |
| [1711_greedy.go](1711_greedy.go) | Go 1.14 x64 | greedy | O(n) | AC | 0.062 s | 1148 KB |
| [1711_greedy.java](1711_greedy.java) | Java 1.8 | greedy | O(n) | AC | 0.140 s | 516 KB |
| [1711_greedy.py](1711_greedy.py) | Python 3.12 x64 | greedy | O(n) | AC | 0.093 s | 456 KB |
| [1711_greedy.rs](1711_greedy.rs) | Rust 1.75 x64 | greedy | O(n) | AC | 0.046 s | 236 KB |
