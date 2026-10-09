# 1097. Colocar un parque cuadrado molestando a los propietarios menos influyentes

[Timus 1097](https://acm.timus.ru/problem.aspx?space=1&num=1097) · dificultad 1363 · bruteforce

Problema original de Stanislav Vasiliev, del USU Open Collegiate Programming Contest, marzo de 2001, Senior Session.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un país cuadrado de lado `L` tiene su esquina inferior izquierda en
`(1, 1)` (`1 ≤ A ≤ L ≤ 10000`). Hay `M ≤ 100` parcelas cuadradas ocupadas,
con vértices enteros y lados paralelos a los ejes; se tocan como mucho por
el borde, y cada una tiene una influencia de 2 a 100, o 255 para las
parcelas del jurado, que no se pueden tomar. Coloca un parque cuadrado
de lado `A` con vértices enteros dentro del país de modo que la mayor
influencia entre las parcelas que solapa (con área positiva) sea lo menor
posible. Imprime 1 si el parque cabe en tierra libre, la menor influencia
posible en otro caso, o `IMPOSSIBLE` si todo sitio solapa una parcela del
jurado.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`L` y `A`, luego `M`, y luego `M` líneas con la influencia, el lado y la
esquina inferior izquierda de una parcela.

## Salida

1, la menor influencia o `IMPOSSIBLE`.

## Evaluación

La salida se compara token a token; los espacios en blanco de más no
importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 3
6
94 2 4 1
3 1 1 1
2 1 1 2
2 2 2 1
100 1 2 4
255 1 5 5
```

Salida:

```
3
```

### Ejemplo 2

Entrada:

```
5 3
1
255 1 3 3
```

Salida:

```
IMPOSSIBLE
```

## Solución

El parque con esquina inferior izquierda `(px, py)` ocupa
`[px, px + A] × [py, py + A]` y solapa una parcela `[x, x + s] × [y, y + s]`
exactamente cuando `px < x + s`, `x < px + A`, y lo mismo vale para `y`.

Se fija `py` y se desliza el parque de izquierda a derecha. El conjunto de
parcelas solapadas solo cambia cuando su lado izquierdo pasa el lado
derecho de una parcela (que queda atrás, en `px = x + s`) o su lado
derecho pasa el lado izquierdo de una parcela (que entra). Entrar solo
añade parcelas, así que las mejores posiciones están en `px = 1` o en
algún `x + s`. Lo mismo vale para `py` con `x` fijo, así que `(px, py)`
se toma de como mucho 101 valores en cada eje, y cada par se comprueba
contra todas las parcelas. `O(M³)`, alrededor de un millón de
comprobaciones.

Detalles a tener en cuenta:

- las parcelas que solo tocan el parque por un lado no cuentan, así que
  todas las comparaciones son estrictas;
- el parque debe quedar dentro del país: `px + A − 1 ≤ L`, es decir
  `px ≤ L − A + 1`;
- 255 no es una influencia grande sino una parcela prohibida: un sitio
  que la solape no está permitido en absoluto.

Las respuestas se comprobaron probando todas las posiciones del parque en
países con `L ≤ 40`.

## Notas por lenguaje

- Python guarda primero, para cada `px`, las parcelas de esa franja
  vertical, lo que acorta mucho el bucle interior.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1097_bruteforce.cpp](1097_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(M^3) | AC | 0.015 s | 388 KB |
| [1097_bruteforce.go](1097_bruteforce.go) | Go 1.14 x64 | bruteforce | O(M^3) | AC | 0.031 s | 1348 KB |
| [1097_bruteforce.java](1097_bruteforce.java) | Java 1.8 | bruteforce | O(M^3) | AC | 0.125 s | 2152 KB |
| [1097_bruteforce.py](1097_bruteforce.py) | Python 3.12 x64 | bruteforce | O(M^3) | AC | 0.078 s | 572 KB |
| [1097_bruteforce.rs](1097_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(M^3) | AC | 0.031 s | 232 KB |
