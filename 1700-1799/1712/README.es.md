# 1712. Rejilla de cifrado

[Timus 1712](https://acm.timus.ru/problem.aspx?space=1&num=1712) · dificultad 86 · implementation

Problema original de Alex Samsonov, preparado por Alexander Ipatov, de la subregión oriental del NEERC 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una rejilla de 4 × 4 tiene cuatro ventanas. Puesta sobre una hoja de
4 × 4, deja ver cuatro casillas, y en ellas se escriben en orden de
lectura las cuatro letras siguientes de una contraseña de 16 letras.
Luego la rejilla gira 90° en sentido horario, y esto se repite cuatro
veces, así que cada casilla recibe exactamente una letra. Dada la
rejilla en su posición inicial y la hoja llena, recuperar la
contraseña.

## Entrada

Cuatro líneas de la rejilla, con X para una ventana y . para el papel,
y luego cuatro líneas de la hoja: letras latinas de ambos tipos.

## Salida

La contraseña, 16 letras.

## Ejemplos

### Ejemplo 1

Entrada:

```
....
X..X
.X..
...X
Pwoo
Khaa
smrs
odbk
```

Salida:

```
KamkohobPassword
```

## Solución

Se repite la escritura. En cada una de las cuatro posiciones se juntan
las letras bajo las ventanas fila por fila y de izquierda a derecha, y
luego se gira la rejilla. Un giro horario lleva la casilla (r, c) a
(c, 3 − r), así que la rejilla girada tiene en (r, c) lo que la antigua
tenía en (3 − c, r). `O(1)`.

Trampas:

- dentro de una posición las letras siguen el orden de lectura de las
  ventanas, no el orden en que se hallaron en la posición anterior;
- el giro es horario: girar al revés lee las mismas casillas en otro
  orden (en el test 04 las cuatro ventanas están en una esquina);
- la entrada no tiene espacios, así que leer por palabras funciona en
  cualquier lenguaje.

Las respuestas coinciden con una implementación aceptada independiente
en 300 rejillas válidas aleatorias.

## Soluciones optimizadas

Las soluciones optimizadas (C++, Java) leen los dos cuadrados carácter a
carácter en arreglos fijos de 4 × 4 en lugar de leer palabras, e
imprimen las letras de la contraseña según las encuentran (C++) o las
reúnen en un arreglo de 17 bytes (Java). Java además reutiliza un
arreglo para la rejilla girada en lugar de crear uno nuevo en cada giro.
C++: 84 KB en lugar de 348 KB, con el mismo tiempo; Java: 0.109 s en
lugar de 0.140 s y 348 KB en lugar de 1568 KB.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1712_implementation.cpp](1712_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.015 s | 348 KB | 11303500 |
| [1712_implementation.go](1712_implementation.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.031 s | 1076 KB | 11289216 |
| [1712_implementation.java](1712_implementation.java) | Java 1.8 | implementation | O(1) | AC | 0.140 s | 1568 KB | 11289222 |
| [1712_implementation.py](1712_implementation.py) | Python 3.12 x64 | implementation | O(1) | AC | 0.078 s | 492 KB | 11303501 |
| [1712_implementation.rs](1712_implementation.rs) | Rust 1.75 x64 | implementation | O(1) | AC | 0.031 s | 236 KB | 11303502 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1712_implementation_optimized.cpp](1712_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.015 s | 84 KB | 11303634 |
| [1712_implementation_optimized.java](1712_implementation_optimized.java) | Java 1.8 | implementation | O(1) | AC | 0.109 s | 348 KB | 11303503 |
