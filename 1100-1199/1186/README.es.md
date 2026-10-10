# 1186. ¿Tienen dos fórmulas químicas los mismos átomos?

[Timus 1186](https://acm.timus.ru/problem.aspx?space=1&num=1186) · dificultad 696 · strings

Problema original de Joseph Romanosky y Roman Elizarov, del concurso regional ACM ICPC del noreste de Europa 2001–2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una fórmula es una lista de secuencias separadas por `+`, cada una con un
multiplicador opcional delante. Una secuencia es una serie de elementos,
cada uno seguido opcionalmente de un multiplicador; un elemento es un
símbolo químico (una mayúscula, quizá seguida de una minúscula) o una
secuencia entre paréntesis. Para un lado izquierdo y hasta 10 lados
derechos de a lo sumo 100 caracteres, hay que decir si cada elemento
químico aparece el mismo número total de veces en ambos lados.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

El lado izquierdo, `N` y luego `N` lados derechos.

## Salida

Para cada lado derecho, `left==right` si los totales coinciden y
`left!=right` si no, copiando ambas fórmulas tal cual.

## Ejemplos

### Ejemplo 1

Entrada:

```
C2H5OH+3O2+3(SiO2)
7
2CO2+3H2O+3SiO2
2C+6H+13O+3Si
99C2H5OH+3SiO2
3SiO4+C2H5OH
C2H5OH+3O2+3(SiO2)+Ge
3(Si(O)2)+2CO+3H2O+O2
2CO+3H2O+3O2+3Si
```

Salida:

```
C2H5OH+3O2+3(SiO2)==2CO2+3H2O+3SiO2
C2H5OH+3O2+3(SiO2)==2C+6H+13O+3Si
C2H5OH+3O2+3(SiO2)!=99C2H5OH+3SiO2
C2H5OH+3O2+3(SiO2)==3SiO4+C2H5OH
C2H5OH+3O2+3(SiO2)!=C2H5OH+3O2+3(SiO2)+Ge
C2H5OH+3O2+3(SiO2)==3(Si(O)2)+2CO+3H2O+O2
C2H5OH+3O2+3(SiO2)!=2CO+3H2O+3O2+3Si
```

## Solución

Se cuentan los átomos de cada fórmula y se comparan. Se parte por `+`
(los paréntesis nunca contienen uno) y en cada término se lee el número
inicial, 1 si falta. Después se recorre el término con una pila de
contadores, uno por paréntesis abierto:

- `(` apila un contador vacío;
- `)` desapila el contador, lo multiplica por el número tras el paréntesis
  y lo suma al contador de debajo;
- un símbolo suma su multiplicador, 1 por defecto, al contador de arriba.

El contador del fondo, por el número inicial, es la parte del término.
`O(L)` por fórmula, aparte del trabajo con los contadores.

Detalles a tener en cuenta:

- `Co` es un elemento, mientras que `CO` es carbono y oxígeno, así que una
  minúscula pertenece a la mayúscula anterior;
- los multiplicadores pueden tener ceros, como `10`, aunque los ejemplos
  evitan el dígito `0` porque se parece al oxígeno;
- un multiplicador ausente vale 1, tanto delante de un término como tras
  un elemento o un paréntesis.

Las respuestas se compararon con una solución escrita aparte en 300
pruebas aleatorias con paréntesis de hasta tres niveles, 3000 lados
derechos en total.

## Notas por lenguaje

- Todos los lenguajes analizan igual y comparan sus mapas de cuentas:
  Counter en Python, mapas ordenados en C++ y Rust, tablas hash en Go y
  Java.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1186_strings.cpp](1186_strings.cpp) | G++ 13.2 x64 | strings | O(L) per formula | AC | 0.015 s | 404 KB |
| [1186_strings.go](1186_strings.go) | Go 1.14 x64 | strings | O(L) per formula | AC | 0.015 s | 1288 KB |
| [1186_strings.java](1186_strings.java) | Java 1.8 | strings | O(L) per formula | AC | 0.187 s | 4096 KB |
| [1186_strings.py](1186_strings.py) | Python 3.12 x64 | strings | O(L) per formula | AC | 0.078 s | 524 KB |
| [1186_strings.rs](1186_strings.rs) | Rust 1.75 x64 | strings | O(L) per formula | AC | 0.031 s | 252 KB |
