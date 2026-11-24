# 2001. Mathematicians and Berries

[Timus 2001](https://acm.timus.ru/problem.aspx?space=1&num=2001) · dificultad 22 · math

Problema original de Oleg Merkurev. (Prepared by Kirill Devyatkin), del Concurso Regional Escolar de Programación de los Urales 2013.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se pesan dos cestas tres veces. Al principio cada una contiene sus
propias bayas. Después se pasan todas las bayas de la segunda a la
primera y se pesan ambas. Finalmente se pasa todo el contenido de la
primera a la segunda y se repite. Recuperar las masas iniciales de
bayas, con masas constantes de las cestas.

## Entrada

Tres parejas cronológicas `a1 b1`, `a2 b2`, `a3 b3`, con lecturas
enteras de 0 a 10000 que corresponden a las transferencias. Tiempo 0,5
segundos y memoria 64 MB.

## Salida

Las masas iniciales de bayas de la primera y segunda cesta, en ese orden.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
1 2
2 1
0 3
```

```
1 1
```

La primera cesta está vacía en la última lectura, pesando 0. La segunda
está vacía en la intermedia, pesando 1. Restar esas masas de las
lecturas iniciales 1 y 2 da 1 y 1.

## Solución

Sean c y d los pesos de las cestas vacías, y x e y los de las bayas. La
primera pesada da a1 = c + x y b1 = d + y. Después de vaciar la segunda
cesta en la primera, b2 = d; después de vaciar la primera en la segunda,
a3 = c. Así x = a1 − a3 e y = b1 − b2; las lecturas a2 y b3 no hacen
falta. `O(1)`.

## Soluciones optimizadas

`2001_math_optimized.java`. Lee los seis valores y conserva diferencias exactas a1−a3 y b1−b2. O(1) aritmética y búferes fijos. Consume todos los campos numéricos usados antes de emitir. Reutiliza un arreglo de 256 bytes primero para entrada y luego salida, reservando doce bytes por int con signo y revirtiendo solo los dígitos nuevos. Elimina arreglos separados sin sobrescribir datos aún necesarios. Análisis/salida lineales en bytes consumidos, búfer fijo.

Accepted exacto Java 1.8 #11327769: 0.078 s / 364 KB. Comparación guardada del grupo de compiladores del 2026-11-20: tiempo 3/1109, memoria 7/1109. Bajo 1024 KB la admisión estricta solo usa tiempo: diez primeros o 15% superior, con empates compartidos y corte porcentual redondeado hacia arriba. Conserva el asterisco por la meta propia del lenguaje: primer puesto en ambas métricas. El registro optimizado documentado antes #11303655 era 0.125 s / 344 KB; es un par histórico distinto, no la medición actual de este fuente. Las bases didácticas permanecen intactas.

- `2001_math_optimized.java`: 0.078 s / 364 KB; base didáctica conservada `2001_math.java`: 0.156 s / 1608 KB.

Descripción y mediciones históricas de la revisión anterior: Las soluciones optimizadas (C++, Java) calculan las mismas dos
diferencias. C++ salta las lecturas a2 y b3 con `%*d` en `scanf` en
lugar de usar `iostream`: 124 KB en lugar de 396 KB, con el mismo
tiempo. Java analiza los números a mano desde `System.in` en lugar de
usar `Scanner`: 0.125 s en lugar de 0.156 s y 344 KB en lugar de
1608 KB.

Leer los seis valores con un búfer de bytes y escribir directamente las dos diferencias. El envío aceptado 11301801 tardó 0.015 s y usó 916 KB. La versión sencilla tardó 0.031 s y usó 1088 KB.

Leer los seis valores desde bytes y usar solo los cuatro necesarios para las dos diferencias. El envío aceptado 11301805 tardó 0.078 s y usó 364 KB. La versión sencilla tardó 0.093 s y usó 384 KB.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [2001_math.cpp](2001_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 396 KB | 11292438 |
| [2001_math.go](2001_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1088 KB | 11292439 |
| [2001_math.java](2001_math.java) | Java 1.8 | math | O(1) | AC | 0.156 s | 1608 KB | 11303362 |
| [2001_math.py](2001_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.093 s | 384 KB | 11292440 |
| [2001_math.rs](2001_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 228 KB | 11292442 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [2001_math_optimized.cpp](2001_math_optimized.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 124 KB | 11303653 |
| [2001_math_optimized.java](2001_math_optimized.java) | Java 1.8 | math | O(1) | AC | 0.078 s | 364 KB | 11327769 |
| [2001_math_optimized.go](2001_math_optimized.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 916 KB | 11301801 |
| [2001_math_optimized.py](2001_math_optimized.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 364 KB | 11301805 |
