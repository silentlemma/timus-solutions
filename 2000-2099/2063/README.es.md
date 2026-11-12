# 2063. Colores iguales sin mirar

[Timus 2063](https://acm.timus.ru/problem.aspx?space=1&num=2063) · dificultad 432 · constructive

Problema original de Alexey Danilyuk, del Concurso Regional Escolar de Programación de los Urales 2015.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una fila tiene n bolas, negras o blancas, en un orden desconocido. La
consulta `? v u` intercambia las bolas de las posiciones v y u si en v
hay una negra y en u una blanca, y no hace nada en otro caso; el
programa nunca sabe qué pasó. Tras cualquier número de consultas hace
una afirmación `! v u`: dos posiciones que ahora tienen bolas del mismo
color.

Una prueba consta de varias partidas; en la i-ésima n = i + 1. Todas
las pruebas salvo la primera tienen 99 partidas, n = 2, …, 100, y hay
que ganar al menos 80; las pruebas están fijadas de antemano y no se
adaptan al programa. La primera prueba es el ejemplo y solo se comprueba
su formato. Se pueden imprimir como mucho 500 000 líneas por prueba. Los
límites son 1 segundo y 64 MB.

## Entrada

El número de partidas m (99 en todas las pruebas salvo la primera) y
después las filas iniciales codificadas, que el programa no debe
intentar leer.

## Salida

m descripciones de partidas, cada una con líneas `? v u` seguidas de una
línea `! v u`, con 1 ≤ v, u ≤ n y v ≠ u.

## Evaluación

Un comprobador juega cada partida. Con 99 partidas al menos 80
afirmaciones deben ser correctas; en el ejemplo solo se comprueba el
formato.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
01
101
```

Salida:

```
? 1 2
? 2 1
? 1 2
! 2 1
? 1 2
? 3 1
! 1 2
```

## Solución

Ordenar las bolas a ciegas. Una consulta entre vecinas `? i i+1` mueve
una bola blanca a la izquierda de una negra, así que las consultas de la
ordenación de burbuja —para cada extremo de n − 1 a 1, los pares
(1, 2), (2, 3), …, (end, end + 1)— dejan todas las blancas antes que
todas las negras sea cual sea la fila. Son n (n − 1) / 2 consultas por
partida, 166 650 consultas en total para n = 2, …, 100. Con las 99
afirmaciones se imprimen 166 749 líneas, dentro del límite.

Ahora la fila son algunas bolas blancas seguidas de algunas negras. Dos
vecinas (j, j + 1) difieren solo en la única frontera entre colores, y
si la fila es de un solo color no hay frontera. Una afirmación sobre un
par de vecinas elegido uniformemente al azar pierde con probabilidad a
lo sumo 1 / (n − 1) para cualquier fila fija. Con elecciones independientes
y uniformes en las 99 partidas, el número esperado de derrotas es a lo sumo
1/1 + 1/2 + … + 1/99 ≈ 5.2, y perder 20 o más ocurre con probabilidad
de como mucho unos 2.6·10⁻⁹.

Una trampa es afirmar siempre (1, 2): pierde todas las partidas de la
prueba gen9, que pone una sola bola blanca al principio. Afirmar siempre
(n − 1, n) falla de modo similar en gen10. Los programas varían el par
con el generador splitmix64 y usan como semilla el hash FNV-1a de toda la
entrada; las filas codificadas nunca se descifran. Para una entrada fija,
el resultado es determinista. Esta semilla no establece elecciones
independientes y uniformes, así que la cota anterior describe un modelo
aleatorio ideal y no es una garantía para estos programas.

La prueba 01 solo comprueba el formato, pero el comando debe ser
exactamente `?` o `!`; se debe rechazar el comando inválido `?!`.

El ejemplo solo muestra el formato: en la primera partida la afirmación
(2, 1) es errónea y en la segunda es correcta.

## Soluciones optimizadas

C++, Go y Rust sustituyen burbuja por la [red odd-even merge de Batcher](https://doi.org/10.1145/1468075.1468121). Se completa a la siguiente potencia de dos con bolas negras virtuales y se omiten comparaciones cuyo extremo derecho sea virtual. Cada comparador va del índice menor al mayor: ningún valor real cambia el relleno negro de su derecha. La parte real queda ordenada como en la red completa. Se fusionan recursivamente subsecuencias pares e impares y luego se comparan pares intermedios adyacentes: O(n log² n) comandos por juego. Se mantienen la semilla FNV de todos los bytes originales y una elección splitmix64 por juego. El orden final y la pareja declarada coinciden con la base, conservando el resultado de cada entrada fija; el hash no implica aleatoriedad independiente. Go calcula el hash por bloques y formatea comandos en un búfer fijo sin asignar cadenas por comando; C++ y Rust acumulan el texto reducido. Se conservan las burbujas; Java y Python reutilizan bases admitidas.

El envío aceptado en Rust 1.75 x64 tarda 0.046 s frente a 0.031 s de la base y usa 1 124 KB frente a 3212 KB.

Las implementaciones base aceptadas [2063_constructive.java](2063_constructive.java), [2063_constructive.py](2063_constructive.py) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Notas por lenguaje

Estas notas describen las implementaciones sencillas.

El hash y el generador usan aritmética de 64 bits sin signo:
multiplicaciones con desbordamiento en Rust y resto sin signo en Java.
Go escribe la salida de forma incremental mediante un búfer; los demás
programas la acumulan antes de escribirla.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [2063_constructive.cpp](2063_constructive.cpp) | G++ 13.2 x64 | constructive | O(n^2) | AC | 0.062 s | 3104 KB | 11294258 |
| [2063_constructive.go](2063_constructive.go) | Go 1.14 x64 | constructive | O(n^2) | AC | 0.046 s | 980 KB | 11294278 |
| [2063_constructive.java](2063_constructive.java) \* | Java 1.8 | constructive | O(n^2) | AC | 0.156 s | 10052 KB | 11294310 |
| [2063_constructive.py](2063_constructive.py) \* | Python 3.12 x64 | constructive | O(n^2) | AC | 0.125 s | 8008 KB | 11294295 |
| [2063_constructive.rs](2063_constructive.rs) | Rust 1.75 x64 | constructive | O(n^2) | AC | 0.031 s | 3212 KB | 11294312 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [2063_constructive_sorting.cpp](2063_constructive_sorting.cpp) \* | G++ 13.2 x64 | constructive, sorting | O(n log² n) | AC | 0.031 s | 1220 KB | 11315021 |
| [2063_constructive_sorting.rs](2063_constructive_sorting.rs) \* | Rust 1.75 x64 | constructive, sorting | O(n log² n) | AC | 0.046 s | 1124 KB | 11315037 |
| [2063_constructive_sorting.go](2063_constructive_sorting.go) \* | Go 1.14 x64 | constructive, sorting | O(n log² n) | AC | 0.031 s | 300 KB | 11315319 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
