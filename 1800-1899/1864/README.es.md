# 1864. Reunión en casa de Den

[Timus 1864](https://acm.timus.ru/problem.aspx?space=1&num=1864) · dificultad 176 · math

Problema original del folclore (preparado por Daniil Ayzenshteyn), del Campeonato Abierto de la Universidad Federal de los Urales, 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

n amigos fueron a casa de Den; el amigo i compró aᵢ litros de zumo, y
todos, Den incluido, bebieron lo mismo. Luego Den paga 100 rublos por
el zumo que bebió quien no lo había comprado, repartidos con justicia
entre los amigos que compraron más de lo que bebieron. ¿Cuántos rublos
recibe cada amigo, redondeando hacia abajo?

## Entrada

n (2 ≤ n ≤ 100), luego a₁, …, aₙ (0 ≤ aᵢ ≤ 100) con suma positiva.

## Salida

Los rublos de cada amigo, redondeados hacia abajo.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
10 10 10
```

Salida:

```
33 33 33
```

### Ejemplo 2

Entrada:

```
2
10 0
```

Salida:

```
100 0
```

## Solución

Con S litros en total, cada una de las n + 1 personas bebe S/(n + 1),
así que el amigo i compró para otros aᵢ − S/(n + 1) litros si eso es
positivo, y nada en otro caso. El dinero se reparte en proporción a
esas cantidades. Multiplicándolo todo por n + 1 todo queda en enteros:
eᵢ = max(0, aᵢ(n + 1) − S), y el amigo i recibe ⌊100·eᵢ / Σ e⌋. La suma
nunca es 0: los amigos compraron S entre todos y solo bebieron
nS/(n + 1). `O(n)`.

En el primer ejemplo cada uno bebió 7,5 litros y cada amigo pagó 2,5
litros para Den, así que el dinero se reparte entre tres: 33 cada uno
tras redondear.

Trampas:

- Den también bebe, así que la parte es S/(n + 1), no S/n;
- los amigos que compraron menos de lo que bebieron no reciben nada;
- los enteros exactos evitan cualquier duda al redondear hacia abajo.

Los repartos coinciden con una implementación aceptada independiente en
doscientas reuniones aleatorias.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1864_math.cpp](1864_math.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.015 s | 200 KB |
| [1864_math.go](1864_math.go) | Go 1.14 x64 | math | O(n) | AC | 0.031 s | 1116 KB |
| [1864_math.java](1864_math.java) | Java 1.8 | math | O(n) | AC | 0.125 s | 1720 KB |
| [1864_math.py](1864_math.py) | Python 3.12 x64 | math | O(n) | AC | 0.093 s | 412 KB |
| [1864_math.rs](1864_math.rs) | Rust 1.75 x64 | math | O(n) | AC | 0.015 s | 236 KB |
