# 1006. Reconstruir el orden de marcos cuadrados superpuestos

[Timus 1006](https://acm.timus.ru/problem.aspx?space=1&num=1006) · dificultad 988 · greedy

Problema original del Campeonato de la Universidad Estatal de los Urales 1997.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una pantalla de texto tiene 50 columnas y 20 filas y está llena de `.`
(byte 46). Un marco cuadrado con la esquina superior izquierda en la columna
`x`, fila `y` y lado `a` (`a ≥ 2`, el marco está dentro de la pantalla) se
dibuja escribiendo estos bytes en su borde; un marco posterior sobrescribe a
uno anterior:

| Celda | Byte (cp437) | Carácter |
|-------|--------------|----------|
| esquina superior izquierda | 218 | `┌` |
| esquina superior derecha | 191 | `┐` |
| esquina inferior izquierda | 192 | `└` |
| esquina inferior derecha | 217 | `┘` |
| demás celdas de los lados izquierdo y derecho | 179 | `│` |
| demás celdas de los lados superior e inferior | 196 | `─` |

La entrada es la pantalla después de dibujar `N` marcos (`1 ≤ N ≤ 15`).
Encuentra cualquier secuencia de como mucho 2000 marcos que, dibujados en orden
sobre una pantalla vacía, den exactamente esta imagen. No tiene que ser la
original.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

20 líneas de 50 bytes: las filas de la pantalla de arriba abajo, en la
codificación de un byte cp437 (no UTF-8). Una solución debe leer bytes crudos
y aceptar finales de línea LF y CRLF.

## Salida

El número `K` de marcos y luego `K` líneas `x y a`: columna y fila de la
esquina superior izquierda (contando desde 0) y el lado, en orden de dibujo.

## Evaluación

Se acepta cualquier respuesta válida. El verificador comprueba que
`0 ≤ K ≤ 2000`, que cada marco tiene `a ≥ 2` y está dentro de la pantalla, y
que dibujar los marcos en el orden dado sobre una pantalla vacía produce
exactamente la imagen de la entrada.

## Ejemplos

Las imágenes se muestran como caracteres; el programa las recibe como bytes cp437.

### Ejemplo 1

Entrada:

```
........................................┌────────┐
....................┌──────────┐........│........│
...┌───────┐........│..........│........│........│
...│.......│........│..........│........│........│
...│.......│........│..........│........│........│
...│......┌────┐....│..........│........│........│
...│......││...│....│..........│........│........│
...│......││...│....│..........│........│........│
...│......││...│....│..........│........│........│
...│......││...│....│......┌───┐........└────────┘
...└──────└────┘....│......│...│..................
....................│......│...│..................
....................└──────│───│...┌──────┐.......
...........................└───┘...│......│.......
...................................│......│.......
...................................│......│.......
...................................│......│.......
...................................│......│.......
...................................│......│.......
...................................└──────┘.......
```

Salida:

```
6
3 2 9
10 5 6
20 1 12
27 9 5
40 0 10
35 12 8
```

## Solución

Se deshace el dibujo desde el final. El último marco dibujado se ve entero. Al
quitarlo, sus celdas podían contener cualquier cosa antes de dibujarlo, así que
se vuelven *comodines*. En general, un marco **encaja** si cada celda de su
borde es un comodín o muestra exactamente el carácter que este marco pondría
ahí, y al menos una de esas celdas todavía no es comodín.

Se recorren repetidamente todas las esquinas y lados (`50 · 20` esquinas, hasta
19 lados cada una; primero se comprueban las cuatro esquinas del candidato, lo
que descarta a la mayoría de inmediato); cada marco que encaja se anota y su
borde se convierte en comodines. Se para cuando no queda ninguna celda distinta
de `.`. Se imprimen los marcos anotados en orden inverso.

Por qué funciona: dibujados en ese orden, cada marco anotado escribe caracteres
correctos en sus celdas no comodín, y sus celdas comodín quedan cubiertas por
marcos anotados antes, es decir, dibujados después. El proceso nunca se atasca:
entre los marcos originales que aún cubren una celda no comodín, tomemos el
dibujado en último lugar; cada celda suya que no muestra está cubierta por un
marco original posterior, cuyas celdas ya son todas comodines, así que este
marco encaja. Cada marco anotado convierte en comodín al menos una de las como
mucho 1000 celdas, por lo que `K ≤ 1000`.

Un recorrido examina unos `50 · 20 · 19` candidatos, casi todos descartados en
una esquina, y hacen falta pocos recorridos (cada uno quita al menos el marco
original superior de los que quedan), así que el tiempo es despreciable.

Detalles a tener en cuenta:

- la entrada no es UTF-8: lee bytes y trata los bytes ≥ 128 como sin signo;
- las celdas `.` nunca deben cubrirse: no son comodines;
- un marco formado solo por comodines no sirve y no se anota.

## Notas por lenguaje

El mismo recorrido en todos los lenguajes. Python descarta los candidatos cuya
celda superior izquierda no es `┌` ni comodín antes de construir la lista de
celdas del borde.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1006_greedy.cpp](1006_greedy.cpp) | G++ 13.2 x64 | greedy | O(K·W·H·S²) worst case, K scans | AC | 0.015 s | 160 KB |
| [1006_greedy.go](1006_greedy.go) | Go 1.14 x64 | greedy | O(K·W·H·S²) worst case, K scans | AC | 0.031 s | 1060 KB |
| [1006_greedy.java](1006_greedy.java) | Java 1.8 | greedy | O(K·W·H·S²) worst case, K scans | AC | 0.093 s | 564 KB |
| [1006_greedy.py](1006_greedy.py) | Python 3.12 x64 | greedy | O(K·W·H·S²) worst case, K scans | AC | 0.109 s | 1348 KB |
| [1006_greedy.rs](1006_greedy.rs) | Rust 1.75 x64 | greedy | O(K·W·H·S²) worst case, K scans | AC | 0.046 s | 224 KB |
