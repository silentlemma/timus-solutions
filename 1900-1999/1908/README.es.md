# 1908. Costes de clics en un árbol podado

[Timus 1908](https://acm.timus.ru/problem.aspx?space=1&num=1908) · difficulty 2118 · dp, trees

Problema original de Denis Dublennykh, preparado por Alexander Fetisov, Ural Championship 2012.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada cadena describe una secuencia de decisiones desde la raíz hasta un final.
Hay que explorar todos los finales; después de cada uno se vuelve gratis
a la raíz. Una opción desaparece cuando todos los finales de su subárbol
ya están explorados. Elegir una arista disponible cuesta un clic. Otro
botón cuesta un clic y recorre la cadena actualmente forzada hasta la
primera bifurcación o final; en una bifurcación no hace nada. Minimiza
el total de clics. Límites: 1 segundo y 64 MB.

## Entrada

Primero n, 1≤n≤100 000, seguido de n cadenas no vacías de letras latinas
minúsculas. Ninguna es prefijo de otra. La longitud total S no supera 100 000.

## Salida

El mínimo número de clics para explorar todos los finales.

## Evaluación

Un entero exacto, comparado por tokens.

## Ejemplos

```
3
aza
azc
b
```

```
4
```

## Solución

Construye un trie. En cada nodo v guarda el número de hojas N[v] y dos
costes: A[v] entra normalmente en cada lectura; B[v] recibe gratis un
salto inicial en cada entrada, incluidos los reinicios tras un final.
Ese salto solo llega a la primera bifurcación o final actual; no se
ofrece otra vez después de decisiones posteriores. Una hoja tiene N=1,A=B=0.

Se pueden completar los subárboles hijos uno a uno. Toma el hijo que
contiene el final visitado en último lugar y mueve todas sus lecturas
anteriores detrás de las de los otros hijos, manteniendo el orden interno.
Los otros todavía ven disponible ese último hijo: su entrada no encarece.
Las lecturas trasladadas solo pueden aprovechar antes los saltos forzados.
Los demás hijos se agrupan recursivamente del mismo modo.

Para un hijo c que no es el último, este nodo sigue siendo una bifurcación:
se paga una elección por final y el coste normal del hijo, N[c]+A[c].
Para el último hijo, la entrada normal paga un salto por lectura que
también proporciona el salto inicial del hijo: N[c]+B[c]. Con salto ya
proporcionado cuesta solamente B[c]. Definiendo T=Σc(A[c]+N[c]),

```text
N[v] = sum N[c]
A[v] = T - max (A[c] - B[c])
B[v] = T - max (N[c] + A[c] - B[c])
```

Los máximos se eligen por separado. Para aa,ab,ac,ad,bxa,bxb, la raíz
tiene A=11 y B=8, con distintos últimos hijos óptimos. Añadir una z
común delante cambia la respuesta real a 6+8=14. Las fórmulas también
sirven con un solo hijo y comprimen una cadena forzada arbitrariamente
larga en un salto. La respuesta es A de la raíz real.

Los nodos nuevos tienen índices mayores que sus padres. Procesa los
índices en orden inverso, sin recursión: una palabra de longitud 100 000
no desborda la pila. Listas enlazadas de hermanos guardan los hijos;
cada búsqueda examina como máximo 26 letras. Tiempo O(S) para el alfabeto
fijo y espacio O(S). Elegir explícitamente todas las decisiones originales
cuesta como máximo S, así que los contadores y sumas caben en 32 bits.

En el ejemplo, elige b, salta a la bifurcación restante a/z, elige c
y salta por el último camino forzado: cuatro clics en total.

## Notas por lenguaje

Todas las versiones insertan y procesan el trie iterativamente.
C++, Go 1.14 y Rust 1.75 usan registros de nodos; Java 8 usa arreglos
primitivos y entrada con búfer. Python 3.12 utiliza arreglos compactos
de enteros y etiquetas de un byte, sin diccionarios ni listas de 26
elementos por nodo. Las cadenas de entrada ocupan O(S). Ninguna versión
usa recursión cuya profundidad dependa de la longitud de las palabras.

Las respuestas coinciden con una BFS sobre los estados de la interfaz en
978 casos, entre ellos todos los conjuntos libres de prefijos de cadenas
binarias de longitud hasta tres.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1908_dp_trees.cpp](1908_dp_trees.cpp) | G++ 13.2 x64 | dp, trees | O(S) | AC | 0.015 s | 2504 KB |
| [1908_dp_trees.go](1908_dp_trees.go) | Go 1.14 x64 | dp, trees | O(S) | AC | 0.031 s | 7092 KB |
| [1908_dp_trees.java](1908_dp_trees.java) | Java 1.8 | dp, trees | O(S) | AC | 0.093 s | 3480 KB |
| [1908_dp_trees.py](1908_dp_trees.py) | Python 3.12 x64 | dp, trees | O(S) | AC | 0.265 s | 3276 KB |
| [1908_dp_trees.rs](1908_dp_trees.rs) | Rust 1.75 x64 | dp, trees | O(S) | AC | 0.046 s | 4992 KB |
