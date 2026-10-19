# 1961. Dialecto cantonés

[Timus 1961](https://acm.timus.ru/problem.aspx?space=1&num=1961) · difficulty 875 · math

Original problem from Open Ural FU Personal Contest 2013 | by Alexander Ipatov.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

En una población de N objetos, un número desconocido M pertenece a una
clase. Una muestra uniforme de n objetos distintos contiene exactamente
m de esa clase. Elegir el entero 0≤M≤N que maximiza esa probabilidad;
si hay empate, el mayor. El muestreo es sin reemplazo. Límites: 1 s, 64 MB.

## Entrada

Tres enteros n,m,N, en ese orden: 1≤n≤N≤10⁸ y 0≤m≤n.

## Salida

Un entero M, el mayor maximizador.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
10 1 200
```

```
20
```

## Solución

En el ejemplo m(N+1)=201 y floor(201/10)=20; se imprime 20.

La probabilidad de un candidato es
P(M)=C(M,m)·C(N−M,n−m)/C(N,n), positiva exactamente en m≤M≤N−n+m.
El denominador no depende de M. Evitamos coeficientes enormes comparando
candidatos factibles adyacentes:

P(M+1)/P(M) = (M+1)/(M+1−m) · (N−M−n+m)/(N−M).

Los denominadores son positivos. La diferencia de productos cruzados es
m(N+1)−n(M+1), así que la probabilidad no decrece exactamente cuando
m(N+1)≥n(M+1). Primero aumenta, puede haber dos vecinos iguales y luego
disminuye. El máximo más a la derecha es

M = min(N, floor(m(N+1)/n)).

Si 0<m<n y q=m(N+1)/n es entero, q−1 y q son máximos iguales; la división
elige el mayor. Por ejemplo n=2,m=1,N=3 da probabilidad 2/3 tanto en
M=1 como M=2, por lo que se requiere 2.

Con m<n el cociente es al menos m. Además,
m(N+1)/n=(N+1)−(n−m)(N+1)/n<N−n+m+1, así que su suelo no supera
N−n+m: es factible. Con m=n resulta N+1 y se limita a N. Con m=0 da
cero. Si n=N se observa toda la población y el resultado es exactamente m.

Tiempo `O(1)` y espacio `O(1)`: una multiplicación, división entera y límite.

Usar N+1, no N, y el empate superior. No sustituir por muestreo independiente
con reemplazo. El producto máximo es 10⁸(10⁸+1)=10 000 000 100 000 000:
excede int32 y el rango entero exacto de binary64, pero cabe en int64 con
signo. Multiplicar y dividir como enteros. Con n=N=10⁸,m=99 999 999, float
puede redondear erróneamente a 10⁸, aunque la observación completa fija
M=99 999 999. El límite N importa cuando m=n.

## Notas por lenguaje

C++ usa int64_t, Go 1.14 int64, Java 8 long y Rust 1.75 u64, ya antes de
multiplicar. Los enteros Python son exactos. Rust solo usa la biblioteca
estándar. Al ser operandos no negativos, la división entera habitual
redondea hacia abajo.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1961_math.cpp](1961_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 396 KB |
| [1961_math.go](1961_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1140 KB |
| [1961_math.java](1961_math.java) | Java 1.8 | math | O(1) | AC | 0.140 s | 1592 KB |
| [1961_math.py](1961_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.109 s | 400 KB |
| [1961_math.rs](1961_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.062 s | 228 KB |
