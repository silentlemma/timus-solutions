# 2032. Realizar tres longitudes en la retícula entera

[Timus 2032](https://acm.timus.ru/problem.aspx?space=1&num=2032) · dificultad 788 · geometry

Problema original de Alexey Danilyuk, del Concurso Regional Escolar de Programación de los Urales 2014.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dadas tres longitudes enteras positivas, encuentra tres puntos enteros
cuyas distancias por parejas sean exactamente esas longitudes, en
cualquier orden. Las longitudes no superan `10000000` y satisfacen la
desigualdad triangular. Cada coordenada tiene valor absoluto máximo
`100000000`. Límites: 1 segundo, 64 MB.

## Entrada

Una línea con las tres longitudes.

## Salida

Cualquier terna de parejas de coordenadas enteras separadas por blancos, o `-1`
si no existe realización. El orden de los vértices es arbitrario.

## Evaluación

Un comprobador compara exactamente los tres cuadrados de las distancias
y verifica el límite de coordenadas; `-1` solo se acepta si no existe un
triángulo entero. Se acepta cualquier colocación válida.

## Ejemplos

```
4 3 5
```

```
0 0
3 4
3 0
```

```
10 17 21
```

```
0 0
0 21
-8 15
```

```
100 100 100
```

```
-1
```

## Solución

Ordena `r ≤ b ≤ a`. Pon `A=(0,0)`, `B=(x,y)`, `C=(u,v)`, con `|B|=r`,
`|C|=b`, `|C-B|=a`. El producto escalar es `D=(r²+b²-a²)/2`: un numerador
impar impide coordenadas enteras. El vectorial es un entero `K` con
`K²=r²b²-D²`. Rechaza negativos y cuadrados no perfectos mediante raíz entera
exacta. El escalar puede ser negativo.

Para cada punto entero `B` del círculo de radio `r`, resuelve el sistema:
`u=(Dx-Ky)/r²`, `v=(Dy+Kx)/r²`. Ambos numeradores deben dividir exactamente.

Enumera el primer cuadrante, empezando por los ejes. Divide los catetos no nulos
por su mcd `t`: la terna pitagórica primitiva tiene hipotenusa `d=r/t`, divisor
de `r`. Euclides da catetos `m²-k²,2mk`, con `m²+k²=d`, `m>k≥1`,
coprimos y de paridades diferentes. Factoriza `r` por prueba y genera todos
los divisores. Para cada `d≥5` impar, prueba `m` desde `floor(sqrt(d/2))+1`
hasta `floor(sqrt(d-1))` y `k=isqrt(d-m²)`, comprobando cuadrado, mcd y
paridad. Escala por `r/d` y prueba ambos órdenes de coordenadas de inmediato,
sin guardar ni ordenar un círculo.

Para demostrar completitud, toma cualquier realización entera y traslada un
vértice al origen. Refleja toda la figura si el vectorial es negativo y luego
gírala un múltiplo de 90 grados para colocar `B` en el primer cuadrante cerrado.
Se conservan enteros. Los ejes o la parametrización completa visitan ese `B`,
y el sistema recupera su único `C`. Agotar candidatos prueba imposibilidad.
Que `K²` sea cuadrado es solo una condición necesaria previa a la búsqueda.

La validez sigue de `|C|²=(D²+K²)/r²=b²` y `|C-B|²=b²+r²-2D=a²`.
La divisibilidad garantiza enteros; sus módulos no superan las distancias
`r,b≤10000000` al origen, satisfaciendo el límite.

El primer ejemplo tiene cuadrados `25,9,16`, longitudes `5,3,4`. El segundo
`441,289,100` da `21,17,10`; los negativos son legales. En el equilátero
de lado 100, `D=5000` y `K²=75000000` no es cuadrado perfecto: corresponde `-1`.

Sean `d(r)` el número de divisores y `M` el mayor lado de entrada. Hay
hasta `O(d(r) sqrt(r))` intentos; las raíces binarias exactas, incluida
la raíz vectorial mayor, dan la cota común `O(d(r) sqrt(r) log(M+1))` de
tiempo y `O(d(r))` de espacio. Todos los valores intermedios, incluidos
límites de la raíz, caben en 128 bits con signo.

Trampas:

- Un lado no siempre puede situarse sobre un eje.
- Prueba todos los divisores y ambos órdenes, con mcd y paridad.
- Las raíces y divisiones deben ser exactas.
- El escalar y las coordenadas pueden ser negativos.
- Los productos llegan a `10^28`: amplía el tipo antes de multiplicar.

## Notas por lenguaje

C++ usa `__int128` con signo y Rust `i128`, con raíces binarias exactas.
Go usa `math/big.Int.Sqrt`; Java 8 usa `BigInteger` y Newton entero, ya
que esa versión no tiene raíz incorporada. Las raíces binarias pequeñas
de estos dos programas reciben valores de hasta `10000000`. Python usa
enteros exactos y `math.isqrt`. Ningún programa usa geometría flotante.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2032_geometry.cpp](2032_geometry.cpp) | G++ 13.2 x64 | geometry | O(d(r) sqrt(r) log(M+1)) | AC | 0.015 s | 404 KB |
| [2032_geometry.go](2032_geometry.go) | Go 1.14 x64 | geometry | O(d(r) sqrt(r) log(M+1)) | AC | 0.031 s | 1236 KB |
| [2032_geometry.java](2032_geometry.java) | Java 1.8 | geometry | O(d(r) sqrt(r) log(M+1)) | AC | 0.140 s | 788 KB |
| [2032_geometry.py](2032_geometry.py) | Python 3.12 x64 | geometry | O(d(r) sqrt(r) log(M+1)) | AC | 0.093 s | 736 KB |
| [2032_geometry.rs](2032_geometry.rs) | Rust 1.75 x64 | geometry | O(d(r) sqrt(r) log(M+1)) | AC | 0.046 s | 244 KB |
