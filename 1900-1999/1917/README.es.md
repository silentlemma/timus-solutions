# 1917. Eliminación segura de grupos por umbral

[Timus 1917](https://acm.timus.ru/problem.aspx?space=1&num=1917) · difficulty 242 · greedy

Problema original de Denis Dublennykh, de la subregión oriental del NEERC 2012.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada moneda tiene un umbral positivo. Un hechizo de fuerza s elimina
todas las monedas restantes con umbral≤s y libera energía s por la
cantidad recién eliminada. Cada hechizo debe liberar como máximo p.
Maximizar monedas eliminadas y, después, minimizar hechizos para ese máximo.
Límites: 1 segundo, 64 MB.

## Entrada

n,p con 1≤n≤1000 y 1≤p≤1 000 000 000, seguidos por n umbrales
1≤aᵢ≤1 000 000 en cualquier orden.

## Salida

Máxima cantidad eliminable y mínimo número de hechizos. Si no se puede
eliminar ninguna moneda, escribir `0 0`.

## Evaluación

Comparación exacta de los dos tokens enteros, en ese orden.

## Ejemplos

```
5 4
4 1 4 1 2
```

```
3 2
```

## Solución

Ordenar y agrupar umbrales iguales. Un grupo de c monedas con umbral t
no puede dividirse: un hechizo débil no elimina ninguna, y el primero
con fuerza≥t elimina todas simultáneamente.

Si ct>p, ese grupo no se puede eliminar ni solo. Mayor fuerza o más
monedas empeoran la energía. También bloquea todos los umbrales superiores,
pues cualquier hechizo que los elimine incluiría este grupo. El máximo
es el prefijo anterior al primer grupo así; cada grupo previo puede
eliminarse individualmente, por lo que se alcanza ese límite.

Dividir el prefijo factible de forma voraz. Mantener active monedas
en el lote actual; añadir el siguiente grupo entero si (active+c)t≤p.
Si no cabe, cerrar el lote previo no vacío y comenzar con el nuevo grupo.
Cerrar el lote final si queda alguno. La fuerza mínima de cada lote
es su umbral máximo. Comprobar ct>p antes de iniciar un lote y no contar vacíos.

### Optimalidad del lote más largo

Al añadir grupos no disminuyen ni cantidad ni umbral máximo. El primer
lote voraz es el mayor prefijo factible. Sustituir el primer lote de
cualquier partición óptima por él, borrar de los lotes posteriores las
monedas adicionales eliminadas y descartar lotes vacíos. Ningún lote
restante aumenta su cantidad ni umbral, así que sigue siendo seguro.
El número de hechizos no crece. Repetir el intercambio sobre los grupos
restantes demuestra el mínimo global.

Tiempo `O(n log n)` por ordenar, recorrido posterior lineal; memoria `O(n)`
incluida la entrada y copia ordenada.

En el ejemplo se eliminan dos unos con fuerza 1 y el dos con fuerza 2.
Los dos cuatros producirían energía 8>4. Se consiguen tres monedas en dos hechizos.

No dividir umbrales iguales ni saltar un grupo inferior inseguro.
La energía permite igualdad; contar todas las monedas destruidas a la vez.
Reiniciar solo tras contabilizar el lote previo no vacío. Un grupo inseguro
posterior no invalida el lote pendiente. Primero maximizar monedas, luego minimizar hechizos.

## Notas por lenguaje

Python usa `groupby`; los otros puertos recorren tramos iguales. Los productos
nativos usan 64 bits. El máximo dado es 1000·1 000 000=10⁹, pero ampliar
explícitamente aclara la multiplicación. Java y Go usan entrada almacenada
en búfer. Solo se imprimen los dos contadores solicitados.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1917_greedy.cpp](1917_greedy.cpp) | G++ 13.2 x64 | greedy | O(n log n) | AC | 0.015 s | 416 KB |
| [1917_greedy.go](1917_greedy.go) | Go 1.14 x64 | greedy | O(n log n) | AC | 0.031 s | 1112 KB |
| [1917_greedy.java](1917_greedy.java) | Java 1.8 | greedy | O(n log n) | AC | 0.125 s | 648 KB |
| [1917_greedy.py](1917_greedy.py) | Python 3.12 x64 | greedy | O(n log n) | AC | 0.078 s | 572 KB |
| [1917_greedy.rs](1917_greedy.rs) | Rust 1.75 x64 | greedy | O(n log n) | AC | 0.031 s | 240 KB |
