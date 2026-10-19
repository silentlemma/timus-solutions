# 1923. Dos regiones que se expanden por colores alternadamente

[Timus 1923](https://acm.timus.ru/problem.aspx?space=1&num=1923) · difficulty 546 · bfs

Problema original de folclore, preparado por Dmitry Karpenko; concurso escolar regional de los Urales de 2012.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una cuadrícula n×m tiene colores 0..9. Celdas del mismo color conectadas
por lados forman un país. El primer bando posee inicialmente el país
completo de la esquina inferior izquierda; el segundo, el de la superior
derecha. Sus colores iniciales difieren. Alternan turnos, empezando el
primero. En un turno cambian al color indicado, conservan el territorio
y anexan países vecinos de ese color. Nunca eligen su color actual ni
el actual del rival. Dada una secuencia legal, calcular ambas áreas finales.
Cada celda tiene área uno. Límites: 1 segundo, 64 MB.

## Entrada

n,m con 2≤n,m≤50 y luego n cadenas de m dígitos. Después l, 2≤l≤100,
seguido de exactamente l colores 0..9 en orden cronológico.
Los números pueden separarse por cualquier espacio en blanco.

## Salida

Área del primer bando en la primera línea y del segundo en la segunda,
en orden de los países iniciales inferior izquierdo y superior derecho.

## Evaluación

Comparación exacta de los dos tokens enteros, en ese orden.

## Ejemplos

```
6 12
000233434133
000233434143
001223434133
101023434143
101223434133
110233434143
4
0 4 2 1
```

```
23
18
```

## Solución

Guardamos un propietario por celda: neutral, primer bando o segundo.
Cada bando conserva una lista de sus celdas. Precalculamos los cuatro
vecinos válidos por lado. El color original de una celda neutral no cambia;
una vez ocupada, su color original deja de determinar la propiedad.

Marcamos ambos puntos iniciales y expandimos cada uno por celdas
neutrales de su color inicial. Así se posee el país completo desde
el principio, no solo una esquina.

Al elegir c, recorremos todas las celdas del territorio activo como cola.
Si un vecino es neutral y tiene color original c, marcamos su propietario
antes de añadirlo a la misma cola. Procesamos los nuevos elementos en
ese mismo turno para anexar países completos, no solo sus fronteras.
Todos los elementos anteriores permanecen pese a cambios posteriores.

No hace falta repintar los dígitos almacenados ni guardar las alianzas
actuales: las elecciones ya son legales. Los colores neutrales siguen
originales y la propiedad se decide exclusivamente con el arreglo.
Una celda rival siempre queda bloqueada, cualquiera que fuera su dígito inicial.

El invariante afirma que cada lista es exactamente el territorio conexo
de su bando. Se cumple tras las expansiones iniciales. Una celda añadida
es neutral, tiene el color elegido y toca territorio previo o recién añadido,
por lo que su país debe anexarse. Recíprocamente, la cola agota caminos
dentro de cada país vecino de ese color, sin omitir anexiones. Marcar antes
de añadir evita duplicados; comprobar propietario protege al rival.
No se elimina territorio anterior, conservando el invariante. Las longitudes
finales de las listas son las áreas pedidas.

Cada expansión recorre como máximo nm celdas y cuatro vecinos por celda.
Tiempo O((l+1)nm). Propietarios, vecinos y listas usan O(nm) espacio;
incluida la secuencia de turnos almacenada, el total es O(nm+l).

Usar las esquinas inferior izquierda y superior derecha. Capturar países
iniciales completos, conservar territorio anterior y procesar celdas nuevas
en el mismo turno. El contacto diagonal no cuenta y los vecinos horizontales
no deben saltar entre filas. El color original no puede anular propietario.
No añadir un turno ficticio si l es impar. Las secuencias de prueba deben
excluir ambos colores actuales.

## Notas por lenguaje

La celda (r,c) se codifica como r·m+c desde cero. C++, Go, Java y Rust
usan un cursor cuyo límite sigue el crecimiento de la lista. La iteración
de listas Python visita las celdas añadidas en la misma pasada.
Java usa dos arreglos planos de capacidad suficiente; las demás versiones,
listas o vectores dinámicos. Todos los recorridos son iterativos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1923_bfs.cpp](1923_bfs.cpp) | G++ 13.2 x64 | bfs | O(l*n*m) | AC | 0.015 s | 544 KB |
| [1923_bfs.go](1923_bfs.go) | Go 1.14 x64 | bfs | O(l*n*m) | AC | 0.015 s | 1404 KB |
| [1923_bfs.java](1923_bfs.java) | Java 1.8 | bfs | O(l*n*m) | AC | 0.109 s | 652 KB |
| [1923_bfs.py](1923_bfs.py) | Python 3.12 x64 | bfs | O(l*n*m) | AC | 0.078 s | 1308 KB |
| [1923_bfs.rs](1923_bfs.rs) | Rust 1.75 x64 | bfs | O(l*n*m) | AC | 0.062 s | 396 KB |
