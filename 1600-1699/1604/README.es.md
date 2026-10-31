# 1604. En el País de los Tontos

[Timus 1604](https://acm.timus.ru/problem.aspx?space=1&num=1604) · dificultad 139 · greedy

Problema original de Alexander Ipatov (idea de Alexander Toropov), del IX Campeonato Abierto Individual de la Universidad Estatal de los Urales, 1 de marzo de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay k tipos de señales de límite de velocidad, nᵢ señales del tipo i y
como mucho 10000 señales en total. Hay que colocarlas todas a lo largo
de una carretera para que los conductores cambien de velocidad lo más a
menudo posible: hay un cambio en la primera señal y en cada señal
distinta de la anterior. Vale cualquier orden óptimo.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

k y luego n₁, …, nₖ, donde 1 ≤ k ≤ 10000, cada nᵢ es positivo
y su suma no supera 10000.

## Salida

Los tipos de las señales en el orden de la carretera.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
2 2
```

Salida:

```
1 2 1 2
```

## Solución

Cambiar de velocidad lo más a menudo posible significa tener los menos
vecinos iguales posibles. Sea m la mayor cantidad y n el total. Las
otras n − m señales parten las m señales del tipo más común en como
mucho n − m + 1 grupos, así que hay al menos max(0, 2m − n − 1) vecinos
iguales.

Un orden voraz alcanza esa cota: se coloca siempre el tipo con más
señales restantes, salvo que haya sido la señal anterior, y entonces el
tipo con la segunda mayor cantidad. Un montículo da ambos en
`O(log k)`, así que todo el orden cuesta `O(n log k)`.

Las pruebas usan un verificador que cuenta los vecinos iguales y los
compara con la cota. La cota se contrastó con una búsqueda exhaustiva
sobre todos los órdenes de conjuntos pequeños de señales.

Detalles a tener en cuenta:

- los vecinos iguales son inevitables exactamente cuando 2m > n + 1,
  y el voraz los deja juntos al final (prueba 05); con 2m = n + 1
  todavía se pueden evitar (pruebas 02 y 04);
- tomar siempre el tipo más común sin mirar la señal anterior lo repite;
  tomar los tipos por turnos sin mirar las cantidades puede agotar los
  otros tipos demasiado pronto (prueba 07).

## Soluciones optimizadas

La solución optimizada en C++ empaqueta un tipo y su cuenta en un solo
`int`, cuenta·2¹⁴ + tipo: los dos valen como mucho 10000, menos que
2¹⁴ = 16384, así que los campos no se solapan, y comparar los números
empaquetados compara primero las cuentas y luego los tipos, igual que
con los pares. El montículo es un arreglo fijo de 10000 de esos números
manejado con `std::push_heap` y `std::pop_heap` en lugar de una
`priority_queue` de pares, y los tipos se imprimen con `printf` según
salen en lugar de juntarse en una cadena: {1604_greedy_optimized.cpp}.

La solución optimizada en Go escribe su propio montículo sobre un slice
de señales con espacio reservado para k entradas, en lugar de
`container/heap`, que convierte cada señal que entra y sale en un valor
`interface{}` y le reserva memoria. Los números se leen byte a byte del
`bufio.Reader` en lugar de con `fmt.Fscan`: {1604_greedy_optimized.go}.

La solución optimizada en Java pasa a la `PriorityQueue` una clase
`Comparator` normal en lugar de una lambda, cuyo primer uso carga
maquinaria adicional del entorno de ejecución. Cuando se coloca un tipo,
su arreglo ya ha salido del montículo, así que la solución baja la
cuenta en ese mismo arreglo y lo devuelve en lugar de crear uno nuevo
por cada señal. Los tipos salen por un `BufferedWriter` en lugar de un
`StringBuilder`: {1604_greedy_optimized.java}.

La solución optimizada en Python empaqueta la entrada del montículo
(−cuenta, tipo) en un solo entero, −cuenta·(k + 1) + tipo, en lugar de
una tupla: el tipo va de 1 a k, por debajo de la base k + 1, así que
los enteros se comparan exactamente igual que las tuplas, y `divmod`
recupera los dos campos. Lee la entrada como bytes, libera la lista de
tokens antes del bucle principal y escribe los tipos en tandas de 256 en
lugar de guardar todo el orden en memoria: {1604_greedy_optimized.py}.

La solución optimizada en Rust escribe cada tipo con un `BufWriter` en
cuanto lo coloca, en lugar de juntar hasta 10000 cadenas en un `Vec` y
unirlas en otra cadena más: {1604_greedy_optimized.rs}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1604_greedy_optimized.cpp`: reducción de tiempo +0.00%; reducción de
  memoria +49.32%; base: `1604_greedy.cpp`.

- `1604_greedy_optimized.go`: reducción de tiempo +51.61%; reducción de
  memoria +49.27%; base: `1604_greedy.go`.

- `1604_greedy_optimized.java`: reducción de tiempo +19.87%; reducción
  de memoria +64.35%; base: `1604_greedy.java`.

- `1604_greedy_optimized.py`: reducción de tiempo +0.00%; reducción de
  memoria +42.12%; base: `1604_greedy.py`.

- `1604_greedy_optimized.rs`: reducción de tiempo -313.33%; reducción de
  memoria +56.70%; base: `1604_greedy.rs`.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1604_greedy.cpp](1604_greedy.cpp) | G++ 13.2 x64 | greedy | O(n log k) | AC | 0.015 s | 292 KB | 11288133 |
| [1604_greedy.go](1604_greedy.go) | Go 1.14 x64 | greedy | O(n log k) | AC | 0.031 s | 2184 KB | 11288136 |
| [1604_greedy.java](1604_greedy.java) | Java 1.8 | greedy | O(n log k) | AC | 0.156 s | 3456 KB | 11288142 |
| [1604_greedy.py](1604_greedy.py) | Python 3.12 x64 | greedy | O(n log k) | AC | 0.093 s | 1776 KB | 11288140 |
| [1604_greedy.rs](1604_greedy.rs) | Rust 1.75 x64 | greedy | O(n log k) | AC | 0.015 s | 1044 KB | 11288144 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1604_greedy_optimized.cpp](1604_greedy_optimized.cpp) | G++ 13.2 x64 | greedy | O(n log k) | AC | 0.015 s | 148 KB | 11304457 |
| [1604_greedy_optimized.go](1604_greedy_optimized.go) | Go 1.14 x64 | greedy | O(n log k) | AC | 0.015 s | 1108 KB | 11304458 |
| [1604_greedy_optimized.java](1604_greedy_optimized.java) \* | Java 1.8 | greedy | O(n log k) | AC | 0.125 s | 1232 KB | 11304459 |
| [1604_greedy_optimized.py](1604_greedy_optimized.py) \* | Python 3.12 x64 | greedy | O(n log k) | AC | 0.093 s | 1028 KB | 11304460 |
| [1604_greedy_optimized.rs](1604_greedy_optimized.rs) | Rust 1.75 x64 | greedy | O(n log k) | AC | 0.062 s | 452 KB | 11304461 |

\* Aceptada; aún no cumple el objetivo de clasificación. Puede optimizarse más.
