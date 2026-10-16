# 1779. El gran equipo

[Timus 1779](https://acm.timus.ru/problem.aspx?space=1&num=1779) · dificultad 344 · constructive

Problema original de Ivan Burmistrov, del XV Campeonato Abierto por Equipos de Programación de la Universidad Estatal de los Urales.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Construir un grafo de amistades entre n estudiantes en el que no haya
tres estudiantes con el mismo número de amigos, o informar de que no
existe.

## Entrada

n (3 ≤ n ≤ 200).

## Salida

El número de parejas de amigos y las parejas, o −1 si ningún grafo
sirve. Se acepta cualquier grafo válido.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
```

Salida:

```
2
1 3
3 4
```

## Solución

Se une a los estudiantes i y j siempre que i + j > n. Así el estudiante
i es amigo de los i estudiantes n − i + 1, …, n, salvo de sí mismo si
está entre ellos, es decir, si 2i > n. Por tanto el estudiante i tiene i
amigos si i ≤ n/2 e i − 1 si i > n/2: los números van 1, 2, … hasta la
mitad y siguen después, y solo uno, el del medio, lo comparten dos
estudiantes. Así que siempre existe un grafo y nunca se imprime −1.
`O(n²)`.

Con cuatro estudiantes esto une 1–4, 2–3, 2–4 y 3–4, con 1, 2, 2 y 3
amigos, lo que sirve igual que la respuesta del ejemplo.

Trampas:

- n − 1 amigos y 0 amigos no pueden darse a la vez, así que los números
  de 0 a n − 1 nunca pueden ser todos distintos, y dos estudiantes
  deben compartir uno;
- el grafo puede ser denso, unas n²/4 parejas, así que la salida es
  grande;
- la respuesta no es única, así que el verificador cuenta los amigos él
  mismo.

La construcción pasa el verificador para todo n de 3 a 200, y también
una implementación aceptada independiente.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1779_constructive.cpp](1779_constructive.cpp) | G++ 13.2 x64 | constructive | O(n^2) | AC | 0.015 s | 292 KB |
| [1779_constructive.go](1779_constructive.go) | Go 1.14 x64 | constructive | O(n^2) | AC | 0.015 s | 2140 KB |
| [1779_constructive.java](1779_constructive.java) | Java 1.8 | constructive | O(n^2) | AC | 0.109 s | 2568 KB |
| [1779_constructive.py](1779_constructive.py) | Python 3.12 x64 | constructive | O(n^2) | AC | 0.093 s | 1952 KB |
| [1779_constructive.rs](1779_constructive.rs) | Rust 1.75 x64 | constructive | O(n^2) | AC | 0.015 s | 644 KB |
