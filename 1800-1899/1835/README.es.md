# 1835. El doctor del pantano

[Timus 1835](https://acm.timus.ru/problem.aspx?space=1&num=1835) · dificultad 3122 · strings

Problema original de Alexey Samsonov (preparado por Dmitry Ivankov e Ivan Burmistrov), del XV Campeonato Abierto de los Urales de Programación Competitiva, abril de 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una dirección es un nombre de usuario y un dominio unidos por "@", cada
uno una cadena no vacía de letras minúsculas y puntos que no empieza ni
termina en punto y no tiene dos puntos seguidos. Contar las direcciones
distintas que aparecen como subcadenas de un texto.

## Entrada

El texto, como mucho 10⁶ bytes de caracteres con códigos de 32 a 126 y
saltos de línea.

## Salida

El número de direcciones distintas del texto.

## Ejemplos

### Ejemplo 1

Entrada:

```
a.b@c.d
b@c.de.
@qq
q@.q
```

Salida:

```
5
```

## Solución

Que una cadena sea una dirección depende solo de la cadena, no de
dónde aparece. Así que sirve el conteo clásico de subcadenas distintas
con un filtro: se construye el arreglo de sufijos y el LCP de cada
sufijo con el anterior en el orden. Un prefijo de un sufijo aparece
antes en ese orden exactamente cuando no es más largo que ese LCP, así
que cada dirección distinta se cuenta una vez, en el primer sufijo que
empieza por ella, contando solo sus prefijos-dirección más largos que
el LCP.

Para un sufijo que empieza por letra, sus prefijos-dirección quedan
fijados por la primera "@" tras él en el mismo tramo de letras y
puntos. El usuario no puede retroceder más allá del último "..", la "@"
debe tener letras a ambos lados, y el dominio termina en una letra
antes del siguiente "..", "@" u otro carácter. Todo esto se precalcula
por cada "@", así que cada sufijo suma un número de letras en un
intervalo, con sumas prefijas.

El arreglo de sufijos sale del doblado cíclico de prefijos con
ordenación por conteo sobre un alfabeto de 30 símbolos en el que todo
otro carácter tiene un único código; los LCP salen del algoritmo de
Kasai. `O(n log n)`.

En el ejemplo las direcciones son a.b@c, a.b@c.d, b@c, b@c.d y b@c.de;
b@c y b@c.d aparecen dos veces pero cuentan una.

Trampas:

- la misma dirección puede aparecer muchas veces, así que contar
  apariciones cuenta de más;
- "a..b@c" contiene aún la dirección b@c, pero no a..b@c ni .b@c;
- una sola "@" entre dos tramos de 5·10⁵ letras da unos 2.5·10¹¹
  direcciones, lo que exige enteros de 64 bits;
- CPython es demasiado lento para un arreglo de sufijos de 10⁶
  caracteres; la solución en Python corre en PyPy y usa arreglos
  compactos.

Las respuestas coinciden con una comprobación de todas las subcadenas
en cientos de textos cortos aleatorios y con una implementación
aceptada independiente en textos de un megabyte.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1835_strings.cpp](1835_strings.cpp) | G++ 13.2 x64 | strings | O(n log n) | AC | 0.734 s | 40808 KB |
| [1835_strings.go](1835_strings.go) | Go 1.14 x64 | strings | O(n log n) | AC | 0.765 s | 41108 KB |
| [1835_strings.java](1835_strings.java) | Java 1.8 | strings | O(n log n) | AC | 0.703 s | 40628 KB |
| [1835_strings.py](1835_strings.py) | PyPy 3.10 x64 | strings | O(n log n) | AC | 1.218 s | 51268 KB |
| [1835_strings.rs](1835_strings.rs) | Rust 1.75 x64 | strings | O(n log n) | AC | 0.718 s | 49896 KB |
