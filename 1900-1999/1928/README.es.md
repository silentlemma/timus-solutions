# 1928. Pagos alternos con una donación final

[Timus 1928](https://acm.timus.ru/problem.aspx?space=1&num=1928) · difficulty 771 · games, dp

Original problem: folklore, prepared by Maria Zyryanova; from Ural Regional School Programming Contest 2012.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dos participantes solicitan por turnos una cantidad entera entre 1 y k.
Empieza el primero y el presupuesto común inicial es n. Con presupuesto
cero, el juego termina antes de otra solicitud. Una solicitud asequible
se paga íntegramente del presupuesto. En caso contrario, quien solicita
recibe solo una donación separada m, el presupuesto queda intacto y
termina el juego. Cada participante maximiza primero su propio total y,
entre totales propios iguales, minimiza el del rival. Hallar ambos totales
con decisiones óptimas. Límites: 1 segundo, 64 MB.

## Entrada

Una línea n m k: 0≤n≤10000, 0≤m≤1000, 1≤k≤100.

## Salida

Dos enteros: total del primer participante y luego del segundo.

## Evaluación

Comparación exacta de los dos tokens enteros.

## Ejemplos

```
12 30 10
```

```
31 10
```

## Solución

Para cada presupuesto restante b, guardar F[b], los ingresos futuros de
quien debe jugar, y G[b], los del otro. Lo ya recibido es constante al
comparar las siguientes opciones y no altera las preferencias.
Para b=0 ambos valores son cero: no hay siguiente jugada.

Una solicitud asequible x, 1≤x≤min(b,k), deja presupuesto b−x e invierte
los papeles. Su pareja candidata es (x+G[b−x], F[b−x]). Existe una
solicitud no asequible exactamente cuando 0<b<k; todas esas solicitudes
producen el mismo final (m,0). No pagan x ni el resto b. Elegir el mayor
primer componente y, en empate, el menor segundo. Calcular b=1..n e
imprimir F[n],G[n].

Por inducción, los estados menores ya representan las continuaciones
óptimas. Cada acción legal termina con la donación o lleva a un estado
menor intercambiando participantes. La fórmula candidata da exactamente
su pareja de ingresos. Seleccionar según las preferencias indicadas es
la decisión óptima actual. La base y el paso prueban el algoritmo.

O(nk) tiempo y O(n) espacio: dos arreglos y como máximo 1 000 000 de
candidatos asequibles. Las soluciones no buscan recursivamente todo el árbol.

Maximizar la diferencia no sustituye maximizar primero el dinero propio.
El desempate importa: n=5,m=2,k=3 da (3,2); ignorarlo puede cambiar el
resultado. Un presupuesto inicial cero da (0,0) incluso con donación alta.
Con b=k no existe solicitud legal no asequible. La rama no asequible paga
solo m, sin restar la solicitud ni regalar el resto, y termina de inmediato.
Tras cada pago asequible hay que intercambiar los dos papeles almacenados.

## Notas por lenguaje

Los pagos son no negativos y ambos totales suman como máximo n+m≤11000;
bastan enteros con signo de 32 bits. Go usa int; Rust separa índices
usize de pagos i32; C++ y Java usan int; Python emplea listas ordinarias.
El mejor valor interno −1 indica ausencia de candidato y nunca se imprime.
CPython basta para este programa dinámico acotado.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1928_games_dp.cpp](1928_games_dp.cpp) | G++ 13.2 x64 | games, dp | O(nk) | AC | 0.015 s | 460 KB |
| [1928_games_dp.go](1928_games_dp.go) | Go 1.14 x64 | games, dp | O(nk) | AC | 0.031 s | 1240 KB |
| [1928_games_dp.java](1928_games_dp.java) | Java 1.8 | games, dp | O(nk) | AC | 0.125 s | 1672 KB |
| [1928_games_dp.py](1928_games_dp.py) | Python 3.12 x64 | games, dp | O(nk) | AC | 0.296 s | 960 KB |
| [1928_games_dp.rs](1928_games_dp.rs) | Rust 1.75 x64 | games, dp | O(nk) | AC | 0.015 s | 292 KB |
