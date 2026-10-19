# 2052. Contar posiciones fijas al ordenar por suma de cifras

[Timus 2052](https://acm.timus.ru/problem.aspx?space=1&num=2052) · difficulty 1486 · dp, binary_search

Problema original de Alexander Ipatov, preparado por Bulat Zaynullin, del Campeonato de Programación Deportiva de los Urales 2015.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Los números 1, …, n se ordenan por la suma de sus cifras decimales y, a
igualdad, por su valor. Contar los números que conservan su posición.
Los límites son 1 segundo y 64 MB.

## Entrada

Un entero n, 2 ≤ n ≤ 10⁹.

## Salida

La cantidad de posiciones que no cambian.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
19
```

```
3
```

Para diecinueve el nuevo orden es
`1,10,2,11,3,12,4,13,5,14,6,15,7,16,8,17,9,18,19`. Exactamente `1,18,19`
mantienen su posición y la respuesta es tres. Sus sumas de cifras son
uno, nueve y diez.

## Solución

### Expresar la posición ordenada

Sea `C(b,s)` la cantidad de enteros positivos no mayores que `b` cuya
suma de cifras es `s`, y `L_s=sum_{t<s} C(n,t)`. Ese grupo ocupa las
posiciones `[L_s+1,L_s+C(n,s)]`. Si `x` tiene suma `s`, su nueva
posición es `rank(x)=L_s+C(x,s)`, porque primero aparecen sumas menores
y el desempate numérico cuenta los miembros de su grupo hasta `x`
inclusive. Queda fijo exactamente si `x-C(x,s)=L_s`.

### Como máximo un entero fijo por suma

Escribamos los miembros de un grupo como `x_1<x_2<…`; sus posiciones son
`L_s+j`. Dos enteros consecutivos nunca tienen igual suma de cifras:
sumar uno la cambia en `1-9k`, siendo `k` el número de nueves finales, y
esto no puede ser cero. Así `x_{j+1}≥x_j+2` y `x_j-j` aumenta
estrictamente, por lo que puede igualar `L_s` como máximo una vez. Basta
encontrar un candidato por suma.

Definimos `F_s(b)=b-C(b,s)`. Al incrementar `b`, el contador aumenta
cero o uno, así que `F_s` es no decreciente. Dentro del intervalo de
posiciones del grupo buscamos el **último** entero que cumple
`F_s(b)≤L_s`. Se omiten grupos vacíos. Se verifica que el candidato esté
dentro del intervalo, tenga suma `s` y cumpla la igualdad exacta;
entonces se añade uno.

La búsqueda es completa. Todo entero fijo está dentro del intervalo de
su grupo y satisface el predicado. El entero siguiente tiene otra suma
de cifras, por lo que `F_s` pasa inmediatamente a `L_s+1`, salvo que el
intervalo ya haya terminado. La monotonía impide candidatos posteriores.
Por eso la búsqueda devuelve el entero fijo cuando existe; las
verificaciones finales prueban la validez de cada candidato contado.

### Contar exactamente en tiempo lineal en cifras

Sean `D` el número de cifras de `n` y `S=9D`. Precalculamos `W_l(q)`,
cantidad de cadenas decimales de longitud `l` y suma `q`, permitiendo
ceros iniciales: `W_0(0)=1` y `W_l(q)=sum_{a=0..9} W_{l-1}(q-a)`. Cada
fila se obtiene con una ventana deslizante. Guardamos acumulados
`P_l(q)=sum_{r≤q} W_l(r)`; índices negativos valen cero y los superiores
a la suma posible valen `10^l`. Solo hacen falta longitudes hasta `D-1`.

Para contar hasta `b` recorremos sus cifras de izquierda a derecha
manteniendo la suma restante `q`. Si la cifra actual es `d` y faltan `l`
posiciones, las elecciones menores `a=0,…,d-1` dejan sumas `q-a` al
sufijo. Su cantidad es `P_l(q)-P_l(q-d)`. La añadimos, restamos `d` de
`q` y continuamos por el prefijo igual. Si la suma restante es negativa
se termina; al final se incluye `b` exactamente cuando `q=0`. Cada
número más corto tiene una representación única con ceros iniciales.
Solo se consultan sumas positivas `s≥1`, por lo que cero no entra en los
rangos. Se calcula `C(b,s)` en `O(D)` sin enumerar enteros.

Recorremos `s=1,…,S`, calculando tamaño del grupo, candidato y acumulado
`L_s`. Toda la aritmética es entera; hay como máximo nueve cifras libres
en las tablas y los contadores de sesenta y cuatro bits bastan
holgadamente.

Las posiciones empiezan en uno y `C(x,s)` incluye `x`. Los sufijos
permiten cero, pero los grupos positivos no incluyen el entero cero. Hay
que tratar grupos vacíos y acarreos decimales. El predicado solo es
monótono tras fijar una suma de cifras: la permutación completa no es un
orden numérico monótono. Se busca el último entero válido y se comprueba
su suma; un vecino ajeno al grupo también puede satisfacer la
desigualdad. Añadir como máximo uno depende de la prueba de unicidad.

## Notas por lenguaje

El precálculo requiere `O(D·S)` tiempo y espacio. Hay como máximo `S`
búsquedas de `O(log n)` pasos con consultas de `O(D)`, dando
`O(D·S·(1+log n))` tiempo y `O(D·S)` espacio auxiliar. Aquí `D≤10,S≤90`.
Nunca se construye la permutación completa.

Los cinco programas usan los mismos acumulados de sufijos y búsquedas en
intervalos de grupos. C++/Go/Java/Rust usan contadores de sesenta y
cuatro bits; Python usa enteros exactos. Las cadenas decimales solo
representan las hasta diez cifras de una consulta, no todos los números.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2052_dp.cpp](2052_dp.cpp) | G++ 13.2 x64 | dp | O(D*S*(1+log n)) | AC | 0.015 s | 436 KB |
| [2052_dp.go](2052_dp.go) | Go 1.14 x64 | dp | O(D*S*(1+log n)) | AC | 0.031 s | 1136 KB |
| [2052_dp.java](2052_dp.java) | Java 1.8 | dp | O(D*S*(1+log n)) | AC | 0.109 s | 552 KB |
| [2052_dp.py](2052_dp.py) | Python 3.12 x64 | dp | O(D*S*(1+log n)) | AC | 0.109 s | 688 KB |
| [2052_dp.rs](2052_dp.rs) | Rust 1.75 x64 | dp | O(D*S*(1+log n)) | AC | 0.031 s | 252 KB |
