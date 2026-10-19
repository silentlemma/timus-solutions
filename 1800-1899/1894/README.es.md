# 1894. Tiempo que impide volar

[Timus 1894](https://acm.timus.ru/problem.aspx?space=1&num=1894) · dificultad 1405 · geometry

Problema original de Daniil Ayzenshteyn, de la subregión oriental del NEERC 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se dan las posiciones de dos polígonos estrictamente convexos y no
degenerados hace 60 segundos. A permanece fijo; B se traslada sin
rotación a exactamente 1 metro por segundo en una dirección desconocida
pero constante. En la imagen, B cubre al menos un punto interior de A.

Entre todas las direcciones fijas posibles, hallar el tiempo mínimo
desde ahora hasta que los polígonos se separen. Si alguna dirección
podría haberlos separado ya, la respuesta es 0. Los límites son
2 segundos y 64 MB.

## Entrada

La primera línea contiene n y m, las cantidades de vértices de A y B,
con 3 ≤ n, m ≤ 50 000. Las siguientes n líneas dan los vértices de A,
y después m líneas dan los de B. Ambos órdenes son antihorarios.
Las coordenadas son metros enteros con valor absoluto como máximo 10⁸.

## Salida

Escribir el tiempo mínimo restante en segundos.

## Evaluación

El error absoluto o relativo no debe superar 10⁻⁶.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 4
400 400
600 400
600 600
400 600
0 0
1000 0
1000 1000
0 1000
```

Salida:

```
540.0
```

## Solución

Sea K = A + (−B), la diferencia de Minkowski: el conjunto de vectores
a − b con a en A y b en B. Tras trasladar B por un vector v, los
polígonos se intersectan exactamente cuando v pertenece a K. El
solapamiento inicial garantiza que el origen está estrictamente dentro.

Para una dirección unitaria fija u, el desplazamiento después de t
segundos es t·u. Separarse equivale a salir de K por ese rayo. La menor
distancia de salida entre todos los rayos es la distancia r del origen
a la frontera de K: toda salida alcanza la frontera y un punto más
cercano proporciona una dirección que alcanza el umbral de separación.
Como la velocidad es 1 y la imagen tiene 60 segundos de antigüedad,
la respuesta es max(0, r − 60).

Construir K en tiempo lineal. Negar cada vértice de B conserva el orden
antihorario. Rotar ambas listas para empezar en el vértice de menor y,
desempatando por x. Sus vectores de arista ya están en orden angular.
Fusionar ambas listas por ángulo, avanzando la dirección menor o
sumando ambos vectores si son paralelos y apuntan en el mismo sentido.
Desde la suma de los primeros vértices, estos pasos producen la frontera
de K en orden antihorario.

Para vértices consecutivos p y q de K, la distancia del origen a la
recta de la arista es cross(p, q) / hypot(q − p). El numerador es
positivo porque el origen está dentro. Tomar el mínimo sobre las
aristas. También es la distancia a la frontera: el disco centrado en
el origen con ese radio mínimo cabe en todos los semiplanos que definen
K, de modo que su contacto con una recta más cercana está en la arista
correspondiente.

La fusión puede evaluar cada arista nueva de inmediato, sin almacenar
K aparte. La lectura, la fusión y el recorrido cuestan `O(n + m)`
tiempo; las listas de entrada ocupan `O(n + m)` memoria.

En el ejemplo, K es el cuadrado [−600, 600] × [−600, 600]. La frontera
más cercana está a 600 metros del origen, así que el tiempo mínimo
restante es 600 − 60 = 540 segundos.

Trampas:

- restar los 60 segundos transcurridos y limitar la respuesta inferiormente a cero;
- negar B sin invertir el orden de sus vértices;
- fusionar juntas las aristas de la misma dirección;
- calcular los productos cruzados exactamente con enteros con signo de
  64 bits antes de dividir en coma flotante; los enteros de Python bastan;
- no elevar un producto cruzado al cuadrado en 64 bits: puede desbordarse;
- las coordenadas negativas son válidas; usar aritmética con signo e `hypot`.

Las pruebas incluyen un polígono delgado que delata la pérdida de
precisión y polígonos de 50 000 vértices cada uno; las respuestas
también se comprobaron aparte en 128 casos.

## Notas por lenguaje

Los productos cruzados de las direcciones y del numerador de la
distancia se calculan con enteros: `long long` en C++, `int64` en Go,
`long` en Java e `i64` en Rust; los enteros de Python tienen precisión
arbitraria. Convertir a coma flotante solo para la hipotenusa y la división
final evita perder el signo o una diferencia pequeña entre productos
grandes cuando las coordenadas son casi paralelas.

Todas las versiones imprimen diez cifras tras el separador decimal.
Java usa explícitamente `Locale.US` para que ese separador sea un punto.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1894_geometry.cpp](1894_geometry.cpp) | G++ 13.2 x64 | geometry | O(n + m) | AC | 0.031 s | 3148 KB |
| [1894_geometry.go](1894_geometry.go) | Go 1.14 x64 | geometry | O(n + m) | AC | 0.031 s | 8288 KB |
| [1894_geometry.java](1894_geometry.java) | Java 1.8 | geometry | O(n + m) | AC | 0.156 s | 4152 KB |
| [1894_geometry.py](1894_geometry.py) | Python 3.12 x64 | geometry | O(n + m) | AC | 0.296 s | 14956 KB |
| [1894_geometry.rs](1894_geometry.rs) | Rust 1.75 x64 | geometry | O(n + m) | AC | 0.031 s | 4744 KB |
