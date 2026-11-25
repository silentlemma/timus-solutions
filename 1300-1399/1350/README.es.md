# 1350. Comedor

[Timus 1350](https://acm.timus.ru/problem.aspx?space=1&num=1350) · dificultad 384 · implementation

Problema original de Pavel Egorov, del Campeonato Escolar, marzo de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un menú tiene N ≤ 100 productos, y la comida del día se hace con M
distintos de ellos, sin saber cuáles. La comen K + 1 ≤ 101 estudiantes;
de cada uno se conocen los productos que le son peligrosos. El primer
estudiante comió y quedó bien. Para cada uno de los otros K hay que
imprimir `YES` si la comida es sin duda inofensiva para esa persona,
`NO` si sin duda contiene algo peligroso para ella, y `MAYBE` si puede
ser cualquiera de las dos cosas.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y los N nombres de producto, luego K, luego K + 1 bloques: una
cantidad y otros tantos productos peligrosos, el primer bloque para el
primer estudiante. La entrada acaba con M.

## Salida

K líneas con `YES`, `NO` o `MAYBE`.

## Evaluación

Las pruebas del repositorio comparan exactamente los tokens de salida; los espacios entre tokens no son significativos.

## Ejemplos

### Ejemplo 1

Entrada:

```
7
Rafinad
Kefir
Pastila
Smetana
Chokolade
Kljukva
Imbir
3
3
Rafinad
Kefir
Imbir
1
Rafinad
3
Kefir
Kljukva
Smetana
2
Imbir
Smetana
3
```

Salida:

```
YES
NO
MAYBE
```

## Solución

Como el primer estudiante quedó bien, ninguno de sus productos
peligrosos está en la comida: la comida son M productos del resto, el
conjunto seguro S. Para otro estudiante con productos peligrosos D:

- si M = 0, o ningún producto de S está en D, toda comida posible es
  inofensiva: `YES`;
- si fuera de D hay menos de M productos de S, toda comida de M
  productos tiene que tomar alguno de D: `NO`;
- si no, una comida puede evitar D y otra incluirlo: `MAYBE`.

`O(N · K)` en promedio; C++: `O(N · K · log N)`.

Detalles a tener en cuenta:

- con M = 0 no se come nada y todos quedan bien (prueba 02);
- los nombres distinguen mayúsculas: `Milk` y `milk` son dos productos
  (prueba 04);
- los productos peligrosos fuera de S no importan, porque no pueden
  estar en la comida.

Las respuestas se compararon con probar todas las comidas posibles en
400 comedores aleatorios de hasta 6 productos.

## Soluciones optimizadas

`1350_bitmask_implementation.java`. La variante de bitsets guarda peligros del menú en palabras de 64 bits por alumno. Una tabla de direccionamiento abierto verifica colisiones comparando todos los caracteres; reutiliza un token de 40 caracteres y solo guarda nombres del menú. Ignora nombres externos y el OR elimina duplicados. Long.bitCount cuenta peligros fuera del conjunto del alumno cero y aplica las mismas condiciones YES/NO/MAYBE. P productos distintos, K alumnos restantes, W=ceil(P/64), I bytes: tiempo esperado O(I+KW+P), estado O(P+KW+K), nombres acotados. Colisiones pueden empeorar tiempo, nunca respuestas; conserva ambas implementaciones anteriores.

Accepted de fuente exacto Java 1.8 #11326945: 0.109 s / 448 KB. Comparación guardada de Java actual, 2026-11-20: tiempo 6/29, memoria 1/29. Al usar menos de 1024 KB, la admisión estricta usa solo tiempo.

- `1350_bitmask_implementation.java`: 0.109 s / 448 KB; base didáctica conservada `1350_implementation.java`: 0.14 s / 6524 KB; cambio de tiempo -22.1%; cambio de memoria -93.1%.

Las versiones compactas asignan un índice a cada alimento del menú. C++ y Rust lo buscan en un vector ordenado, y Go en una tabla hash. Rust reutiliza el mismo búfer para cada palabra de la entrada. Un vector guarda el último estudiante que mencionó cada alimento para contar una sola vez los nombres repetidos. Tras excluir los alimentos peligrosos para el primer estudiante, se conserva solo el número de alimentos peligrosos elegibles para cada otro estudiante. Esos recuentos bastan cuando se lee el tamaño de la comida.

Las bases Accepted conservadas [1350_implementation.go](1350_implementation.go) y [1350_implementation.py](1350_implementation.py) pasan el criterio estricto de diez primeros o 15% superior en la comparación guardada: tiempo/memoria 2/2 y 3/15, respectivamente. La base Java ocupa 16/29 en tiempo y 27/29 en memoria y no cubre el conjunto rápido estricto; sí lo cubre la variante Java de bitsets anterior. Se reutilizan las bases sin copias idénticas; el asterisco corresponde a la meta propia del lenguaje.

`1350_implementation_optimized.java`. Java conserva el algoritmo y las estructuras descritas para la versión sencilla. Un búfer fijo de bytes y FastInput sustituyen Scanner y su maquinaria de expresiones regulares y configuración regional. Los enteros se analizan directamente; las cadenas siguen decodificándose como UTF-8 cuando se solicitan y los decimales mantienen conversión numérica explícita. La anticipación guarda un token solo cuando hace falta. El algoritmo de salida no cambia. Se elimina el coste del análisis general; la tabla describe el trabajo algorítmico, con lectura lineal en bytes y un búfer acotado.

Frente a `1350_implementation.java`: tiempo 0.140 s → 0.125 s; memoria 6524 KB → 3 484 KB.

## Notas por lenguaje

Estas notas describen las implementaciones sencillas.

- Las cinco soluciones cuentan los productos de S dentro y fuera de D.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1350_implementation.cpp](1350_implementation.cpp) | G++ 13.2 x64 | implementation | O(N·K·log N) | AC | 0.062 s | 1344 KB | 11285155 |
| [1350_implementation.go](1350_implementation.go) | Go 1.14 x64 | implementation | O(N·K) | AC | 0.031 s | 2156 KB | 11285156 |
| [1350_implementation.java](1350_implementation.java) \* | Java 1.8 | implementation | O(N·K) | AC | 0.140 s | 6524 KB | 11285160 |
| [1350_implementation.py](1350_implementation.py) \* | Python 3.12 x64 | implementation | O(N·K) | AC | 0.078 s | 2240 KB | 11285157 |
| [1350_implementation.rs](1350_implementation.rs) | Rust 1.75 x64 | implementation | O(N·K) | AC | 0.015 s | 1560 KB | 11285161 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1350_implementation_optimized.cpp](1350_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(N·K·log N) | AC | 0.015 s | 424 KB | 11310451 |
| [1350_implementation_optimized.go](1350_implementation_optimized.go) | Go 1.14 x64 | implementation | O(N·K) expected | AC | 0.031 s | 944 KB | 11310453 |
| [1350_implementation_optimized.rs](1350_implementation_optimized.rs) \* | Rust 1.75 x64 | implementation | O(N·K·log N) | AC | 0.015 s | 192 KB | 11310869 |
| [1350_bitmask_implementation.java](1350_bitmask_implementation.java) | Java 1.8 | bitmask, implementation | Expected O(I+KW+P) time; O(P+KW+K) space | AC | 0.109 s | 448 KB | 11326945 |
| [1350_implementation_optimized.java](1350_implementation_optimized.java) \* | Java 1.8 | implementation | O(N·K) | AC | 0.125 s | 3484 KB | 11324808 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
