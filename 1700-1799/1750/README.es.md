# 1750. Pajom y el barranco

[Timus 1750](https://acm.timus.ru/problem.aspx?space=1&num=1750) · dificultad 1267 · geometry

Problema original de Petr Lezhankin, del concurso de la USATU de Ufá en el campus de entrenamiento de verano de Petrozavodsk, agosto de 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un barranco es la línea quebrada ABC. Hallar el camino más corto de S a
T que no lo cruce; andar por su borde o rodear sus extremos está
permitido.

## Entrada

El número de pruebas n (1 ≤ n ≤ 5000) y luego, para cada prueba, las
coordenadas de S, T, A, B y C, enteros de valor absoluto hasta 10. Los
cinco puntos son distintos, y S y T no están en el barranco.

## Salida

La longitud del camino más corto en cada prueba, con un error de a lo
sumo 10⁻⁶.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
1 2 5 6 4 4 5 2 1 6
2 2 4 3 1 3 3 3 3 1
2 1 4 4 3 2 4 3 1 4
```

Salida:

```
8.000000
3.650282
3.828427
```

## Solución

Un camino más corto es una línea quebrada que solo se dobla en puntos
del barranco, así que es S, luego algunos de A, B y C en algún orden, y
luego T: a lo sumo 16 candidatos. Se ordenan por longitud y se toma el
primero permitido. `O(1)` por prueba.

Todas las pruebas usan enteros. Un candidato no está permitido si uno
de sus tramos cruza propiamente AB o BC. El codo B necesita más
cuidado: el barranco sigue desde él en ambas direcciones, así que el
camino puede tocar B pero debe quedarse en uno de los dos sectores
cerrados entre los rayos BA y BC, tanto si pasa recto por B como si gira
allí. Cuando BA y BC apuntan en la misma dirección, el barranco se
pliega sobre sí mismo, B es un extremo libre, y un extremo del barranco
que queda dentro del otro tramo no es ninguna esquina: el camino no
puede cambiar de lado allí.

En el primer ejemplo el camino recto cruza BC, y rodear C cuesta
4 + 4 = 8.

Trampas:

- el barranco puede ser recto, con B en medio: cruzar en B sigue siendo
  cruzar;
- el barranco puede plegarse de modo que A quede dentro de BC, o C
  dentro de AB; entonces ese punto está en medio del barranco, no es un
  extremo que rodear;
- un camino a lo largo de un lado del barranco solo lo toca.

Las longitudes coinciden con una implementación aceptada independiente
en 4986 de 5000 pruebas aleatorias. Las otras 14 son todas barrancos
plegados, donde esa implementación pasa recto por el extremo que queda
dentro del otro tramo, lo que cruza el barranco; aquí el camino rodea el
extremo libre.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1750_geometry.cpp](1750_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) per test | AC | 0.046 s | 240 KB |
| [1750_geometry.go](1750_geometry.go) | Go 1.14 x64 | geometry | O(1) per test | AC | 0.109 s | 6956 KB |
| [1750_geometry.java](1750_geometry.java) | Java 1.8 | geometry | O(1) per test | AC | 0.296 s | 6096 KB |
| [1750_geometry.py](1750_geometry.py) | Python 3.12 x64 | geometry | O(1) per test | AC | 0.453 s | 5016 KB |
| [1750_geometry.rs](1750_geometry.rs) | Rust 1.75 x64 | geometry | O(1) per test | AC | 0.031 s | 1380 KB |
