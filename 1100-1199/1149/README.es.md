# 1149. Escribir una expresión anidada de senos

[Timus 1149](https://acm.timus.ru/problem.aspx?space=1&num=1149) · dificultad 61 · strings

Problema original de Vladimir Gladkov, del campeonato de programación por equipos de los Urales, Perm, abril de 2001, ronda de prueba.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Sea `Aₙ = sin(1−sin(2+sin(3−…sin(n)…)))`, con los signos alternando menos
y más, y `S_N = (…((A₁+N)A₂+N−1)A₃+…+2)A_N+1`. Para `1 ≤ N ≤ 200`, imprime
el texto de `S_N` exactamente como en el ejemplo, sin espacios.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N`.

## Salida

La expresión `S_N`.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
```

Salida:

```
((sin(1)+3)sin(1-sin(2))+2)sin(1-sin(2+sin(3)))+1
```

## Solución

Solo se pide el texto; no se calcula nada. `Aₙ` es `sin(1`, luego para
cada `k` siguiente el signo (menos tras un número impar, más tras uno par)
y `sin(k`, y al final `n` paréntesis de cierre. `S_N` empieza con `N − 1`
paréntesis de apertura; luego, para `i` de 1 a `N`, contiene `Aᵢ`, un más,
el número `N − i + 1` y un paréntesis de cierre tras cada parte menos la
última. La salida tiene unos `4·N²` caracteres, 165 mil para `N = 200`,
construidos en una sola cadena. `O(N²)`.

Detalles a tener en cuenta:

- el signo tras `k` depende de `k`, no de la profundidad del seno;
- la última parte `A_N+1` no lleva paréntesis de cierre;
- para `N = 1` la respuesta es simplemente `sin(1)+1`;
- no hay espacios en ningún sitio.

Las respuestas se compararon en todas las pruebas con una segunda
construcción que envuelve la expresión de dentro hacia fuera, `(S)Aᵢ+…`,
con `Aᵢ` construido por recursión.

## Notas por lenguaje

- Todos los lenguajes construyen la cadena en un solo búfer.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1149_strings.cpp](1149_strings.cpp) | G++ 13.2 x64 | strings | O(N²) | AC | 0.015 s | 768 KB |
| [1149_strings.go](1149_strings.go) | Go 1.14 x64 | strings | O(N²) | AC | 0.015 s | 2976 KB |
| [1149_strings.java](1149_strings.java) | Java 1.8 | strings | O(N²) | AC | 0.125 s | 4356 KB |
| [1149_strings.py](1149_strings.py) | Python 3.12 x64 | strings | O(N²) | AC | 0.046 s | 780 KB |
| [1149_strings.rs](1149_strings.rs) | Rust 1.75 x64 | strings | O(N²) | AC | 0.015 s | 636 KB |
