# 1049. La última cifra del número de divisores de un producto

[Timus 1049](https://acm.timus.ru/problem.aspx?space=1&num=1049) · dificultad 249 · number_theory

Problema original de Stanislav Vasiliev, del concurso universitario de programación de la Universidad Estatal de los Urales, 25 de marzo de 2000.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se dan diez enteros `a1 … a10`, cada uno de 1 a 10000. Halla la última
cifra del número de divisores positivos del producto `a1 · … · a10`.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

Diez enteros, uno por línea.

## Salida

Una cifra: la última cifra del número de divisores.

## Evaluación

Se comparan los tokens exactos; los espacios no afectan.

- `1049_number_theory_optimized.go` (Go 1.14 x64): 14 pruebas del repositorio; 14 comparaciones adicionales de fuente exacta.

`1049_number_theory_optimized.java` (Java 1.8): 59 pruebas de proceso, incluidos los 14 casos del repositorio; 11007 comprobaciones independientes adicionales del main.

- `1049_number_theory_optimized.py` (PyPy 3.10 x64): 14 pruebas del repositorio.

## Ejemplos

### Ejemplo 1

Entrada:

```
1
2
6
1
3
1
1
1
1
1
```

Salida:

```
9
```

### Ejemplo 2

Entrada:

```
1
1
1
1
1
1
1
1
1
1
```

Salida:

```
1
```

## Solución

Si `P = p1^e1 · p2^e2 · … · pk^ek`, un divisor de `P` elige cada
exponente de forma independiente entre `0` y `ei`, así que `P` tiene
`(e1 + 1)(e2 + 1)…(ek + 1)` divisores.

El producto puede tener 40 cifras, pero no hace falta: se factoriza cada
número por división de prueba hasta su raíz cuadrada (como mucho 100
pasos), se suman los exponentes de los primos iguales y se multiplican los
`(e + 1)` módulo 10. `O(10 · √10000)`.

Detalles a tener en cuenta:

- los exponentes deben sumarse sobre los diez números antes del `+ 1`:
  `2 · 2` tiene 3 divisores, no `2 · 2`;
- un factor primo mayor que la raíz cuadrada queda tras la división de
  prueba y también cuenta;
- la última cifra puede ser 0 (48 = `2^4 · 3` tiene 10 divisores).

## Soluciones optimizadas

`1049_number_theory_optimized.java`. Guarda los diez valores como residuos. Para cada divisor de prueba elimina sus potencias de TODOS los residuos antes de multiplicar el exponente final más uno módulo diez. Actualiza el residuo máximo en ese recorrido; si el siguiente divisor al cuadrado lo supera, los residuos mayores que uno son primos y se agrupan los iguales. Los factores primos menores ya eliminados hacen inocuos los divisores compuestos. Si el producto módulo diez llega a cero tras completar un divisor, los factores independientes posteriores no lo cambian: puede terminar. No es seguro hacerlo con un exponente parcial de una sola entrada. No asigna una tabla de 10001 exponentes. Para C=10 y máximo inicial V≤10000: tiempo O(C sqrt(V)+C²), estado O(C), menos recorridos al reducir residuos. Analiza directamente la entrada breve, escribe y vacía dos bytes normalmente. El fuente exacto pasó 59 pruebas de proceso y 11007 comprobaciones independientes del main, incluidos los 10000 valores aislados y casos de primos repetidos. Conserva factorización didáctica y otros lenguajes.

Accepted exacto Java 1.8 #11328052: 0.062 s / 316 KB. Comparación guardada del grupo de compiladores del 2026-11-20: tiempo 1/77, memoria 1/77. Bajo 1024 KB la admisión estricta solo usa tiempo: diez primeros o 15% superior, con empates compartidos y corte porcentual redondeado hacia arriba. Ambas métricas son primeras; cumple también la meta propia del lenguaje, sin asterisco. El registro optimizado documentado antes #11308799 era 0.109 s / 368 KB; es un par histórico distinto, no la medición actual de este fuente. Las bases didácticas permanecen intactas.

- `1049_number_theory_optimized.java`: 0.062 s / 316 KB; base didáctica conservada `1049_number_theory.java`: 0.14 s / 3880 KB.

`1049_number_theory_optimized.py`. Conserva exponentes exactos y product(e+1) módulo diez. Extrae potencia de dos por bit menor: (value & −value).bit_length()−1, y desplaza. Elimina tres y prueba rueda 6k±1; residuo mayor que uno es primo. Diccionario/variables locales. Escribe dos bytes por archivo sin búfer, sin imports ni salida temprana. C=10,V≤10000: O(C sqrt(V)) pruebas, O(C log V) registros. CPython nuevo usa 572 KB frente a PyPy histórico 296 KB; no mezcla runtimes/pares, conserva factorización didáctica.

Fuente exacto: Python 3.12 x64 Accepted #11327877: 0.062 s / 572 KB. Puestos guardados del grupo de compilador del 2026-11-20, tiempo y luego memoria: 1/70; 34/70. Admisión estricta usa solo tiempo bajo 1024 KB: diez primeros o 15% superior, empates comparten puesto y corte se redondea arriba. Conserva asterisco por la meta propia de primer puesto en ambas. La variante anterior conservada tiene su par propio #11309728 (PyPy 3.10 x64): 0.109 s / 296 KB; no mezclar métricas ni runtimes. Bases didácticas intactas.

- `1049_number_theory_optimized.py`: 0.062 s / 572 KB; base didáctica conservada `1049_number_theory.py`: 0.078 s / 456 KB.

La fórmula no cambia: factorizar los diez valores, sumar exponentes y multiplicar exponente+1 módulo diez. Se retira toda la potencia de dos y luego solo se prueban divisores impares; el residuo mayor que uno es primo. Go usa exponentes uint8 y una lista de primos tocados; Java conserva diez residuos y usa el recorrido compartido descrito arriba. El máximo 10*floor(log2(10000))=130 cabe en uint8 de Go; Java suma exponentes en int. Seis primos distintos ya multiplican 30030: cada entrada aporta como máximo cinco. Los arreglos de Go requieren O(V) inicialización/espacio y sus diez factorizaciones O(C sqrt(V)). Python conserva un pequeño diccionario y operaciones de bits; el intercambio de tiempo por memoria se declara aparte.

- `1049_number_theory_optimized.go`: 0.015 s / 308 KB; base `1049_number_theory.go`: 0.031 s / 1108 KB; cambio respecto a la base: tiempo -51.6%, memoria -72.2%.

`1049_number_theory_optimized.rs`. Factoriza los diez números al leerlos y acumula exponentes primos en un arreglo fijo de bytes. Cada exponente es como máximo 130 al ser los valores de hasta 10000, por lo que cabe en un byte. Multiplica exponente+1 módulo diez recorriendo el arreglo. La factorización cuesta O(10√M) y el recorrido final O(M), con M=10000; se usan M+1 bytes y estado constante. Rust usa el entorno de C para entrada y salida, evitando cadenas String completas decodificadas y el formato de Rust. La fuente sencilla aceptada se conserva sin cambios.

Frente a `1049_number_theory.rs`: tiempo 0.015 s → 0.015 s; memoria 416 KB → 52 KB.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1049_number_theory_optimized.rs`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1049_number_theory.cpp](1049_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(10 · √10000) | AC | 0.015 s | 184 KB | 11278665 |
| [1049_number_theory.go](1049_number_theory.go) | Go 1.14 x64 | number_theory | O(10 · √10000) | AC | 0.031 s | 1108 KB | 11278667 |
| [1049_number_theory.java](1049_number_theory.java) | Java 1.8 | number_theory | O(10 · √10000) | AC | 0.140 s | 3880 KB | 11278675 |
| [1049_number_theory.py](1049_number_theory.py) | Python 3.12 x64 | number_theory | O(10 · √10000) | AC | 0.078 s | 456 KB | 11278673 |
| [1049_number_theory.rs](1049_number_theory.rs) | Rust 1.75 x64 | number_theory | O(10 · √10000) | AC | 0.015 s | 416 KB | 11278679 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1049_number_theory_optimized.go](1049_number_theory_optimized.go) | Go 1.14 x64 | number_theory | O(C sqrt(V)+V) time; O(V) space | AC | 0.015 s | 308 KB | 11328262 |
| [1049_number_theory_optimized.java](1049_number_theory_optimized.java) | Java 1.8 | number_theory | O(C sqrt(V)+C^2) time; O(C) space | AC | 0.062 s | 316 KB | 11328052 |
| [1049_number_theory_optimized.py](1049_number_theory_optimized.py) \* | Python 3.12 x64 | number_theory | O(C sqrt(V)) time; O(C log V) prime records | AC | 0.062 s | 572 KB | 11327877 |
| [1049_number_theory_optimized.rs](1049_number_theory_optimized.rs) \* | Rust 1.75 x64 | number_theory | O(10√M+M), M=10000 | AC | 0.015 s | 52 KB | 11325082 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
