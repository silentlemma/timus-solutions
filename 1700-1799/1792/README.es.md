# 1792. Código de Hamming

[Timus 1792](https://acm.timus.ru/problem.aspx?space=1&num=1792) · dificultad 84 · implementation

Problema original de Sofia Tekhazheva (preparado por Olga Soboleva), del Concurso Regional Escolar de Programación de los Urales 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cuatro discos que se cortan tienen un bit cada uno, y tres pétalos, las
zonas comunes a tres discos, tienen la paridad de la suma de los discos
que los cubren. En el orden de la figura del enunciado, el pétalo j
está en todos los discos salvo el disco j, y el cuarto disco cubre los
tres pétalos. Se cambió como mucho uno de los siete bits. Restaurar un
código válido.

## Entrada

Siete bits: los cuatro discos y luego los tres pétalos.

## Salida

Los siete bits de un código válido que difiera de la entrada en a lo
sumo un lugar.

## Ejemplos

### Ejemplo 1

Entrada:

```
0 1 0 1 1 0 1
```

Salida:

```
0 1 0 0 1 0 1
```

### Ejemplo 2

Entrada:

```
1 1 1 1 1 1 1
```

Salida:

```
1 1 1 1 1 1 1
```

## Solución

Se comprueba la palabra tal cual: el pétalo j debe ser igual a la suma
de los discos distintos del disco j, módulo 2. Si falla, se prueba a
cambiar cada uno de los siete bits por turno y se conserva el primer
cambio que hace válida la palabra. Dos palabras válidas siempre
difieren en al menos tres lugares, así que la respuesta es única.
`O(1)`.

En el primer ejemplo los tres pétalos están mal, y solo el cuarto disco
está bajo todos ellos; cambiarlo de 1 a 0 hace que los pétalos sean 1,
0, 1, como están escritos.

Trampas:

- el bit cambiado puede ser un pétalo, no un disco;
- la palabra puede ser ya válida, y entonces se imprime sin cambios.

Cada una de las 128 entradas posibles da la misma respuesta que una
implementación aceptada independiente.

## Soluciones optimizadas

Las soluciones optimizadas (C++, Java) leen los siete bits como
caracteres sueltos con `getchar` y `System.in.read` en lugar de
`iostream` y `Scanner`, y escriben la respuesta carácter a carácter
(C++) o como un solo arreglo de bytes (Java). La búsqueda entre los
cambios de un solo bit es la misma. C++: 84 KB en lugar de 396 KB, con
el mismo tiempo; Java: 0.109 s en lugar de 0.156 s y 380 KB en lugar de
1604 KB.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1792_implementation.cpp](1792_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.015 s | 396 KB | 11303512 |
| [1792_implementation.go](1792_implementation.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.031 s | 1168 KB | 11289857 |
| [1792_implementation.java](1792_implementation.java) | Java 1.8 | implementation | O(1) | AC | 0.156 s | 1604 KB | 11303513 |
| [1792_implementation.py](1792_implementation.py) | Python 3.12 x64 | implementation | O(1) | AC | 0.093 s | 464 KB | 11303514 |
| [1792_implementation.rs](1792_implementation.rs) | Rust 1.75 x64 | implementation | O(1) | AC | 0.046 s | 228 KB | 11303515 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1792_implementation_optimized.cpp](1792_implementation_optimized.cpp) \* | G++ 13.2 x64 | implementation | O(1) | AC | 0.031 s | 84 KB | 11303639 |
| [1792_implementation_optimized.java](1792_implementation_optimized.java) | Java 1.8 | implementation | O(1) | AC | 0.109 s | 380 KB | 11303516 |

\* No está entre las 10 mejores ni en el 15% mejor de las soluciones de
su lenguaje en el juez actual; quizá se pueda optimizar más.
