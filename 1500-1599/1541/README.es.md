# 1541. La persecución

[Timus 1541](https://acm.timus.ru/problem.aspx?space=1&num=1541) · dificultad 2122 · backtracking

Problema original de Alexander Ipatov, del Octavo Campeonato Personal Abierto de la Universidad Estatal de los Urales, 3 de marzo de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Los amigos corrieron K leguas (K < 20), la i-ésima a una velocidad
entera de Vi leguas por hora, cada una más lenta que la anterior
(Vi < Vj para i > j) y ninguna por encima de 100000. La persecución
duró M/N horas, con M y N coprimos, 1 ≤ M, N ≤ 50 y M/N ≤ 3. Hay que
hallar K y las velocidades, o escribir -1 si no las hay. Se acepta
cualquier respuesta.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

M y N.

## Salida

K y luego V1 … VK.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 3
```

Salida:

```
2
6 2
```

## Solución

El tiempo es 1/V1 + … + 1/VK, así que M/N debe escribirse como suma de
menos de 20 fracciones unitarias distintas con denominadores hasta 10⁵,
listadas del mayor denominador al menor.

Se busca con profundización iterativa sobre el número de fracciones,
eligiendo los denominadores en orden creciente. Si queda p/q por cubrir
con a lo sumo `left` fracciones tras el denominador `last`, el siguiente
denominador d cumple

- d > last y 1/d ≤ p/q, así que d ≥ ⌈q/p⌉;
- `left` fracciones de a lo sumo 1/d deben alcanzar p/q, así que
  d ≤ left·q/p;
- la mayor suma posible de `left` fracciones desde d, un tramo de la
  serie armónica tomado de sumas prefijas, debe alcanzar p/q, tanto antes
  de elegir d como para lo que queda después.

El resto se guarda como fracción irreducible. Su numerador y su
denominador se mantienen por debajo de 2⁶¹ para que los lenguajes de 64
bits no desborden; las ramas que se saldrían de ese rango se saltan, y
todos los lenguajes saltan las mismas, así que los cinco recorren el
mismo árbol.

Se ejecutaron las 1291 entradas válidas: todas tienen respuesta, con 13
fracciones como mucho (para M/N cerca de 3 hacen falta casi todos los
denominadores pequeños), el mayor denominador queda por debajo de 10⁵ y
la entrada más lenta tarda unos 0,3 s en Python. Las respuestas se
comprobaron de forma exacta con fracciones.

Detalles a tener en cuenta:

- las velocidades se escriben decrecientes, al revés del orden de
  búsqueda (todas las pruebas);
- 3/1 necesita 1, 1/2, …, 1/10 y tres fracciones más (prueba 02);
- una respuesta puede ser una sola fracción, incluso 1/1 (pruebas 03,
  04);
- sin la cota de arriba, los productos de denominadores desbordan 64
  bits;
- hay varias respuestas, así que las pruebas usan un verificador (todas
  las pruebas).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1541_backtracking.cpp](1541_backtracking.cpp) | G++ 13.2 x64 | backtracking | exponential | AC | 0.015 s | 968 KB |
| [1541_backtracking.go](1541_backtracking.go) | Go 1.14 x64 | backtracking | exponential | AC | 0.031 s | 1876 KB |
| [1541_backtracking.java](1541_backtracking.java) | Java 1.8 | backtracking | exponential | AC | 0.125 s | 2896 KB |
| [1541_backtracking.py](1541_backtracking.py) | Python 3.12 x64 | backtracking | exponential | AC | 0.156 s | 4552 KB |
| [1541_backtracking.rs](1541_backtracking.rs) | Rust 1.75 x64 | backtracking | exponential | AC | 0.031 s | 1016 KB |
