# 1989. Palíndromos con reemplazos de letras

[Timus 1989](https://acm.timus.ru/problem.aspx?space=1&num=1989) · dificultad 338 · strings, fenwick, hashing

Problema original de Mikhail Rubinchik, del Campeonato Abierto de la UrFU 2013.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Mantenga una palabra de `n` letras inglesas minúsculas. Cada operación
cambia una letra o pregunta si una subcadena inclusiva se lee igual en
ambos sentidos. Hay `m` operaciones, `5≤n,m≤100000`, con posiciones
numeradas desde 1. Límite de tiempo: 0.5 segundos; memoria: 64 MB.

## Entrada

La palabra, luego `m` y después las `m` operaciones. `change i a` asigna
la letra `a` a la posición `i`, con `1≤i≤n`. `palindrome? l r` consulta
el intervalo inclusivo `l..r`, con `1≤l≤r≤n`. Se permite asignar la
letra que ya estaba presente.

## Salida

Para cada consulta, en orden, imprima `Yes` si la subcadena es
palíndroma, y `No` en caso contrario. Los reemplazos no producen salida.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

Entrada:

```
abcda
5
palindrome? 1 5
palindrome? 1 1
change 4 b
palindrome? 1 5
palindrome? 2 4
```

Salida:

```
No
Yes
Yes
Yes
```

La palabra inicial completa no es palíndroma; una sola letra siempre lo
es. Cambiar la cuarta letra por `b` produce `abcba`; tanto la palabra
como su interior `bcb` son palíndromos.

## Solución

### Búferes reflejados exactos: C++, Go, Python, Rust

Guarde la palabra `s` y su reverso `t`, manteniendo `t[n−1−i]=s[i]`.
Cada reemplazo escribe en las dos posiciones correspondientes. Convierta
la consulta al intervalo semiabierto `[l,r)` con índices desde cero. Su
reverso es exactamente `t[n−r:n−l]`, que se compara con `s[l:r]`.

La construcción inicial cumple el invariante y cada escritura doble lo
conserva, incluso si la letra no cambia. Para todo desplazamiento `j`,
`t[n−r+j]=s[r−1−j]`. Así, los intervalos son iguales exactamente cuando
todas las parejas reflejadas de la subcadena coinciden. Esto demuestra
cada respuesta sin colisiones. Los intervalos unitarios y los extremos
no necesitan casos especiales.

Sea `L` la suma de las longitudes consultadas. La inicialización cuesta
`O(n)`, un reemplazo `O(1)` y una consulta a lo sumo su longitud. El
total es `O(n+m+L)`, con peor caso `O(nm)`, no logarítmico. Las
comparaciones contiguas usan `memcmp` en C++, `bytes.Equal` en Go,
igualdad de cortes en Rust y `bytearray.startswith` con un `memoryview`
del reverso en CPython. Se ejecutan en código nativo. La vista de Python
observa las modificaciones puntuales; las consultas no copian los
caracteres ni redimensionan los búferes.

La comparación real solo necesita `h=floor((r−l)/2)` caracteres:
`s[l:l+h]` frente a `t[n−r:n−r+h]`. Así se verifica cada pareja una vez;
el carácter central de una longitud impar coincide consigo mismo. Para
un solo carácter ambos rangos son vacíos y el resultado es verdadero.

### Cuatro campos y árboles de Fenwick: Java

Para cada primo `p=1000000007,1000000009,998244353,1000000033`,
seleccione independientemente una base uniforme `B` de `2..p−2`.
Precalcule potencias y mantenga dos árboles con pesos `s[i]Bⁱ` y
`s[i]Bⁿ⁻¹⁻ⁱ` módulo `p`. La construcción lineal suma cada nodo a su
padre. La diferencia entre la letra nueva y la anterior modifica dos
pesos; cada actualización cuesta `O(log n)`.

Para `[l,r)`, calcule las sumas `F,G` restando prefijos y compruebe
`F·Bⁿ⁻ʳ ≡ G·Bˡ (mod p)` en todos los campos. El escalado alinea las
potencias de las letras reflejadas. Un palíndromo siempre pasa. Si no lo
es, la resta de los polinomios alineados, tras quitar la potencia común,
es un polinomio no nulo de grado a lo sumo `n−1`: algún coeficiente es
una diferencia no nula entre −25 y 25, también no nula en cada campo.

Un polinomio no nulo sobre un campo tiene a lo sumo tantas raíces como
su grado. Para una entrada fija independiente de las bases, la
probabilidad de algún `Yes` falso entre como máximo `m` consultas es a
lo sumo `m·∏((n−1)/(p−3)) < 1.1·10⁻¹¹`. Se eligen las bases con
`java.util.Random`. Es un algoritmo Monte Carlo, no una certificación
determinista; la cota supone elecciones uniformes independientes y
excluye consultas adaptativas basadas en las bases secretas. Cuatro
campos requieren `O(n+m log n)` tiempo y `O(n+m)` memoria con las
respuestas acumuladas. Una desigualdad en cualquier campo permite
rechazar de inmediato.

### Implementación y límites

Se usan códigos ASCII. Java calcula productos menores que `p²<1.01·10¹⁸`
en `long` y normaliza las diferencias negativas antes de multiplicar.
Cada nodo es menor que `p`; sumar dos nodos cabe en `int`, y acumular
hasta 17 nodos de un prefijo cabe en `long`. No hacen falta inversos
modulares. Java usa entrada por búfer de bytes y Go es compatible con
1.14.

Las versiones exactas guardan `O(n)` letras y hasta `O(m)` respuestas.
Go y Rust también retienen `I` bytes de entrada: memoria real
`O(n+m+I)`. Python usa CPython 3.12; las mediciones de PyPy 3.10
excedieron tiempo y memoria con consultas palíndromas largas. La
comparación exacta conserva un peor caso cuadrático, así que el límite
de 0,5 segundos es ajustado para ella. Los radios estáticos de Manacher no soportan por sí
solos cambios puntuales; reconstruirlos tras cada cambio también puede
ser cuadrático.

Trampa al generar pruebas: los casos del generador 26–29
(`generated_exhaustive5` a `generated_exhaustive8`) solo usan tamaños
`5..8`. El modo binario `exhaustiveN` produce
`m=N·2^N·(1+N(N+1)/2)` operaciones. Por tanto, `exhaustive4` viola `n≥5`,
y `exhaustive9` produce 211968 operaciones, superando `m≤100000`.
El generador rechaza tamaños fuera de `5..8` antes de construir la secuencia.

## Soluciones optimizadas

C++ y Go guardan la cadena y su inversa y comparan exactamente las mitades reflejadas. Cuentan las parejas adyacentes distintas. Un cambio afecta como máximo a dos parejas y, si no queda ninguna, toda consulta se cumple de inmediato. PyPy guarda sumas polinómicas directas e inversas en árboles de Fenwick con dos módulos primos y bases aleatorias independientes. Un cambio actualiza cuatro sumas. Cada consulta resta prefijos y alinea los exponentes de los dos sentidos. La comparación es probabilística por posibles colisiones. PyPy conserva las órdenes como bytes y escribe respuestas en lotes limitados.

El envío aceptado en Go 1.14 x64 tarda 0.281 s frente a 0.265 s de la base y usa 1 364 KB frente a 10216 KB.

El envío aceptado en PyPy 3.10 x64 tarda 0.234 s frente a 0.500 s de la base y usa 11 204 KB frente a 9896 KB.

Las implementaciones base aceptadas [1989_strings.java](1989_strings.java), [1989_strings.rs](1989_strings.rs) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1989_strings.cpp](1989_strings.cpp) | G++ 13.2 x64 | strings | O(n+m+L) | AC | 0.375 s | 1560 KB | 11292373 |
| [1989_strings.go](1989_strings.go) | Go 1.14 x64 | strings | O(n+m+L) | AC | 0.265 s | 10216 KB | 11292374 |
| [1989_strings.java](1989_strings.java) \* | Java 1.8 | strings | O(n+m log n) | AC | 0.156 s | 10448 KB | 11294029 |
| [1989_strings.py](1989_strings.py) | Python 3.12 x64 | strings | O(n+m+L) | AC | 0.500 s | 9896 KB | 11292375 |
| [1989_strings.rs](1989_strings.rs) \* | Rust 1.75 x64 | strings | O(n+m+L) | AC | 0.281 s | 5200 KB | 11292377 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1989_strings_optimized.cpp](1989_strings_optimized.cpp) \* | G++ 13.2 x64 | strings | O(n+m+L) | AC | 0.281 s | 280 KB | 11310441 |
| [1989_strings_optimized.go](1989_strings_optimized.go) \* | Go 1.14 x64 | strings | O(n+m+L) | AC | 0.281 s | 1364 KB | 11310442 |
| [1989_fenwick.py](1989_fenwick.py) \* | PyPy 3.10 x64 | fenwick | O(n + m log n) | AC | 0.234 s | 11204 KB | 11311248 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
