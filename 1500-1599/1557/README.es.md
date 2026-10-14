# 1557. Ataque a la red

[Timus 1557](https://acm.timus.ru/problem.aspx?space=1&num=1557) · dificultad 1699 · graphs

Problema original del Novosibirsk SU Contest en el campus de Petrozavodsk, septiembre de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una red conexa tiene N servidores (N ≤ 2000) y M canales (M ≤ 100000);
un canal puede unir un servidor consigo mismo, y varios pueden unir el
mismo par. Dos hackers destruyen un canal cada uno, dos canales
distintos en total. Hay que contar los pares no ordenados de canales
cuya eliminación deja dos servidores sin conexión entre sí.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

N y M, y luego los dos servidores de cada canal.

## Salida

El número de pares.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 3
1 2
2 3
3 1
```

Salida:

```
3
```

## Solución

Se toma un árbol generador. Cada canal fuera del árbol cierra un ciclo:
el camino del árbol entre sus extremos más el propio canal. Quitar un
conjunto de canales desconecta la red exactamente cuando se quita algún
canal del árbol y cada ciclo que pasa por él pierde también un canal.

Cada canal fuera del árbol recibe una etiqueta aleatoria de 64 bits, y
cada canal del árbol, el XOR de las etiquetas de los ciclos que pasan
por él. Dos canales forman un corte exactamente cuando están en el mismo
conjunto de ciclos, es decir, cuando sus etiquetas coinciden; un puente
no está en ningún ciclo y recibe la etiqueta 0. El XOR del canal del
árbol sobre un servidor es el XOR de todas las etiquetas exteriores con
un extremo en su subárbol, así que una pasada desde las hojas hacia
arriba rellena todas las etiquetas.

Un puente corta la red junto con cualquier otro canal, lo que da
C(M, 2) − C(M − B, 2) pares para B puentes. Los demás canales suman
C(c, 2) por cada grupo de c etiquetas iguales no nulas. Un lazo recibe
una etiqueta propia y nunca forma parte de un corte. Las etiquetas salen
de aplicar splitmix64 al número del canal, así que la ejecución es
determinista, y dos etiquetas coinciden por azar con probabilidad menor
que 10⁻⁹. Todas las soluciones tardan O(N + M log M). Los resultados se
contrastaron con una fuerza bruta sobre todos los pares en 400 redes
pequeñas.

Detalles a tener en cuenta:

- los pares no son ordenados: en el ejemplo los tres pares del triángulo
  dan 3, no 6;
- con un solo canal no hay ningún par (prueba 08);
- C(M, 2) ronda 5·10⁹ y necesita 64 bits, aunque la respuesta misma
  es como mucho de unos 2·10⁸ (prueba gen3);
- dos canales entre los mismos servidores no forman un corte mientras
  un tercer camino los una (prueba 07).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1557_graphs.cpp](1557_graphs.cpp) | G++ 13.2 x64 | graphs | O(N + M log M) | AC | 0.093 s | 3968 KB |
| [1557_graphs.go](1557_graphs.go) | Go 1.14 x64 | graphs | O(N + M log M) | AC | 0.140 s | 13124 KB |
| [1557_graphs.java](1557_graphs.java) | Java 1.8 | graphs | O(N + M log M) | AC | 0.109 s | 3800 KB |
| [1557_graphs.py](1557_graphs.py) | Python 3.12 x64 | graphs | O(N + M log M) | AC | 0.390 s | 50944 KB |
| [1557_graphs.rs](1557_graphs.rs) | Rust 1.75 x64 | graphs | O(N + M log M) | AC | 0.015 s | 9060 KB |
