# 1748. El número más complejo

[Timus 1748](https://acm.timus.ru/problem.aspx?space=1&num=1748) · dificultad 266 · number_theory

Problema original de Petr Lezhankin, del concurso de la USATU de Ufá en el campus de entrenamiento de verano de Petrozavodsk, agosto de 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

La complejidad de un número es su número de divisores. Para cada n
dado, hallar el número más complejo de 1 a n, el menor si hay empate, y
su complejidad.

## Entrada

t (1 ≤ t ≤ 100) y luego t números n (1 ≤ n ≤ 10¹⁸).

## Salida

Para cada n, el número y su número de divisores.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
1
10
100
1000
10000
```

Salida:

```
1 1
6 4
60 12
840 32
7560 64
```

## Solución

El número de divisores de p₁^a₁ · p₂^a₂ · … es (a₁ + 1)(a₂ + 1)…, que
solo depende de los exponentes. Poner los exponentes mayores en los
primos menores da el menor número con esos exponentes, así que la
respuesta siempre es de la forma 2^a · 3^b · 5^c · … con a ≥ b ≥ c ≥ …
en primos consecutivos. Hasta 10¹⁸ hay solo unas decenas de miles de
números así, y los primos necesarios terminan antes de 53, pues
2 · 3 · … · 53 ya pasa de 10¹⁸.

Se listan todos con una búsqueda sobre los exponentes, se ordenan y se
recorren hacia arriba guardando el mejor hasta el momento: un número
sustituye al mejor solo con estrictamente más divisores, lo que deja el
menor en los empates. Cada consulta es entonces una búsqueda binaria
del último número de la lista que no pasa de n.
`O(K log K + t log K)` para los K = 32 749 números listados.

Para n = 100 la respuesta es 60 = 2² · 3 · 5 con 3 · 2 · 2 = 12
divisores.

Trampas:

- los productos cerca de 10¹⁸ desbordan 64 bits salvo que se compruebe
  el límite dividiendo antes de multiplicar;
- en un empate gana el número menor: 2 y 3 tienen dos divisores.

Las respuestas coinciden con una criba de números de divisores en 100
consultas aleatorias hasta 20 000, y con una implementación aceptada
independiente en 30 pruebas aleatorias hasta 10¹⁸ y alrededor de los
números récord.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1748_number_theory.cpp](1748_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(K log K + t log K) | AC | 0.015 s | 1924 KB |
| [1748_number_theory.go](1748_number_theory.go) | Go 1.14 x64 | number_theory | O(K log K + t log K) | AC | 0.031 s | 5404 KB |
| [1748_number_theory.java](1748_number_theory.java) | Java 1.8 | number_theory | O(K log K + t log K) | AC | 0.187 s | 8084 KB |
| [1748_number_theory.py](1748_number_theory.py) | Python 3.12 x64 | number_theory | O(K log K + t log K) | AC | 0.156 s | 6608 KB |
| [1748_number_theory.rs](1748_number_theory.rs) | Rust 1.75 x64 | number_theory | O(K log K + t log K) | AC | 0.031 s | 1368 KB |
