# 2091. Dos asignaturas que reparten los planes de forma más pareja

[Timus 2091](https://acm.timus.ru/problem.aspx?space=1&num=2091) · dificultad 271 · bruteforce

Problema original de Dmitry Ivankov, del Concurso Individual Abierto de la UrFU 2014.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una tabla n × m dice cuáles de m asignaturas incluye cada uno de n
planes de estudio. Elegir dos asignaturas distintas A y B; reparten los
planes en cuatro grupos: con ambas, solo con A, solo con B y con
ninguna. Hacer el grupo mayor lo más pequeño posible e imprimir su
tamaño y las dos asignaturas. Se acepta cualquier pareja óptima. Los
límites son 1 segundo y 64 MB.

## Entrada

n y m, 4 ≤ n, m ≤ 100, y después las n filas de m ceros y unos.

## Salida

El menor tamaño posible del grupo mayor y después las dos asignaturas.

## Evaluación

Un comprobador compara el tamaño y recuenta los grupos de la pareja
impresa.

## Ejemplos

### Ejemplo 1

Entrada:

```
6 4
0 0 0 1
0 0 1 0
0 1 1 1
1 1 1 1
0 0 0 0
1 0 0 1
```

Salida:

```
2
1 3
```

## Solución

Hay menos de 5000 parejas de asignaturas, y los grupos de una pareja se
cuentan en una pasada por los planes, con número de grupo 2·[A] + [B].
Probar todas las parejas cuesta O(m² n), medio millón de pasos.

En el ejemplo las asignaturas 1 y 3 dan los grupos {4}, {6}, {2, 3} y
{1, 5}, así que el mayor tiene 2 planes.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2091_bruteforce.cpp](2091_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(m^2 n) | AC | 0.015 s | 252 KB |
| [2091_bruteforce.go](2091_bruteforce.go) | Go 1.14 x64 | bruteforce | O(m^2 n) | AC | 0.031 s | 1200 KB |
| [2091_bruteforce.java](2091_bruteforce.java) | Java 1.8 | bruteforce | O(m^2 n) | AC | 0.140 s | 5712 KB |
| [2091_bruteforce.py](2091_bruteforce.py) | Python 3.12 x64 | bruteforce | O(m^2 n) | AC | 0.140 s | 776 KB |
| [2091_bruteforce.rs](2091_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(m^2 n) | AC | 0.015 s | 436 KB |
