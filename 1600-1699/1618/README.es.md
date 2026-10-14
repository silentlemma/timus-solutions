# 1618. Arrays Printing

[Timus 1618](https://acm.timus.ru/problem.aspx?space=1&num=1618) · dificultad 4085 · combinatorics

Problema original del SPbSU ITMO Contest en el campus de Petrozavodsk, invierno de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un arreglo de Java de la forma `new Object[a1][a2]…[an][0]` (n ≤ 100,
a1, …, an son enteros positivos, a1 · … · an ≤ 512) se imprime con
`Arrays.deepToString` y da la cadena S (a lo sumo 10⁵ caracteres).
Los elementos son referencias, así que un
mismo objeto arreglo puede aparecer en varios lugares. Dos
configuraciones son iguales si dos caminos de índices llevan al mismo
objeto en una exactamente cuando lo hacen en la otra. Cuenta las
configuraciones que se imprimen como S, módulo 10007.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

La cadena S.

## Salida

El número de configuraciones módulo 10007.

## Ejemplos

### Ejemplo 1

Entrada:

```
[[], []]
```

Salida:

```
2
```

### Ejemplo 2

Entrada:

```
[[[[]]]]
```

Salida:

```
1
```

### Ejemplo 3

Entrada:

```
[[[]], [[]]]
```

Salida:

```
3
```

## Solución

Al analizar los corchetes se obtienen los tamaños a1, …, an. Se cuenta
desde abajo. m referencias a arreglos vacíos pueden agruparse en objetos
de cualquier manera: una partición de conjunto, B(m) formas (números de
Bell). Un nivel más arriba, m referencias a arreglos de ancho w se
reparten primero en k objetos distintos, de S(m, k) formas (números de
Stirling de segunda especie); esos k objetos tienen k · w referencias al
nivel siguiente, cuyas configuraciones se cuentan en conjunto:

f(m) = Σₖ S(m, k) · g(k · w),

donde g cuenta el nivel de abajo. Objetos distintos pueden tener las
mismas referencias, así que el nivel inferior es libre. La raíz es un
arreglo con a1 referencias, de modo que la respuesta es f(a1) arriba.
En cada nivel no vacío, m nunca pasa de 512 / w ni del número de posiciones
de esa profundidad. `O(|S| + n · 512²)`.

Detalles a tener en cuenta:

- `[]` solo no tiene referencias y tiene exactamente una configuración
  (prueba 04);
- los dos arreglos del primer ejemplo pueden ser o no un mismo objeto: 2;
- los conteos crecen rápido y se toman módulo 10007 desde la tabla de
  Stirling.

Las respuestas coinciden con una implementación aceptada independiente
en 100 formas aleatorias.

## Notas por lenguaje

- Python se ejecuta con PyPy: CPython excede el límite de 2 s en la
  prueba 6 del juez.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1618_combinatorics.cpp](1618_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(n · 512²) | AC | 0.015 s | 1212 KB |
| [1618_combinatorics.go](1618_combinatorics.go) | Go 1.14 x64 | combinatorics | O(n · 512²) | AC | 0.031 s | 4348 KB |
| [1618_combinatorics.java](1618_combinatorics.java) | Java 1.8 | combinatorics | O(n · 512²) | AC | 0.156 s | 2872 KB |
| [1618_combinatorics.py](1618_combinatorics.py) | PyPy 3.10 x64 | combinatorics | O(n · 512²) | AC | 0.421 s | 6788 KB |
| [1618_combinatorics.rs](1618_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(n · 512²) | AC | 0.031 s | 2468 KB |
