# 1896. Juegos de guerra 2.1

[Timus 1896](https://acm.timus.ru/problem.aspx?space=1&num=1896) · dificultad 866 · fenwick, bitmask

Problema preparado por Maxim Pivko.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Colocar las etiquetas de 1 a N en un círculo. Desde 1, contar K
etiquetas que sigan presentes y eliminar la última contada. Reanudar
el conteo en su siguiente sucesora presente y repetir hasta vaciar
el círculo. La primera etiqueta eliminada es K.

Si sᵢ es la etiqueta eliminada en el paso i, calcular el XOR bit a bit
de |i − sᵢ| para todos los pasos de 1 a N. Los límites son 0,5 segundos
y 6 MB; el enunciado solo admite C, C++ y Pascal; el formulario de envío ofrece además Rust.

## Entrada

Una línea contiene N y K, con 1 ≤ N ≤ 1 100 000 y 1 ≤ K ≤ N.

## Salida

Escribir el XOR entero resultante.

## Evaluación

Las salidas se comparan como secuencias de tokens enteros.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 3
```

Salida:

```
2
```

## Solución

Considerar las etiquetas restantes en orden creciente. Sea r el índice
desde cero donde se reanuda el conteo, inicialmente 0. Con c etiquetas
restantes, el siguiente índice eliminado es (r + K − 1) módulo c.
Buscar su etiqueta, incorporar al XOR la diferencia absoluta con el
número de paso y eliminarla. Mantener r: ahora identifica a la sucesora,
y el siguiente módulo se encarga de volver al principio si hace falta.

Para buscar por rango dentro del límite de memoria, dividir las etiquetas
en palabras de 64 bits de presencia. Un bit activo indica una etiqueta
restante. Un árbol de Fenwick sobre esas palabras guarda sus cantidades
de bits activos. Su búsqueda de prefijos halla la primera palabra cuya
cuenta acumulada supera el rango r contado desde cero. Restar la cuenta
de las palabras anteriores para obtener el rango interior, también desde cero.

La selección dentro de una palabra es constante: usar cuentas de bits
activos para elegir mitades sucesivas hasta localizar el bit. El tamaño
de palabra está fijado en 64 bits. Borrar ese bit y reducir en uno la
cuenta de su palabra en Fenwick.

Las cuentas de prefijo siempre coinciden con las cantidades de etiquetas
restantes. Buscar primero la palabra y después el bit devuelve exactamente
el rango requerido. La recurrencia del rango representa el conteo circular,
por lo que cada eliminación y cada término del XOR son correctos.

Para W = ⌈N/64⌉, cada eliminación cuesta `O(1 + log W)` y el tiempo
total es `O(N(1 + log W))`, también acotado por `O(N log N)`. La memoria
es `O(W)` palabras de máquina. No se guarda la secuencia completa
de eliminaciones.

En el ejemplo se eliminan 3, 1, 5, 2, 4. Las diferencias absolutas
son 2, 1, 2, 2, 1, cuyo XOR es 2.

Trampas:

- K cuenta solo etiquetas presentes e incluye la etiqueta inicial;
- los rangos empiezan en 0, pero las etiquetas y los pasos empiezan en 1;
- no incrementar r tras borrar: se saltaría la sucesora;
- borrar los bits no usados de la última palabra;
- usar máscaras sin signo de 64 bits y evitar desplazar 64 en una palabra completa;
- no guardar innecesariamente un árbol por etiqueta ni toda la permutación.

## Notas por lenguaje

El enunciado solo admite C, C++ y Pascal, pero el formulario de envío de
Timus ofrece además Rust 1.75, así que hay soluciones en C++ y Rust; Go,
Python y Java no se pueden enviar. Ambas guardan unas 17 000 palabras y
contadores, muy por debajo de 6 MB.

Las respuestas coinciden con una simulación directa de las eliminaciones
en 1625 casos, incluidos el mayor N y tamaños en los límites de palabra.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1896_fenwick_bitmask.cpp](1896_fenwick_bitmask.cpp) | G++ 13.2 x64 | fenwick, bitmask | O(N log N) | AC | 0.156 s | 628 KB |
| [1896_fenwick_bitmask.rs](1896_fenwick_bitmask.rs) | Rust 1.75 x64 | fenwick, bitmask | O(N log N) | AC | 0.187 s | 364 KB |
