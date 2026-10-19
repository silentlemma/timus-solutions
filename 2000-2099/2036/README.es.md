# 2036. Clausura finita bajo intersecciones de rectas

[Timus 2036](https://acm.timus.ru/problem.aspx?space=1&num=2036) · dificultad 1706 · geometry

Problema original de Mikhail Rubinchik, del concurso Dandelion de la UrFU, campamento de Petrozavodsk, verano de 2014.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Parte de `n` puntos distintos. En cada iteración traza las rectas
determinadas por cada pareja de puntos actuales, intersecta todas las
parejas de rectas distintas no paralelas y añade sus intersecciones.
Repite mientras crezca el conjunto. Calcula el número final de puntos o
determina que el proceso es infinito. Límites: 0,5 segundos y 64 MB.

## Entrada

Un entero `1 ≤ n ≤ 100000` y `n` líneas con coordenadas enteras `x y`,
con `|x|,|y| ≤ 100000000`. Los puntos son distintos; hay una sola instancia,
sin cantidad inicial de pruebas. Las cotas solo limitan los puntos iniciales:
las intersecciones posteriores pueden ser fraccionarias y estar fuera del rango.

## Salida

El número final de puntos o exactamente `oo`, dos letras latinas minúsculas,
si el crecimiento es infinito.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
4
0 0
0 1
1 0
1 1
```

```
5
```

## Solución

Un conjunto es cerrado si una iteración no añade nada. Un conjunto colineal
es cerrado. También lo es uno cuyos puntos salvo uno están en una recta:
las demás rectas unen el punto exterior con los puntos de la base y todas
sus intersecciones finitas ya existen. La otra posibilidad finita consta
de cuatro vértices de un paralelogramo y el centro de sus diagonales.

### Demostración de que la clasificación es completa

En un conjunto finito, cerrado y no colineal, elige un triángulo `ABC`
de área positiva mínima. No hay puntos del conjunto en el segmento
abierto de ningún lado: con el vértice opuesto darían un triángulo de
área positiva menor. Todos los puntos están en las tres rectas
prolongadas de los lados. Si un punto no estuviera en ninguna, sus tres
coordenadas baricéntricas serían no nulas y dos tendrían el mismo signo.
La recta al vértice restante intersectaría el segmento abierto opuesto;
la clausura daría un punto prohibido. Esto también funciona si ambas
coordenadas del mismo signo son negativas.

Aplica una transformación afín invertible para obtener `A=(0,0),
B=(1,0), C=(0,1)`. Si hay puntos adicionales en dos lados, renombra los
vértices y escribe `D=(t,0), E=(0,u)`, con `t,u` fuera de `[0,1]`. Si
`tu≠1`, las rectas `DC` y `EB` se cortan en `(t(u−1)/(tu−1),
u(t−1)/(tu−1))`. Ninguna coordenada es cero y su suma no es uno, pues
`(t−1)(u−1)≠0`. El punto estaría fuera de las tres rectas laterales,
imposible. Por tanto `tu=1`; las restricciones obligan a que ambos
parámetros sean negativos.

Si `DE` corta `BC`, aparece un punto adicional `F` fuera del segmento
abierto. Repite el argumento de dos lados en el vértice `B`, con `D` en
`BA` y `F` en `BC`. El primer parámetro es `1−t>1`, aunque ambos
deberían ser negativos. Así, `DE` es paralela a `BC`, lo que da `t=u` y,
por producto y signo, `t=u=−1`. Los cinco puntos son los vértices
`B,C,D,E` de un paralelogramo y su centro `A`. Otro punto en `AB` o `AC`
violaría `tu=1` con el punto existente del otro lado; uno en `BC`
volvería a contradecir el argumento en `B`. No puede haber más.

Si los puntos adicionales están en un solo lado, todos salvo el vértice
opuesto son colineales. Esto completa la clasificación.
Recíprocamente, el paralelogramo con centro es cerrado: solo determina las
cuatro rectas laterales y las dos diagonales, con intersecciones finitas
en vértices o centro.

### Comprobar el conjunto inicial

Para `n≤3` devuelve `n`. En otro caso prueba las tres rectas entre parejas
de los primeros tres puntos. Si alguna deja fuera como máximo un punto,
devuelve `n`. Esto encuentra toda configuración de ese tipo: al menos dos
de los tres primeros puntos están en su recta base.

Tras fallar esas pruebas, una clausura finita solo puede ser el conjunto
especial de cinco puntos. Por eso `n>5` implica `oo`.
Para `n=4` deben ser los cuatro vértices de un paralelogramo, cuyo centro
añade un punto. Un subconjunto con centro y tres vértices contiene tres
puntos colineales y ya habría sido detectado. Para `n=5` deben existir
los cuatro vértices y su verdadero centro.

Prueba las tres particiones de cuatro puntos en parejas de extremos de
diagonales: las sumas de coordenadas de ambas parejas deben coincidir.
Con cinco puntos prueba cada posible centro; los otros cuatro deben formar
un paralelogramo y sumar cuatro veces el centro en cada coordenada.
Todo otro caso es infinito porque no cabe en ningún conjunto finito cerrado.

En el ejemplo, los cuatro vértices del cuadrado añaden `(1/2,1/2)` y el conjunto
de cinco puntos queda cerrado, dando `5`. Un centro no tiene que ser entero.
Los tres recorridos cuestan `O(n)` tiempo; las pruebas de cuatro o cinco puntos
son constantes. Guardar la entrada usa `O(n)` espacio y el trabajo geométrico
adicional `O(1)`.

Trampas:

- Un conjunto grande puede ser cerrado si todos salvo uno son colineales.
- Un trapecio con una sola pareja de lados paralelos no es el caso especial.
- El quinto punto debe ser el centro real de las diagonales.
- Se intersectan rectas completas, no solo segmentos.
- Imprime letras `oo` y no dígitos `00`; un límite de iteraciones no
  prueba infinitud.

## Notas por lenguaje

C++, Go, Java y Rust usan coordenadas enteras con signo de 64 bits antes de
multiplicar; Python usa enteros exactos. Las diferencias no superan `2·10^8`,
y el determinante tiene valor absoluto como máximo `8·10^16`.
Comparar sumas de extremos evita divisiones y admite centros semienteros.
Java usa arreglos de coordenadas primitivas; Python construye tuplas de puntos
sin guardar otra lista de todos los enteros convertidos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2036_geometry.cpp](2036_geometry.cpp) | G++ 13.2 x64 | geometry | O(n) | AC | 0.046 s | 1512 KB |
| [2036_geometry.go](2036_geometry.go) | Go 1.14 x64 | geometry | O(n) | AC | 0.140 s | 4496 KB |
| [2036_geometry.java](2036_geometry.java) | Java 1.8 | geometry | O(n) | AC | 0.125 s | 1992 KB |
| [2036_geometry.py](2036_geometry.py) | Python 3.12 x64 | geometry | O(n) | AC | 0.218 s | 25868 KB |
| [2036_geometry.rs](2036_geometry.rs) | Rust 1.75 x64 | geometry | O(n) | AC | 0.031 s | 4720 KB |
