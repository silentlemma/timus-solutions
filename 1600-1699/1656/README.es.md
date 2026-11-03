# 1656. El ejército del Reino Lejano

[Timus 1656](https://acm.timus.ru/problem.aspx?space=1&num=1656) · dificultad 206 · constructive

Problema original de Vladimir Yakovlev (idea de Magaz Asanov), del cuarto de final de la subregión oriental del NEERC 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay que colocar n² soldados de alturas dadas en un cuadrado de n × n de
modo que en cada fila y cada columna el más alto esté en el medio y las
alturas no crezcan del medio hacia ningún extremo.

## Entrada

Un n impar de 3 a 9 y luego n² alturas de 170 a 200.

## Salida

El cuadrado, n filas de n alturas. Se acepta cualquier disposición
válida.

## Evaluación

Se comprueban dimensiones, multiconjunto de alturas y todas las desigualdades hacia fuera; se acepta cualquier cuadrícula válida.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
170
170
180
175
170
175
175
170
175
```

Salida:

```
170 175 170
175 180 175
170 175 170
```

## Solución

Se ordenan las casillas por el par (menor, mayor) de sus distancias a la
fila central y a la columna central, y los soldados más altos van a los
rangos más bajos. En una fila a distancia a del centro, una casilla a
distancia b tiene rango (b, a) mientras b < a y (a, b) desde ahí: de
cualquier modo el rango crece con b, así que a cada lado del medio las
alturas no aumentan hacia fuera. Las columnas, igual por simetría. Las
casillas de igual rango son imágenes especulares y nunca quedan del mismo
lado de una misma línea. `O(n² log n)`; ordenación estable de Go: `O(n² log² n)`.

Detalles a tener en cuenta:

- «no crecer hacia los extremos» permite alturas iguales (prueba 02);
- hay muchas disposiciones válidas, así que un verificador comprueba las
  reglas y el conjunto de alturas.

Los cuadrados del programa pasan el verificador en 90 ejércitos
aleatorios.

## Soluciones optimizadas

Se cuentan alturas acotadas sin ordenar tuplas de coordenadas. Las celdas de menor distancia Manhattan al centro reciben alturas no menores; cada paso hacia fuera aumenta la distancia, probando las restricciones. Cada celda se rellena una vez y se permiten alturas iguales. Python expande los recuentos de alturas en un arreglo de bytes y usa desplazamientos de prefijos por niveles para emitir filas sin cuadrícula completa. Se conserva la construcción simple.

- `1656_constructive_optimized.cpp`: 0.001 s / 108 KB; base `1656_constructive.cpp`: 0.001 s / 180 KB; cambio respecto a la base: tiempo -0.0%, memoria -40.0%.
- `1656_constructive_optimized.java`: 0.078 s / 472 KB; base `1656_constructive.java`: 0.156 s / 4188 KB; cambio respecto a la base: tiempo -50.0%, memoria -88.7%.
- `1656_constructive_optimized.py`: 0.109 s / 268 KB; base `1656_constructive.py`: 0.046 s / 436 KB; cambio respecto a la base: tiempo +137.0%, memoria -38.5%.

## Notas por lenguaje

Se usa la instantánea guardada del 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en tiempo y memoria; las demás familias exigen el primer puesto en ambas métricas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

- C++: base didáctica preferida `1656_constructive.cpp`; versión que cubre `1656_constructive.cpp`; puestos tiempo/memoria 1/1, registros de otros autores 48/48.

- Go: base didáctica preferida `1656_constructive.go`; versión que cubre `1656_constructive.go`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

- Java: base didáctica preferida `1656_constructive.java`; versión que cubre `1656_constructive_optimized.java`; puestos tiempo/memoria 1/1, registros de otros autores 2/2.

- Python/PyPy: base didáctica preferida `1656_constructive.py`; versión que cubre `1656_constructive_optimized.py`; puestos tiempo/memoria 9/2, registros de otros autores 13/13.

- Rust: base didáctica preferida `1656_constructive.rs`; versión que cubre `1656_constructive.rs`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

## Soluciones

La tabla sencilla incluye las fuentes didácticas preferidas y las alternativas Accepted conservadas. Las notas identifican la base preferida de cada familia.

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1656_constructive.cpp](1656_constructive.cpp) | G++ 13.2 x64 | constructive | O(n² log n) | AC | 0.001 s | 180 KB | 11308831 |
| [1656_constructive.go](1656_constructive.go) | Go 1.14 x64 | constructive | O(n² log² n) | AC | 0.031 s | 1152 KB | 11288581 |
| [1656_constructive.java](1656_constructive.java) | Java 1.8 | constructive | O(n² log n) | AC | 0.156 s | 4188 KB | 11288583 |
| [1656_constructive.py](1656_constructive.py) | Python 3.12 x64 | constructive | O(n² log n) | AC | 0.046 s | 436 KB | 11308832 |
| [1656_constructive.rs](1656_constructive.rs) | Rust 1.75 x64 | constructive | O(n² log n) | AC | 0.031 s | 220 KB | 11308833 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1656_constructive_optimized.cpp](1656_constructive_optimized.cpp) | G++ 13.2 x64 | constructive | O(N^2+H) | AC | 0.001 s | 108 KB | 11308068 |
| [1656_constructive_optimized.java](1656_constructive_optimized.java) | Java 1.8 | constructive | O(N^2+H) | AC | 0.078 s | 472 KB | 11308073 |
| [1656_constructive_optimized.py](1656_constructive_optimized.py) \* | PyPy 3.10 x64 | constructive | O(N^2+H) time, O(N^2+H+N) compact bytes/counts; H31 | AC | 0.109 s | 268 KB | 11309461 |

\* Accepted; todavía no se alcanza el objetivo de clasificación. Esta versión admite mejoras.
