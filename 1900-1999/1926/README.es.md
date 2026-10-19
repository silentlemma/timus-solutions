# 1926. Restos dinámicos mediante un único módulo común

[Timus 1926](https://acm.timus.ru/problem.aspx?space=1&num=1926) · difficulty 999 · number_theory

Problema original de Alexander Onokhin y Bulat Zaynullin; concurso escolar regional de los Urales de 2012.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Mantener un entero decimal positivo n con reemplazos de dígitos y consultas
de resto. Las posiciones empiezan en 1 por la derecha. Se cambia una posición
existente por 0..9 y el primer dígito nunca pasa a cero; la longitud permanece.
Cada divisor c es 1 o producto de primos distintos no mayores que 47.
Responder tras todas las modificaciones anteriores. Límites: 2 segundos,64 MB.

## Entrada

n con 1≤n<10^100000, hasta 100000 dígitos. Luego m, 1≤m≤10000.
Cada consulta es `0 c` o `1 k b`: k es la posición desde la derecha y b
el nuevo dígito. c es positivo y cumple la condición de primos distintos;
puede alcanzar 614889782588491410, por lo que requiere lectura de 64 bits.

## Salida

Para cada consulta tipo 0 imprimir n mod c en una línea, en orden.
Las modificaciones no imprimen nada. Si todas modifican, la salida es vacía.

## Evaluación

Comparar exactamente la secuencia de tokens enteros.

## Ejemplos

```
4123456789897654321
5
0 1
0 7
0 10
1 2 9
0 6
```

```
0
0
1
5
```

## Solución

Sea P el producto de los quince primos hasta 47:
2,3,5,7,11,13,17,19,23,29,31,37,41,43,47.
P=614889782588491410. Todo c permitido divide P, incluido 1.
Si R=n mod P, entonces n mod c=R mod c. Basta mantener un residuo,
sin reconstrucción a partir de residuos por primo.

Leer n como texto. Para D dígitos precalcular W[j]=10^j mod P,
j=0..D−1. El residuo inicial se obtiene recorriendo de izquierda a derecha
con Horner: R=(10R+dígito) mod P.

Cambiar la posición k desde la derecha altera el entero en
(nuevo−viejo)·10^(k−1). Guardar los dígitos actuales, leer el viejo en D−k,
reemplazarlo y actualizar

```text
R = (R + (nuevo−viejo)·W[k−1]) mod P, normalizado a 0..P−1.
```

Horner establece R≡n mod P y el cambio exacto de valor preserva esa
congruencia. Por inducción vale tras cada actualización. Como c divide P,
R mod c es el resto pedido. Guardar el nuevo dígito permite cambios repetidos.

### Límites aritméticos

Todo cabe en 64 bits con signo. R,W están en [0,P); los pasos de Horner
y potencias son menores que 10P. La diferencia de dígitos está en [−9,9],
así que la expresión de actualización queda entre −9P y 10P estrictamente.
10P=6148897825884914100 es menor que 2^63−1=9223372036854775807.
Convertir a 64 bits antes de multiplicar.

Si el resto puede ser negativo, primero aplicar `% P` y después sumar P
si quedó negativo. Rust usa `rem_euclid`; Python normaliza `%` directamente.
Las soluciones no convierten n entero a un tipo de máquina ni necesitan
aritmética de precisión arbitraria.

O(D+m) tiempo y espacio total, incluidas consultas y salida almacenadas.
Dígitos y potencias usan O(D) espacio de trabajo. Cada consulta realiza
O(1) operaciones de ancho fijo.

El exponente es k−1 y el índice textual D−k. Leer el dígito vigente,
normalizar restos negativos y usar la condición de primos distintos.
Los factores 2 y 5 no molestan porque nunca se divide por 10 ni se invierte.
Incluso con n pequeño, el divisor puede necesitar 64 bits.

## Notas por lenguaje

C++, Go, Java y Rust usan 64 bits con signo para restos, potencias y c.
Java usa lectura con búfer; Go evita el límite fijo de tokens de scanner
mediante un reader. Python conserva n como texto, evitando el límite de
conversión de enteros enormes. Todas mantienen dígitos mutables y salida vacía.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1926_number_theory.cpp](1926_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(D+m) | AC | 0.015 s | 1692 KB |
| [1926_number_theory.go](1926_number_theory.go) | Go 1.14 x64 | number_theory | O(D+m) | AC | 0.046 s | 3652 KB |
| [1926_number_theory.java](1926_number_theory.java) | Java 1.8 | number_theory | O(D+m) | AC | 0.125 s | 3464 KB |
| [1926_number_theory.py](1926_number_theory.py) | Python 3.12 x64 | number_theory | O(D+m) | AC | 0.171 s | 6808 KB |
| [1926_number_theory.rs](1926_number_theory.rs) | Rust 1.75 x64 | number_theory | O(D+m) | AC | 0.046 s | 1684 KB |
