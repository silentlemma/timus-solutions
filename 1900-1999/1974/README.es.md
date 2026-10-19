# 1974. Máximo de coincidencias al alinear notas

[Timus 1974](https://acm.timus.ru/problem.aspx?space=1&num=1974) · difficulty 1156 · bitmask, bruteforce

Problema original de Denis Dublennykh, del Campeonato de Programación Deportiva de los Urales 2013.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Comparar una melodía fuente con m objetivos. Para subcadenas contiguas
de igual longitud, contar posiciones de la misma altura absoluta. La
similitud absoluta es el máximo entre todos esos pares; las diferencias
están permitidas y no penalizan. La relativa divide ese máximo por la
longitud del objetivo. Límites: 1 segundo, 64 MB.

## Entrada

Primera línea: longitud fuente n y sus n notas. Después m, 1≤m≤100,
y m líneas con longitud y notas de cada objetivo. Todas las longitudes
están entre 1 y 1000 inclusive.

Una nota es dN, dN+ o dN-, con octava d=1…8 y N=A…G. Los desplazamientos
naturales son C=0, D=2, E=4, F=5, G=7, A=9, B=11; + y - añaden o
restan un semitono. Así C+=D-, D+=E-, E=F-, F=E+, F+=G-, G+=A-, A+=B-.
B+ es C de la octava siguiente; C- es B de la anterior. Se excluyen
las notas inexistentes 1C- y 8B+.

## Salida

m similitudes reales en orden de objetivos. Error absoluto o relativo
de hasta 10⁻⁶. Los valores pertenecen a [0,1].

## Evaluación

Un comprobador compara cada número con un error de como mucho 10⁻⁶ ·
max(1, |respuesta|).

## Ejemplos

```
4 5C+ 5D 5C 5G
3
2 5D- 5D
2 5D 4B+
4 5D 5C+ 5D 5F-
```

```
1.000000
1.000000
0.500000
```

## Solución

### Alturas canónicas y solapes completos

Convertir cada nota en 12(d−1)+desplazamiento+alteración, entre 0 y 95.
Esto incluye equivalencias entre octavas. La octava importa y no se
permite transponer toda una melodía.

Fijar la diferencia i−j entre índices. Cualquier par de subcadenas con
ese desplazamiento puede ampliarse al solape completo. Añadir posiciones
no elimina coincidencias porque una diferencia no penaliza. Basta contar
igualdades en los n+L−1 solapes no vacíos, con L longitud del objetivo;
el máximo coincide exactamente con la definición.

### Pares de posiciones en las versiones compiladas

Guardar posiciones fuente por altura. Un par igual (i,j) pertenece al
único desplazamiento i−j: incrementar contador i−j+L−1 y tomar el máximo.
Cada igualdad se cuenta una vez y ninguna diferencia se cuenta, probando
la corrección. Reutilizar listas fuente y crear contadores nuevos por objetivo.

Con K pares iguales, tiempo `O(n+L+K)`, peor caso `O(nL)`, espacio de
trabajo `O(n+L+96)` sin búferes. Es el método de C++, Go, Java y Rust.

### Python: campos independientes en un entero

Usar base 2¹⁰=1024. Para altura p, M[p]=Σᵢ:altura(i)=p 2^(10i). Sumar

T = Σⱼ M[objetivo[j]] · 2^(10(L−1−j)).

El dígito i−j+L−1 cuenta los pares iguales de ese desplazamiento. Cada
campo es como máximo min(n,L)≤1000, menor que 1024; no hay acarreo
entre campos. Extraer diez bits cada vez y tomar el máximo. Al llegar
a min(n,L) se puede terminar. Dividir por L, no por n.

El entero tiene B=10(n+L−1) bits. Se hacen L sumas/desplazamientos y
hasta n+L−1 extracciones. En palabras de w bits, una cota conservadora
por comparación es `O((n+L)·ceil(B/w))`; las máscaras ocupan
`O(96·ceil(10n/w))` palabras. Los enteros arbitrarios ejecutan dentro
las operaciones densas, evitando un bucle Python sobre nL pares.

En el ejemplo 5C+=5D-, por lo que el primer objetivo coincide con el
inicio de la fuente: 2/2=1. El segundo coincide con posiciones 2 y 3
porque 4B+=5C: también 2/2=1. En el último, alinear sus notas segunda
y tercera con las dos primeras de la fuente da dos coincidencias,
máximo 2/4=0.5.

No es subcadena común ni subsecuencia común máxima: se permiten diferencias,
pero el desplazamiento debe ser único. Normalizar equivalencias, también
B+ y C- entre octavas. El denominador es la longitud objetivo. Cero es
válido. Hasta 1000 coincidencias requieren diez bits, no nueve. Considerar
todos los desplazamientos y limpiar contadores entre objetivos.

## Notas por lenguaje

Python empaqueta campos en enteros exactos grandes. Las cuatro versiones
compiladas enumeran pares de posiciones iguales. Java lee alturas de un
búfer de bytes sin crear 100 000 cadenas temporales. La estructura de
posiciones fuente no se modifica durante las comparaciones.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1974_bitmask.py](1974_bitmask.py) | Python 3.12 x64 | bitmask | O((n+L)*ceil(B/w)) | AC | 0.390 s | 7056 KB |
| [1974_bruteforce.cpp](1974_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(n*L) | AC | 0.093 s | 596 KB |
| [1974_bruteforce.go](1974_bruteforce.go) | Go 1.14 x64 | bruteforce | O(n*L) | AC | 0.140 s | 3988 KB |
| [1974_bruteforce.java](1974_bruteforce.java) | Java 1.8 | bruteforce | O(n*L) | AC | 0.140 s | 1884 KB |
| [1974_bruteforce.rs](1974_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(n*L) | AC | 0.078 s | 1280 KB |
