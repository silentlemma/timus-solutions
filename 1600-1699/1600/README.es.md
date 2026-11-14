# 1600. El aeropuerto

[Timus 1600](https://acm.timus.ru/problem.aspx?space=1&num=1600) · dificultad 552 · geometry

Problema original de Vladimir Yakovlev, del IX Campeonato Abierto Individual de la Universidad Estatal de los Urales, 1 de marzo de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hasta 500 objetos vuelan en línea recta a velocidad constante en el
espacio; todos empiezan a más distancia entre sí que una distancia
crítica d. Hay que hallar el primer momento en que algún par se acerca a
distancia d, e imprimir `ALARM!` y luego el tiempo con tres decimales y
el par, u `OK` si eso nunca ocurre. Si en ese momento se acercan varios
pares, se puede imprimir cualquiera.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

n y d, y luego la posición y la velocidad de cada objeto, seis números.

## Salida

`OK`, o `ALARM!` y luego el tiempo y los números de los dos objetos.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 1.0
1.0 1.0 -1.0 0.0 0.0 10.0
0.0 0.0 4.0 2.0 0.0 0.0
```

Salida:

```
ALARM!
0.500 1 2
```

## Solución

Visto desde un objeto del par, el otro se mueve por la recta p + v·t,
donde p y v son las diferencias de posiciones y velocidades. Están a
distancia d cuando |p + v·t|² = d², una ecuación cuadrática:
(v·v)t² + 2(p·v)t + (p·p − d²) = 0. Con velocidades iguales o
discriminante negativo, el par nunca se acerca. Si no, la raíz menor es
el momento en que la distancia llega por primera vez a d; como todos los
pares empiezan separados, una raíz negativa significa que se alejan. El
momento más temprano entre todos los pares es la respuesta: `O(n²)`,
unos 125000 pares.

Las pruebas usan un verificador que acepta cualquier par que se acerque
en el momento correcto, con el redondeo a tres decimales. Los tiempos se
contrastaron con una bisección sobre la distancia antes del máximo
acercamiento.

Detalles a tener en cuenta:

- un par que solo toca la distancia d en su máximo acercamiento también
  da la alarma: el discriminante es entonces exactamente 0 (prueba 04);
- con una velocidad relativa diminuta el tiempo puede ser grande, casi
  10⁶ segundos en la prueba 07, así que no hay que acotarlo de antemano;
- con el semidiscriminante, b = p·v y b² − a·c, no hace falta arrastrar
  el factor 4.

La versión sencilla en C++ escala los datos decimales a enteros y calcula exactamente el signo del discriminante. La versión sencilla en Java escala los datos decimales a enteros y calcula exactamente el signo del discriminante.

La versión sencilla en Rust escala los datos decimales a enteros y calcula exactamente el signo del discriminante.

## Soluciones optimizadas

Python ordena los objetos por la coordenada x y descarta los pares cuya separación en ese eje no puede llegar a la distancia crítica. Tras encontrar un encuentro, una cota superior entera de su tiempo limita el recorrido. El signo del discriminante se calcula exactamente para los pares restantes. Python 3.12 x64, envío 11322507. Tiempo 0,203 → 0,078 s, memoria 1492 → 1084 KB.

El envío de Java 11321903 tardó 0,125 s y usó 1780 KB. La versión sencilla actual tardó 0,281 s y usó 7020 KB.

**Envíos de las versiones sencillas en Timus**

G++ 13.2 x64 №11322335 · Go 1.14 x64 №11322334 · Java 1.8 №11322333 · Python 3.12 x64 №11322332 · Rust 1.75 x64 №11322336.

Go omite los pares que se alejan. Para los pares cerca de la tangencia vuelve a calcular el discriminante con aritmética racional a partir de los valores decimales de entrada y aplica la fórmula estable del tiempo de entrada.

C++ calcula la separación mínima con el producto vectorial y revisa las trayectorias casi tangentes en precisión cuádruple.

Rust escala la entrada decimal a enteros. Si todos los valores escalados tienen magnitud de hasta 500 000 000, calcula el discriminante exactamente con enteros de 128 bits. En los demás casos usa enteros de precisión arbitraria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1600_geometry.cpp](1600_geometry.cpp) | G++ 13.2 x64 | geometry | O(n²) | AC | 0.328 s | 664 KB | 11322335 |
| [1600_geometry.go](1600_geometry.go) | Go 1.14 x64 | geometry | O(n²) | AC | 0.093 s | 2428 KB | 11322334 |
| [1600_geometry.java](1600_geometry.java) | Java 1.8 | geometry | O(n²) | AC | 0.281 s | 7020 KB | 11322333 |
| [1600_geometry.py](1600_geometry.py) | Python 3.12 x64 | geometry | O(n²) | AC | 0.203 s | 1492 KB | 11322332 |
| [1600_geometry.rs](1600_geometry.rs) | Rust 1.75 x64 | geometry | O(n²) | AC | 0.234 s | 616 KB | 11322336 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1600_geometry_optimized.py](1600_geometry_optimized.py) \* | Python 3.12 x64 | geometry | O(n²) | AC | 0.078 s | 1084 KB | 11322507 |
| [1600_geometry_optimized.java](1600_geometry_optimized.java) \* | Java 1.8 | geometry | O(n²) | AC | 0.125 s | 1780 KB | 11321903 |
| [1600_geometry_optimized.go](1600_geometry_optimized.go) \* | Go 1.14 x64 | geometry | O(n²) | AC | 0.031 s | 1304 KB | 11322026 |
| [1600_geometry_optimized.cpp](1600_geometry_optimized.cpp) \* | G++ 13.2 x64 | geometry | O(n²) | AC | 0.031 s | 256 KB | 11321905 |
| [1600_geometry_optimized.rs](1600_geometry_optimized.rs) \* | Rust 1.75 x64 | geometry | O(n²) | AC | 0.031 s | 560 KB | 11322367 |

\* Las soluciones marcadas aún pueden mejorar en la clasificación objetivo.
