# 1700. Despertar

[Timus 1700](https://acm.timus.ru/problem.aspx?space=1&num=1700) · dificultad 480 · implementation

Problema original de Pavel Atnashev, del XIII Campeonato de los Urales de Programación Competitiva, 4 de abril de 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada objeto tiene un conjunto de asociaciones. Para cada uno de varios
grupos de objetos, imprimir en orden alfabético las asociaciones comunes
a todos ellos, o «No solution.» si no hay ninguna.

## Entrada

n (2 ≤ n ≤ 1000) líneas «nombre: asociación asociación …», y luego m
(1 ≤ m ≤ 1000) líneas, cada una un grupo de al menos dos nombres de
objetos. Las palabras son de letras latinas minúsculas y las líneas
tienen a lo sumo 250 caracteres.

## Salida

Una línea por grupo.

## Ejemplos

### Ejemplo 1

Entrada:

```
6
whale: big black water animal
penguin: black white ice beak
piano: keyboard black white wire
jackboot: leather heel black
train: rail wheel black
rose: red green thorn
3
whale penguin piano jackboot train
penguin piano
jackboot rose
```

Salida:

```
black
black white
No solution.
```

## Solución

Se guardan las asociaciones de cada objeto como un conjunto, por su
nombre. Para un grupo se intersecan los conjuntos de sus miembros y se
imprime el resultado ordenado, o «No solution.» si queda vacío. Todas
las líneas son cortas, así que un grupo cuesta a lo sumo unos miles de
consultas a conjuntos. `O((n + m) · L log L)` para líneas de longitud
L.

Trampas:

- una asociación puede aparecer dos veces en un objeto, pero se
  imprime una vez (test 02);
- un grupo puede nombrar dos veces el mismo objeto (test 03);
- un objeto puede no tener ninguna asociación, y entonces su línea
  acaba justo después de los dos puntos.

Las respuestas coinciden con una implementación aceptada independiente.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1700_implementation.cpp](1700_implementation.cpp) | G++ 13.2 x64 | implementation | O((n + m) · L log L) | AC | 0.359 s | 7788 KB |
| [1700_implementation.go](1700_implementation.go) | Go 1.14 x64 | implementation | O((n + m) · L log L) | AC | 0.765 s | 8908 KB |
| [1700_implementation.java](1700_implementation.java) | Java 1.8 | implementation | O((n + m) · L log L) | AC | 0.437 s | 12376 KB |
| [1700_implementation.py](1700_implementation.py) | Python 3.12 x64 | implementation | O((n + m) · L log L) | AC | 0.390 s | 13524 KB |
| [1700_implementation.rs](1700_implementation.rs) | Rust 1.75 x64 | implementation | O((n + m) · L log L) | AC | 0.593 s | 3584 KB |
