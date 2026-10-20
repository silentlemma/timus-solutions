# 2178. Contar segmentos que contienen un conjunto de números consecutivos

[Timus 2178](https://acm.timus.ru/problem.aspx?space=1&num=2178) · dificultad 1932 · two_pointers

Problema original de Vadim Barinov, del Concurso Escolar de Programación de los Urales 2023.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Contar los segmentos de un arreglo de N números cuyos valores son
distintos y forman, en algún orden, un conjunto de enteros consecutivos.
Los límites son 1 segundo y 512 MB.

## Entrada

N, 1 ≤ N ≤ 10⁵, y luego a₁ … aₙ, 1 ≤ aᵢ ≤ 10⁵.

## Salida

El número de esos segmentos.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
4 2 3 1 2
```

Salida:

```
11
```

## Solución

Un segmento [l, r] vale exactamente cuando sus valores son distintos y
max − min = r − l. Que sean distintos es una condición de ventana: para
cada posición, el final más lejano sin valores repetidos sale de las
últimas apariciones de los valores en dos pasadas lineales, así que cada
inicio l tiene una cota R(l) para su final y cada final una cota para
su inicio.

El resto es el habitual divide y vencerás sobre el arreglo. Los
segmentos dentro de una mitad se cuentan recursivamente; para los que
cruzan el centro se toman mínimos y máximos de prefijo desde el centro
hacia fuera en ambos lados. Hay cuatro casos según dónde estén el mínimo
y el máximo:

- ambos a la izquierda: el final queda fijado como l + max − min, y se
  comprueba;
- ambos a la derecha: simétrico, queda fijado el inicio;
- máximo a la izquierda y mínimo a la derecha: la condición dice
  min(parte derecha) + r = max(parte izquierda) + l, así que los finales
  derechos cuyo máximo de prefijo sigue por debajo del máximo izquierdo y
  cuyo mínimo de prefijo está por debajo del mínimo izquierdo forman una
  ventana que se mueve de forma monótona al avanzar l a la izquierda;
  contar la clave min + r en la ventana responde cada l;
- mínimo a la izquierda y máximo a la derecha: igual con la clave
  max − r.

Las ventanas también se recortan con R(l). Cada nivel hace trabajo
lineal, así que el total es O(N log N), con un recorrido directo para
rangos muy cortos.

En el ejemplo valen 11 segmentos, entre ellos [4, 2, 3, 1] y [3, 1, 2].

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2178_two_pointers.cpp](2178_two_pointers.cpp) | G++ 13.2 x64 | two_pointers | O(N log N) | AC | 0.046 s | 2488 KB |
| [2178_two_pointers.go](2178_two_pointers.go) | Go 1.14 x64 | two_pointers | O(N log N) | AC | 0.062 s | 9076 KB |
| [2178_two_pointers.java](2178_two_pointers.java) | Java 1.8 | two_pointers | O(N log N) | AC | 0.156 s | 3168 KB |
| [2178_two_pointers.py](2178_two_pointers.py) | PyPy 3.10 x64 | two_pointers | O(N log N) | AC | 0.656 s | 18628 KB |
| [2178_two_pointers.rs](2178_two_pointers.rs) | Rust 1.75 x64 | two_pointers | O(N log N) | AC | 0.046 s | 4680 KB |
