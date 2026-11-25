# 1701. Ostap y sus socios

[Timus 1701](https://acm.timus.ru/problem.aspx?space=1&num=1701) · dificultad 639 · dsu

Problema original de Dmitry Ivankov, del XIII Campeonato de los Urales de Programación Competitiva, 4 de abril de 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un cuaderno contiene afirmaciones «el empleado i gana d más que el
empleado j». El empleado 0, Vasili, gana 0, y nadie más gana más de
10⁹ (ni menos de 0). Hallar salarios que cumplan todas las
afirmaciones, o el número de la primera afirmación que no puede
cumplirse junto con las anteriores.

## Entrada

n y m (1 ≤ n, m ≤ 50000), y luego m afirmaciones i j d
(0 ≤ i, j < n; |d| ≤ 20000).

## Salida

Possible y los n salarios, o «Impossible after i statements». Se acepta
cualquier conjunto de salarios válido.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 6
3 4 1200
4 1 -5500
2 3 4300
3 0 8200
0 4 -7000
2 1 0
```

Salida:

```
Possible
0
12500
12500
8200
7000
```

### Ejemplo 2

Entrada:

```
3 5
1 2 5
0 2 0
1 0 -5
1 2 5
2 2 0
```

Salida:

```
Impossible after 3 statements
```

### Ejemplo 3

Entrada:

```
3 2
1 0 871
1 2 903
```

Salida:

```
Impossible after 2 statements
```

## Solución

Se procesan las afirmaciones en orden con una unión-búsqueda con pesos.
Cada empleado guarda la diferencia entre su salario y el de su padre,
así que salary(x) = salary(root) + offset(x) tras comprimir el camino.
Cada conjunto guarda además el rango de valores que puede tomar el
salario de su raíz para que todos sus salarios queden en 0 … 10⁹. El
conjunto de Vasili empieza con el único valor 0.

Una afirmación salary(i) − salary(j) = d dentro de un conjunto debe
concordar con los desplazamientos. Entre dos conjuntos fija
salary(rⱼ) = salary(rᵢ) + shift. El rango de la raíz unida es el rango
antiguo intersecado con el de la otra raíz desplazado en −shift, y un
rango vacío significa que la afirmación lo rompe todo. Al final cada
raíz toma el menor valor de su rango y todos los salarios salen de los
desplazamientos. `O((n + m) α(n))`.

Trampas:

- una afirmación puede contradecir solo los límites, no las demás
  afirmaciones: en el tercer ejemplo la segunda deja un salario
  negativo;
- una afirmación puede comparar a un empleado consigo mismo, y entonces
  d debe ser 0 (test 05);
- el límite superior nunca actúa aquí, pues |d| ≤ 20000 y a lo sumo
  49999 enlaces mantienen toda diferencia por debajo de 10⁹, pero el
  inferior sí;
- las búsquedas comprimen caminos sin recursión; la unión por tamaño
  mantiene poca profundidad.

El verificador comprueba el 0 de Vasili, los rangos y cada afirmación,
o la línea Impossible exacta; una implementación aceptada independiente
lo pasa con las mismas pruebas.

## Soluciones optimizadas

La versión en C++ guarda un registro por empleado. En la raíz, el campo del padre contiene el tamaño negativo del componente. En los demás nodos contiene el índice del padre. La compresión de caminos acumula la diferencia salarial hasta la raíz y la unión por tamaño limita la profundidad de la recursión. Un búfer de bytes lee las comparaciones sin crear cadenas para los números. El tiempo es O((n + m) α(n)) y el espacio es O(n). Las métricas corresponden al envío 11316975.

La versión en Python lee las afirmaciones línea por línea y acorta los caminos a la mitad en la estructura de conjuntos disjuntos con pesos. Conserva los datos de los componentes y los sueldos para la salida. Usa O(n) de espacio. Las métricas corresponden al envío 11317043.

Rust lee una comparación por vez y reutiliza el búfer de línea. Cada registro de la estructura de conjuntos disjuntos guarda el padre o el tamaño negativo, el desplazamiento al padre y el intervalo salarial factible de una raíz. El envío 11317269 tardó 0,046 s y usó 992 KB frente a 0,031 s y 5152 KB en la base.

Go analiza las comparaciones byte a byte desde un búfer. La estructura de conjuntos disjuntos con pesos guarda cuatro enteros de 32 bits por empleado y reutiliza un búfer de dígitos al escribir los salarios. El envío 11317271 tardó 0,015 s y usó 1712 KB frente a 0,109 s y 5968 KB en la base.

Java analiza las comparaciones desde un búfer de bytes y guarda los datos de los conjuntos disjuntos en cuatro arreglos de enteros. Reutiliza un búfer de dígitos para los salarios. El envío 11317272 tardó 0,125 s y usó 1320 KB frente a 0,14 s y 6400 KB en la base.

**Envíos de las versiones sencillas en Timus**

G++ 13.2 x64 №11318326 · Java 1.8 №11318331 · Python 3.12 x64 №11318337 · Rust 1.75 x64 №11318346.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1701_dsu.cpp](1701_dsu.cpp) | G++ 13.2 x64 | dsu | O((n + m) α(n)) | AC | 0.109 s | 2768 KB | 11318326 |
| [1701_dsu.go](1701_dsu.go) | Go 1.14 x64 | dsu | O((n + m) α(n)) | AC | 0.109 s | 5968 KB | 11322029 |
| [1701_dsu.java](1701_dsu.java) | Java 1.8 | dsu | O((n + m) α(n)) | AC | 0.14 s | 6400 KB | 11318331 |
| [1701_dsu.py](1701_dsu.py) | Python 3.12 x64 | dsu | O((n + m) α(n)) | AC | 0.343 s | 18168 KB | 11318337 |
| [1701_dsu.rs](1701_dsu.rs) | Rust 1.75 x64 | dsu | O((n + m) α(n)) | AC | 0.031 s | 5152 KB | 11318346 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1701_dsu_optimized.cpp](1701_dsu_optimized.cpp) | G++ 13.2 x64 | dsu | O((n + m) α(n)) | AC | 0.015 s | 928 KB | 11316975 |
| [1701_dsu_optimized.go](1701_dsu_optimized.go) \* | Go 1.14 x64 | dsu | O((n + m) α(n)) | AC | 0.015 s | 1712 KB | 11317271 |
| [1701_dsu_optimized.java](1701_dsu_optimized.java) | Java 1.8 | dsu | O((n + m) α(n)) | AC | 0.125 s | 1320 KB | 11317272 |
| [1701_dsu_optimized.py](1701_dsu_optimized.py) | Python 3.12 x64 | dsu | O((n + m) α(n)) | AC | 0.234 s | 7652 KB | 11317043 |
| [1701_dsu_optimized.rs](1701_dsu_optimized.rs) | Rust 1.75 x64 | dsu | O((n + m) α(n)) | AC | 0.046 s | 992 KB | 11317269 |

\* Aceptada. Aún queda por alcanzar el objetivo de clasificación de Python. El objetivo de clasificación de Rust sigue pendiente. El objetivo de clasificación de Go sigue pendiente. El objetivo de clasificación de Java sigue pendiente.
