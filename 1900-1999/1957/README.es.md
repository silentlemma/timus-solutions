# 1957. Todas las clasificaciones finales posibles

[Timus 1957](https://acm.timus.ru/problem.aspx?space=1&num=1957) · difficulty 4747 · math

Original problem from Ural FU contest. Kontur Cup. Petrozavodsk training camp. Winter 2013 | by Mikhail Rubinchik (prepared by Denis Dublennykh).

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cuatro equipos juegan una vez contra cada rival: seis partidos en total.
Se conocen algunos marcadores; los pendientes permiten cualquier número
de goles. Victoria: 3 puntos; empate: 1 por equipo; derrota: 0. Se ordena
por puntos, luego por goles marcados menos recibidos. Si ambos valores
empatan, un sorteo admite cualquier orden. Enumerar todas las clasificaciones.
Límites: 1 s, 64 MB.

## Entrada

Primero n, 0≤n≤6, partidos completados. Siguen n líneas a,b,c,d:
1≤a<b≤4 y 0≤c,d≤10, goles de a y b respectivamente. Ninguna pareja se
repite. El límite 10 solo afecta a partidos ya jugados.

## Salida

Primero m, 1≤m≤24, y luego m permutaciones de 1,2,3,4: los equipos del
primer al cuarto puesto. Sin duplicados, en orden lexicográfico. Solo
los puestos distinguen resultados, no los futuros marcadores.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
5
1 2 1 0
1 3 2 1
1 4 3 2
2 3 1 0
2 4 5 4
```

```
2
1 2 3 4
1 2 4 3
```

## Solución

Enumeramos empate, victoria del primero o del segundo en cada partido
pendiente. Los puntos quedan fijados. Un empate aporta diferencia cero.
Una victoria tiene margen 1+x, con x entero no negativo, realizable mediante
(1+x):0. Sumamos el margen unitario a las diferencias base g y dejamos x libre.

Probamos las 24 permutaciones. Se rechaza si un vecino posterior tiene más
puntos. Entre vecinos a antes de b con iguales puntos exigimos
final_g[a]≥final_g[b]. Estas como máximo tres condiciones, junto con x≥0,
dan A·x≤b en como máximo seis variables enteras. La igualdad permite el
sorteo; basta comparar vecinos por transitividad en cada bloque empatado.

### Factibilidad entera exacta

Dividimos cada fila por el gcd positivo h de sus coeficientes, reemplazando
b por floor(b/h). Es equivalente para variables enteras, también con b
negativo. Un lado izquierdo nulo con cota negativa es contradicción; en
otro caso se descarta. Para coeficientes iguales conservamos la menor cota.

Eliminamos una variable x cuyos coeficientes positivos sean todos 1 o
cuyos negativos sean todos −1. Una cota inferior y superior se escriben
−p·x+L≤bL y q·x+U≤bU, p,q>0. Por cada pareja generamos
q·L+p·U≤q·bL+p·bU y conservamos filas sin x.

La necesidad se deduce sumando desigualdades escaladas. Si todos los
coeficientes inferiores son −1, las cotas inferiores son enteras al fijar
las otras variables enteras. Elegimos la máxima; las combinaciones aseguran
todas las cotas superiores. Si las superiores tienen coeficiente 1,
elegimos su mínimo entero. Una parte ausente es ilimitada. Cada paso
conserva factibilidad entera, no solo real. Normalizamos y repetimos;
constantes sin contradicción equivalen a éxito.

La existencia de un pivote permitido es una propiedad finita de los
coeficientes de cuatro equipos. Renumeramos por la clasificación candidata.
Cada una de seis parejas tiene ninguna variable o uno de dos sentidos de
margen: 3⁶ opciones. Los tres empates adyacentes tienen 2³ máscaras.
[tests/gen.py](tests/gen.py) comprueba exhaustivamente las 5832 familias
y todos los caminos de eliminación permitidos: 13 286 sistemas distintos,
44 054 pasos, sin atasco. Incluye cualquier orden de variables y selección
entre pivotes de igual coste. Las constantes no alteran la traza de
coeficientes: gcd, fusión de filas paralelas y proyección dependen solo
de coeficientes; una contradicción únicamente termina antes. Es una prueba
finita ejecutable de la propiedad especial usada.

Así, se conserva exactamente cada orden realizable por marcadores enteros.
Se imprime en el orden lexicográfico de generación.

Para r=6−n pendientes, como máximo 3ʳ patrones y 24 órdenes. Hay como máximo
seis eliminaciones, 14 filas normalizadas y coeficientes de módulo ≤31.
Con cuatro equipos el trabajo E de eliminación es constante: tiempo
O(3ʳ·24·E), espacio O(1). Antes de dividir coeficientes son ≤2·31²; desde
|b|≤66, seis pasos dan como máximo 66·62⁶<2⁴²: basta int64 con signo.
Hay que redondear hacia abajo cotas negativas. No limitar futuros goles
a 10, ignorar diferencias o sorteos, ni aceptar márgenes no enteros.

## Notas por lenguaje

Las cinco versiones usan proyección entera exacta. Python usa enteros
grandes, las demás int64. Go 1.14 y Java 8 generan las permutaciones.
Java usa Math.floorDiv y Rust div_euclid con divisor positivo. C++ y Go
corrigen truncamiento con resto negativo. Rust usa solo la biblioteca
estándar. La elección CPython se comprueba con medidas de recursos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1957_math.cpp](1957_math.cpp) | G++ 13.2 x64 | math | O(3^(6-n)) | AC | 0.015 s | 448 KB |
| [1957_math.go](1957_math.go) | Go 1.14 x64 | math | O(3^(6-n)) | AC | 0.031 s | 1152 KB |
| [1957_math.java](1957_math.java) | Java 1.8 | math | O(3^(6-n)) | AC | 0.109 s | 620 KB |
| [1957_math.py](1957_math.py) | Python 3.12 x64 | math | O(3^(6-n)) | AC | 0.109 s | 1144 KB |
| [1957_math.rs](1957_math.rs) | Rust 1.75 x64 | math | O(3^(6-n)) | AC | 0.062 s | 256 KB |
