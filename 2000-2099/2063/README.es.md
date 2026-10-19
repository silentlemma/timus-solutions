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
partida, 166 650 líneas en total para n = 2, …, 100, dentro del límite.

Ahora la fila son algunas bolas blancas seguidas de algunas negras. Dos
vecinas (j, j + 1) difieren solo en la única frontera entre colores, y
si la fila es de un solo color no hay frontera. Una afirmación sobre un
par de vecinas elegido uniformemente al azar pierde con probabilidad a
lo sumo 1 / (n − 1), se hayan construido como se hayan construido las
pruebas. En 99 partidas el número esperado de derrotas es a lo sumo
1/1 + 1/2 + … + 1/99 ≈ 5.2, y perder 20 o más ocurre con probabilidad
de unos 2.6·10⁻⁹.

Una elección fija, como afirmar siempre (1, 2), perdería todas las
partidas de una prueba en la que cada fila tiene una sola bola blanca,
así que la elección debe ser aleatoria. Los programas usan el generador
splitmix64 con semilla igual al hash FNV-1a de toda la entrada: la
entrada cambia entre pruebas pero está fijada de antemano, y las filas
codificadas nunca se descifran.

El ejemplo solo muestra el formato: en la primera partida la afirmación
(2, 1) es errónea y en la segunda es correcta.

## Notas por lenguaje

El hash y el generador usan aritmética de 64 bits sin signo:
multiplicaciones con desbordamiento en Rust y resto sin signo en Java.
Todos los programas construyen la salida en un solo búfer.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2063_constructive.cpp](2063_constructive.cpp) | G++ 13.2 x64 | constructive | O(n^2) | AC | 0.062 s | 3104 KB |
| [2063_constructive.go](2063_constructive.go) | Go 1.14 x64 | constructive | O(n^2) | AC | 0.046 s | 980 KB |
| [2063_constructive.java](2063_constructive.java) | Java 1.8 | constructive | O(n^2) | AC | 0.156 s | 10052 KB |
| [2063_constructive.py](2063_constructive.py) | Python 3.12 x64 | constructive | O(n^2) | AC | 0.125 s | 8008 KB |
| [2063_constructive.rs](2063_constructive.rs) | Rust 1.75 x64 | constructive | O(n^2) | AC | 0.031 s | 3212 KB |
