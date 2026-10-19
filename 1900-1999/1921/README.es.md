# 1921. Una cuadrícula con racha recta máxima exacta

[Timus 1921](https://acm.timus.ru/problem.aspx?space=1&num=1921) · difficulty 1264 · constructive

Problema original de Grigoriy Nazarov, del concurso escolar regional de los Urales de 2012.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Llenar una cuadrícula n×m usando solo las primeras k letras latinas
mayúsculas. Deben aparecer l−1 letras iguales consecutivas en alguna
fila, columna o diagonal, pero nunca l en ninguna de esas direcciones.
Las diagonales incluyen ambas pendientes, con pasos unitarios en ambas
coordenadas. La racha recta máxima debe ser exactamente l−1.
No es obligatorio utilizar todas las letras disponibles.
Límites: 2 segundos, 64 MB.

## Entrada

Cuatro enteros n,m,k,l con 1≤n,m≤100, 1≤k≤26 y 2≤l≤100.

## Salida

Si no existe un relleno, imprimir `NO`. En otro caso imprimir `YES`,
seguido de n filas de m letras. Cualquier cuadrícula que cumpla ambas
condiciones es válida.

## Evaluación

Un comprobador propio valida cabecera, dimensiones, alfabeto y longitud
máxima de rachas iguales en las cuatro direcciones no orientadas.
El máximo debe ser exactamente l−1, no solo menor que l.
Rechaza un `NO` falso mediante el criterio completo demostrado abajo.
No compara el resultado con una disposición canónica.

## Ejemplos

```
3 4 4 2
```

```
YES
ABCB
CDAD
ABCB
```

```
2 2 1 2
```

```
NO
```

## Solución

Sea q=l−1 y d=max(n,m). Si d<q, ninguna fila, columna ni diagonal
alcanza la longitud necesaria, por lo que es imposible.

Si k=1, toda la cuadrícula es A y su racha máxima vale d.
Este caso es factible exactamente cuando d=q.

Si q=1, cualesquiera dos celdas vecinas por lado o diagonal deben
diferir. Las cuatro celdas de un cuadrado 2×2 son mutuamente vecinas
y necesitan cuatro letras. Una fila o columna no trivial necesita dos;
una sola celda necesita una. La cantidad exacta es min(n,2)·min(m,2).
Para índices desde cero r,c, asignamos

```text
(r mod 2) · min(m,2) + (c mod 2).
```

Así una sola columna usa A y B, no A y C. Los pares de paridad de
celdas vecinas difieren, demostrando suficiencia si hay letras suficientes.

En el caso restante q≥2,k≥2, bastan dos letras siempre que d≥q.
Si m≥q, el índice de letra es

```text
(r + floor(c/q)) mod 2.
```

Cada fila tiene bloques constantes alternados de longitud q, salvo
el último posiblemente más corto. Hay un bloque completo, de modo que
aparece la racha requerida. Los vecinos verticales siempre difieren.

En ambas pendientes diagonales, la paridad de fila cambia en cada paso.
La paridad de bloque cambia solo al cruzar una frontera. Dos vecinos
diagonales pueden ser iguales únicamente en ese cruce. Las fronteras
están separadas q pasos, con q≥2: no hay dos pasos de igualdad consecutivos.
Por tanto, las rachas diagonales miden como máximo 2≤q y el máximo
global es exactamente q.

Si m<q, entonces n≥q; transponemos a (c+floor(r/q)) mod 2.
Intercambiar filas y columnas conserva ambas diagonales. Esto cubre
todos los casos factibles restantes y prueba que cada rechazo es necesario.

O(nm) tiempo y espacio, incluida la cuadrícula y salida almacenadas.
Un caso imposible se reconoce en O(1).

Un tablero de ajedrez tiene diagonales monocromas largas y no sirve
en general. Revisar ambas pendientes. Evitar longitud l no garantiza
la existencia de l−1. Tratar por separado k=1 y l=2. Transponer cuando
solo el número de filas alcanza q. No exigir que aparezcan las k letras,
ni emitir C en una columna única con k=2.

## Notas por lenguaje

Solo hacen falta división entera pequeña, paridad y aritmética de letras.
Todas las fórmulas usan índices desde cero y letras desde A.
Go 1.14 calcula mínimos y máximos explícitamente; las demás versiones
nativas usan operaciones estándar. Se almacenan filas o salida;
no se necesita búsqueda ni recursión.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1921_constructive.cpp](1921_constructive.cpp) | G++ 13.2 x64 | constructive | O(n*m) | AC | 0.015 s | 408 KB |
| [1921_constructive.go](1921_constructive.go) | Go 1.14 x64 | constructive | O(n*m) | AC | 0.031 s | 1104 KB |
| [1921_constructive.java](1921_constructive.java) | Java 1.8 | constructive | O(n*m) | AC | 0.109 s | 516 KB |
| [1921_constructive.py](1921_constructive.py) | Python 3.12 x64 | constructive | O(n*m) | AC | 0.093 s | 584 KB |
| [1921_constructive.rs](1921_constructive.rs) | Rust 1.75 x64 | constructive | O(n*m) | AC | 0.015 s | 240 KB |
