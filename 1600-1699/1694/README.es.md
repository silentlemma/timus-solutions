# 1694. Palabras asesinas

[Timus 1694](https://acm.timus.ru/problem.aspx?space=1&num=1694) · dificultad 2933 · backtracking

Problema original de Alex Samsonov, del Ural SU Contest en el campus de invierno de Petrozavodsk, febrero de 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una palabra asesina usa solo las m primeras letras latinas, es una
k-repetición (k copias de una misma palabra seguidas) y ninguna
subcadena propia suya es una k-repetición. Contar las palabras asesinas
de longitud a lo sumo n.

## Entrada

m, k, n (1 ≤ m ≤ 18; 2 ≤ k ≤ 5; 1 ≤ n ≤ 22).

## Salida

El número de palabras asesinas.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 2 4
```

Salida:

```
9
```

## Solución

Una palabra asesina es wᵏ para una palabra w de longitud L ≤ n / k, a
lo sumo 11. Que wᵏ sirva no depende de qué letras use w, solo de su
patrón. Así que se enumera w numerando sus letras por orden de primera
aparición (0, luego 0 o 1, etc.). Un patrón con d letras distintas
representa m(m − 1)⋯(m − d + 1) palabras.

Toda subcadena de w lo es de wᵏ, así que un prefijo de w que ya termina
en una k-repetición se descarta junto con todas sus extensiones. Para
cada w que sobrevive se comprueba wᵏ. Como w no tiene k-repeticiones y
wᵏ tiene periodo L, solo hay que mirar las ventanas que empiezan en la
primera copia de w y salen de ella. Un w cuya potencia falla se sigue
extendiendo, porque un w más largo puede servir: (010)² contiene 00,
mientras que (0102)² está bien.

Los conteos de patrones por longitud y número de letras se suman con
los factoriales descendentes de m. La búsqueda visita unos 10⁵ patrones
con k = 2 y n = 22, y muchos menos con k mayor. La mayor respuesta,
3.5 · 10¹³, cabe en 64 bits.

Trampas:

- la palabra entera no es una subcadena propia, así que wᵏ mismo está
  permitida;
- no hay que detenerse en un w cuya potencia falla (el test 06 con tres
  letras lo necesita);
- con n < k no hay ninguna palabra (test 07).

La solución en Python se envía con PyPy: una ejecución local de
CPython tarda unos 0.6 s con k = 2 y n = 22, demasiado cerca del
límite de 1 s.

Las respuestas coinciden con un recuento sobre todas las palabras para
m y n pequeños y con una implementación aceptada independiente en 120
conjuntos de parámetros.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1694_backtracking.cpp](1694_backtracking.cpp) | G++ 13.2 x64 | backtracking | about 10^5 patterns | AC | 0.062 s | 192 KB |
| [1694_backtracking.go](1694_backtracking.go) | Go 1.14 x64 | backtracking | about 10^5 patterns | AC | 0.156 s | 1120 KB |
| [1694_backtracking.java](1694_backtracking.java) | Java 1.8 | backtracking | about 10^5 patterns | AC | 0.171 s | 1596 KB |
| [1694_backtracking.py](1694_backtracking.py) | PyPy 3.10 x64 | backtracking | about 10^5 patterns | AC | 0.546 s | 7688 KB |
| [1694_backtracking.rs](1694_backtracking.rs) | Rust 1.75 x64 | backtracking | about 10^5 patterns | AC | 0.078 s | 232 KB |
