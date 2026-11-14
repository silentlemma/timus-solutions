# 1098. El último carácter que queda contando de 1999 en 1999

[Timus 1098](https://acm.timus.ru/problem.aspx?space=1&num=1098) · dificultad 557 · math

Problema original de Stanislav Vasiliev, de la ronda de prueba del III Campeonato Universitario por Equipos de Programación de los Urales, 1999.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

La pregunta es toda la entrada sin los saltos de línea (de uno a 30000
caracteres; los espacios y la puntuación cuentan). Empezando por el
primer carácter, se cuentan `N − 1` caracteres y se borra el `N`-ésimo,
volviendo al principio al llegar al final; luego se cuenta otra vez desde
el carácter siguiente al borrado, hasta que queda uno, con `N = 1999`.
Imprime `Yes` si es `?`, `No` si es un espacio y `No comments` en otro
caso.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

La pregunta, posiblemente en varias líneas.

## Salida

`Yes`, `No` o `No comments`.

## Evaluación

La salida se compara línea a línea; dentro de una línea, token a token.

## Ejemplos

### Ejemplo 1

Entrada:

```
Does the jury of this programming contest use the
algorithm described in this problem to answer my questions?
```

Salida:

```
Yes
```

### Ejemplo 2

Entrada:

```
At least, will anybody READ my question?
```

Salida:

```
No
```

### Ejemplo 3

Entrada:

```
This is
UNFAIR!
```

Salida:

```
No comments
```

## Solución

Es el problema de Josefo. Sea `J(m)` la posición, contada desde donde
empieza la cuenta, del último que queda entre `m` caracteres. Tras el
primer borrado quedan `m − 1` caracteres y la cuenta empieza `N` lugares
más adelante, así que `J(m) = (J(m − 1) + N) mod m` con `J(1) = 0`. Una
pasada hasta la longitud de la pregunta da la posición, y solo importa
el carácter que está ahí. `O(L)`.

Borrar caracteres de uno en uno de una cadena costaría `O(L²)` con
`L = 30000`: bastante rápido en un lenguaje compilado, pero la
recurrencia lo evita del todo.

Detalles a tener en cuenta:

- cuenta todo carácter salvo los saltos de línea, incluidos los espacios
  al final de las líneas y entre palabras, así que la entrada se lee como
  bytes en bruto y solo se quitan `\n` y `\r`;
- la pregunta puede tener un solo carácter, y entonces ese carácter
  decide la respuesta.

Las respuestas se comprobaron con una simulación directa que borra cada
carácter número 1999 de una lista.

## Notas por lenguaje

- Rust pliega la recurrencia sobre `2..=L`.
- Java y C++ leen la entrada byte a byte, lo que conserva cada espacio.

## Soluciones optimizadas

La versión Python elimina los retornos de carro y los saltos de línea con dos operaciones
sobre bytes. La secuencia filtrada aporta tanto la longitud para la recurrencia de Josephus
como el byte final. El envío 11316943 usó 348 KB frente a 500 KB de la versión base y tardó
0,078 s frente a 0,078 s.

Go guarda las posiciones de los signos de interrogación y de los espacios en dos conjuntos de bits y omite los saltos de línea. La recurrencia de Josefo obtiene la posición final y sus dos bits determinan la respuesta. El envío 11317592 tardó 0,015 s y usó 900 KB, frente a 0,015 s y 1304 KB de la versión sencilla.

**Envíos de las versiones sencillas en Timus**

G++ 13.2 x64 №11321759 · Go 1.14 x64 №11322213 · Java 1.8 №11321761 · Python 3.12 x64 №11322214 · Rust 1.75 x64 №11322215.

Rust guarda interrogaciones y espacios en dos máscaras de bits y continúa la recurrencia de Josefo desde un punto precalculado. Rust 1.75 x64, envío 11323266. Tiempo 0,015 → 0,015 s, memoria 224 → 56 KB.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1098_math.cpp](1098_math.cpp) | G++ 13.2 x64 | math | O(L) | AC | 0.015 s | 184 KB | 11321759 |
| [1098_math.go](1098_math.go) | Go 1.14 x64 | math | O(L) | AC | 0.015 s | 1304 KB | 11322213 |
| [1098_math.java](1098_math.java) | Java 1.8 | math | O(L) | AC | 0.093 s | 488 KB | 11321761 |
| [1098_math.py](1098_math.py) | Python 3.12 x64 | math | O(L) | AC | 0.078 s | 500 KB | 11322214 |
| [1098_math.rs](1098_math.rs) | Rust 1.75 x64 | math | O(L) | AC | 0.015 s | 224 KB | 11322215 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1098_math_optimized.py](1098_math_optimized.py) \* | Python 3.12 x64 | math | O(L) | AC | 0.078 s | 348 KB | 11316943 |
| [1098_math_optimized.go](1098_math_optimized.go) \* | Go 1.14 x64 | math | O(L) | AC | 0.015 s | 900 KB | 11317592 |
| [1098_math_optimized.rs](1098_math_optimized.rs) \* | Rust 1.75 x64 | math | O(N) | AC | 0.015 s | 56 KB | 11323266 |

\* Las soluciones marcadas aún pueden mejorar en la clasificación objetivo.
