# 2012. Doce Tareas Antes del Límite

[Timus 2012](https://acm.timus.ru/problem.aspx?space=1&num=2012) · dificultad 17 · math

Problema original de Alexander Ipatov, preparado por Olga Soboleva, de la subregión oriental del NEERC 2014.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una sesión de cinco horas contiene doce tareas. Durante la primera hora
se terminan exactamente `f`. Aunque se acaben antes, la tarea siguiente
comienza solo al terminar esa hora completa. Cada tarea restante ocupa
exactamente 45 minutos y se trabaja en secuencia. Decide si todas
terminan dentro de la sesión.

## Entrada

Un entero `f`, `1 ≤ f ≤ 11`. Tiempo límite 1 segundo, memoria 64 MB.

## Salida

Escribe `YES` en mayúsculas si el plan termina a tiempo, o `NO` en caso
contrario. La respuesta única se compara por tokens.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
7
```

```
YES
```

```
5
```

```
NO
```

Con `f=7` quedan cinco tareas y se necesitan `60+5·45=285` minutos, como
máximo 300. Con `f=5` quedan siete y el tiempo es `60+7·45=375`, que
supera el límite.

## Solución

La primera hora ocupa 60 minutos, y las 12 − f tareas restantes 45
minutos cada una, una tras otra. El plan cabe cuando
60 + 45 · (12 − f) ≤ 300, es decir, cuando f ≥ 7. `O(1)`.

Detalle: las tareas restantes empiezan solo después de la primera hora
completa, aunque las primeras f se terminen antes.

## Soluciones optimizadas

Las soluciones optimizadas en C++ y Java comprueban la misma
desigualdad. C++ lee con `scanf` e imprime con `puts` en lugar de
`iostream`: 116 KB en lugar de 380 KB, con el mismo tiempo. Java analiza
el número a mano desde `System.in` en lugar de usar `Scanner`: 0.078 s
en lugar de 0.125 s y 432 KB en lugar de 1532 KB.

La solución optimizada en Rust escribe la respuesta como bytes en una
sola llamada en lugar de usar `println!`: 0.015 s en lugar de 0.046 s y
220 KB en lugar de 236 KB.

## Notas por lenguaje

Ningún lenguaje necesita nada especial.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [2012_math.cpp](2012_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 380 KB | 11292500 |
| [2012_math.go](2012_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 1080 KB | 11292501 |
| [2012_math.java](2012_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1532 KB | 11303528 |
| [2012_math.py](2012_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 348 KB | 11292502 |
| [2012_math.rs](2012_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.046 s | 236 KB | 11292505 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [2012_math_optimized.cpp](2012_math_optimized.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 116 KB | 11303657 |
| [2012_math_optimized.java](2012_math_optimized.java) | Java 1.8 | math | O(1) | AC | 0.078 s | 432 KB | 11303529 |
| [2012_math_optimized.rs](2012_math_optimized.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 220 KB | 11303792 |
