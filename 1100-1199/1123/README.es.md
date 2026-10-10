# 1123. El menor palíndromo no inferior a un número largo

[Timus 1123](https://acm.timus.ru/problem.aspx?space=1&num=1123) · dificultad 122 · strings

Problema original de Leonid Volkov y Oleg Kats, del USU Open Collegiate Programming Contest, octubre de 2001, Junior Session.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dado un entero no negativo de hasta 2001 cifras, imprime el menor
palíndromo (un número que se lee igual desde ambos extremos) mayor o igual
que él.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

El número en una línea.

## Salida

El palíndromo.

## Evaluación

La salida se compara token a token; los espacios en blanco de más no
importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
12341321
```

Salida:

```
12344321
```

## Solución

La respuesta tiene el mismo número de cifras: el número formado solo por
nueves es un palíndromo. Un palíndromo de esta longitud queda fijado por
su mitad izquierda junto con la cifra central, y una mitad izquierda
mayor da siempre un palíndromo mayor. Así que se copia la mitad izquierda
al revés sobre la derecha; si el resultado no es menor que el número, es
la respuesta. Si no, se suma uno a la mitad izquierda (con su cifra
central) y se refleja de nuevo: es la siguiente mitad izquierda posible,
así que el siguiente palíndromo. La suma no puede desbordarse, porque una
mitad izquierda de nueves se refleja en el mayor número de esa longitud,
que nunca es demasiado pequeño. Las cadenas de igual longitud se comparan
como los números, así que no hacen falta enteros grandes. `O(L)`.

Detalles a tener en cuenta:

- el acarreo de la suma puede atravesar un bloque largo de nueves (1999
  pasa a 2002);
- con longitud impar la cifra central pertenece a la mitad izquierda;
- el número tiene hasta 2001 cifras, muy por encima de cualquier tipo
  entero.

Las respuestas se comprobaron contando hacia arriba hasta el siguiente
palíndromo para números de hasta seis cifras, y para los más largos
construyendo con enteros grandes los palíndromos de la mitad izquierda
`p` y de `p + 1` y tomando el menor que no quede por debajo del número;
coincidieron 400 números aleatorios y las pruebas largas, con acarreos a
través de cientos de nueves.

## Notas por lenguaje

- Todos los lenguajes trabajan directamente con la cadena de cifras.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1123_strings.cpp](1123_strings.cpp) | G++ 13.2 x64 | strings | O(L) | AC | 0.015 s | 360 KB |
| [1123_strings.go](1123_strings.go) | Go 1.14 x64 | strings | O(L) | AC | 0.015 s | 1116 KB |
| [1123_strings.java](1123_strings.java) | Java 1.8 | strings | O(L) | AC | 0.093 s | 452 KB |
| [1123_strings.py](1123_strings.py) | Python 3.12 x64 | strings | O(L) | AC | 0.078 s | 376 KB |
| [1123_strings.rs](1123_strings.rs) | Rust 1.75 x64 | strings | O(L) | AC | 0.015 s | 204 KB |
