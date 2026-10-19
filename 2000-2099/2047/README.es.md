# 2047. Una secuencia determinada por divisores de sumas prefijas

[Timus 2047](https://acm.timus.ru/problem.aspx?space=1&num=2047) · difficulty 483 · number_theory

Problema popular, preparado por Alexander Ipatov, del Campeonato de Programación Deportiva de los Urales 2015.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Construir n enteros a₁, …, aₙ con 1 ≤ aᵢ ≤ 300 tales que, para cada k de
2 a n, la suma prefija a₁ + … + aₖ tenga exactamente aₖ divisores
positivos distintos. El primer término no tiene condición propia. Los
límites son 1 segundo y 64 MB.

## Entrada

Un entero n, 2 ≤ n ≤ 100 000.

## Salida

Imprimir una secuencia válida con los enteros separados por espacios, o
`Impossible` si no existe.

## Evaluación

Un comprobador verifica la longitud y los límites y cuenta los divisores
de cada suma prefija desde la segunda; se acepta cualquier secuencia
válida, e `Impossible` solo si no existe ninguna.

## Ejemplos

```
3
```

```
1 3 4
```

`1+3=4` tiene divisores `1,2,4`, por lo que el segundo término es tres.
La siguiente suma `8` tiene `1,2,4,8` y exige cuatro. Otra respuesta
válida es `2 4 6`: las sumas `6` y `12` tienen cuatro y seis divisores.

## Solución

Sea `τ(s)` el número de divisores positivos. Si una secuencia de al
menos dos términos termina en suma `s`, su último término está forzado:
`d=τ(s)`. La suma anterior es únicamente `s-d`. Recorrer estas aristas
predecesoras por suma creciente.

Definir `depth[s]` como la longitud máxima de una secuencia válida con
suma `s`. Una secuencia de un término es posible exactamente para
`1≤s≤300`, dando base uno; en otro caso base cero, inaccesible. Si
`d≤300`, `s>d` y `depth[s-d]>0`, considerar también `depth[s-d]+1` y
tomar el máximo.

El límite completo es `M=300n`, porque ninguna secuencia requerida puede
sumar más. Detenerse en la primera profundidad `n`, retroceder `n-1`
aristas guardando los últimos términos forzados y usar la suma restante
como primer término. Invertir el resultado. Si se agota `M` sin alcanzar
la longitud, imprimir `Impossible`.

### Divisores mediante bloques

Cribar los primos hasta `floor(sqrt(M))`. Procesar bloques de `K=65536`
valores. Inicializar cada resto al propio entero y su contador a uno.
Para cada primo `p` con `p²≤right`, visitar sus múltiplos del bloque,
extraer sus `e` factores y multiplicar el contador por `e+1`. Un resto
mayor que uno aporta otro factor dos. Es la fórmula `τ(s)=product(e+1)`.

Guardar los contadores en un historial compacto para reconstruir. Un
predecesor válido está a distancia máxima 300: bastan 301 posiciones
circulares para profundidades, leyendo la anterior antes de sobrescribir
la actual. Saltar las aristas cuyo contador supera 300.

### Corrección

Se extraen todos los primos hasta la raíz del extremo derecho. Un resto
compuesto tendría un factor primo ya extraído, contradicción. El resto
es uno o primo; el producto de exponentes incrementados da el número
exacto de divisores, incluido `τ(1)=1`.

Por inducción en la suma, toda secuencia válida tiene un término inicial
permitido o su último valor es `τ(s)` y su parte anterior termina en el
único predecesor menor. Recíprocamente, añadir ese valor a un predecesor
accesible cumple la condición nueva y conserva las anteriores. El máximo
del paso calcula, por tanto, la longitud máxima exacta. La distancia de
una arista válida está entre uno y 300 y su profundidad sigue disponible
en el anillo.

Antes del primer éxito toda profundidad es menor que `n`; como solo se
añade uno, el primer éxito vale exactamente `n`. Retroceder sigue esas
aristas y reduce la profundidad en uno hasta una base no mayor que 300.
Así todos los términos y prefijos cumplen sus condiciones. Si no hay
éxito hasta `300n`, una respuesta válida contradiría la profundidad
exacta de su suma final. También `Impossible` es correcto, sin suponer
un corte adivinado.

### Complejidad y recorrido real

La cota conservadora es `O(M log M+n)` tiempo y `O(M+K+sqrt(M)+n)`
espacio, con parada anticipada. Si se recorren `B` sumas, el historial
usa `O(B)` y se factoriza como máximo un bloque adicional. La sobrecarga
de primos entre bloques queda acotada por `floor(sqrt(M))≤5477<K`. Se cumple
`τ(s)≤2sqrt(s)≤2sqrt(30000000)<11000`: caben contadores de 16 bits,
incluso short con signo en Java.

Una criba ordinaria independiente obtuvo una cadena válida de 100000
términos con suma final `1568617` y comprobó cada prefijo enumerando
divisores. Sus prefijos certifican existencia para todas las longitudes
permitidas, así que todo primer éxito ocurre como máximo en esa suma. El
programa mantiene el límite completo `300n` y no incorpora ni la cadena
ni su extremo como corte fijo.

## Notas por lenguaje

La condición comienza en `k=2`. Contar divisores positivos distintos, no
factores primos. No extender un predecesor inaccesible. El anillo de 301
posiciones distingue la actual de las 300 posiciones predecesoras
posibles; leer el predecesor antes de escribir la profundidad actual.
Reconstruir requiere el historial de divisores, además del anillo. No
iniciar extracción de factores con cero.

Los cinco puertos usan la misma búsqueda completa segmentada. Java
amplía un historial short primitivo; C++, Go y Rust también guardan 16
bits. Python utiliza `array("H")` y pequeñas listas de bloque y anillo.

La solución en Python se ejecuta con PyPy: con CPython 3.12 supera el
límite de tiempo en la prueba 13 del juez, mientras que con PyPy 3.10 se
acepta en 0.437 s.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2047_number_theory.cpp](2047_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(M log M+n) | AC | 0.078 s | 4972 KB |
| [2047_number_theory.go](2047_number_theory.go) | Go 1.14 x64 | number_theory | O(M log M+n) | AC | 0.140 s | 15940 KB |
| [2047_number_theory.java](2047_number_theory.java) | Java 1.8 | number_theory | O(M log M+n) | AC | 0.171 s | 13508 KB |
| [2047_number_theory.py](2047_number_theory.py) | PyPy 3.10 x64 | number_theory | O(M log M+n) | AC | 0.437 s | 11296 KB |
| [2047_number_theory.rs](2047_number_theory.rs) | Rust 1.75 x64 | number_theory | O(M log M+n) | AC | 0.093 s | 5644 KB |
