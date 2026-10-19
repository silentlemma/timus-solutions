# 1852. Cubo en un cubo en un cubo

[Timus 1852](https://acm.timus.ru/problem.aspx?space=1&num=1852) · dificultad 2437 · simulation

Problema original de Grigoriy Nazarov, del Ural SU Team.GOV Contest en la sesión de verano de Petrozavodsk, agosto de 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Vadik hizo una secuencia de giros de caras en un cubo de Rubik con un dibujo.
Repitiendo la misma secuencia una y otra vez, se recupera ese dibujo.
¿Cuántas veces más hay que aplicar la secuencia para recuperar el
dibujo original?

## Entrada

Una línea de como mucho 10⁵ letras U, D, L, R, F y B, para las caras
superior, inferior, izquierda, derecha, delantera y trasera: una letra
minúscula gira esa cara 90° en sentido horario, una mayúscula 90° en
sentido antihorario.

## Salida

El número de repeticiones que faltan.

## Ejemplos

### Ejemplo 1

Entrada:

```
Ud
```

Salida:

```
3
```

### Ejemplo 2

Entrada:

```
RRRR
```

Salida:

```
0
```

## Solución

La secuencia mueve las 54 pegatinas según una permutación fija, y
repetirla k veces restaura el cubo exactamente cuando k es múltiplo del
orden de esa permutación, el mínimo común múltiplo de las longitudes de
sus ciclos. La respuesta es el orden menos 1, porque la secuencia ya se
aplicó una vez.

Una pegatina se describe por la posición de su cubito, con coordenadas
en {−1, 0, 1}, y la normal exterior de su cara. Girar la cara de normal
exterior a mueve las pegatinas cuya posición p cumple p·a = 1: tanto p
como la normal giran un cuarto de vuelta alrededor de a. Visto desde
fuera de la cara, el giro antihorario es v → a × v + a(a·v) y el horario
lo mismo con −a × v. Así cada una de las doce letras se convierte en una
tabla de adónde va cada pegatina, y la secuencia se pliega en una sola
permutación con 54 consultas por letra (en Python, un `bytes.translate`
por letra). `O(54·|s|)`.

En el primer ejemplo, U antihorario visto desde arriba y d horario visto
desde abajo hacen girar ambas capas exteriores en el mismo sentido
alrededor del eje vertical, así que el dibujo vuelve tras cuatro
secuencias: faltan tres. En el segundo ejemplo cuatro cuartos de vuelta
de R ya restauran el cubo.

Trampas:

- el sentido horario se mira desde fuera de cada cara, así que la cara
  inferior gira al revés que la superior con la misma clase de letra;
- la secuencia ya se aplicó una vez, de ahí el menos uno;
- el orden es pequeño (como mucho 1260 en un cubo), pero las longitudes
  de los ciclos se combinan con el mcm, no multiplicándolas.

Las respuestas coinciden con una implementación aceptada independiente
en trescientas secuencias aleatorias y en órdenes conocidos, como 105
para dos giros horarios de caras vecinas y 6 para un giro, otro y
deshacer ambos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1852_simulation.cpp](1852_simulation.cpp) | G++ 13.2 x64 | simulation | O(54 n) | AC | 0.031 s | 524 KB |
| [1852_simulation.go](1852_simulation.go) | Go 1.14 x64 | simulation | O(54 n) | AC | 0.031 s | 1872 KB |
| [1852_simulation.java](1852_simulation.java) | Java 1.8 | simulation | O(54 n) | AC | 0.109 s | 1764 KB |
| [1852_simulation.py](1852_simulation.py) | Python 3.12 x64 | simulation | O(54 n) | AC | 0.109 s | 936 KB |
| [1852_simulation.rs](1852_simulation.rs) | Rust 1.75 x64 | simulation | O(54 n) | AC | 0.015 s | 676 KB |
