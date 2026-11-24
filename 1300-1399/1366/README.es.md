# 1366. Regalos

[Timus 1366](https://acm.timus.ru/problem.aspx?space=1&num=1366) · dificultad 523 · math

Problema original con idea de Stanislav Vasiliev, preparado por Pavel Egorov, del Noveno Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 19–24 de abril de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada uno de n ≤ 1000 niños trae un regalo, y los regalos se intercambian
de modo que cada niño reciba exactamente un regalo y nadie se quede con
el suyo. Hay que contar las formas de hacerlo.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

El número n.

## Salida

La cantidad de intercambios.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
```

Salida:

```
2
```

## Solución

Un intercambio es una permutación sin puntos fijos, un desarreglo. Por
inclusión–exclusión su número es d(k) = Σ (−1)ⁱ · k! / i! con
i = 0 … k, y multiplicar d(k − 1) por k da todos los términos de d(k)
salvo el último, (−1)ᵏ. Así que d(1) = 0 y d(k) = k · d(k − 1) + (−1)ᵏ:
se empieza en 0 y se aplica para k = 2 … n.

La respuesta para n = 1000 tiene 2 568 cifras, así que hace falta
aritmética larga: cada paso multiplica por un número pequeño y suma o
resta 1. `O(n² log n)` operaciones con cifras.

Detalles a tener en cuenta:

- un solo niño no puede intercambiar: la respuesta es 0 (prueba 02);
- d(21) es el primer valor que ya no cabe en 64 bits (prueba 06);
- tras la multiplicación el número vale al menos 3 para k ≥ 3, así que
  restar 1 nunca baja de cero.

La recurrencia se comparó con contar todas las permutaciones para n ≤ 8
y con la suma de inclusión–exclusión para n = 50.

La versión didáctica en C++ guarda los dígitos decimales de menor a mayor peso. En el paso k, el acarreo empieza en +1 si k es par y en −1 si es impar. Cada dígito se multiplica por k, se suma el acarreo, se conserva la unidad y el cociente pasa a ser el siguiente acarreo. Así se calcula k·D(k−1)+(−1)^k en una pasada. Para k impar, el índice anterior es par y D(k−1) es impar, por lo que su último dígito es positivo y la primera resta es segura. Se imprimen los dígitos en orden inverso. Tiempo O(n² log n), espacio O(n log n).

## Soluciones optimizadas

Go, Java y Rust combinan dos pasos de los desarreglos: de D(k)=kD(k−1)+(−1)^k, para k par resulta D(k)=k(k−1)D(k−2)−(k−1). Empezar con D(2)=1 y tratar n=1 aparte; si n es impar, terminar con nD(n−1)−1 si n>1. Una pasada por bloques en base 10⁹ sirve para dos pasos. Por la recurrencia, D de índice par es impar, así que el bloque bajo es positivo. La resta inicial es menor que el factor f y el primer producto vale al menos f. Los acarreos posteriores están en [0,f−1], con valores intermedios menores que f·10⁹. Como f≤999 000, bastan 64 bits con signo y el acarreo final cabe en un bloque. Con D(n)<n!≤10³⁰⁰⁰ bastan 334 bloques y la salida completa de Go y Java cabe en 3001 bytes. Los arreglos fijos sustituyen los temporales grandes de Go y Java. Go usa los descriptores estándar y llena el búfer decimal desde el final. Java elimina Scanner. Rust usa un punto de entrada de C y lee y escribe carácter por carácter con su biblioteca, con nueve bytes por bloque. Tiempo O(n² log n) operaciones de palabra y O(n log n) dígitos. Se conservan bases; C++/Python reutilizan las admitidas para cobertura rápida.

Las implementaciones base aceptadas [1366_math.cpp](1366_math.cpp), [1366_math.py](1366_math.py) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Notas por lenguaje

Los originales de Python, Go y Java usan enteros grandes de sus lenguajes. C++ y Rust originales usan bloques en base 10⁹. Go, Java y Rust optimizados usan arreglos fijos de bloques y combinan dos pasos de la recurrencia.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1366_math.cpp](1366_math.cpp) | G++ 13.2 x64 | math | O(n² log n) | AC | 0.031 s | 196 KB | 11285547 |
| [1366_math.go](1366_math.go) | Go 1.14 x64 | math | O(n² log n) | AC | 0.031 s | 1268 KB | 11285549 |
| [1366_math.java](1366_math.java) | Java 1.8 | math | O(n² log n) | AC | 0.125 s | 3320 KB | 11285574 |
| [1366_math.py](1366_math.py) \* | Python 3.12 x64 | math | O(n² log n) | AC | 0.093 s | 412 KB | 11285552 |
| [1366_math.rs](1366_math.rs) | Rust 1.75 x64 | math | O(n² log n) | AC | 0.046 s | 252 KB | 11285579 |
| [1366_combinatorics.cpp](1366_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(n² log n) | AC | 0.015 s | 192 KB | 11315859 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1366_math_optimized.java](1366_math_optimized.java) | Java 1.8 | math | O(n² log n) | AC | 0.109 s | 380 KB | 11315509 |
| [1366_math_optimized.go](1366_math_optimized.go) | Go 1.14 x64 | math | O(n² log n) | AC | 0.015 s | 344 KB | 11328273 |
| [1366_math_optimized.rs](1366_math_optimized.rs) | Rust 1.75 x64 | math | O(n² log n) | AC | 0.031 s | 52 KB | 11315876 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
