# 1094. Una pantalla de una línea con un cursor que da la vuelta

[Timus 1094](https://acm.timus.ru/problem.aspx?space=1&num=1094) · dificultad 466 · simulation

Problema original de Stanislav Vasiliev, del USU Open Collegiate Programming Contest, marzo de 2001, Senior Session.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una pantalla muestra una línea de 80 caracteres, al principio todos
espacios, con el cursor en la posición más a la izquierda. Pulsar una
tecla de carácter lo escribe en el cursor, sustituyendo lo que había, y
mueve el cursor una posición a la derecha; `<` y `>` mueven el cursor sin
escribir. Cuando el cursor sobrepasa el borde izquierdo o el derecho,
salta a la posición más a la izquierda. Dada una línea de hasta 10000
pulsaciones, imprime la pantalla al final.

Límite de tiempo: 0.25 segundos. Límite de memoria: 64 MB.

## Entrada

Una línea de pulsaciones: letras, cifras, `:;-!?.,`, espacios, `<` y `>`.

## Salida

Los 80 caracteres de la pantalla.

## Evaluación

La salida debe ser igual al texto esperado; solo se ignoran los espacios
en blanco del final.

## Ejemplos

### Ejemplo 1

Entrada:

```
>><<<Look for clothes at the <<<<<<<<<<<<<<<second floor. <<<<<<<Fresh pizza and <<<<<<<<<<<<<<<<hamburger at a shop right to <<<<<<<<<<<<<the entrance. Call <<<<<<<<<< 123<-456<-8790 <<<<<<<<<<<<<<<<to order <<<<<<<<<<<<<<<<<computers< and office<<<<<<< chairs.
```

Salida:

```
Look for second hamburger at computer and chairs.790                            
```

## Solución

Se guarda un arreglo de 80 caracteres y la posición del cursor. Con `<` y
`>` se mueve el cursor; cualquier otra tecla se escribe y se avanza a la
derecha. Tras cada pulsación, un cursor fuera de `0 … 79` vuelve a 0.
`O(L)` para `L` pulsaciones.

Detalles a tener en cuenta:

- el borde izquierdo también manda el cursor a la posición más a la
  izquierda, que es lo mismo que quedarse: `<` en la posición 0 deja el
  cursor en 0;
- tras escribir la posición 80 el cursor vuelve a la primera, y lo mismo
  hace `>` desde la última posición;
- los espacios son teclas normales y no deben saltarse, así que la línea
  se lee entera, quitando solo el salto de línea;
- la línea puede estar vacía, y entonces la pantalla queda en blanco.

Las respuestas se comprobaron con una simulación aparte que guarda las
casillas escritas en un diccionario.

## Soluciones optimizadas

C++, Go y Rust consumen las teclas como flujo, conservando solo las 80 celdas y el cursor. La izquierda desde cero queda en cero; avanzar o escribir en la última celda vuelve a cero. Los espacios son escrituras normales. Se termina al primer fin de línea o EOF y se imprimen las 80 celdas, incluidos blancos finales. Tiempo O(L), espacio O(80) con entrada Go acotada. C++/Rust usan caracteres del C runtime, Rust con entrada C; Go manejadores estándar. Se conservan las bases; Java/Python reutilizan las admitidas.

Las implementaciones base aceptadas [1094_simulation.java](1094_simulation.java), [1094_simulation.py](1094_simulation.py) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1094_simulation_parsing_optimized.rs`. Se procesan comandos de terminal en bloques, evitando comprobar el rellenado por byte; se conservan movimientos y retorno del cursor.

Accepted #11328989 (Rust 1.75 x64): **0.015 s / 52 KB**. Comparación archivada: `1094_simulation_optimized.rs` (Rust 1.75 x64) — 0.031 s / 52 KB (#11315266).

## Notas por lenguaje

Estas notas describen las implementaciones sencillas.

- Los cinco lenguajes leen una línea e imprimen los 80 caracteres,
  incluidos los espacios del final.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1094_simulation.cpp](1094_simulation.cpp) | G++ 13.2 x64 | simulation | O(L) | AC | 0.015 s | 376 KB | 11279111 |
| [1094_simulation.go](1094_simulation.go) | Go 1.14 x64 | simulation | O(L) | AC | 0.015 s | 1092 KB | 11279112 |
| [1094_simulation.java](1094_simulation.java) | Java 1.8 | simulation | O(L) | AC | 0.093 s | 564 KB | 11279114 |
| [1094_simulation.py](1094_simulation.py) | Python 3.12 x64 | simulation | O(L) | AC | 0.078 s | 468 KB | 11279113 |
| [1094_simulation.rs](1094_simulation.rs) | Rust 1.75 x64 | simulation | O(L) | AC | 0.046 s | 204 KB | 11279115 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1094_simulation_optimized.cpp](1094_simulation_optimized.cpp) | G++ 13.2 x64 | simulation | O(L) | AC | 0.001 s | 76 KB | 11315263 |
| [1094_simulation_optimized.go](1094_simulation_optimized.go) | Go 1.14 x64 | simulation | O(L) | AC | 0.015 s | 276 KB | 11315265 |
| [1094_simulation_optimized.rs](1094_simulation_optimized.rs) | Rust 1.75 x64 | simulation | O(L) | AC | 0.031 s | 52 KB | 11315266 |
| [1094_simulation_parsing_optimized.rs](1094_simulation_parsing_optimized.rs) | Rust 1.75 x64 | simulation, parsing | O(L) | AC | 0.015 s | 52 KB | 11328989 |
