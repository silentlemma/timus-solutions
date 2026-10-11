# 1274. Aritmética de fracciones

[Timus 1274](https://acm.timus.ru/problem.aspx?space=1&num=1274) · dificultad 684 · math

Problema original de Sergey Volchenkov, Vladimir Pinaev y Michael Kopachev, del cuarto de final de la región central de Rusia del ACM ICPC 2003–2004, Rybinsk, 15–16 de octubre de 2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Sumar, restar, multiplicar o dividir dos fracciones escritas como
números mixtos, como `-7 3/4`, `8 1/2`, `-7/11`, `0` u `11`. El signo
solo se escribe en los negativos, la parte entera nula se omite si hay
fracción, y la fracción se omite si es nula. Las fracciones de entrada
pueden ser reducibles; la respuesta se escribe igual y totalmente
reducida. Partes enteras y numeradores llegan a 30 000, denominadores
de 1 a 30 000, tanto en la entrada como en la respuesta.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

La primera fracción, el signo de la operación y la segunda fracción,
cada uno en su línea.

## Salida

El resultado.

## Ejemplos

### Ejemplo 1

Entrada:

```
-3 1/6
+
2/4
```

Salida:

```
-2 2/3
```

## Solución

Cada operando se convierte en un numerador con signo sobre un
denominador: w n/d pasa a ±(w·d + n)/d. Se aplica la operación con las
fórmulas de siempre, se pasa el signo de un denominador negativo al
numerador y se dividen ambos por su máximo común divisor. Luego se
escriben el signo, la parte entera y el resto sobre el denominador,
omitiendo las partes nulas. Los productos intermedios quedan por debajo
de 10¹⁸, holgadamente en 64 bits. `O(log 30000)`.

Detalles a tener en cuenta:

- un resultado nulo se escribe `0`, sin signo (pruebas 02, 09);
- un resultado entero no lleva fracción, y uno menor que uno no lleva
  parte entera (pruebas 04, 06);
- dividir entre un negativo lleva el signo al denominador, y hay que
  devolverlo (prueba 04);
- la operación `-` en su propia línea no debe confundirse con el signo
  de una fracción.

Las respuestas se compararon con `Fraction` de Python en 300 casos
generados.

## Notas por lenguaje

- Todos los lenguajes analizan la fracción por palabras, aparte el
  signo, e imprimen con los mismos tres casos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1274_math.cpp](1274_math.cpp) | G++ 13.2 x64 | math | O(log 30000) | AC | 0.015 s | 424 KB |
| [1274_math.go](1274_math.go) | Go 1.14 x64 | math | O(log 30000) | AC | 0.031 s | 1068 KB |
| [1274_math.java](1274_math.java) | Java 1.8 | math | O(log 30000) | AC | 0.109 s | 784 KB |
| [1274_math.py](1274_math.py) | Python 3.12 x64 | math | O(log 30000) | AC | 0.078 s | 544 KB |
| [1274_math.rs](1274_math.rs) | Rust 1.75 x64 | math | O(log 30000) | AC | 0.031 s | 244 KB |
