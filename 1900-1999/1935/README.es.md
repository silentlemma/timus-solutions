# 1935. Mínimo de hojas con separaciones reordenables

[Timus 1935](https://acm.timus.ru/problem.aspx?space=1&num=1935) · difficulty 80 · greedy

Original problem from Open Ural FU Championship 2012 | by Tatiana Sharypova (prepared by Oleg Dolgorukov).

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Colocar n objetos finos entre las hojas de un libro, en cualquier orden.
El objeto i necesita al menos a_i hojas hasta cada objeto vecino o tapa.
Un hueco compartido debe satisfacer ambos extremos. Hallar el número
mínimo total de hojas. Límites: 1 segundo, 64 MB.

## Entrada

Primero n, 1≤n≤100. Después n enteros a_i, 1≤a_i≤100.
El orden de entrada no obliga al orden de colocación.

## Salida

Un entero: la cantidad mínima suficiente de hojas.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
3
5 10 3
```

```
28
```

## Solución

Sean S la suma de los requisitos y M su máximo. La respuesta es S+M.
Se calculan directamente ambas cantidades, sin ordenar el arreglo.

Para probar la cota inferior, fijar cualquier colocación y elegir un
objeto con requisito M. Cada objeto a su izquierda se asigna al hueco
inmediatamente a su izquierda; cada objeto a su derecha, al hueco
inmediatamente a su derecha. El máximo elegido se asigna a sus dos
huecos vecinos. Se usan los n+1 huecos distintos, y cada uno necesita
al menos el requisito asignado. Todos los requisitos se cuentan una
vez salvo el máximo seleccionado, que se cuenta dos veces. Por tanto
hacen falta al menos S+M hojas. También vale con n=1 o máximos repetidos.

Para alcanzar esa cota, colocar los requisitos en orden no decreciente
b_1≤...≤b_n. Poner b_1 hojas antes del primer objeto, b_{i+1} entre
los objetos i e i+1, y b_n tras el último. Cada hueco interior contiene
el mayor de los dos requisitos, por lo que satisface ambos. El total
es b_1+(b_2+...+b_n)+b_n=S+M. La cota inferior es alcanzable y la
fórmula es óptima. Ordenar solo sirve como testigo en la demostración.

Tiempo O(n). Las implementaciones guardan los valores de entrada:
espacio total O(n) y estado aritmético adicional O(1).

Los vecinos comparten hojas: tomar el mayor requisito, no la suma.
No conservar el orden de entrada: 100,1,100 necesita 301 hojas tras
reordenar, pero 400 con ese orden fijo. El máximo contribuye una vez
adicional. Un solo objeto requiere 2a_1 hojas por las dos tapas;
tener varios máximos no cambia la fórmula.

## Notas por lenguaje

El resultado no supera 100·100+100=10100 y cabe en un entero de 32 bits.
C++ usa acumulación entera y máximo; Go y Java calculan ambos en un
bucle. Python usa sum y max. Rust suma con i32 y obtiene el máximo
de una sección no vacía. Todos leen enteros separados por espacios
en blanco y terminan la salida con un salto de línea.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1935_greedy.cpp](1935_greedy.cpp) | G++ 13.2 x64 | greedy | O(n) | AC | 0.015 s | 428 KB |
| [1935_greedy.go](1935_greedy.go) | Go 1.14 x64 | greedy | O(n) | AC | 0.015 s | 1092 KB |
| [1935_greedy.java](1935_greedy.java) | Java 1.8 | greedy | O(n) | AC | 0.109 s | 436 KB |
| [1935_greedy.py](1935_greedy.py) | Python 3.12 x64 | greedy | O(n) | AC | 0.078 s | 332 KB |
| [1935_greedy.rs](1935_greedy.rs) | Rust 1.75 x64 | greedy | O(n) | AC | 0.015 s | 236 KB |
