# 1918. Mapas que escapan de todo prefijo propio

[Timus 1918](https://acm.timus.ru/problem.aspx?space=1&num=1918) · difficulty 936 · dp

Problema original de Denis Dublennykh, de la subregión oriental del NEERC 2012.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Elegir f:{1,…,n}→{1,…,n}: cada control tiene n opciones independientes.
Comenzar en 1. Activar lleva i a f(i); esperar permite i→i−1 si i>1.
Se puede activar en cualquier estado intermedio. Contar los mapas que
permiten alcanzar n. Límites: 2 segundos, 64 MB.

## Entrada

Un entero n, 2≤n≤5000.

## Salida

Cantidad de mapas adecuados módulo M=1 000 000 007.

## Evaluación

Comparación exacta de un token entero.

## Ejemplos

```
2
```

```
2
```

## Solución

Los estados alcanzables forman un prefijo, pues esperar permite llegar
a todos los menores. Sea a[k] la cantidad de mapas adecuados en {1,…,k},
con base auxiliar a[1]=1. Particionar los nⁿ mapas por su prefijo final
{1,…,k}. Sus primeros k valores quedan dentro de él y permiten alcanzar k:
hay a[k] restricciones. Los otros n−k valores eligen cualquiera de n
estados, dando n^(n−k) extensiones. Cada combinación tiene exactamente
ese prefijo. No hay coeficiente binomial: el prefijo es fijo. Por tanto

nⁿ = Σ(k=1..n) a[k]·n^(n−k).

Aislar a[n] y factorizar n. Con H=Σ(k=1..n−1) a[k]·n^(n−1−k),

a[n] = n·(n^(n−1)−H) mod M.

Evaluar H por Horner con k creciente: H←(H·n+a[k]) mod M desde cero.
Calcular n^(n−1) por exponenciación binaria modular y normalizar la resta.
La partición exhaustiva y disjunta demuestra la DP por inducción.

### Bucle de Python

Python combina dos coeficientes: H←(H·n²+a[k]·n+a[k+1]) mod M.
Son dos pasos exactos de Horner con un solo resto. Si n−1 es impar,
procesar el último aparte. El iterador compartido de `zip` puede consumir
el valor sin pareja sin procesarlo; por eso la cola se obtiene por índice.
Los puertos nativos usan pasos individuales.

Tiempo `O(n²)` y memoria `O(n)`, incluido el trabajo menor `O(n log n)`
de potencias. Los productos ordinarios quedan por debajo de aproximadamente
5·10¹² y los de potencia por debajo de M²: caben en 64 bits. El intermedio
doble de Python es menor que aproximadamente 2.501·10¹⁶ y también exacto.

Con n=2 debe cumplirse f(1)=2; f(2) tiene dos opciones, dando la salida 2.
n=1 solo es una base interna.

Los controles fuera del prefijo tienen n opciones, no n−k. Incluir a[1],
contar cada prefijo final una sola vez, normalizar restas y tratar la cola
impar. No sustituir prefijos por subconjuntos conexos arbitrarios ni usar potencias flotantes.

## Notas por lenguaje

C++/Go/Java/Rust usan aritmética modular de 64 bits. Python emplea enteros
exactos, pasos dobles y cortes temporales de memoria lineal. Se elige
CPython3.12: la memoria medida de PyPy supera 64 MB. Cada programa calcula
la tabla y muestra solo la entrada n, sin enumerar mapas completos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1918_dp.cpp](1918_dp.cpp) | G++ 13.2 x64 | dp | O(n^2) | AC | 0.031 s | 416 KB |
| [1918_dp.go](1918_dp.go) | Go 1.14 x64 | dp | O(n^2) | AC | 0.062 s | 1128 KB |
| [1918_dp.java](1918_dp.java) | Java 1.8 | dp | O(n^2) | AC | 0.328 s | 496 KB |
| [1918_dp.py](1918_dp.py) | Python 3.12 x64 | dp | O(n^2) | AC | 1.734 s | 8620 KB |
| [1918_dp.rs](1918_dp.rs) | Rust 1.75 x64 | dp | O(n^2) | AC | 0.046 s | 252 KB |
