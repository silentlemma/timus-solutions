# 1262. Número pseudorromano

[Timus 1262](https://acm.timus.ru/problem.aspx?space=1&num=1262) · dificultad 391 · strings

Problema original de Alexander Ipatov, de la Competición Abierta por Equipos de Programación para Escolares de la Región de Sverdlovsk, 11 de octubre de 2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Las cifras pseudorromanas valen 1, 5, 10, 50, 100, 500, 1000 y así
sin fin. El enunciado da reglas para escribir un número con ellas,
parecidas a las romanas de siempre: como mucho tres potencias de diez
iguales seguidas y nunca dos "cincos" iguales seguidos; una cifra menor
puede ir delante de una mayor solo si es potencia de diez y la mayor es
como mucho diez veces más grande; como mucho una cifra menor delante de
una cifra y una mayor detrás; y una regla sobre cada tres vecinas. Una
cifra delante de otra mayor se resta y, si no, se suma. Hay que hallar
cuántas cifras tiene la notación pseudorromana de N
(1 ≤ N ≤ 10²⁰⁰³).

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N.

## Salida

El número de cifras.

## Ejemplos

### Ejemplo 1

Entrada:

```
1939
```

Salida:

```
8
```

## Solución

Como las cifras siguen más allá de M (5000, 10 000, …), cada posición
decimal de N se escribe por separado, igual que las unidades, decenas
o centenas en los números romanos de siempre: los dígitos decimales del
0 al 9 ocupan 0, 1, 2, 3, 2, 1, 2, 3, 4, 2 letras (nada, I, II, III,
IV, V, VI, VII, VIII, IX). La respuesta es la suma de esos valores sobre
los dígitos decimales de N, leído como cadena. `O(log N)`.

Detalles a tener en cuenta:

- N tiene hasta 2004 dígitos, así que hay que leerlo como cadena;
- las reglas tal como están impresas permiten escribir algunos números
  de forma más larga: VIV es 5 + 4 = 9 y las cumple todas. La forma de
  siempre es la más corta de las válidas, y el ejemplo coincide con
  ella;
- los ceros no cuestan nada, así que 10²⁰⁰³ es una sola letra
  (prueba 03).

Una búsqueda exhaustiva sobre todas las cadenas de hasta siete letras
con valores hasta 10 000, comprobadas con las reglas, mostró que para
cada N menor que 4000 la forma de siempre es la más corta de las
válidas.

## Notas por lenguaje

- Todos los lenguajes suman una tabla sobre los caracteres de la
  entrada.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1262_strings.cpp](1262_strings.cpp) | G++ 13.2 x64 | strings | O(log N) | AC | 0.031 s | 384 KB |
| [1262_strings.go](1262_strings.go) | Go 1.14 x64 | strings | O(log N) | AC | 0.031 s | 1096 KB |
| [1262_strings.java](1262_strings.java) | Java 1.8 | strings | O(log N) | AC | 0.078 s | 456 KB |
| [1262_strings.py](1262_strings.py) | Python 3.12 x64 | strings | O(log N) | AC | 0.078 s | 400 KB |
| [1262_strings.rs](1262_strings.rs) | Rust 1.75 x64 | strings | O(log N) | AC | 0.015 s | 240 KB |
