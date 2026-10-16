# 1800. La ley de Murphy

[Timus 1800](https://acm.timus.ru/problem.aspx?space=1&num=1800) · dificultad 170 · math

Problema original de Alex Samsonov, de la subregión oriental del NEERC 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una tostada, un segmento delgado de longitud l, cae desde la altura h
con la mantequilla hacia abajo, sostenida horizontal. Cae libremente
(g = 9,81 m/s²) y gira alrededor de su centro a ω revoluciones por
minuto en un plano vertical. ¿Qué lado toca primero el suelo? Se
garantiza que no lo toca estando vertical.

## Entrada

l y h en centímetros y ω en revoluciones por minuto, enteros de 1 a
1000.

## Salida

"butter" o "bread".

## Ejemplos

### Ejemplo 1

Entrada:

```
10 400 15
```

Salida:

```
butter
```

### Ejemplo 2

Entrada:

```
10 500 15
```

Salida:

```
bread
```

## Solución

Tras t segundos el centro está a h − g·t²/2 y la tostada ha girado
ω·t, así que su extremo inferior está a
gap(t) = h − g·t²/2 − (l/2)·|sin ωt|. La respuesta solo depende del
cuarto de vuelta en que gap llega a cero por primera vez: en los
cuartos 0 y 3 de una vuelta la mantequilla mira hacia abajo, en el 1 y
el 2 el pan. Así que se recorren los cuartos en orden.

En un cuarto par |sin ωt| crece, el extremo inferior baja más rápido
que el centro y gap solo decrece: la tostada toca en él exactamente
cuando gap ≤ 0 al final del cuarto. En un cuarto impar el extremo sube
respecto al centro, y gap puede bajar, luego subir y luego bajar de
nuevo. Su derivada ahí es cóncava, pues la tercera derivada es
(l/2)·ω³·cos ≤ 0. Se halla el pico de la derivada por bisección sobre
la segunda derivada. Si la derivada en el pico es positiva, una
segunda bisección encuentra dónde se vuelve positiva, el mínimo local
de gap. El cuarto contiene el primer contacto si ese mínimo o el valor
al final es como mucho cero. El centro llega al suelo en
aproximadamente 1,5 segundos, así que hay como mucho un centenar de
cuartos. `O(ω)`.

En el primer ejemplo la tostada gira un cuarto de vuelta por segundo y
cae tras unos 0,9 s, a unos 81°: mantequilla. Desde 5 m cae justo
pasados los 90°: pan.

Trampas:

- el extremo de la tostada puede tocar antes de que el centro haya
  caído mucho: una tostada larga sostenida baja toca en el primer
  cuarto;
- en un cuarto impar gap no es monótona, así que su valor al final del
  cuarto puede perder un contacto;
- las unidades: centímetros a metros, revoluciones por minuto a
  radianes por segundo.

Las respuestas coinciden con una implementación aceptada independiente,
que avanza por el tiempo en microsegundos, en 1548 entradas: 1500
aleatorias y los valores extremos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1800_math.cpp](1800_math.cpp) | G++ 13.2 x64 | math | O(omega) | AC | 0.015 s | 376 KB |
| [1800_math.go](1800_math.go) | Go 1.14 x64 | math | O(omega) | AC | 0.031 s | 1084 KB |
| [1800_math.java](1800_math.java) | Java 1.8 | math | O(omega) | AC | 0.109 s | 1636 KB |
| [1800_math.py](1800_math.py) | Python 3.12 x64 | math | O(omega) | AC | 0.093 s | 592 KB |
| [1800_math.rs](1800_math.rs) | Rust 1.75 x64 | math | O(omega) | AC | 0.031 s | 236 KB |
