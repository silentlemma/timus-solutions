# 1796. Parque de atracciones

[Timus 1796](https://acm.timus.ru/problem.aspx?space=1&num=1796) · dificultad 111 · math

Problema original de Eugene Kurpilyansky (preparado por Egor Shchelkonogov), del Concurso Regional Escolar de Programación de los Urales 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una maestra paga unas entradas con billetes de 10, 50, 100, 500, 1000 y
5000 rublos. El dinero alcanza para las entradas, pero ya no alcanzaría
si se quitara cualquier billete. Dados los billetes de cada tipo y el
precio de la entrada, listar todos los números posibles de entradas.

## Entrada

Seis cantidades de billetes, del menor al mayor, y luego el precio.
Todos los números son como mucho 1000, y el precio es positivo. Existe
al menos una respuesta.

## Salida

El número de respuestas posibles y luego las respuestas en orden
creciente.

## Ejemplos

### Ejemplo 1

Entrada:

```
0 2 0 0 0 0
10
```

Salida:

```
5
6 7 8 9 10
```

### Ejemplo 2

Entrada:

```
1 2 0 0 0 0
10
```

Salida:

```
1
11
```

## Solución

Sea T la suma y s el menor billete entregado. Para k entradas el dinero
debe alcanzar, k·price ≤ T. Sin cualquier billete no debe alcanzar, y
el menor billete es el caso más difícil: si T − s es poco, también lo
es la suma sin cualquier billete mayor. Así que T − s < k·price, y las
respuestas son todos los k de ⌊(T − s)/price⌋ + 1 a ⌊T/price⌋.
`O(answers)`, como mucho 5000.

En el primer ejemplo T = 100 y s = 50: sin un billete 50 rublos no
deben alcanzar, así que más de 5 entradas, y como mucho 10.

Trampas:

- el billete que se quita es el menor de los presentes, no el de 10
  rublos en general;
- con un billete de 5000 rublos y precio 1 hay 5000 respuestas en una
  línea.

Las respuestas coinciden con una implementación aceptada independiente
en 300 casos aleatorios con pocos y con muchos billetes.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1796_math.cpp](1796_math.cpp) | G++ 13.2 x64 | math | O(answers) | AC | 0.031 s | 460 KB |
| [1796_math.go](1796_math.go) | Go 1.14 x64 | math | O(answers) | AC | 0.031 s | 1288 KB |
| [1796_math.java](1796_math.java) | Java 1.8 | math | O(answers) | AC | 0.109 s | 1964 KB |
| [1796_math.py](1796_math.py) | Python 3.12 x64 | math | O(answers) | AC | 0.078 s | 752 KB |
| [1796_math.rs](1796_math.rs) | Rust 1.75 x64 | math | O(answers) | AC | 0.015 s | 480 KB |
