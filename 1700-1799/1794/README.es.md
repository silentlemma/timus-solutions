# 1794. Obras maestras de la arquitectura mundial

[Timus 1794](https://acm.timus.ru/problem.aspx?space=1&num=1794) · dificultad 197 · implementation

Problema original de Vladislav Isenbaev (preparado por Oleg Dolgorukov), del Concurso Regional Escolar de Programación de los Urales 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

n estudiantes se sientan en círculo, numerados de 1 a n en sentido
horario, y hablarán uno tras otro en sentido horario. El estudiante i
quiere hablar en el turno aᵢ. Elegir quién habla primero para que el
mayor número posible de estudiantes hable justo en el turno que quiere.
Se acepta cualquier mejor elección.

## Entrada

n (2 ≤ n ≤ 10⁵), luego a₁, …, aₙ (1 ≤ aᵢ ≤ n).

## Salida

El número del estudiante que empieza.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
4 1 2 3
```

Salida:

```
2
```

### Ejemplo 2

Entrada:

```
3
1 1 1
```

Salida:

```
3
```

## Solución

Si empieza el estudiante k, el estudiante i habla en el turno
((i − k) mod n) + 1. Así que al estudiante i le conviene exactamente un
inicio, k = ((i − aᵢ) mod n) + 1. Se cuentan esos votos de todos los
estudiantes y se imprime un inicio con más votos. `O(n)`.

En el primer ejemplo los cuatro estudiantes votan por el inicio 2: por
ejemplo, el estudiante 1 quiere ser cuarto, y 2, 3, 4, 1 lo pone
cuarto.

Trampas:

- i − aᵢ puede ser negativo, y en C++, Go y Java el resto también lo es
  entonces;
- varios inicios pueden empatar, como en el segundo ejemplo, donde se
  acepta cualquiera de los tres.

El verificador cuenta los votos por sí mismo y acepta cualquier inicio
con el máximo. Coincide con un recuento directo sobre todos los inicios
en 300 clases pequeñas, y las respuestas coinciden con una
implementación aceptada independiente en las grandes.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1794_implementation.cpp](1794_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.078 s | 588 KB |
| [1794_implementation.go](1794_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.031 s | 2400 KB |
| [1794_implementation.java](1794_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.140 s | 812 KB |
| [1794_implementation.py](1794_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.109 s | 8340 KB |
| [1794_implementation.rs](1794_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.031 s | 2136 KB |
