# 2003. Iteración de máximos comunes divisores

[Timus 2003](https://acm.timus.ru/problem.aspx?space=1&num=2003) · dificultad 366 · number_theory

Problema original de Kirill Borozdin, del Concurso Regional Escolar de Programación de los Urales 2013.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un arreglo contiene enteros positivos. Un paso lo sustituye por el
máximo común divisor de cada pareja no ordenada de posiciones distintas.
Cada pareja aporta un elemento aunque se repitan valores originales o
resultados. Así, la longitud `k` pasa a `k(k−1)/2`. Hallar el mínimo de
pasos para que todos los elementos sean 1.

## Entrada

La primera línea contiene `n`, con `3 ≤ n ≤ 10000`. Las siguientes `n`
líneas contienen valores de 1 a `10^7`. Los números están separados por
espacios en blanco. Tiempo 1 segundo, memoria 64 MB.

## Salida

El mínimo de pasos, o `infinity` en minúsculas si el objetivo es
imposible o el mínimo supera `10^18`. Un arreglo inicial de unos
necesita cero pasos.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
3
1
2
3
```

```
1
```

```
4
2
2
2
2
```

```
infinity
```

En el primer ejemplo todas las parejas tienen MCD 1, así que basta un
paso. En el segundo todo nuevo elemento sigue siendo 2 indefinidamente.

## Solución

Fijemos un primo `p` y sea `c` el número de elementos actuales
divisibles por él. Un nuevo MCD contiene `p` exactamente cuando ambas
posiciones elegidas lo contenían. Su nueva incidencia es por tanto
`c(c−1)/2`. Se cuentan posiciones, no exponentes en la factorización.

Las trayectorias son `0→0`, `1→0` y `2→1→0`. La incidencia 3 se
mantiene. Para `c≥4`, `c(c−1)/2≥c`, por lo que una incidencia de al
menos 3 nunca desaparece. La longitud permanece al menos 3 porque
inicialmente también lo es.

Un primo que divida tres elementos originales demuestra `infinity`. Si
no existe tal primo, todos desaparecen en dos pasos como máximo. Una
incidencia original de 2 exige exactamente dos pasos; en otro caso
cualquier valor mayor que 1 exige exactamente uno. Sin factores primos,
el resultado es 0. Esto demuestra alcanzabilidad y minimalidad. Ninguna
respuesta finita supera 2, por lo que el límite `10^18` no requiere
aritmética grande.

Sea `A` el máximo valor y `B=floor(sqrt(A))`. Una criba pequeña obtiene
los primos hasta `B`. Factorizamos cada valor por ellos hasta que el
cuadrado del divisor supere al resto. Contamos cada primo una vez y
eliminamos todas sus potencias. Un resto mayor que 1 es primo y también
se cuenta una vez. Un mapa hash guarda incidencias: la tercera aparición
devuelve inmediatamente `infinity`. Si no ocurre, devolvemos la mayor
incidencia, inicialmente 0.

Sea `P` la cantidad de primos hasta `B` y `F` la suma de cantidades de
factores primos distintos de cada elemento. Tiempo esperado `O(B log
log(B+2) + nP + n log(A+1))`, incluyendo divisiones y actualizaciones
hash; memoria `O(n+B+F)`, incluida la entrada. Las cotas hash son
esperadas. Aquí `B≤3162`, `P≤446`, `F≤8n`, pues el producto de los
primeros nueve primos supera `10^7`. No se almacena una criba de tamaño
`10^7` ni el arreglo creciente de MCD.

Contar cada primo una sola vez por posición: `[4,8,1]` necesita dos
pasos sin importar las potencias de 2. Un MCD global de 1 no garantiza
terminar: `[2,2,2,3]` es infinito. En cambio `[6,10,15]` necesita dos
pasos aunque cada pareja comparta un factor. Valores iguales siguen
siendo posiciones distintas. El 1 no aporta factores y `infinity` debe
escribirse con exactitud.

## Notas por lenguaje

Los cinco programas usan división por primos pequeños y contadores
dispersos. C++, Go, Java y Rust calculan la cota de raíz con enteros;
Python usa `isqrt`. Los productos caben en enteros con signo de 32 bits.
Java utiliza entrada almacenada en búfer y Python analiza todos los
enteros de una vez. Se elige CPython tras medir el programa completo con
entradas máximas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2003_number_theory.cpp](2003_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(B log log(B+2) + n pi(B) + n log(A+1)) | AC | 0.031 s | 568 KB |
| [2003_number_theory.go](2003_number_theory.go) | Go 1.14 x64 | number_theory | O(B log log(B+2) + n pi(B) + n log(A+1)) | AC | 0.078 s | 2048 KB |
| [2003_number_theory.java](2003_number_theory.java) | Java 1.8 | number_theory | O(B log log(B+2) + n pi(B) + n log(A+1)) | AC | 0.156 s | 1480 KB |
| [2003_number_theory.py](2003_number_theory.py) | Python 3.12 x64 | number_theory | O(B log log(B+2) + n pi(B) + n log(A+1)) | AC | 0.578 s | 2024 KB |
| [2003_number_theory.rs](2003_number_theory.rs) | Rust 1.75 x64 | number_theory | O(B log log(B+2) + n pi(B) + n log(A+1)) | AC | 0.031 s | 1008 KB |
