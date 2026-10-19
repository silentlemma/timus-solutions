# 1925. El último valor para igualar una suma total

[Timus 1925](https://acm.timus.ru/problem.aspx?space=1&num=1925) · difficulty 70 · math

Problema original de Pavel Ageev, del concurso escolar regional de los Urales de 2012.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se conocen n rondas anteriores. En la ronda i se mostró bᵢ, la entrada
prevista era bᵢ−2 y la real fue gᵢ. Ahora se muestra k. Solo se comprueba
el total de las n+1 rondas: la suma real debe igualar la prevista.
Encontrar un entero no negativo para la ronda actual, o declarar que no
existe. Las rondas pasadas no necesitan ser correctas individualmente.
Límites: 1 segundo, 64 MB.

## Entrada

n,k con 1≤n,k≤100, seguidos de n pares bᵢ,gᵢ, cada valor entre 0 y 100.

## Salida

El entero no negativo necesario, incluido cero. La salida no está
limitada a 100. Si es imposible, escribir exactamente `Big Bang!`,
respetando espacio, mayúsculas y signo de exclamación.

## Evaluación

Comparación exacta de tokens: un entero o los tokens `Big` y `Bang!`.

## Ejemplos

```
6 5
3 1
3 1
5 3
6 5
5 5
7 2
```

```
3
```

```
1 3
4 6
```

```
Big Bang!
```

## Solución

Sea x la entrada actual. La condición agregada es

```text
sum(gᵢ) + x = sum(bᵢ−2) + (k−2).
```

Despejando, x=k−2+sum(bᵢ−gᵢ−2). Iniciar un balance con signo en k−2
y sumar bᵢ−gᵢ−2 por cada par. Comprobar su signo solo al terminar:
si es no negativo, imprimirlo; si es negativo, dar la frase de fallo.

El coeficiente de x es uno, así que el candidato es único. Si es no
negativo, sustituirlo satisface la igualdad. Si es negativo, ningún otro
entero no negativo puede satisfacerla. Esto demuestra ambos resultados.

Un valor previsto individual o un balance intermedio puede ser negativo.
Solo importa el total final. Por ejemplo, k=100 y pares (0,100),(100,0)
dan 94, aunque el primer par vuelva negativo el balance.
Con k=1 y par (3,0), el resultado correcto es cero.

O(n) tiempo. El acumulador usa O(1) espacio de trabajo; las versiones
guardan el historial o toda la entrada, por lo que el espacio total es O(n).

Son n+1 rondas, incluida la actual; restar dos por cada una.
No rechazar antes de tiempo, verificar rondas separadas, truncar subtotales
negativos a cero ni exigir k≥2. Cero es válido y el resultado puede superar
100. Mantener exactamente la frase de fallo.

## Notas por lenguaje

Usar enteros con signo, también en Rust. Todos los balances intermedios
están entre −10201 y 9898, dentro de 32 bits con signo. El máximo ocurre
con n=100,k=100 y todos los pares (100,0). Las cinco versiones retornan
un balance con signo y eligen el formato al final. Python ofrece los pares
perezosamente sobre la entrada almacenada.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1925_math.cpp](1925_math.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.015 s | 428 KB |
| [1925_math.go](1925_math.go) | Go 1.14 x64 | math | O(n) | AC | 0.031 s | 1088 KB |
| [1925_math.java](1925_math.java) | Java 1.8 | math | O(n) | AC | 0.140 s | 1796 KB |
| [1925_math.py](1925_math.py) | Python 3.12 x64 | math | O(n) | AC | 0.093 s | 504 KB |
| [1925_math.rs](1925_math.rs) | Rust 1.75 x64 | math | O(n) | AC | 0.031 s | 236 KB |
