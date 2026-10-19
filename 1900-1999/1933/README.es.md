# 1933. Una matriz de emparejamientos con participantes impares

[Timus 1933](https://acm.timus.ru/problem.aspx?space=1&num=1933) · difficulty 408 · constructive

Original problem from Open Ural FU Championship 2012 | by Alexander Ipatov (prepared by Oleg Dolgorukov).

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay R=2n+1 participantes y R rondas. Cada ronda asigna n parejas disjuntas
y una persona sin pareja como responsable. No se repite ninguna pareja
y cada participante dirige exactamente una vez. Construir una matriz
simétrica que indique la ronda asignada a cada pareja.
Límites: 1 segundo, 64 MB.

## Entrada

Un entero n, 1≤n≤100.

## Salida

R líneas de R enteros entre 0 y R. La diagonal es cero. La entrada
fuera de diagonal (i,j) indica la ronda 1..R en que i y j colaboran.
Hay nR=C(R,2) plazas totales; sin repeticiones, cada pareja aparece
exactamente una vez. Sirve cualquier calendario con todas las propiedades.

## Evaluación

checker.py lee R² enteros y verifica diagonal, rangos, simetría, n parejas
disjuntas por ronda, una única persona responsable por ronda y responsables
distintos. Acepta otros calendarios válidos, incluidos cambios de etiquetas
de rondas y permutaciones de participantes.

## Ejemplos

```
1
```

```
0 1 2
1 0 3
2 3 0
```

## Solución

Usar índices i,j desde cero. Poner 0 en la diagonal y
A[i][j]=((i+j+R−1) mod R)+1 fuera de ella. Sumar R mantiene la expresión
no negativa en todos los lenguajes. Simetría y rango son inmediatos.

Fijar participante i. Al recorrer todos los R valores de j, la fórmula
da cada etiqueta de ronda una vez. Excluir j=i deja etiquetas distintas
para todos los acompañantes reales y omite solo
L_i=((2i+R−1) mod R)+1. Como R es impar, multiplicar por 2 es invertible
módulo R. Las etiquetas omitidas L_i son, por tanto, distintas, también
si R es compuesto. Cada ronda tiene una sola persona ausente; todas
las demás aparecen una vez, y la simetría las agrupa en n parejas.
La ausente dirige. Cada persona falta en una ronda y estas rondas son
distintas, así que cada una dirige exactamente una vez. Cada pareja
sin orden recibe una sola etiqueta y no puede repetirse.
Esto demuestra toda la construcción.

O(n²) tiempo, igual al número de entradas que se deben imprimir.
Estas implementaciones guardan la matriz completa, con O(n²) espacio
incluido el posible búfer de salida.

Basta que R sea impar, no tiene que ser primo. Solo la diagonal lleva
ceros; ambas entradas simétricas deben dar la misma ronda. Tener una
persona responsable por ronda no basta sin que cada participante dirija
una vez. Reetiquetar rondas o participantes cambia la matriz manteniendo
su validez; comprobar propiedades en vez de igualdad textual.

## Notas por lenguaje

R≤201, etiquetas≤201 e i+j+R−1≤600; bastan enteros ordinarios.
C++ usa matriz de vectores y flujos sin sincronización; Go escribe
con búfer; Java y Rust construyen cadenas; Python une cada fila.
Todos imprimen R filas sin espacios finales.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1933_constructive.cpp](1933_constructive.cpp) | G++ 13.2 x64 | constructive | O(n^2) | AC | 0.015 s | 492 KB |
| [1933_constructive.go](1933_constructive.go) | Go 1.14 x64 | constructive | O(n^2) | AC | 0.031 s | 1836 KB |
| [1933_constructive.java](1933_constructive.java) | Java 1.8 | constructive | O(n^2) | AC | 0.125 s | 2592 KB |
| [1933_constructive.py](1933_constructive.py) | Python 3.12 x64 | constructive | O(n^2) | AC | 0.109 s | 744 KB |
| [1933_constructive.rs](1933_constructive.rs) | Rust 1.75 x64 | constructive | O(n^2) | AC | 0.031 s | 640 KB |
