# 2005. La ruta permitida más corta entre cinco paradas

[Timus 2005](https://acm.timus.ru/problem.aspx?space=1&num=2005) · dificultad 94 · bruteforce

Problema original de Mikhail Rubinchik. (Prepared by Oleg Merkurev), del Concurso Regional Escolar de Programación de los Urales 2013.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Visitar cinco lugares exactamente una vez, empezando en 1 y terminando
en 5. El lugar 3 no puede ser la penúltima parada. Dadas todas las
distancias, hallar una ruta permitida de distancia total mínima y su
longitud. Se admite cualquier óptimo.

## Entrada

Una matriz entera de distancias de 5 por 5. Sus valores están entre 0 y
10000, la diagonal es cero, la matriz es simétrica y satisface la
desigualdad triangular `d[i][j]≤d[i][k]+d[k][j]`. Tiempo 0,5 segundos,
memoria 64 MB.

## Salida

En la primera línea, la distancia total mínima. En la segunda, los cinco
números de lugar en orden de visita, separados por espacios. Los empates
pueden resolverse libremente.

## Evaluación

Un comprobador verifica que la ruta está permitida, que la longitud
impresa es la suya y que es óptima; se acepta cualquier ruta óptima.

## Ejemplos

```
0 2600 3800 2600 2500
2600 0 5300 3900 4400
3800 5300 0 1900 4500
2600 3900 1900 0 3700
2500 4400 4500 3700 0
```

```
13500
1 2 3 4 5
```

La ruta mostrada cuesta `2600+5300+1900+3700=13500`; su penúltima parada
es 4, por lo que cumple la restricción.

## Solución

Solo cambia el orden de 2, 3 y 4. De sus seis permutaciones, dos
terminan en 3 y están prohibidas. Quedan `1,2,3,4,5`, `1,3,2,4,5`,
`1,3,4,2,5` y `1,4,3,2,5`. Sumamos las cuatro distancias consecutivas de
cada candidata y conservamos una mínima con su coste.

Los programas enumeran el primer y último lugar intermedio, distintos
entre sí y sin permitir 3 como último. El intermedio central es el
restante. Internamente sus índices desde cero son 1, 2 y 3, cuya suma es
6; restar los extremos elegidos recupera el índice central. Así se
considera cada permutación válida exactamente una vez y ninguna
prohibida. Toda respuesta posible está entre las cuatro candidatas, por
lo que elegir su mínimo prueba optimalidad. Guardar coste y ruta juntos
garantiza que la ruta impresa tenga la longitud declarada.

Tiempo `O(1)` y memoria `O(1)`: siempre hay cinco lugares, cuatro
candidatas y cuatro aristas por candidata. La suma no supera 40000, de
modo que bastan enteros con signo de 32 bits. Las distancias métricas
dadas no necesitan preprocesamiento de caminos mínimos.

La restricción se refiere a la penúltima parada, no a la segunda o
tercera. Mantener 1 al inicio y 5 al final. Las distancias cero y los
empates son legales. Inicializar el mejor coste permitiendo que gane
cero; 10000 no limita la ruta completa. Convertir índices internos a
números 1..5 al imprimir.

## Notas por lenguaje

Los cinco lenguajes evalúan las mismas cuatro candidatas y leen las 25
entradas. Se usan arreglos fijos cuando resulta práctico y listas
pequeñas en Python. La ruta guardada no se modifica al considerar
candidatas posteriores.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2005_bruteforce.cpp](2005_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(1) | AC | 0.031 s | 432 KB |
| [2005_bruteforce.go](2005_bruteforce.go) | Go 1.14 x64 | bruteforce | O(1) | AC | 0.031 s | 1108 KB |
| [2005_bruteforce.java](2005_bruteforce.java) | Java 1.8 | bruteforce | O(1) | AC | 0.125 s | 432 KB |
| [2005_bruteforce.py](2005_bruteforce.py) | Python 3.12 x64 | bruteforce | O(1) | AC | 0.093 s | 508 KB |
| [2005_bruteforce.rs](2005_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(1) | AC | 0.031 s | 224 KB |
