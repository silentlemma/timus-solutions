# 1133. Hallar un término de una sucesión de tipo Fibonacci a partir de otros dos

[Timus 1133](https://acm.timus.ru/problem.aspx?space=1&num=1133) · dificultad 225 · number_theory

Problema original del cuarto de final de la región central de Rusia, Rybinsk, 17–18 de octubre de 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una sucesión entera, infinita en ambos sentidos, cumple
`F(k + 2) = F(k + 1) + F(k)` para todo `k`. Dados `F(i)` y `F(j)` con
`i ≠ j`, halla `F(n)`. Todos los índices están en `[−1000, 1000]`, y cada
término desde el menor hasta el mayor de `i, j, n` está dentro de
`±2·10⁹`.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Cinco enteros: `i`, `F(i)`, `j`, `F(j)`, `n`.

## Salida

`F(n)`.

## Evaluación

Se compara un token entero. La fuente Python nueva real coincidió con
una recurrencia entera independiente hacia delante y atrás en 2500 consultas
válidas generadas y 100 nulas, con índices invertidos, negativos, exteriores
y el rango completo de 2000. Ambos programas nuevos pasaron por separado
los 13 datos del repositorio en Docker y tienen Accepted de sus bytes exactos.
Las 2600 comprobaciones diferenciales ejecutaron Python, no 2600 veces Java.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 5 -1 4 5
```

Salida:

```
12
```

## Solución

Ordena los términos conocidos por índice, `i < j`, y toma `D=j−i`.
Sean `H(0)=0,H(1)=1` los Fibonacci ordinarios. Sustituir la recurrencia da
`F(j)=H(D−1)·F(i)+H(D)·F(i+1)`. Como `D≥1`, `H(D)>0`: la división entera
exacta determina un único siguiente término. Se avanza sumando o se
retrocede con `F(k−1)=F(k+1)−F(k)` hasta el índice pedido. Esto prueba
la reconstrucción y unicidad cuando la secuencia existe, como se garantiza.

Los nuevos archivos `math` de Python, Go y Java usan enteros de precisión
arbitraria directamente. No necesitan elegir un primo, invertir residuos
ni demostrar que el denominador es invertible; son la base didáctica
preferida en esos tres lenguajes. Con `W=max(i,j,n)−min(i,j,n)` hacen
`O(W)` operaciones con enteros de `O(W)` bits. Una cota conservadora es
`O(W²)` de tiempo en bits y `O(W)` bits auxiliares vivos, con el límite
fijo de los valores de entrada. No son operaciones de coste constante.

Las fuentes conservadas `number_theory` calculan lo mismo módulo el primo
`P=4294967291`, mayor que los `4·10⁹+1` resultados posibles. Un residuo
mayor que `P/2` representa un valor negativo. Se comprobó por recurrencia
exacta que ningún denominador Fibonacci de índices 1 a 2000 es cero módulo
`P`, por lo que vale invertir mediante Fermat. Los productos caben en
64 bits sin signo. Así se obtiene tiempo `O(W)` con enteros de tamaño fijo
y almacenamiento numérico constante, sin bibliotecas externas en C++/Rust.

Se leen cinco tokens, independientemente de los saltos de línea. Los
índices pueden estar invertidos, ser negativos, consecutivos o quedar fuera
del intervalo dado. La secuencia nula permite incluso los índices más
lejanos. Ambas formas se contrastaron con recurrencias independientes,
incluidos rangos nulos largos y consultas fuera del intervalo.

## Soluciones optimizadas

El Go modular inalterado es otro algoritmo, optimizado frente a la base
Go preferida con enteros grandes: 1064 KB frente a 1544 KB, 31,1% menos
memoria. 0,015 s frente a 0,031 s es un solo tick, sin afirmar una mejora
temporal fiable. Las fuentes modulares Java/Python anteriores quedan como
alternativas matemáticas aceptadas, sin calificarlas de optimizadas.

Las nuevas fuentes Java/Python `math_optimized` conservan la aritmética
exacta directa y añaden una salida anticipada demostrable. Si ambos términos
conocidos son cero, la identidad de reconstrucción y `H(D)>0` fuerzan que
el término adyacente sea cero. Sumar hacia delante y restar hacia atrás
fuerza toda la secuencia a cero. Se devuelve sin generar coeficientes
Fibonacci grandes. Para otros datos no cambia el algoritmo: cota conservadora
`O(W²)` de tiempo en bits y `O(W)` bits vivos; trabajo aritmético constante
en el caso nulo. Es un caso especial de la recurrencia, no una tabla de respuestas.

Se compara con las bases preferidas `math`, no con los archivos modulares.
Java Accepted usa 536 KB frente a 828 KB: 35,3% menos; 0,093 s frente a
0,109 s es un tick y no prueba aceleración fiable. Python usa explícitamente
PyPy 3.10: 256 KB frente a 436 KB de CPython, 41,3% menos, pero 0,140 s
frente a 0,078 s, 79,5% más tiempo registrado. La comparación en la familia
Python acordada incluye el cambio de intérprete, sin aislar su efecto del
atajo. Ambas se admiten por memoria medida por el juez; las bases didácticas se conservan.

## Notas por lenguaje

Python usa enteros incorporados, Go `math/big` y Java `BigInteger`.
C++ y Rust conservan las implementaciones modulares Accepted con enteros
estándar sin signo. La alternativa modular Java usa `Long.remainderUnsigned`
para los productos de 64 bits que desbordan con signo. Su lector de tokens
representa exactamente todos los valores de entrada.

La instantánea filtrada guardada del 2 de noviembre de 2026 usa el perfil
acordado: C++ en el 15% superior o los primeros diez puestos de ambas métricas;
otras familias, primero en ambas. Las versiones admitidas por debajo del
objetivo llevan asterisco. Las muestras vacías Go/Rust ofrecen cobertura
formal, sin demostrar superioridad competitiva.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1133_number_theory.cpp](1133_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(W) | AC | 0.015 s | 128 KB | 11279389 |
| [1133_math.go](1133_math.go) | Go 1.14 x64 | math | O(W²) bit time | AC | 0.031 s | 1544 KB | 11308040 |
| [1133_math.java](1133_math.java) | Java 1.8 | math | O(W²) bit time | AC | 0.109 s | 828 KB | 11308043 |
| [1133_math.py](1133_math.py) | Python 3.12 x64 | math | O(W²) bit time | AC | 0.078 s | 436 KB | 11308038 |
| [1133_number_theory.rs](1133_number_theory.rs) | Rust 1.75 x64 | number_theory | O(W) | AC | 0.015 s | 220 KB | 11279395 |
| [1133_number_theory.java](1133_number_theory.java) | Java 1.8 | number_theory | O(W) | AC | 0.156 s | 1688 KB | 11279393 |
| [1133_number_theory.py](1133_number_theory.py) | Python 3.12 x64 | number_theory | O(W) | AC | 0.078 s | 480 KB | 11297961 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1133_number_theory.go](1133_number_theory.go) | Go 1.14 x64 | number_theory | O(W) | AC | 0.015 s | 1064 KB | 11279391 |
| [1133_math_optimized.java](1133_math_optimized.java) | Java 1.8 | math | O(W²) bit time | AC | 0.093 s | 536 KB | 11308413 |
| [1133_math_optimized.py](1133_math_optimized.py) \* | PyPy 3.10 x64 | math | O(W²) bit time | AC | 0.140 s | 256 KB | 11308412 |

\* Aceptada; aún no cumple el objetivo de clasificación. Puede optimizarse más.
