# 1517. Libertad de elección

[Timus 1517](https://acm.timus.ru/problem.aspx?space=1&num=1517) · dificultad 240 · suffix_structures

Problema original de Ilya Grebnov, Nikita Rybak y Dmitry Kovalioff, de Timus Top Coders: Third Challenge.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se dan dos discursos de N letras latinas mayúsculas cada uno
(1 ≤ N ≤ 100000). Hay que escribir su fragmento común más largo: la
cadena más larga que aparece en ambos como parte contigua. Se acepta
cualquiera de las más largas.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

N y luego los dos discursos, uno por línea.

## Salida

El fragmento común más largo; una línea vacía si los discursos no
comparten ninguna letra.

## Ejemplos

### Ejemplo 1

Entrada:

```
28
VOTEFORTHEGREATALBANIAFORYOU
CHOOSETHEGREATALBANIANFUTURE
```

Salida:

```
THEGREATALBANIA
```

## Solución

Se construye el autómata de sufijos del primer discurso: sus estados
son las clases de subcadenas que terminan en el mismo conjunto de
posiciones, con la longitud de la cadena más larga de cada clase y un
enlace de sufijo a la clase de sus sufijos más cortos. Tiene como mucho
2N estados y se construye letra a letra en `O(N)`. Luego se lee el
segundo discurso a través de él, guardando el estado y la longitud run
del sufijo más largo de la parte leída que aparece en el primer
discurso. Si la siguiente letra no tiene transición, se siguen los
enlaces de sufijo, poniendo run a la longitud de cada estado alcanzado,
hasta que uno tenga la transición o se llegue al inicio; luego se toma
la transición y se suma uno. El mayor run, y dónde terminó en el
segundo discurso, dan la respuesta. `O(N)` con un alfabeto de 26
letras.

Detalles a tener en cuenta:

- los discursos pueden no compartir ninguna letra, y entonces la
  respuesta es una línea vacía (prueba 03, gen5);
- la respuesta puede ser un discurso entero (gen4);
- comparar todos los pares de posiciones lleva 10¹⁰ pasos;
- puede haber muchos fragmentos empatados, así que las pruebas usan un
  comprobador (todas las pruebas).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1517_suffix_structures.cpp](1517_suffix_structures.cpp) | G++ 13.2 x64 | suffix_structures | O(N) | AC | 0.093 s | 29044 KB |
| [1517_suffix_structures.go](1517_suffix_structures.go) | Go 1.14 x64 | suffix_structures | O(N) | AC | 0.046 s | 25012 KB |
| [1517_suffix_structures.java](1517_suffix_structures.java) | Java 1.8 | suffix_structures | O(N) | AC | 0.203 s | 35156 KB |
| [1517_suffix_structures.py](1517_suffix_structures.py) | Python 3.12 x64 | suffix_structures | O(N) | AC | 0.500 s | 56240 KB |
| [1517_suffix_structures.rs](1517_suffix_structures.rs) | Rust 1.75 x64 | suffix_structures | O(N) | AC | 0.062 s | 28496 KB |
