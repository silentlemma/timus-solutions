# 1070. La diferencia horaria entre dos aeropuertos a partir de un viaje de ida y vuelta

[Timus 1070](https://acm.timus.ru/problem.aspx?space=1&num=1070) · dificultad 665 · bruteforce

Problema original de Magaz Asanov y Stanislav Vasiliev, del Ural State University Personal Contest Online, febrero de 2001, Students Session.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un vuelo va de un aeropuerto a otro y un segundo vuelo regresa. Para cada
vuelo se dan la salida y la llegada en la hora local del aeropuerto donde
ocurren. Los relojes de los dos aeropuertos difieren en un número entero
de horas, como mucho 5; cada vuelo dura como mucho 6 horas, y las
duraciones de los dos vuelos difieren como mucho en 10 minutos. Halla la
diferencia entre los relojes.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Dos líneas, una por vuelo, cada una con las horas de salida y de llegada
en la forma `HH.MM`.

## Salida

La diferencia en horas, un entero no negativo.

## Evaluación

La salida se compara token a token; los espacios en blanco de más no
importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
23.42 00.39
08.10 17.11
```

Salida:

```
4
```

## Solución

Sea `k` el número de horas que el segundo aeropuerto va por delante. Entonces la
duración real del primer vuelo es su diferencia de reloj menos `k` horas,
y la del segundo vuelo es su diferencia de reloj más `k` horas, ambas
módulo un día, ya que según el reloj un vuelo puede aterrizar «antes» de
salir. Se prueban todos los `k` de −5 a 5 y se queda el que deja ambas
duraciones en 6 horas o menos y con una diferencia de 10 minutos o menos.
Se imprime `|k|`. `O(1)`.

Solo un `k` cumple: un paso de una hora cambia la diferencia de las dos
duraciones en dos horas, y con duraciones de como mucho 6 horas la vuelta
del día no puede producir una segunda coincidencia.

Detalles a tener en cuenta:

- un vuelo puede cruzar la medianoche, y con la diferencia horaria un
  vuelo puede incluso aterrizar según el reloj antes de salir, así que las
  duraciones se toman módulo 24 horas;
- `HH.MM` no es una fracción decimal: las horas y los minutos se leen por
  separado y no como un número real.

Las respuestas se comprobaron de otra forma: probando cada duración real
del primer vuelo hasta seis horas, deduciendo de ella la diferencia y
comprobando el vuelo de vuelta; la diferencia resulta única.

## Notas por lenguaje

- C++ lee cada hora con `scanf("%d.%d")`; los demás lenguajes parten el
  token por el punto.
- Python, Java (`Math.floorMod`) y Rust (`rem_euclid`) tienen un módulo
  que nunca es negativo; C++ y Go suman un día antes del segundo `%`.

## Soluciones optimizadas

Se restan las dos diferencias horarias y se reduce el resultado al intervalo de −12 a 12 horas. Se obtiene el doble del desfase horario más una diferencia de duración de hasta diez minutos. Se redondea el valor absoluto al múltiplo de dos horas más próximo.

El envío 11317998 en Java tardó 0.093 s y usó 324 KB. La versión sencilla tardó 0.093 s y usó 1540 KB.

**Envíos de las versiones sencillas en Timus**

G++ 13.2 x64 №11322403 · Go 1.14 x64 №11322484 · Python 3.12 x64 №11322478 · Rust 1.75 x64 №11322445 · Java 1.8 №11322489.

Go 1.14 x64, envío 11322471. Tiempo 0,015 → 0,015 s, memoria 1072 → 276 KB.

La versión para PyPy lleva la diferencia entre las dos duraciones locales a un intervalo alrededor de cero y la redondea al múltiplo de dos horas más cercano. PyPy 3.10 x64, envío 11322490. Tiempo 0,062 → 0,14 s, memoria 352 → 240 KB.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1070_bruteforce.cpp](1070_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(1) | AC | 0.015 s | 112 KB | 11322403 |
| [1070_bruteforce.go](1070_bruteforce.go) | Go 1.14 x64 | bruteforce | O(1) | AC | 0.015 s | 1072 KB | 11322484 |
| [1070_bruteforce.java](1070_bruteforce.java) | Java 1.8 | bruteforce | O(1) | AC | 0.093 s | 1540 KB | 11322489 |
| [1070_bruteforce.py](1070_bruteforce.py) | Python 3.12 x64 | bruteforce | O(1) | AC | 0.062 s | 352 KB | 11322478 |
| [1070_bruteforce.rs](1070_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(1) | AC | 0.015 s | 204 KB | 11322445 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1070_math.java](1070_math.java) | Java 1.8 | math | O(1) | AC | 0.093 s | 324 KB | 11317998 |
| [1070_math.go](1070_math.go) \* | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 276 KB | 11322471 |
| [1070_math.py](1070_math.py) \* | PyPy 3.10 x64 | math | O(1) | AC | 0.14 s | 240 KB | 11322490 |

\* Las soluciones marcadas aún pueden mejorar en la clasificación objetivo.
