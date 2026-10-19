# 2092. Un abono y entradas sueltas al menor coste

[Timus 2092](https://acm.timus.ru/problem.aspx?space=1&num=2092) · dificultad 1175 · greedy, binary_search

Problema original de Denis Dublennykh, del Concurso Individual Abierto de la UrFU 2014.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay n conciertos; el concierto i cuesta sᵢ y una entrada suelta para él
tiene un descuento de estudiante de dᵢ por ciento. Un abono del tipo j
cubre cualesquiera kⱼ conciertos o más con un descuento de pⱼ por ciento
de su total, pero dentro de él no valen los descuentos de estudiante.
Se asiste a cada concierto una vez. Hallar el menor coste total. Los
límites son 1 segundo y 64 MB.

## Entrada

n y m, 2 ≤ n ≤ 10⁵, 1 ≤ m ≤ 10⁵, los n pares sᵢ (de 100 a 50 000) y dᵢ
(de 0 a 100), y después los m pares kⱼ (de 2 a n) y pⱼ (de 1 a 100).

## Salida

El menor coste con error absoluto o relativo de a lo sumo 10⁻⁶.

## Ejemplos

### Ejemplo 1

Entrada:

```
6 2
500 0
700 0
300 0
400 0
500 50
800 0
5 10
6 15
```

Salida:

```
2680.00
```

## Solución

Nunca hacen falta dos abonos: fundirlos en el de mayor descuento cubre
los mismos conciertos más barato y sigue teniendo bastantes conciertos.
Para un descuento p solo importa el menor k con que se ofrece, y un tipo
con menor descuento y k no menor es inútil. Python, Go y Java prueban
los descuentos de 100 hacia abajo, conservando solo aquellos cuyo k es
menor que el de todos los descuentos mayores. C++ y Rust prueban todos
los descuentos ofrecidos en orden ascendente sin esta poda opcional.

Todos los costes se guardan en céntimos de rublo: una entrada suelta
cuesta s (100 − d) y el mismo concierto dentro del abono s (100 − p). Con
un abono de descuento p, todo concierto con d ≤ p entra en él y el resto
se compra suelto; si así quedan menos de k conciertos, los que faltan son
los traslados más baratos, cada concierto con d > p añade s (d − p). Los
conciertos se agrupan por descuento y se ordenan por precio dentro de
cada grupo, con sumas de prefijos, así que el coste de los need
traslados más baratos se halla con una búsqueda binaria sobre el coste
añadido: con un umbral x, un grupo de descuento d aporta los conciertos
con s ≤ x / (d − p). Todos los traslados del umbral final cuestan lo
mismo, así que el sobrante se resta de forma exacta. La respuesta es el
mejor de estos valores y de comprar todas las entradas sueltas. Sean
D = 100 y S = 50000. Cada descuento cuesta O(D log(DS) log n): la búsqueda
del umbral hace O(log(DS)) iteraciones, cada una con búsquedas en hasta
D grupos ordenados. Incluyendo la lectura y la ordenación, el tiempo
total es O(n log n + m + D^2 log(DS) log n).

Trampas: las entradas con igual descuento completan plazas del abono
sin coste adicional (prueba 07), y los empates en el umbral solo deben
cobrarse hasta completar la cantidad necesaria (prueba 06). La poda por
dominancia es opcional; las ofertas competidoras y dominadas deben dar
el mismo mínimo (prueba 10).

En el ejemplo el abono del 10 % para todos los conciertos menos el
quinto cuesta 2700 · 0.9 = 2430, y la quinta entrada con su descuento
del 50 % cuesta 250: 2680.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2092_greedy_binary_search.cpp](2092_greedy_binary_search.cpp) | G++ 13.2 x64 | greedy, binary_search | O(n log n + m + D^2 log(DS) log n) | AC | 0.234 s | 1620 KB |
| [2092_greedy_binary_search.go](2092_greedy_binary_search.go) | Go 1.14 x64 | greedy, binary_search | O(n log n + m + D^2 log(DS) log n) | AC | 0.046 s | 7356 KB |
| [2092_greedy_binary_search.java](2092_greedy_binary_search.java) | Java 1.8 | greedy, binary_search | O(n log n + m + D^2 log(DS) log n) | AC | 0.125 s | 2480 KB |
| [2092_greedy_binary_search.py](2092_greedy_binary_search.py) | Python 3.12 x64 | greedy, binary_search | O(n log n + m + D^2 log(DS) log n) | AC | 0.187 s | 26884 KB |
| [2092_greedy_binary_search.rs](2092_greedy_binary_search.rs) | Rust 1.75 x64 | greedy, binary_search | O(n log n + m + D^2 log(DS) log n) | AC | 0.015 s | 4348 KB |
