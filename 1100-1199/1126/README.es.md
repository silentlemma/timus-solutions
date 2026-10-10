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
valor no sea mayor que el suyo, porque ya no puede ser máximo mientras la
nueva esté en la ventana; luego entra por el final. El frente sale cuando
queda fuera de la ventana. El frente de la cola es siempre el máximo de
la ventana actual. Cada índice entra y sale una vez, así que el recorrido
entero es `O(N)`; recalcular cada ventana costaría `O(N·M)`, hasta 150
millones de pasos.

Detalles a tener en cuenta:

- las lecturas terminan en `-1`, no se da su número;
- de varias lecturas iguales pueden quitarse del final todas salvo la más
  nueva, que sale la última de la ventana;
- con `M = N` hay una sola ventana.

Las respuestas se comprobaron con el máximo de cada ventana calculado
directamente, en todas las pruebas.

## Notas por lenguaje

- Go y Java guardan la cola en un arreglo con un frente que avanza; C++,
  Rust y Python usan las colas dobles de su biblioteca.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1126_two_pointers.cpp](1126_two_pointers.cpp) | G++ 13.2 x64 | two_pointers | O(N) | AC | 0.015 s | 776 KB |
| [1126_two_pointers.go](1126_two_pointers.go) | Go 1.14 x64 | two_pointers | O(N) | AC | 0.062 s | 2896 KB |
| [1126_two_pointers.java](1126_two_pointers.java) | Java 1.8 | two_pointers | O(N) | AC | 0.156 s | 2332 KB |
| [1126_two_pointers.py](1126_two_pointers.py) | Python 3.12 x64 | two_pointers | O(N) | AC | 0.140 s | 3448 KB |
| [1126_two_pointers.rs](1126_two_pointers.rs) | Rust 1.75 x64 | two_pointers | O(N) | AC | 0.046 s | 1192 KB |
