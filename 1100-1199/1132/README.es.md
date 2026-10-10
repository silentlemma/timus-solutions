# 1132. Todas las raíces cuadradas de a módulo un primo n, hasta 100000 consultas

[Timus 1132](https://acm.timus.ru/problem.aspx?space=1&num=1132) · dificultad 548 · number_theory

Problema original de Mikhail Medvedev.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Para hasta `K ≤ 100000` consultas `a, n` con `n ≤ 32767` primo y
`1 ≤ a ≤ 32767` no divisible por `n`, imprime en orden creciente todos los
`x` de `1` a `n − 1` con `x² ≡ a (mod n)`, o `No root` si no hay ninguno.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`K` y luego `K` líneas con `a` y `n`.

## Salida

Una línea por consulta: las raíces separadas por espacios, o `No root`.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
4 17
3 7
2 7
14 31
10007 20011
```

Salida:

```
2 15
No root
3 4
13 18
5382 14629
```

## Solución

Se reduce `a` módulo `n`. Para `n = 2` la única raíz es `1`. Para un
primo impar, el criterio de Euler decide si hay raíz: `a^((n−1)/2)` vale
`1` para un residuo cuadrático y `n − 1` en otro caso. Si existe una raíz
`r`, la otra es `n − r`, y son distintas porque `n` es impar y `a` no es
cero.

La raíz misma sale del algoritmo de Tonelli–Shanks. Se escribe
`n − 1 = q·2^s` con `q` impar y se toma cualquier no residuo `z`. Se
empieza con `r = a^((q+1)/2)`, `t = a^q` y `c = z^q`; entonces siempre se
cumple `r² = a·t`. Mientras `t ≠ 1`, se busca el menor `i` con
`t^(2^i) = 1`, se toma `b = c^(2^(s−i−1))` y se actualiza `r ← r·b`,
`t ← t·b²`, `c ← b²`, `s ← i`. Cada paso baja el orden de `t`, así que en
como mucho `s` pasos `t = 1` y `r² = a`. El menor no residuo de cada
primo se busca una vez y se guarda. Para `n ≡ 3 (mod 4)` el bucle no se
ejecuta y `r = a^((n+1)/4)`. `O(log² n)` por consulta.

Detalles a tener en cuenta:

- `a` puede ser mayor que `n`, así que primero se reduce;
- `n = 2` tiene una sola raíz, `1`, y el criterio de Euler no se aplica;
- las dos raíces se imprimen empezando por la menor;
- con hasta 100000 consultas, la entrada y la salida van con búfer.

Las respuestas se compararon en todas las pruebas con una tabla de todos
los cuadrados módulo cada primo que aparece.

## Notas por lenguaje

- Todos los lenguajes usan el mismo Tonelli–Shanks y guardan el no
  residuo de cada primo.
- Go lee los 200000 números con un pequeño lector byte a byte, más rápido
  que `fmt.Fscan`.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1132_number_theory.cpp](1132_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(K log² n) | AC | 0.203 s | 2196 KB |
| [1132_number_theory.go](1132_number_theory.go) | Go 1.14 x64 | number_theory | O(K log² n) | AC | 0.093 s | 1668 KB |
| [1132_number_theory.java](1132_number_theory.java) | Java 1.8 | number_theory | O(K log² n) | AC | 0.281 s | 5908 KB |
| [1132_number_theory.py](1132_number_theory.py) | Python 3.12 x64 | number_theory | O(K log² n) | AC | 0.468 s | 19404 KB |
| [1132_number_theory.rs](1132_number_theory.rs) | Rust 1.75 x64 | number_theory | O(K log² n) | AC | 0.015 s | 4068 KB |
