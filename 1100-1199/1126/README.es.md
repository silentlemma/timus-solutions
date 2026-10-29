# 1126. El máximo de cada ventana de M lecturas consecutivas

[Timus 1126](https://acm.timus.ru/problem.aspx?space=1&num=1126) · dificultad 92 · two_pointers

Problema original de Alexander Mironenko, del sexto concurso universitario de programación de la Universidad Estatal de los Urales, 21 de octubre de 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dados un ancho de ventana `M` (`2 ≤ M ≤ 14000`) y `N` lecturas
(`M ≤ N ≤ 25000`, cada una de 0 a 100000) terminadas en `-1`, imprime el
máximo de las lecturas `1..M`, luego de `2..M+1`, y así hasta la última
ventana completa.

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

`M`, luego las lecturas una por línea y luego `-1`.

## Salida

Los `N − M + 1` máximos de las ventanas, uno por línea.

## Evaluación

La salida se compara token a token; los espacios en blanco de más no
importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
10
11
10
0
0
0
1
2
3
2
-1
```

Salida:

```
11
11
10
0
1
2
3
3
```

## Solución

Se mantiene una cola doble de índices cuyos valores decrecen del frente
al final. Una lectura nueva quita primero del final todo índice cuyo
valor no sea mayor que el suyo, porque ya no puede aumentar el máximo mientras la
nueva esté en la ventana; luego entra por el final. El frente sale cuando
queda fuera de la ventana. El frente de la cola es siempre el máximo de
la ventana actual. Cada índice entra y sale a lo sumo una vez, así que el recorrido
entero es `O(N)`; recalcular cada ventana costaría `O(N·M)`, hasta unos 156
millones de pasos.

Detalles a tener en cuenta:

- las lecturas terminan en `-1`, no se da su número;
- de varias lecturas iguales pueden quitarse del final todas salvo la más
  nueva, que sale la última de la ventana;
- con `M = N` hay una sola ventana.

Las respuestas se comprobaron con el máximo de cada ventana calculado
directamente, en todas las pruebas.

## Soluciones optimizadas

Las soluciones optimizadas (C++, Java) no guardan las lecturas: cada una
entra en la cola doble junto con su índice en cuanto se lee, y el máximo de
una ventana completa se imprime enseguida. C++ lee con `getchar`; Java
analiza a mano un búfer de bytes, guarda la cola doble en un búfer circular
de `M` celdas, ya que la ventana nunca tiene más, y escribe los números a
través de un búfer de bytes. C++: 224 KB en lugar de 776 KB, con el
mismo tiempo; Java: 0.109 s en lugar de 0.156 s y 624 KB en lugar de
2332 KB.

Las soluciones optimizadas en Python y Rust tampoco guardan las
lecturas: solo mantienen la ventana. Python la guarda en un búfer
circular de dos `array` en lugar de una deque y escribe las respuestas
en lotes de 256 líneas: 668 KB en lugar de 3448 KB, con el mismo tiempo.
Rust analiza los números a mano desde un búfer de 4 KB en lugar de leer
toda la entrada en una cadena, y escribe cada respuesta por una salida
con búfer en cuanto la conoce: 332 KB en lugar de 1192 KB, con el mismo
tiempo.

## Notas por lenguaje

- En las soluciones simples, Go y Java guardan la cola en un arreglo con
  un frente que avanza; C++, Rust y Python usan las colas dobles de su
  biblioteca.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1126_two_pointers.cpp](1126_two_pointers.cpp) | G++ 13.2 x64 | two_pointers | O(N) | AC | 0.015 s | 776 KB | 11279323 |
| [1126_two_pointers.go](1126_two_pointers.go) | Go 1.14 x64 | two_pointers | O(N) | AC | 0.062 s | 2896 KB | 11279328 |
| [1126_two_pointers.java](1126_two_pointers.java) | Java 1.8 | two_pointers | O(N) | AC | 0.156 s | 2332 KB | 11279331 |
| [1126_two_pointers.py](1126_two_pointers.py) | Python 3.12 x64 | two_pointers | O(N) | AC | 0.140 s | 3448 KB | 11279329 |
| [1126_two_pointers.rs](1126_two_pointers.rs) | Rust 1.75 x64 | two_pointers | O(N) | AC | 0.046 s | 1192 KB | 11279332 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1126_two_pointers_optimized.cpp](1126_two_pointers_optimized.cpp) | G++ 13.2 x64 | two_pointers | O(N) | AC | 0.015 s | 224 KB | 11303561 |
| [1126_two_pointers_optimized.java](1126_two_pointers_optimized.java) | Java 1.8 | two_pointers | O(N) | AC | 0.109 s | 624 KB | 11303563 |
| [1126_two_pointers_optimized.py](1126_two_pointers_optimized.py) \* | Python 3.12 x64 | two_pointers | O(N) | AC | 0.125 s | 668 KB | 11303710 |
| [1126_two_pointers_optimized.rs](1126_two_pointers_optimized.rs) | Rust 1.75 x64 | two_pointers | O(N) | AC | 0.031 s | 332 KB | 11303711 |

\* No está entre las 10 mejores ni en el 15% mejor de las soluciones de
su lenguaje en el juez actual; quizá se pueda optimizar más.
