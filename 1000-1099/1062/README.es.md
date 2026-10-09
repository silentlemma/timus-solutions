# 1062. Quién puede ganar un triatlón con longitudes de etapa adecuadas

[Timus 1062](https://acm.timus.ru/problem.aspx?space=1&num=1062) · dificultad 1830 · geometry

Problema original del concurso regional ACM ICPC del noreste de Europa 2000–2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una carrera tiene tres etapas. `N` atletas (`1 ≤ N ≤ 100`) tienen
velocidades `Vi, Ui, Wi` (enteros de 1 a 10000) en las tres etapas. Los
organizadores pueden elegir cualesquiera longitudes positivas de las
etapas. Para cada atleta, decide si alguna elección de longitudes lo deja
como el único con el menor tiempo total.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

`N` y luego `N` líneas con `Vi Ui Wi`.

## Salida

Para cada atleta, `Yes` o `No`.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
9
10 2 6
10 7 3
5 6 7
3 2 7
6 2 6
3 5 7
8 4 6
10 4 2
1 8 7
```

Salida:

```
Yes
Yes
Yes
No
No
No
Yes
No
Yes
```

### Ejemplo 2

Entrada:

```
3
5 5 5
5 5 5
1 1 10
```

Salida:

```
No
No
Yes
```

## Solución

Con longitudes `(a, b, c)` el tiempo del atleta `j` es
`a/Vj + b/Uj + c/Wj`. El atleta `i` le gana a `j` cuando

```text
(1/Vi − 1/Vj)·a + (1/Ui − 1/Uj)·b + (1/Wi − 1/Wj)·c < 0
```

Se reescalan las longitudes para el atleta `i`: `u = (a/Vi, b/Ui, c/Wi)`
sigue siendo cualquier terna positiva, y tras multiplicar por `Vj·Uj·Wj`
la condición queda `Σ (Sj − Si) · (las otras dos velocidades de j) · u < 0`
sobre las tres etapas, con coeficientes enteros menores que `10^12`. Solo
importan las proporciones, así que `u` recorre el triángulo
`x > 0, y > 0, x + y < 1` (la tercera parte es `1 − x − y`), y cada rival
lo corta con un semiplano abierto. El atleta `i` puede ganar cuando la
región abierta que queda no está vacía.

Decidirlo en coma flotante es frágil: la región puede ser una franja de
área diminuta pero positiva, o un segmento de área nula, y ninguna
tolerancia los distingue con seguridad. Las soluciones lo deciden de forma
exacta. Cada restricción se endurece en el mismo `ε > 0` diminuto; la
región abierta no está vacía exactamente cuando el polígono cerrado y
endurecido no está vacío para todo `ε` pequeño. El polígono se guarda como
la lista de sus rectas en el orden del borde, un vértice es el punto donde
se cortan dos rectas consecutivas, y el lado de un vértice respecto de una
recta nueva es el signo de un valor entero y, si es cero, el de su
coeficiente de `ε`. Estos valores quedan por debajo de `3 · 10^37`, dentro
de 128 bits. El recorte conserva cada lado con una parte estrictamente
dentro y coloca la recta nueva donde el borde sale del semiplano. `O(N)`
por rival, `O(N^3)` en total, como mucho un millón de pasos.

Detalles a tener en cuenta:

- atletas idénticos: ninguno puede llegar primero en solitario;
- un atleta igual en dos etapas y más lento en la tercera nunca es
  primero;
- la región de longitudes buenas puede ser un segmento o un punto, y eso
  no basta: una victoria estricta necesita una región abierta;
- una prueba de área en coma flotante con tolerancia fija (una primera
  versión usaba `10^-12`) falló en el juez; la prueba exacta no necesita
  tolerancia.

Las respuestas se comprobaron con una implementación exacta con
fracciones (recorte con semiplanos cerrados y luego área positiva) en
varios cientos de entradas aleatorias, muchas llenas de empates o de
velocidades casi iguales, y en una franja fina de victorias construida
justo por debajo del punto medio de dos rivales.

## Notas por lenguaje

- C++ y Rust usan enteros de 128 bits, Java `BigInteger`, Go `math/big` y
  Python sus propios enteros.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1062_geometry.cpp](1062_geometry.cpp) | G++ 13.2 x64 | geometry | O(N^3) | AC | 0.015 s | 212 KB |
| [1062_geometry.go](1062_geometry.go) | Go 1.14 x64 | geometry | O(N^3) | AC | 0.046 s | 6444 KB |
| [1062_geometry.java](1062_geometry.java) | Java 1.8 | geometry | O(N^3) | AC | 0.109 s | 5156 KB |
| [1062_geometry.py](1062_geometry.py) | Python 3.12 x64 | geometry | O(N^3) | AC | 0.093 s | 756 KB |
| [1062_geometry.rs](1062_geometry.rs) | Rust 1.75 x64 | geometry | O(N^3) | AC | 0.046 s | 244 KB |
