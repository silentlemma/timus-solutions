# 1936. Rondas esperadas en un juego eliminatorio de tres gestos

[Timus 1936](https://acm.timus.ru/problem.aspx?space=1&num=1936) · difficulty 1122 · probability, dp

Original problem from Open Ural FU Championship 2012 | by Denis Dublennykh (prepared by Oleg Dolgorukov).

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

n participantes eligen uno de tres gestos de forma independiente y
uniforme en cada ronda. Los gestos forman un ciclo dirigido: cada uno
vence a otro. Si aparecen exactamente dos, solo sigue el grupo del
gesto ganador. Si aparece uno o los tres, nadie sale. Se termina con
una persona; su premio equivale al total de rondas, incluidas las que
no eliminan a nadie. Hallar el premio esperado condicionado a que gane
una persona determinada. Límites: 1 segundo, 64 MB.

## Entrada

Un entero n, 2≤n≤100, la cantidad inicial de participantes.

## Salida

Un real: el premio esperado del ganador. Se admite error absoluto
o relativo de hasta 10⁻⁶.

## Evaluación

La respuesta se compara con error absoluto o relativo 10⁻⁶.

## Ejemplos

```
2
```

```
1.5
```

## Solución

El condicionamiento no divide la respuesta entre n. Para cualquier
duración r, permutar etiquetas conserva probabilidades y transforma
cualquier ganador en otro. Por tanto P(T=r,ganador=i)=P(T=r)/n y
P(ganador=i)=1/n. La duración condicionada a ese ganador tiene la misma
distribución. Basta calcular el total esperado de rondas sin condicionar.

Sea E_m esa expectativa con m personas, con E_1=0. Hay 3^m asignaciones
equiprobables. Para que sobrevivan k, 1≤k<m, elegir el subconjunto en
C(m,k) formas y el gesto ganador en tres. El gesto perdedor queda
determinado: hay 3C(m,k) asignaciones. En total 3(2^m−2) asignaciones
eliminan a alguien; las demás vuelven al mismo estado. La probabilidad
positiva de avanzar garantiza espera esperada finita hacia un estado menor.

Cada ronda aporta uno. Se traslada el término del mismo estado a la
izquierda y se cancela el factor común 3:

E_m = (3^(m−1) + Σ_{k=1}^{m−1} C(m,k)·E_k) / (2^m−2).

Calcular E_2,...,E_n en orden creciente. Todas las expectativas menores
ya se conocen, y la ecuación del primer paso determina la actual;
la inducción prueba la DP. Los coeficientes se generan por fila con
B_0=1 y B_k=B_{k−1}(m−k+1)/k. Las potencias de 2 y 3 se mantienen
mediante multiplicación.

No calcular el denominador como 1−P(sin eliminación) en coma flotante:
para n=96..100 esa probabilidad se redondea a 1. La recurrencia divide
directamente entre 2^m−2 y suma solo términos positivos. Coeficientes,
potencias y resultados caben en doble precisión, aunque algunos
coeficientes superan enteros de 64 bits. La expectativa mayor es
aproximadamente 1.355203941481465·10¹⁷; doce decimales bastan con
la tolerancia absoluta O relativa permitida.

Tiempo O(n²), espacio O(n). La fila binomial se genera sobre la marcha;
no se almacena la matriz completa ni se simulan rondas individuales.

Las rondas sin eliminación también cuentan. No restar probabilidades
casi iguales ya redondeadas, guardar coeficientes binomiales grandes
en enteros ordinarios ni dividir la expectativa por la probabilidad
individual de ganar. La orientación del ciclo no cambia las tres
parejas de gesto ganador y perdedor.

## Notas por lenguaje

Las cinco versiones usan double/float64/f64 para expectativas,
potencias y coeficientes; solo los índices son enteros. C++ fija
precisión decimal, Go formatea la salida, Java usa Locale.US, Python
una f-string y Rust precisión de formato. Todos imprimen un número
con 12 cifras fraccionarias y salto final.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1936_probability_dp.cpp](1936_probability_dp.cpp) | G++ 13.2 x64 | probability, dp | O(n^2) | AC | 0.015 s | 444 KB |
| [1936_probability_dp.go](1936_probability_dp.go) | Go 1.14 x64 | probability, dp | O(n^2) | AC | 0.031 s | 1128 KB |
| [1936_probability_dp.java](1936_probability_dp.java) | Java 1.8 | probability, dp | O(n^2) | AC | 0.125 s | 1064 KB |
| [1936_probability_dp.py](1936_probability_dp.py) | Python 3.12 x64 | probability, dp | O(n^2) | AC | 0.093 s | 480 KB |
| [1936_probability_dp.rs](1936_probability_dp.rs) | Rust 1.75 x64 | probability, dp | O(n^2) | AC | 0.031 s | 260 KB |
