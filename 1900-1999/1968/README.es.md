# 1968. Reconstruir colores de una pirámide escalonada

[Timus 1968](https://acm.timus.ru/problem.aspx?space=1&num=1968) · difficulty 1640 · constructive

Problema original del Concurso Individual Abierto de la UrFU 2013.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una pirámide usa bloques de altura uno y base cuadrada 2×2. La capa
inferior ocupa m×n. Cada capa superior se desplaza una unidad hacia
dentro y tiene una fila y columna de bloques menos, hasta que alguna
dimensión de la cuadrícula queda en uno. Cada bloque es rojo o incoloro;
la vista superior indica cuántos bloques rojos cubren cada celda unitaria.

Recuperar los colores. Un bloque rojo no puede estar exactamente encima
de uno incoloro con la misma huella horizontal. Sí se permite solapamiento
parcial con bloques incoloros. Se garantiza una disposición válida.
Límites: 1 segundo, 64 MB.

## Entrada

m,n pares, 2≤m,n≤40; después m filas de n enteros no negativos con
las coberturas rojas. Los datos respetan geometría y restricción de colores.

## Salida

Capas de abajo hacia arriba, R para rojo y W para incoloro. La capa z,
numerada desde cero, tiene m/2−z filas de n/2−z caracteres. Separar
capas consecutivas con una línea vacía. Cualquier disposición válida sirve.

## Evaluación

Un comprobador verifica los tamaños de las capas, los símbolos, la vista
superior exacta y que ningún bloque rojo está justo encima de uno
incoloro con la misma base; se acepta cualquier coloración válida.

## Ejemplos

```
4 6
0 0 1 1 0 0
0 0 1 2 1 0
0 0 0 1 2 1
0 0 0 0 1 1
```

```
WRW
WWR

WR
```

## Solución

En el ejemplo los bloques rojos inferiores empiezan en (0,2) y (2,4),
con coordenadas unitarias desde cero; el superior rojo empieza en (1,3).
Sumar sus tres proyecciones 2×2 da la foto, con dos celdas de valor 2
por solapamiento. Resultan WRW/WWR abajo y WR arriba. El rojo superior
solapa parcialmente bloques incoloros, pero sus huellas no son iguales.

### Recuperar cantidades por huella

Sea F[x,y] la cantidad de bloques rojos, en cualquier nivel, cuya esquina
superior izquierda horizontal es (x,y). Cada uno cubre cuatro celdas.
La foto A satisface

A[i,j]=F[i,j]+F[i−1,j]+F[i,j−1]+F[i−1,j−1],

con valores exteriores cero. Recorrer filas de arriba abajo y columnas
de izquierda a derecha, calculando

F[i,j]=A[i,j]−F[i−1,j]−F[i,j−1]−F[i−1,j−1].

Los tres términos restados ya se conocen. El sistema triangular determina
de forma única cada multiplicidad roja. La validez de entrada garantiza
no negatividad, cero en posiciones imposibles y suficientes bloques
físicos para cada cantidad; no hace falta recortar valores.

### Rojo en la parte baja de cada cadena

El bloque (r,c) del nivel z tiene esquina (z+2r,z+2c). La misma huella
aparece dos niveles abajo en (r+1,c+1), no en la capa adyacente. Todas
sus apariciones forman una cadena vertical de niveles de igual paridad,
empezando en cero o uno.

La restricción obliga a colocar primero todos los rojos desde abajo,
seguidos por los incoloros. Con cantidad F[x,y], son rojos exactamente
los F[x,y] bloques más bajos. Debajo del nivel z hay floor(z/2) bloques
alineados; por tanto es rojo si F[z+2r,z+2c]>floor(z/2).

La construcción cumple la restricción y conserva la cantidad roja de
cada huella. Sumar sus proyecciones reproduce A por la ecuación original,
lo que demuestra corrección.

Sea B=Σ_z(m/2−z)(n/2−z) el número de bloques. Tiempo y espacio incluyendo
las capas devueltas son `O(mn+B)`; espacio adicional sin salida `O(mn)`.
Para la base máxima 40×40 hay B=2870.

“Exactamente encima” significa la misma huella 2×2. Exigir rojos todos
los bloques inferiores parcialmente solapados rechazaría el ejemplo.
Las huellas se repiten cada dos niveles. En la inversión se restan los
tres términos, también el diagonal. El desplazamiento por capa es uno,
pero el paso entre bloques es dos. Mantener líneas vacías y terminar
cuando alguna dimensión de la cuadrícula de bloques llegue a uno.

## Notas por lenguaje

Bastan enteros ordinarios con signo: la foto no supera veinte y la
multiplicidad roja por huella diez. Cada versión guarda la matriz de
cantidades y forma cadenas por capa. Python 3.12, C++ con G++ 13.2,
Go 1.14, Java 8 y Rust 1.75 usan solo biblioteca estándar, sin recursión.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1968_constructive.cpp](1968_constructive.cpp) | G++ 13.2 x64 | constructive | O(m*n+B) | AC | 0.031 s | 424 KB |
| [1968_constructive.go](1968_constructive.go) | Go 1.14 x64 | constructive | O(m*n+B) | AC | 0.031 s | 1144 KB |
| [1968_constructive.java](1968_constructive.java) | Java 1.8 | constructive | O(m*n+B) | AC | 0.125 s | 2904 KB |
| [1968_constructive.py](1968_constructive.py) | Python 3.12 x64 | constructive | O(m*n+B) | AC | 0.078 s | 600 KB |
| [1968_constructive.rs](1968_constructive.rs) | Rust 1.75 x64 | constructive | O(m*n+B) | AC | 0.015 s | 268 KB |
