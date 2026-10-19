# 1991. Contar suministros sin usar y objetivos restantes

[Timus 1991](https://acm.timus.ru/problem.aspx?space=1&num=1991) · dificultad 48 · implementation

Problema original de Denis Dublennykh, preparado por Egor Shchelkonogov.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay `n` grupos independientes, cada uno con exactamente `k` objetivos.
El grupo `i` recibe `a_i` suministros, cada uno utilizable una vez para
eliminar un objetivo de ese mismo grupo. Cada uso tiene éxito. No se
permite transferir suministros entre grupos. Tras eliminar cuantos
objetivos sea posible, cuente los suministros sin usar y los objetivos
restantes.

Límites: `1≤n,k≤10000`, `0≤a_i≤100000`. Tiempo: 1 segundo; memoria: 64 MB.

## Entrada

La primera línea contiene `n k`; la siguiente, los `n` suministros.

## Salida

Dos enteros: primero los suministros sin usar y luego los objetivos restantes.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

Entrada:

```
4 5
2 7 5 0
```

Salida:

```
2 8
```

Los pares `(suministros,objetivos)` restantes son `(0,3)`, `(2,0)`,
`(0,0)` y `(0,5)`. Suman `(2,8)`.

## Solución

Un grupo no puede usar más de `a_i` suministros ni atender más de `k`
objetivos. Emparejar una unidad con un objetivo repetidamente consigue
exactamente `b_i=min(a_i,k)` parejas; después uno de los lados está
vacío. Quedan `a_i−b_i=max(a_i−k,0)` suministros y `k−b_i=max(k−a_i,0)`
objetivos.

Mantenga dos totales inicialmente cero. Si `a_i>k`, añada `a_i−k` al
suministro restante; en otro caso añada `k−a_i` a los objetivos
restantes. Tras los primeros `j` grupos, ambos totales son sus restos
verdaderos: la fórmula de un grupo es correcta y no hay intercambios
entre grupos. Este invariante demuestra el resultado final.

No junte primero todos los suministros: un grupo puede tener excedente
mientras otro mantiene objetivos. Si `a_i=k`, ambos aportes son cero; si
`a_i=0`, quedan los `k` objetivos. La identidad
`sin_usar−restantes=Σa_i−nk` sirve como comprobación, pero no determina
por sí sola las dos respuestas.

## Notas por lenguaje

Tiempo `O(n)` y estado auxiliar `O(1)` para los dos totales. C++, Go y
Java consumen una entrada por flujo con búfer. Python guarda `O(n)`
valores analizados y Rust `I` bytes de entrada; la memoria real de
entrada es `O(n)` y `O(I)`, respectivamente. El corte de Python crea
otro arreglo temporal `O(n)` sin cambiar el tiempo.

El máximo sin usar es `10000·(100000−1)=999990000`; el máximo de
objetivos restantes, `10000²=100000000`. Ambos caben en 32 bits con
signo; las versiones compiladas usan acumuladores más anchos. Rust resta
solo después de comparar para evitar desbordamiento sin signo. El
tokenizador de Java lee exactamente estos enteros pequeños. No hacen
falta ordenación, redistribución ni salida flotante.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1991_implementation.cpp](1991_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 448 KB |
| [1991_implementation.go](1991_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.031 s | 1236 KB |
| [1991_implementation.java](1991_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.093 s | 496 KB |
| [1991_implementation.py](1991_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.093 s | 1380 KB |
| [1991_implementation.rs](1991_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.046 s | 480 KB |
