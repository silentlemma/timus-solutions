# 1343. Cuento de hadas

[Timus 1343](https://acm.timus.ru/problem.aspx?space=1&num=1343) · dificultad 417 · number_theory

Problema original de Pavel Atnashev, del USU Championship 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se dan las primeras k de 12 cifras, 0 ≤ k ≤ 12. Hay que imprimir
cualquier número de 12 cifras que empiece por ellas y no tenga más
divisores que 1 y él mismo. Se garantiza que existe respuesta.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

k en la primera línea y las k cifras en la segunda.

## Salida

El número de 12 cifras.

## Comprobación

El comprobador acepta cualesquiera 12 cifras que empiecen por las dadas
y formen un número sin otros divisores.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
64631
```

Salida:

```
646310554187
```

## Solución

La base didáctica preferida es división de prueba en C++. Completa el prefijo con ceros, trata 2 aparte y prueba candidatos impares. Un número es primo si no tiene divisor hasta su raíz cuadrada entera. Tras 2 y 3, los primos son 6q−1 o 6q+1; se prueban esos pares. Con N<10¹² los productos caben en 64 bits. Para G candidatos, tiempo O(G·sqrt(N)) y espacio auxiliar O(1), sin potencias modulares ni tabla de primos. La garantía de respuesta asegura encontrar un primo dentro del prefijo. Se imprimen doce dígitos con ceros iniciales. Si se dieron los doce, se reproduce el valor válido garantizado, incluido 000000000001. Esta base existe en C++; se conservan aparte las implementaciones aceptadas más avanzadas.

## Soluciones optimizadas

Miller–Rabin usa bases 2,3,5,7,11,13. Tras probar primos pequeños, escribe N−1=2ˢd con d impar. Calcula x=aᵈ mod N por base; pasa si x es 1 o N−1, o uno de sus s−1 cuadrados modulares siguientes es N−1; de lo contrario rechaza el candidato. [La cota de seis bases de Jaeschke](https://doi.org/10.1090/S0025-5718-1993-1192971-8), 3474749660383, cubre todo el dominio: aquí es determinista. G candidatos requieren O(G log N) operaciones de palabra. Go y Rust nuevos usan E/S acotada, con bits.Mul64/bits.Rem64 y u128 respectivamente. Java y Python reutilizan sus archivos admitidos. La cobertura rápida C++ comparte la [división de prueba](1343_bruteforce.cpp) de Sencillas: su Accepted exacto cumple la inclusión, sin copiar optimized. Esto no afirma que su complejidad sea mejor que Miller–Rabin. Las bases originales C++/Go/Rust permanecen en Otros enfoques Accepted.

Las implementaciones base aceptadas [1343_number_theory.java](1343_number_theory.java), [1343_number_theory.py](1343_number_theory.py) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Notas por lenguaje

La base elemental no necesita productos modulares anchos. Miller–Rabin C++/Rust usa 128 bits, Go math/bits y Java partes de 20 bits. Python mantiene el CPython realmente aceptado. Archivos y métricas originales no cambian. Los asteriscos afectan solo a fuentes rápidas seleccionadas que aún no alcanzan la meta de su lenguaje.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1343_bruteforce.cpp](1343_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(G sqrt N) | AC | 0.015 s | 112 KB | 11314926 |

### Otros enfoques Accepted

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1343_number_theory.cpp](1343_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(G·log N) | AC | 0.015 s | 392 KB | 11285094 |
| [1343_number_theory.go](1343_number_theory.go) | Go 1.14 x64 | number_theory | O(G·log N) | AC | 0.031 s | 1024 KB | 11285096 |
| [1343_number_theory.rs](1343_number_theory.rs) | Rust 1.75 x64 | number_theory | O(G·log N) | AC | 0.046 s | 216 KB | 11285099 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1343_number_theory_optimized.go](1343_number_theory_optimized.go) \* | Go 1.14 x64 | number_theory | O(G log N) | AC | 0.015 s | 312 KB | 11314932 |
| [1343_number_theory.java](1343_number_theory.java) \* | Java 1.8 | number_theory | O(G·log N) | AC | 0.125 s | 1752 KB | 11285098 |
| [1343_number_theory.py](1343_number_theory.py) \* | Python 3.12 x64 | number_theory | O(G·log N) | AC | 0.078 s | 524 KB | 11285097 |
| [1343_number_theory_optimized.rs](1343_number_theory_optimized.rs) \* | Rust 1.75 x64 | number_theory | O(G log N) | AC | 0.046 s | 56 KB | 11314929 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
