# 1013. Contar números en base K sin dos ceros seguidos, módulo M

[Timus 1013](https://acm.timus.ru/problem.aspx?space=1&num=1013) · dificultad 198 · matrix

Problema original: la versión más difícil de los [problemas 1009](../1009/README.es.md) y [1012](../1012/README.es.md).

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cuenta, módulo `M`, los números de `N` dígitos en base `K` (el primer dígito
no es cero) cuyos dígitos no contienen dos ceros seguidos.
`2 ≤ N, K, M ≤ 10^18`.

Límite de tiempo: 0.5 segundos. Límite de memoria: 64 MB.

## Entrada

`N`, `K` y `M`, cada uno en su propia línea.

## Salida

La cantidad módulo `M`.

## Evaluación

Se comparan enteros exactos. Las fuentes nuevas tienen pruebas completas de destino y Accepted propio; las bases publicadas conservan su propio Accepted, sin sustituir medidas del archivo antiguo.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
2
1000
```

Salida:

```
8
```

### Ejemplo 2

Entrada:

```
3
10
7
```

Salida:

```
2
```

## Solución

Las cinco versiones sencillas mantienen los dos estados matriciales.
Tras la primera cifra no nula, `(zero,other)=(0,K−1)`. Al añadir una cifra,
`zero'=other` y `other'=(K−1)(zero+other)`: cero solo sigue a una cifra no
nula, y cualquier prefijo válido admite `K−1` cifras no nulas. Con
`c=(K−1) mod M`, elevar `A=[[0,1],[c,c]]` a `N−1` por exponenciación binaria
y aplicarla a `(0,c)` da los estados finales; su suma módulo `M` es la
respuesta. No hay división modular, incluso con módulos compuestos.

El exponente tiene como máximo 60 bits: `O(log N)` pasos matriciales y un
número constante de residuos. C++/Rust ensanchan a 128 bits: la suma de dos
productos es menor que `2M²≤2·10³⁶<2¹²¹`. Go usa `bits.Mul64` y el resto de
`bits.Div64`; la palabra alta es menor que `M`, cumpliendo la precondición.
Java/Python usan enteros arbitrarios; el coste depende de `log M`, por lo
que un número constante de residuos no implica bits constantes. El texto
de entrada y la representación del exponente se contabilizan aparte.

Solo se simplifica la entrada Rust: obtener tres `u64` de un iterador, sin
crear e indexar un vector. El cálculo matricial y la salida son idénticos.
Tiene un Accepted propio y medidas nuevas; no se llama optimización del
30%. Las otras cuatro bases conservan sus bytes, y se respalda el Rust anterior.

## Notas por lenguaje

Instantáneas guardadas: 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en ambas métricas; las otras familias exigen el primer puesto en ambas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

Se usa el perfil guardado de compiladores actuales, sin nuestro autor ni registros antiguos inferiores a 0,015 s; salvo C++, se exige ID de envío ≥10770000. La memoria de C++ se compara con las primeras 1000 filas admisibles. Los tiempos propios inferiores a 0,015 s se consideran 0,015 s. El corte por ID es una regla fija, no un filtro exacto de fechas.

- C++: base didáctica preferida `1013_matrix.cpp`; fuente que cubre `1013_matrix.cpp`; puestos tiempo/memoria 1/2, registros de otros autores 89/89.

- Go: base didáctica preferida `1013_matrix.go`; fuente que cubre `1013_matrix.go`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

- Java: base didáctica preferida `1013_matrix.java`; fuente que cubre `1013_dp_math.java`; puestos tiempo/memoria 3/1, registros de otros autores 5/5.

- Python/PyPy: base didáctica preferida `1013_matrix.py`; fuente que cubre `1013_dp_math.py`; puestos tiempo/memoria 26/1, registros de otros autores 43/43.

- Rust: base didáctica preferida `1013_matrix.rs`; fuente que cubre `1013_dp_math.rs`; puestos tiempo/memoria 2/1, registros de otros autores 1/1.

## Soluciones optimizadas

Se conservan las cinco matrices educativas, incluida la simplificación Rust ya aceptada. Sea c=(K-1)mod M y representar aX+b módulo X²-cX-c. Al cuadrar, a'=c*a²+2ab,b'=c*a²+b²; al multiplicar por X, a'=ca+b,b'=ca. Recorrer los bits de N desde el mayor, empezando en 1, obtiene X^N. La respuesta a*c+b mod M coincide con la recurrencia de dos estados y primer dígito no nulo. No hay división modular: M compuesto y factores comunes son seguros. Rust amplía productos a 128 bits; toda suma previa < 3M²<2^122. Python usa enteros grandes y máscara entera, sin cadena binaria. O(log N) pasos modulares y cantidad constante de residuos de O(log M) bits. Rust usa E/S ABI C acotada sin heap/arranque. La base es la matriz Rust actual de 200 KB, no los 220 KB históricos.

- `1013_dp_math.java`: 0.125 s / 752 KB; base `1013_matrix.java`: 0.125 s / 1868 KB; cambio respecto a la base: tiempo -0.0%, memoria -59.7%.
- `1013_dp_math.py`: 0.109 s / 272 KB; base `1013_matrix.py`: 0.078 s / 400 KB; cambio respecto a la base: tiempo +39.7%, memoria -32.0%.
- `1013_dp_math.rs`: 0.031 s / 44 KB; base `1013_matrix.rs`: 0.031 s / 200 KB; cambio respecto a la base: tiempo -0.0%, memoria -78.0%.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1013_matrix.cpp](1013_matrix.cpp) | G++ 13.2 x64 | matrix | O(log N) | AC | 0.015 s | 136 KB | 11278088 |
| [1013_matrix.go](1013_matrix.go) | Go 1.14 x64 | matrix | O(log N) | AC | 0.031 s | 1072 KB | 11278089 |
| [1013_matrix.java](1013_matrix.java) | Java 1.8 | matrix | O(log N) | AC | 0.125 s | 1868 KB | 11278093 |
| [1013_matrix.py](1013_matrix.py) | Python 3.12 x64 | matrix | O(log N) | AC | 0.078 s | 400 KB | 11278091 |
| [1013_matrix.rs](1013_matrix.rs) | Rust 1.75 x64 | matrix | O(log N) | AC | 0.031 s | 200 KB | 11308297 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1013_dp_math.java](1013_dp_math.java) \* | Java 1.8 | dp, math | O(log N) modular steps; O(1) residues | AC | 0.125 s | 752 KB | 11308293 |
| [1013_dp_math.py](1013_dp_math.py) \* | PyPy 3.10 x64 | dp, math | O(log N) modular steps; O(1) residues | AC | 0.109 s | 272 KB | 11309745 |
| [1013_dp_math.rs](1013_dp_math.rs) \* | Rust 1.75 x64 | dp, math | O(log N) modular steps; O(1) residues | AC | 0.031 s | 44 KB | 11309707 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
