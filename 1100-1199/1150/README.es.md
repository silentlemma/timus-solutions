# 1150. Cuántas veces aparece cada cifra en los números de página de 1 a N

[Timus 1150](https://acm.timus.ru/problem.aspx?space=1&num=1150) · dificultad 249 · math

Problema original de Evgeny Bryzgalov, del campeonato de programación por equipos de los Urales, Perm, abril de 2001, ronda en inglés.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Las páginas se numeran de 1 a `N`, `N < 10⁹`. Cuenta cuántas veces se
escribe cada cifra de 0 a 9.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N`.

## Salida

Diez líneas: la cantidad de ceros, unos, …, nueves.

## Ejemplos

### Ejemplo 1

Entrada:

```
12
```

Salida:

```
1
5
2
1
1
1
1
1
1
1
```

## Solución

Se cuenta cada posición decimal por separado. Para la posición de peso
`p` (1, 10, 100, …) se parte `N` en la parte de encima, `high = N / (10p)`,
la cifra `cur` en ella y la parte de debajo, `low = N mod p`. Se miran los
números de 1 a `N` según su parte por encima de esta posición:

- cada parte superior de `0` a `high − 1` va seguida de los `10p` finales
  inferiores, así que para cada una cada cifra aparece `p` veces en esta
  posición;
- con la parte superior igual a `high`, una cifra `d < cur` aparece `p`
  veces más, `d = cur` aparece `low + 1` veces más (para los finales de `0`
  a `low`), y las cifras mayores no aparecen.

Los ceros son distintos: un cero en esta posición solo se escribe si hay
alguna cifra no nula encima, así que la parte superior `0` no cuenta. Eso
da `(high − 1)·p` para las partes superiores completas desde 1, y luego
`p` o `low + 1` como antes, todo solo cuando `high > 0`. Hay como mucho
nueve posiciones. `O(log N)`.

Detalles a tener en cuenta:

- los ceros a la izquierda no se escriben, por eso los ceros necesitan la
  regla aparte;
- las cantidades llegan a `9·10⁸` para `N = 999999999`, aún dentro de 32
  bits;
- `N` también se incluye.

Las respuestas se compararon con escribir cada número para todos los `N`
hasta 3000 y muchos hasta 30000, y con un recuento cifra a cifra sobre la
escritura decimal de `N` en todas las pruebas.

## Notas por lenguaje

- Todos los lenguajes hacen el mismo bucle por posiciones.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1150_math.cpp](1150_math.cpp) | G++ 13.2 x64 | math | O(log N) | AC | 0.015 s | 128 KB |
| [1150_math.go](1150_math.go) | Go 1.14 x64 | math | O(log N) | AC | 0.031 s | 1084 KB |
| [1150_math.java](1150_math.java) | Java 1.8 | math | O(log N) | AC | 0.109 s | 1568 KB |
| [1150_math.py](1150_math.py) | Python 3.12 x64 | math | O(log N) | AC | 0.062 s | 460 KB |
| [1150_math.rs](1150_math.rs) | Rust 1.75 x64 | math | O(log N) | AC | 0.015 s | 236 KB |
