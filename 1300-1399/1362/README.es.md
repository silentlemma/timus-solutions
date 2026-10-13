# 1362. Compañeros de clase 2

[Timus 1362](https://acm.timus.ru/problem.aspx?space=1&num=1362) · dificultad 443 · dp

Problema original de Evgeny Krokhalev, del Noveno Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 19–24 de abril de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una agencia de N ≤ 100 000 empleados es un árbol: todos salvo el
director tienen exactamente un jefe. Tanya tiene una noticia, y quien
la conoce puede llamar a su jefe o a uno de sus subordinados directos;
una llamada dura un minuto, y cada persona hace una sola llamada a la
vez. Hay que imprimir el menor número de minutos hasta que toda la
agencia lo sepa. Es la versión en árbol de
[1323](../1323/README.es.md).

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

N, luego N líneas: la línea K enumera los subordinados del empleado K y
termina en 0. La última línea tiene el número de Tanya.

## Salida

El menor número de minutos.

## Ejemplos

### Ejemplo 1

Entrada:

```
10
2 3 0
4 5 7 0
6 9 0
0
0
8 10 0
0
0
0
0
2
```

Salida:

```
5
```

## Solución

Las llamadas van hacia arriba y hacia abajo, así que el jefe es un
vecino más. Se enraíza el árbol en Tanya; entonces la noticia entra en
cada subárbol una sola vez, por su raíz.

Sea time(v) los minutos que v necesita para avisar a todo su subárbol
tras conocer la noticia. Si v llama a sus hijos en cierto orden, el
hijo i-ésimo se entera en el minuto i y termina en i + time(hijo). El
mejor orden llama primero al subárbol más lento: se ordenan los tiempos
de los hijos de mayor a menor t₁ ≥ t₂ ≥ …, y time(v) = max(tᵢ + i).
Intercambiar dos vecinos que no siguen este orden nunca ayuda, lo que
lo demuestra.

El árbol se recorre en anchura y los tiempos se calculan desde las
hojas hacia arriba, así que ni una cadena de 100 000 necesita
recursión. `O(N log N)`.

Detalles a tener en cuenta:

- el director no es la raíz: si Tanya es subordinada, la noticia sube y
  luego baja por otras ramas (pruebas 03 y 04);
- una cadena de 100 000 es demasiado profunda para la recursión en la
  mayoría de los lenguajes (prueba generada 2);
- una estrella de 100 000 necesita 99 999 minutos, una llamada cada vez
  (prueba generada 3).

Las respuestas se compararon con una búsqueda sobre todas las formas de
llamar, minuto a minuto, en 400 árboles aleatorios de hasta 8
empleados.

## Notas por lenguaje

- Java guarda el árbol en arreglos planos y lee la entrada byte a byte;
  Go también la lee byte a byte.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1362_dp.cpp](1362_dp.cpp) | G++ 13.2 x64 | dp | O(N log N) | AC | 0.171 s | 8896 KB |
| [1362_dp.go](1362_dp.go) | Go 1.14 x64 | dp | O(N log N) | AC | 0.093 s | 17784 KB |
| [1362_dp.java](1362_dp.java) | Java 1.8 | dp | O(N log N) | AC | 0.093 s | 6848 KB |
| [1362_dp.py](1362_dp.py) | Python 3.12 x64 | dp | O(N log N) | AC | 0.468 s | 33988 KB |
| [1362_dp.rs](1362_dp.rs) | Rust 1.75 x64 | dp | O(N log N) | AC | 0.031 s | 15320 KB |
