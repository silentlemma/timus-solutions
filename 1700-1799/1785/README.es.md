# 1785. Perdidos en la localización

[Timus 1785](https://acm.timus.ru/problem.aspx?space=1&num=1785) · dificultad 16 · implementation

Problema original del folclore, del Concurso Regional Escolar de Programación de los Urales 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un juego nombra el tamaño de un ejército con una palabra en lugar de un
número: 1–4 es "few", 5–9 "several", 10–19 "pack", 20–49 "lots", 50–99
"horde", 100–249 "throng", 250–499 "swarm", 500–999 "zounds", y 1000 o
más "legion". Imprimir la palabra para un número dado de monstruos.

## Entrada

n (1 ≤ n ≤ 2000).

## Salida

La palabra para n.

## Ejemplos

### Ejemplo 1

Entrada:

```
7
```

Salida:

```
several
```

### Ejemplo 2

Entrada:

```
40
```

Salida:

```
lots
```

## Solución

Se guardan los extremos inferiores de los rangos de mayor a menor,
1000, 500, 250, 100, 50, 20, 10, 5, 1, junto a sus palabras. Se saltan
los extremos mayores que n; el primero que no lo es da la palabra.
`O(1)`.

En los ejemplos 7 pasa de 1000 hasta 10 y se detiene en 5, "several";
40 se detiene en 20, "lots".

Trampas:

- los extremos pertenecen a la palabra mayor: 5 es "several", 1000 es
  "legion";
- todo n de 1000 a 2000 es "legion".

Las respuestas coinciden con una implementación aceptada independiente
en cada n de 1 a 2000.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1785_implementation.cpp](1785_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.031 s | 380 KB |
| [1785_implementation.go](1785_implementation.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.031 s | 1080 KB |
| [1785_implementation.java](1785_implementation.java) | Java 1.8 | implementation | O(1) | AC | 0.093 s | 1576 KB |
| [1785_implementation.py](1785_implementation.py) | Python 3.12 x64 | implementation | O(1) | AC | 0.093 s | 424 KB |
| [1785_implementation.rs](1785_implementation.rs) | Rust 1.75 x64 | implementation | O(1) | AC | 0.015 s | 228 KB |
