# 1940. Contar años sin divisor propio pequeño

[Timus 1940](https://acm.timus.ru/problem.aspx?space=1&num=1940) · difficulty 835 · number_theory

Original problem from Open Ural FU Championship 2012 | by Ksenia Karpova (prepared by Egor Shchelkonogov).

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se examinan los B años A+1,…,A+B, incluido el último. Para un número n,
se prueban divisores 2,3,…,n−1 en orden, un minuto por división. Se para
al hallar un divisor o gastar k minutos. Si no aparece divisor, el año
se considera primo, aunque sea compuesto. Si se agotan antes todos los
candidatos propios, también pasa. Contar los años que pasan.
Límites: 1 segundo, 64 MB.

## Entrada

Tres enteros A,B,k: 2≤A,B≤10^9 y 1≤k≤300. El mayor año es 2·10^9.
Se permiten espacios y saltos de línea entre números.

## Salida

Un entero entre 0 y B: los años que pasan dentro de (A,A+B].

## Evaluación

Se compara un único entero; los espacios no importan.

## Ejemplos

```
23 7 3
```

```
2
```

## Solución

El último divisor disponible es y=k+1, no k. Un divisor compuesto no
añade rechazos: un factor primo menor ya se ha probado. Sean p₁,…,p_s
los primos no mayores que y.

Definir φ(x,t) como los enteros de [1,x] no divisibles por ninguno de
los primeros t primos, incluido 1. Entonces
φ(x,t)=φ(x,t−1)−φ(⌊x/p_t⌋,t−1): los múltiplos eliminados corresponden
a cocientes que sobreviven a los primeros t−1 primos. Memorizar (x,t)
con una caché compartida por los dos extremos.

Un primo n≤y pasa porque no se permite dividirlo por sí mismo, pero
φ lo elimina. Hay que añadir esos primos:

answer = φ(A+B,s)−φ(A,s) + π(min(A+B,y))−π(min(A,y)).

Todo compuesto eliminado tiene un factor primo propio ≤y, por lo que
no hay otra excepción. El 1 artificial se cancela al restar prefijos.
La resta excluye A e incluye A+B.

Usar b=min(s,6) primos como base periódica; su producto W≤30030.
Precalcular supervivientes por prefijo en un periodo. Así φ(x,b) se
obtiene en O(1) con periodos completos y el prefijo restante.

Para niveles mayores, φ(0,t)=0. Si 1≤x<p_t, solo queda 1. Si
p_t≤x<p_t², un compuesto superviviente tendría sus dos factores primos
mínimos mayores que p_t, imposible bajo x. Luego φ(x,t)=1+π(x)−t.
Una criba con prefijos de primos hasta L=301² cubre tales consultas.
Los demás estados usan la recurrencia. Cada paso reduce t; la base y
las podas demuestran por inducción la corrección del conteo.

Sean N=A+B, s=π(k+1)≤62, b≤6, W≤30030 y L=301². Para cada extremo X
hay O(√N) cocientes distintos ⌊X/d⌋; divisiones enteras anidadas
conservan esa forma. Hay O(s√N) estados memorizados. El tiempo esperado
es O(L log log L+bW+s√N), espacio O(L+W+s√N), profundidad ≤s.
La criba y el periodo son pequeños; no hay un bucle o vector de tamaño B.

Empezar por A+1, incluir A+B y probar hasta k+1. Un compuesto sin factor
pequeño puede pasar: 25 con k=3. No rechazar un primo por sí mismo.
Al añadir un divisor compuesto la respuesta puede quedar igual.
No hace falta recorrer mil millones de años ni enumerar todos los
subconjuntos de inclusión-exclusión sin podas.

## Notas por lenguaje

Los extremos y conteos caben en enteros con signo de 32 bits: N≤2·10^9,
respuesta≤10^9. La clave que desplaza x seis bits y añade t requiere
64 bits. C++, Go y Rust usan mapas hash estándar; Java usa una tabla
creciente de direccionamiento abierto con matrices primitivas para
evitar objetos empaquetados. Python usa enteros ilimitados y prefijos
unsigned short. Solo bibliotecas estándar; salida con salto final.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1940_number_theory.cpp](1940_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(s sqrt(N)) | AC | 0.031 s | 3596 KB |
| [1940_number_theory.go](1940_number_theory.go) | Go 1.14 x64 | number_theory | O(s sqrt(N)) | AC | 0.031 s | 8528 KB |
| [1940_number_theory.java](1940_number_theory.java) | Java 1.8 | number_theory | O(s sqrt(N)) | AC | 0.140 s | 6668 KB |
| [1940_number_theory.py](1940_number_theory.py) | Python 3.12 x64 | number_theory | O(s sqrt(N)) | AC | 0.171 s | 8424 KB |
| [1940_number_theory.rs](1940_number_theory.rs) | Rust 1.75 x64 | number_theory | O(s sqrt(N)) | AC | 0.031 s | 5564 KB |
