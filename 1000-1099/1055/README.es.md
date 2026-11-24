# 1055. El número de divisores primos de un coeficiente binomial

[Timus 1055](https://acm.timus.ru/problem.aspx?space=1&num=1055) · dificultad 424 · number_theory

Problema original de la Academia Estatal de Aviación de Rybinsk.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dados `1 ≤ M < N ≤ 50000`, halla cuántos primos distintos dividen al
coeficiente binomial `C(N, M) = N! / (M! · (N − M)!)`.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y `M`.

## Salida

El número de divisores primos distintos de `C(N, M)`.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 3
```

Salida:

```
2
```

### Ejemplo 2

Entrada:

```
10 5
```

Salida:

```
3
```

## Solución

`C(N, M)` tiene decenas de miles de cifras, así que nunca se calcula. Solo
los primos hasta `N` pueden dividirlo, y el exponente de un primo `p` en
`x!` lo da la fórmula de Legendre:

```text
e_p(x!) = ⌊x/p⌋ + ⌊x/p²⌋ + ⌊x/p³⌋ + …
```

así que `p` divide a `C(N, M)` exactamente cuando
`e_p(N!) − e_p(M!) − e_p((N − M)!) > 0`. Una criba de Eratóstenes da los
primos hasta `N`, y cada primo cuesta `O(log N)` divisiones:
`O(N log log N)` en total.

Detalles a tener en cuenta:

- los factoriales desbordan enseguida: se trabaja solo con exponentes;
- hay que comprobar todos los primos hasta `N`, también los mayores que
  `N / 2`;
- `M = N − 1` da `C = N`, cuyos divisores primos son los de `N`.

Una prueba equivalente es el teorema de Kummer: `p` divide a `C(N, M)`
exactamente cuando sumar `M` y `N − M` en base `p` produce un acarreo.
Las pruebas se comprobaron con él y, para `N ≤ 3000`, factorizando el
coeficiente exacto.

## Soluciones optimizadas

Go conserva la criba y la comparación de exponentes de Legendre. Trata el primo 2 aparte y guarda un bit por impar, marcando múltiplos desde p² con paso 2p. Para N≤50000, los 391 bloques ocupan 3128 bytes; un impar x corresponde al bit x/2. Un primo se cuenta una vez si su exponente en N! supera la suma de los de M! y (N−M)!. El tiempo sigue siendo O(N log log N); los manejadores estándar sustituyen fmt sin cambiar las matemáticas. Se conservan las bases y las otras cuatro también cubren el conjunto rápido.

Las implementaciones base aceptadas [1055_number_theory.cpp](1055_number_theory.cpp), [1055_number_theory.java](1055_number_theory.java), [1055_number_theory.py](1055_number_theory.py), [1055_number_theory.rs](1055_number_theory.rs) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

`1055_number_theory_optimized.java`. Java conserva el algoritmo y las estructuras descritas para la versión sencilla. Un búfer fijo de bytes y FastInput sustituyen Scanner y su maquinaria de expresiones regulares y configuración regional. Los enteros se analizan directamente; las cadenas siguen decodificándose como UTF-8 cuando se solicitan y los decimales mantienen conversión numérica explícita. La anticipación guarda un token solo cuando hace falta. El algoritmo de salida no cambia. Se elimina el coste del análisis general; la tabla describe el trabajo algorítmico, con lectura lineal en bytes y un búfer acotado.

Frente a `1055_number_theory.java`: tiempo 0.093 s → 0.109 s; memoria 1680 KB → 520 KB.

## Notas por lenguaje

Estas notas describen las implementaciones sencillas.

- Todos los lenguajes usan la misma criba; Python marca los múltiplos de
  un primo con una sola asignación de corte sobre un `bytearray`.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1055_number_theory.cpp](1055_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(N log log N) | AC | 0.015 s | 184 KB | 11278720 |
| [1055_number_theory.go](1055_number_theory.go) | Go 1.14 x64 | number_theory | O(N log log N) | AC | 0.015 s | 1112 KB | 11278721 |
| [1055_number_theory.java](1055_number_theory.java) | Java 1.8 | number_theory | O(N log log N) | AC | 0.093 s | 1680 KB | 11278729 |
| [1055_number_theory.py](1055_number_theory.py) \* | Python 3.12 x64 | number_theory | O(N log log N) | AC | 0.078 s | 580 KB | 11278723 |
| [1055_number_theory.rs](1055_number_theory.rs) \* | Rust 1.75 x64 | number_theory | O(N log log N) | AC | 0.031 s | 268 KB | 11278731 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1055_number_theory_optimized.go](1055_number_theory_optimized.go) | Go 1.14 x64 | number_theory | O(N log log N) | AC | 0.015 s | 352 KB | 11314956 |
| [1055_number_theory_optimized.java](1055_number_theory_optimized.java) | Java 1.8 | number_theory | O(N log log N) | AC | 0.109 s | 520 KB | 11324817 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
