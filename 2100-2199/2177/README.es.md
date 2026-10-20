# 2177. La fila más larga de números distintos cuyos vecinos suman X o V

[Timus 2177](https://acm.timus.ru/problem.aspx?space=1&num=2177) · dificultad 1242 · math

Problema original de Vadim Barinov, del Concurso Escolar de Programación de los Urales 2023.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hallar la fila más larga de enteros positivos distintos en la que cada
dos vecinos sumen X o V. Los límites son 1 segundo y 256 MB.

## Entrada

X y V, 3 ≤ X, V ≤ 10⁹.

## Salida

La mayor longitud.

## Ejemplos

### Ejemplo 1

Entrada:

```
10
5
```

Salida:

```
4
```

## Solución

Solo los números de [1, max(X, V) − 1] pueden aparecer en una fila de
longitud al menos dos. Se unen a y b distintos en este rango cuando
a + b es X o V. Cada número tiene a lo sumo dos compañeros, X − a y V − a,
así que los números forman caminos y ciclos disjuntos, y la fila más
larga es la mayor de esas componentes.

Sean X ≤ V y d = V − X. Si d = 0 las componentes son pares o vértices
aislados; siempre existe un par, así que la respuesta es 2. Si no,
alternar los dos tipos de compañero mueve un número en d:
a, X − a, a + d, X − a − d, … Así que una componente vive en
a lo sumo dos clases de restos módulo d, r y X − r, dentro de [1, V − 1].
Un camino termina cuando el siguiente compañero no es positivo o coincide
con el número actual (en X / 2 o V / 2 cuando son enteros).

- d = 1: una clase, todo el rango, V − 1 números.
- d = 2: si V es impar, las dos clases son las dos paridades y la
  respuesta vuelve a ser V − 1; si V es par, ambos compañeros conservan
  la paridad y la mejor clase tiene V / 2 números.
- d ≥ 3: la mejor componente toma dos clases distintas con
  ⌊(V − 3) / d⌋ + 1 números cada una, así que la respuesta es
  2 (⌊(V − 3) / d⌋ + 1).

Estas fórmulas coinciden con un conteo directo de las componentes para
todos los X, V menores que 60. El trabajo es O(1).

En el ejemplo d = 5, y la fila 8, 2, 3, 7 usa las clases de 2 y 3 módulo
5: 2 (⌊7 / 5⌋ + 1) = 4.

Cuidado (pruebas 03 y 21): un compañero ausente no tiene por qué coincidir
con el propio número. En la prueba 03, X = 3, V = 4, la fila más larga
2, 1, 3 termina en 3 porque su otro compañero es cero. Las sumas iguales
y pares, como en la prueba 21, también dejan aislado el punto medio;
no todas las componentes son pares.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2177_math.cpp](2177_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.031 s | 400 KB |
| [2177_math.go](2177_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1120 KB |
| [2177_math.java](2177_math.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 448 KB |
| [2177_math.py](2177_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 456 KB |
| [2177_math.rs](2177_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.046 s | 232 KB |
