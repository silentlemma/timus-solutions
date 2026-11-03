# 1200. Cuántos cuernos y pezuñas fabricar

[Timus 1200](https://acm.timus.ru/problem.aspx?space=1&num=1200) · dificultad 257 · math

Problema original de Magaz Asanov, del Concurso por Equipos de la Universidad Estatal de los Urales, marzo de 2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada cuerno da `A` rublos y cada pezuña `B` rublos, con
`-10000 ≤ A, B ≤ 10000` dados con dos decimales. Se pueden vender como
mucho `K ≤ 10000` artículos en total, y los extorsionadores cobran el
cuadrado del número de artículos de cada tipo. Hay que elegir `x` cuernos
e `y` pezuñas con `x + y ≤ K` que maximicen `A·x + B·y − x² − y²`; entre
los mejores planes, el de menos cuernos y luego el de menos pezuñas.

Límite de tiempo: 0.25 segundos. Límite de memoria: 64 MB.

## Entrada

`A` y `B`, y luego `K`.

## Salida

El mayor beneficio con dos decimales y luego `x` e `y`.

## Ejemplos

### Ejemplo 1

Entrada:

```
34.20 61.70
45
```

Salida:

```
1239.50
16 29
```

## Solución

Convierte precios a kopeks enteros `a,b`. Maximiza
`P(x,y)=a·x+b·y−100(x²+y²)`, con enteros `x,y≥0`, `x+y≤K`.
No producir es válido, por lo que el óptimo es no negativo.

La base enumera cuernos `x=0..K`. Para cada `x`, la ganancia de pezuñas
es una parábola cóncava con vértice `b/200`, restringida a `0≤y≤K−x`.
Prueba los dos enteros vecinos del vértice, recortados al intervalo; si
es negativo, conviene cero. Todo `x` y su mejor `y` están incluidos, lo
que prueba el óptimo global. Recorre `x` y candidatos `y` crecientes y
actualiza solo por ganancia mayor: los empates conservan menos cuernos,
luego menos pezuñas. Las cinco bases Accepted lo respetan. Tiempo `O(K)`,
estado de trabajo constante más entrada/salida acotada.

Los beneficios se comparan en kopeks exactos. Las bases redondean el precio
de dos decimales multiplicado por 100; para `|A|,|B|≤10000`, el error binario
es mucho menor que medio kopek y la conversión inicial es segura. Después
solo hay enteros. Para `K≤10000`, expresiones intermedias de valor absoluto
hasta `2·10¹⁰` y beneficio máximo `5·10⁹` kopeks requieren enteros nativos
con signo de 64 bits, no puntuaciones de 32 bits.

## Soluciones optimizadas

El beneficio es una cuadrática cóncava separable sobre un triángulo entero. Un óptimo interior redondea ambos vértices independientes; si viola la capacidad, existe un óptimo en un borde. Sustituir la igualdad de capacidad produce una cuadrática de una variable, cuyos enteros vecinos al vértice y extremos bastan. Java comprueba ese conjunto constante; Python efectúa directamente la proyección equivalente con desempate. Los beneficios son kopeks enteros exactos; se prefieren menos cuernos y después menos pezuñas. Es un algoritmo geométrico constante distinto del recorrido lineal.

- `1200_math_geometry.java`: 0.109 s / 868 KB; base `1200_math.java`: 0.140 s / 2096 KB; cambio respecto a la base: tiempo -22.1%, memoria -58.6%.
- `1200_math_geometry.py`: 0.125 s / 284 KB; base `1200_math.py`: 0.093 s / 488 KB; cambio respecto a la base: tiempo +34.4%, memoria -41.8%.

## Evaluación

Compara beneficio en kopeks exactos y ambos recuentos, incluido
el desempate. El candidato Java real pasó 13 entradas del repositorio
en Docker y tiene Accepted exacto. La implementación Python del método
de candidatos constantes se contrastó con enumerar todos los puntos
enteros de 8400 triángulos pequeños válidos, más 400 casos de capacidad
cero fuera del rango declarado `K≥1`: 8800 ejecuciones Python en total, no Java.
Casos importantes: precios negativos, cero producción, capacidad sin usar,
diagonal activa y vértices semienteros con ganancias iguales.

## Notas por lenguaje

Se usa la instantánea guardada del 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en tiempo y memoria; las demás familias exigen el primer puesto en ambas métricas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

- C++: base didáctica preferida `1200_math.cpp`; versión que cubre `1200_math.cpp`; puestos tiempo/memoria 1/2, registros de otros autores 54/54.

- Go: base didáctica preferida `1200_math.go`; versión que cubre `1200_math.go`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

- Java: base didáctica preferida `1200_math.java`; versión que cubre `1200_math_geometry.java`; puestos tiempo/memoria 1/1, registros de otros autores 3/3.

- Python/PyPy: base didáctica preferida `1200_math.py`; versión que cubre `1200_math_geometry.py`; puestos tiempo/memoria 8/1, registros de otros autores 12/12.

- Rust: base didáctica preferida `1200_math.rs`; versión que cubre `1200_math.rs`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

## Soluciones

La tabla sencilla incluye las fuentes didácticas preferidas y las alternativas Accepted conservadas. Las notas identifican la base preferida de cada familia.

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1200_math.cpp](1200_math.cpp) | G++ 13.2 x64 | math | O(K) | AC | 0.015 s | 156 KB | 11283537 |
| [1200_math.go](1200_math.go) | Go 1.14 x64 | math | O(K) | AC | 0.031 s | 1096 KB | 11283538 |
| [1200_math.java](1200_math.java) | Java 1.8 | math | O(K) | AC | 0.140 s | 2096 KB | 11283540 |
| [1200_math.py](1200_math.py) | Python 3.12 x64 | math | O(K) | AC | 0.093 s | 488 KB | 11283539 |
| [1200_math.rs](1200_math.rs) | Rust 1.75 x64 | math | O(K) | AC | 0.046 s | 260 KB | 11283542 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1200_math_geometry.java](1200_math_geometry.java) | Java 1.8 | math, geometry | O(1) | AC | 0.109 s | 868 KB | 11308035 |
| [1200_math_geometry.py](1200_math_geometry.py) \* | PyPy 3.10 x64 | math, geometry | O(1) | AC | 0.125 s | 284 KB | 11309374 |

\* Accepted; todavía no se alcanza el objetivo de clasificación. Esta versión admite mejoras.
