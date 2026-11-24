# 1685. Ortografía

[Timus 1685](https://acm.timus.ru/problem.aspx?space=1&num=1685) · dificultad 184 · strings

Problema original de Eugene Krokhalev, del X Campeonato Abierto Individual de la Universidad Estatal de los Urales, 28 de febrero de 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un texto se cifra escribiendo su carácter central (el número
(1 + n) div 2 de n), luego cifrando la parte a su izquierda y después
la parte a su derecha. Dada la línea cifrada, recuperar el texto.

## Entrada

Una línea de a lo sumo 20000 caracteres: letras latinas, espacios y
signos de puntuación.

## Salida

El texto original.

## Evaluación

Las pruebas del repositorio comparan todo el texto de salida, ignorando solo el espacio en blanco final. Conserva los espacios significativos, los saltos de línea, las mayúsculas y la puntuación.

## Ejemplos

### Ejemplo 1

Entrada:

```
kyaVs alisse uop.
```

Salida:

```
Vasya likes soup.
```

### Ejemplo 2

Entrada:

```
gtorhoprahy
```

Salida:

```
orthography
```

## Solución

El cifrado recorre las posiciones del texto en un orden fijo: el centro
de un rango, luego el rango izquierdo, luego el derecho. Ese orden solo
depende de n, así que se reproduce y se coloca el i-ésimo carácter
cifrado en la i-ésima posición visitada. Con rangos lo..hi numerados
desde 0, el centro es (lo + hi) div 2. Una pila explícita sustituye la
recursión, aunque su profundidad es solo de unos log n. `O(n)`.

Trampas:

- la línea puede empezar o acabar con espacios, que son caracteres del
  texto: solo se quita el salto de línea;
- el texto puede contener varios espacios seguidos (test 05).

Las respuestas coinciden con una implementación aceptada independiente
y devuelven la salida del cifrador a textos aleatorios.

## Soluciones optimizadas

La solución optimizada en C++ lee la línea con `fgets` en un búfer
estático de 20003 bytes, suficiente para 20000 caracteres, un retorno de
carro, un salto de línea y el cero final, y llena un arreglo estático de
salida de 20000 bytes que imprime con `fwrite`, en lugar de
`std::string` e `iostream`. Reproduce el orden con recursión simple
sobre intervalos semiabiertos en lugar de un vector de pares, ya que la
profundidad es como mucho unos 15 niveles para 20000 caracteres:
{1685_strings_optimized.cpp}.

La solución optimizada en Java reproduce el orden con recursión simple
sobre intervalos semiabiertos, de como mucho unos 15 niveles para
20000 caracteres, en lugar de un `ArrayDeque` que reserva dos rangos
`int[]` por cada carácter: {1685_strings_optimized.java}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1685_strings_optimized.cpp`: reducción de tiempo +0.00%; reducción de
  memoria +71.13%; base: `1685_strings.cpp`.

- `1685_strings_optimized.java`: reducción de tiempo +14.68%; reducción
  de memoria +60.05%; base: `1685_strings.java`.

`1685_strings_optimized.rs`. Conserva una línea codificada y reproduce centro-izquierda-derecha por recursión equilibrada sobre secciones de salida. Mantiene espacios iniciales y finales, eliminando solo CR/LF. Dos arreglos fijos de 20000 bytes reemplazan String, salida dinámica y pila explícita de intervalos. Cada carácter se visita una vez: tiempo O(n). Almacenamiento explícito de 40000 bytes y O(log(n+1)) marcos recursivos; el límite del enunciado justifica las capacidades. La versión Rust lee y escribe mediante el entorno de C, sin conservar un String de entrada decodificada ni construir un String de salida con formato. Se conserva la fuente sencilla con Accepted.

Frente a `1685_strings.rs`: tiempo 0.062 s → 0.046 s; memoria 248 KB → 88 KB.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1685_strings_optimized.rs`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1685_strings.cpp](1685_strings.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.015 s | 388 KB | 11288861 |
| [1685_strings.go](1685_strings.go) | Go 1.14 x64 | strings | O(n) | AC | 0.031 s | 1228 KB | 11288862 |
| [1685_strings.java](1685_strings.java) | Java 1.8 | strings | O(n) | AC | 0.109 s | 1672 KB | 11288864 |
| [1685_strings.py](1685_strings.py) | Python 3.12 x64 | strings | O(n) | AC | 0.078 s | 536 KB | 11288863 |
| [1685_strings.rs](1685_strings.rs) | Rust 1.75 x64 | strings | O(n) | AC | 0.062 s | 248 KB | 11288865 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1685_strings_optimized.cpp](1685_strings_optimized.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.015 s | 112 KB | 11307312 |
| [1685_strings_optimized.java](1685_strings_optimized.java) | Java 1.8 | strings | O(n) | AC | 0.093 s | 668 KB | 11307316 |
| [1685_strings_optimized.rs](1685_strings_optimized.rs) | Rust 1.75 x64 | strings | O(n) | AC | 0.046 s | 88 KB | 11325106 |
