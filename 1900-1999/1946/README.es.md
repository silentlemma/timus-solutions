# 1946. Contar tablas ordenadas de goles

[Timus 1946](https://acm.timus.ru/problem.aspx?space=1&num=1946) · difficulty 1831 · dp

Original problem from Open Ural FU Personal Contest 2012 | by Alexander Ipatov.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

n jugadores se enfrentan por parejas una vez. Cada partido reparte tres
goles:3:0,2:1,1:2 o 0:3. Se suman goles individuales y ordenan de mayor
a menor. Contar listas finales distintas, sin nombres ni multiplicidad
de resultados que producen una misma lista. Límites:1 segundo,64 MB.

## Entrada

Un entero n,2≤n≤50.

## Salida

Número de listas módulo 1000000007.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
3
```

```
8
```

## Solución

Contar listas invertidas a₁≤…≤a_n. Sean T=3n(n−1)/2,L(k)=3k(k−1)/2.
Una lista entera no negativa es factible si y solo si suma T y cada
prefijo de k valores suma al menos L(k). Cada puntuación≤M=3(n−1).
Necesidad: todo conjunto de k jugadores tiene k(k−1)/2 partidos internos;
sus tres goles quedan dentro y los externos añaden goles no negativos.

Suficiencia por flujo: fuente→partido capacidad 3, partido→sus dos jugadores
capacidad T+1, jugador j→sumidero capacidad a_j. En un corte≤T, sean S
los jugadores del lado fuente. Un partido de ese lado necesita ambos
extremos en S o cruza una arista T+1. Para S fijo se incluyen todos los
partidos internos; capacidad 3·(C(n,2)−C(|S|,2))+Σ_{j∈S}a_j≥T por el
menor prefijo. Existe flujo entero T: cada partido reparte tres goles
enteros y cada jugador recibe su total. Queda probada la suficiencia.

dp_i[P][v] cuenta prefijos no decrecientes de i puntuaciones, suma P,
último v y cotas inferiores satisfechas. Base dp₀[0][0]=1. La media
del prefijo no supera la global:guardar solo L(i)≤P≤U(i)=floor(Ti/n).
Al añadir x,

dp_(i+1)[P+x][x] = Σ_{v≤x} dp_i[P][v].

Para cada suma anterior recorrer x con suma prefija. La nueva suma y x
fijan la anterior, por eso asignar la celda, no acumular de otra suma.
Alternar dos capas puestas a cero, con último valor 0..M. Cotas exactas:

first=max(0,L(i+1)−P,ceil(P/i) si i>0),
last=min(M,U(i+1)−P,floor((T−P)/(n−i))).

El último valor anterior≥media del prefijo y los n−i restantes, incluido
x, serán≥x. Solo se podan prefijos imposibles de completar. Iniciar
con posiciones menores que first y añadir dp_i[P][x] antes de escribir.
Sumar los últimos valores de dp_n[T]. Cada lista sigue una ruta, sin
factor de nombres ni realizaciones de partidos.

Tiempo O(n⁴), espacio O(n³): n capas, O(n²) sumas, O(n) últimos valores.
Las sumas prefijas evitan otro factor n. Para n=50 hay hasta 938 filas
y 148 columnas,138824 celdas por capa.

Contar tablas, no 4^(partidos), vectores con nombres ni solo particiones
del total. Las cotas prefijas importan, empates y ceros son válidos.
Usar floor/ceil enteros, incluir x=v, limpiar capas y acumular en 64 bits.

## Notas por lenguaje

Los nativos reutilizan dos búferes planos de 32 bits, limpiando el siguiente;
Python usa listas. Prefijos y suma final requieren 64 bits: hasta
148·(MOD−1)=148000000888. Reducir al guardar una celda; enteros Python
no desbordan. Todos los productos de índices caben en 32 bits.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1946_dp.cpp](1946_dp.cpp) | G++ 13.2 x64 | dp | O(n^4) | AC | 0.015 s | 1468 KB |
| [1946_dp.go](1946_dp.go) | Go 1.14 x64 | dp | O(n^4) | AC | 0.031 s | 2216 KB |
| [1946_dp.java](1946_dp.java) | Java 1.8 | dp | O(n^4) | AC | 0.140 s | 1528 KB |
| [1946_dp.py](1946_dp.py) | Python 3.12 x64 | dp | O(n^4) | AC | 0.390 s | 5156 KB |
| [1946_dp.rs](1946_dp.rs) | Rust 1.75 x64 | dp | O(n^4) | AC | 0.046 s | 1316 KB |
