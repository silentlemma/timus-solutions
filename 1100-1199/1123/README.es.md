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

Primero se eliminan los ceros iniciales, conservando un cero si todas las
cifras son cero. La respuesta tiene tantas cifras como este número
normalizado: el número formado solo por
nueves es un palíndromo. Un palíndromo de esta longitud queda fijado por
su mitad izquierda junto con la cifra central, y una mitad izquierda
mayor da siempre un palíndromo mayor. Así que se copia la mitad izquierda
al revés sobre la derecha; si el resultado no es menor que el número, es
la respuesta. Si no, se suma uno a la mitad izquierda (con su cifra
central) y se refleja de nuevo: es la siguiente mitad izquierda posible,
así que el siguiente palíndromo. La suma no puede desbordarse, porque una
mitad izquierda de nueves se refleja en el mayor número de esa longitud,
que nunca es demasiado pequeño. Las cadenas de igual longitud se comparan
como los números, así que no hacen falta enteros grandes. Tiempo `O(L)`
y espacio auxiliar `O(L)`, donde `L` es la longitud de la entrada.

Detalles a tener en cuenta:

- el acarreo de la suma puede atravesar un bloque largo de nueves (1999
  pasa a 2002);
- con longitud impar la cifra central pertenece a la mitad izquierda;
- se deben eliminar los ceros iniciales antes de reflejar (`01` debe dar
  `1`, prueba `11`); una entrada formada solo por ceros debe dar `0`;
- el número tiene hasta 2001 cifras, muy por encima de cualquier tipo
  entero.

Las respuestas se comprobaron contando hasta el siguiente palíndromo para
todos los números de 0 a 9999 y 3000 entradas aleatorias con semilla fija
y hasta seis cifras significativas, incluidos ceros iniciales. Las entradas
largas se comprobaron con una programación dinámica independiente que
asigna cifras simétricas y mantiene su comparación con la entrada.
Coincidieron las pruebas guardadas, los casos del generador y los casos
límite de hasta 2001 cifras, incluidos los acarreos largos.

## Notas por lenguaje

- Todos los lenguajes trabajan directamente con la cadena de cifras.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1123_strings.cpp](1123_strings.cpp) | G++ 13.2 x64 | strings | O(L) | AC | 0.001 s | 360 KB |
| [1123_strings.go](1123_strings.go) | Go 1.14 x64 | strings | O(L) | AC | 0.031 s | 1152 KB |
| [1123_strings.java](1123_strings.java) | Java 1.8 | strings | O(L) | AC | 0.093 s | 436 KB |
| [1123_strings.py](1123_strings.py) | Python 3.12 x64 | strings | O(L) | AC | 0.078 s | 448 KB |
| [1123_strings.rs](1123_strings.rs) | Rust 1.75 x64 | strings | O(L) | AC | 0.015 s | 204 KB |
