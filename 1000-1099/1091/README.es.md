# 1091. Contar conjuntos de números con un divisor común

[Timus 1091](https://acm.timus.ru/problem.aspx?space=1&num=1091) · dificultad 529 · number_theory

Problema original de Stanislav Vasiliev, del USU Open Collegiate Programming Contest, marzo de 2001, Senior Session.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cuenta los conjuntos de `K` enteros positivos distintos, ninguno mayor
que `S` (`2 ≤ K ≤ S ≤ 50`), cuyo máximo común divisor es mayor que 1.
Imprime la cuenta, o 10000 si es mayor.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`K` y `S`.

## Salida

El número de conjuntos, como mucho 10000.

## Evaluación

La salida se compara token a token; los espacios en blanco de más no
importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 10
```

Salida:

```
11
```

## Solución

La base didáctica Go cuenta por gcd exacto sin Möbius. Si K>floor(S/2), ningún divisor≥2 tiene suficientes múltiplos. Calcular solo C(m,K) para K≤m≤floor(S/2), desde1 con C(m−1,K)·m/(m−K). Descender d=D=floor(S/K)…2: de C(floor(S/d),K), restar cantidades ya conocidas con gcd2d,3d,… . Cada conjunto tiene gcd único; clases disjuntas y suma d≥2 dan respuesta. Para K=3 y S=10, el gcd exacto 3 aporta C(3,3)=1 conjunto y el gcd exacto 2 aporta C(5,3)=10, para un total de 11. Si C(m,K) llega a 10 000, elegir K entre los primeros m números pares ya da suficientes conjuntos válidos para devolver 10 000. Hasta entonces se multiplica un valor menor que 10 000 por m ≤ 25. Cada conteo exacto está acotado por su coeficiente binomial, así que al sumarlo a un total menor que 10 000 se obtiene menos de 20 000. La respuesta se limita a 10 000. Tiempo O(S + D log D), espacio O(S). Las versiones originales usan la tabla completa de Pascal para la suma con signo Σ−μ(d)C(floor(S/d),K) y limitan el resultado final.

## Soluciones optimizadas

La versión rápida de Go conserva la recurrencia por gcd exacto y usa los descriptores estándar y un búfer de seis bytes para la respuesta. Rust usa igual algoritmo con arreglos fijos32, E/S de caracteres C y entrada C. C++/Java/Python reutilizan originales admitidos. D=floor(S/K)≤25, sin tablas de respuestas precalculadas. Go anterior queda en Otros enfoques Accepted y Rust anterior como versión estándar sencilla. Asteriscos solo señalan objetivos de ranking.

Las implementaciones base aceptadas [1091_number_theory.cpp](1091_number_theory.cpp), [1091_number_theory.java](1091_number_theory.java), [1091_number_theory.py](1091_number_theory.py) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Notas por lenguaje

Go didáctico usa entrada con búfer y dos arreglos de26 enteros. Rust dos arreglos u32 de26 y getchar/putchar sin punteros. Respuesta≤10000 requiere como máximo cinco dígitos. Los cinco originales conservan Accepted/métricas exactos e intérprete Python real.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1091_number_theory.cpp](1091_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(S^2) | AC | 0.015 s | 232 KB | 11279091 |
| [1091_dp.go](1091_dp.go) | Go 1.14 x64 | dp | O(S + D log D) | AC | 0.015 s | 912 KB | 11315680 |
| [1091_number_theory.java](1091_number_theory.java) | Java 1.8 | number_theory | O(S^2) | AC | 0.109 s | 1640 KB | 11279094 |
| [1091_number_theory.py](1091_number_theory.py) \* | Python 3.12 x64 | number_theory | O(S^2) | AC | 0.078 s | 424 KB | 11279093 |
| [1091_number_theory.rs](1091_number_theory.rs) | Rust 1.75 x64 | number_theory | O(S^2) | AC | 0.046 s | 228 KB | 11279095 |

### Otros enfoques Accepted

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1091_number_theory.go](1091_number_theory.go) | Go 1.14 x64 | number_theory | O(S^2) | AC | 0.015 s | 1088 KB | 11279092 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1091_dp_optimized.go](1091_dp_optimized.go) \* | Go 1.14 x64 | dp | O(S + D log D) | AC | 0.015 s | 264 KB | 11315895 |
| [1091_dp.rs](1091_dp.rs) \* | Rust 1.75 x64 | dp | O(S + D log D) | AC | 0.015 s | 60 KB | 11315681 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
