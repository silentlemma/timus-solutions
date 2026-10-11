# 1300. Impuestos

[Timus 1300](https://acm.timus.ru/problem.aspx?space=1&num=1300) · dificultad 2895 · binary_search

Problema original del Segundo Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 3–4 de abril de 1998.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una escala de impuestos tiene límites N1 < … < Nm y tipos S1, …, Sm+1
por ciento: un ingreso K paga el S1 % de la parte hasta N1, el S2 % de
la parte entre N1 y N2, etc., y el Sm+1 % de la parte por encima de Nm.
Llamémoslo T(K).

Además del salario R, cada empresa paga un plus regional del L % de R,
y el plus tributa por separado: la empresa retiene T(R) + T(L % · R) y
paga R − T(R) + L % · R − T(L % · R). Todas estas cantidades se
redondean a céntimos.

Una persona trabajó para hasta 30 empresas, y solo se conocen las
cantidades pagadas. Hay que imprimir cuánto impuesto más debe por el
año entero: el impuesto sobre el salario total y sobre el plus total
menos lo que las empresas ya retuvieron.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

L; luego líneas `N S`, terminadas por una línea `0 S` con el tipo más
alto; luego las cantidades pagadas, una por línea, terminadas en −1.
Los tipos son porcentajes enteros de 0 a 99; las cantidades y los
límites son positivos, tienen como mucho dos decimales y no pasan de
10⁹. Hay como mucho 20 límites.

## Salida

La diferencia, con dos decimales.

## Ejemplos

### Ejemplo 1

Entrada:

```
15         
12000000 12
24000000 20
36000000 25
48000000 30
0        35
12000000   
12000000   
-1
```

Salida:

```
937233.19
```

## Solución

Todo se calcula en céntimos enteros, así que no se acumula ningún error
de redondeo. Un porcentaje de una cantidad se redondea al céntimo con
las mitades hacia arriba, y T(K) suma los tramos de forma exacta antes
de redondear una sola vez.

Lo difícil es volver de una cantidad pagada al salario. Sea net(R) la
cantidad pagada para un salario R. Un céntimo más de salario sube el
impuesto como mucho un céntimo (todos los tipos están por debajo del
100 %), y el plus y su impuesto se comportan igual, así que net(R) nunca
decrece al crecer R. Por eso una búsqueda binaria encuentra el salario
de una cantidad: primero se duplica una cota superior hasta que su net
supera la cantidad, y luego se parte el intervalo por la mitad unas 45
veces.

Varios salarios pueden dar la misma cantidad pagada, porque un céntimo
de salario puede comérselo un céntimo de impuesto. Las soluciones toman
el mayor salario cuyo net no supera la cantidad. Después, con los
salarios Ri conocidos:

respuesta = T(ΣRi) + T(L % · ΣRi) − Σ(T(Ri) + T(L % · Ri)).

`O(J · m · log V)` para J empresas y cantidades hasta V.

Detalles a tener en cuenta:

- la respuesta puede ser negativa: la escala no tiene por qué subir, y
  con una escala decreciente a la persona le devuelven dinero
  (prueba 08); el redondeo por sí solo puede dar −0.02 (prueba 07);
- con tipos del 99 % el salario tras una cantidad de 10⁹ es unas 50
  veces mayor, así que hacen falta céntimos de 64 bits (prueba 07);
- las cantidades pueden tener un decimal o ninguno, y las líneas pueden
  acabar en espacios (pruebas 01 y 06);
- el plus tributa con su propia escala, no junto al salario
  (prueba 04).

La búsqueda se comprobó contra un recorrido simple de todos los
salarios en 150 entradas aleatorias pequeñas.

## Notas por lenguaje

- Todos los lenguajes analizan las cantidades a mano en céntimos
  enteros.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1300_binary_search.cpp](1300_binary_search.cpp) | G++ 13.2 x64 | binary_search | O(J * m * log V) | AC | 0.015 s | 400 KB |
| [1300_binary_search.go](1300_binary_search.go) | Go 1.14 x64 | binary_search | O(J * m * log V) | AC | 0.031 s | 1032 KB |
| [1300_binary_search.java](1300_binary_search.java) | Java 1.8 | binary_search | O(J * m * log V) | AC | 0.093 s | 988 KB |
| [1300_binary_search.py](1300_binary_search.py) | Python 3.12 x64 | binary_search | O(J * m * log V) | AC | 0.078 s | 736 KB |
| [1300_binary_search.rs](1300_binary_search.rs) | Rust 1.75 x64 | binary_search | O(J * m * log V) | AC | 0.015 s | 260 KB |
