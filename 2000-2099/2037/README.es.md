# 2037. Palabras binarias con cantidades prescritas de palíndromos

[Timus 2037](https://acm.timus.ru/problem.aspx?space=1&num=2037) · dificultad 1225 · constructive

Problema original de Mikhail Rubinchik, del concurso Dandelion de la UrFU, campamento de Petrozavodsk, verano de 2014.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Para cada `i` desde `1` hasta `n` construye una palabra de longitud `n`
sobre `a,b` con exactamente `i` subcadenas palindrómicas distintas no vacías.
Se distinguen sus valores como cadenas, no sus posiciones ni sus ocurrencias.
Indica si no existe. Límites: 0,5 segundos y 64 MB.

## Entrada

Un entero `1 ≤ n ≤ 2000`, una sola instancia sin cantidad inicial de pruebas.

## Salida

Exactamente `n` líneas en orden creciente: `i : palabra` o `i : NO`.
Se acepta cualquier palabra válida, con letras minúsculas `a,b`.
El marcador de inexistencia `NO` va en mayúsculas.

## Evaluación

Un comprobador verifica la longitud y las letras de cada palabra y
cuenta sus palíndromos distintos con un árbol palindrómico; se acepta
cualquier palabra válida, y la negativa solo si no existe ninguna.

## Ejemplos

```
4
```

```
1 : NO
2 : NO
3 : NO
4 : aaaa
```

## Solución

El mínimo es `n` si `n≤7`, `7` si `n=8` y `8` si `n≥9`.
Todos los enteros entre ese mínimo y `n` son alcanzables.

### Certificar las cantidades imposibles

Añadir una letra introduce como máximo un palíndromo distinto nuevo.
Todo nuevo palíndromo es sufijo. Si dos longitudes de sufijo fueran nuevas,
el menor también sería un prefijo propio del mayor palíndromo y ya habría
aparecido antes del último carácter. Por ello una palabra de longitud `n`
no tiene más de `n` palíndromos distintos.

Las cotas pequeñas se certifican mediante enumeración finita completa,
reproducida en [tests/gen.py --proof](tests/gen.py). Enumera cada
palabra binaria de longitudes uno a nueve y guarda en un conjunto cada
subcadena que coincide con su inversión. Los histogramas son:

| Longitud | Cantidad de palíndromos : número de palabras |
| --- | --- |
| 1–7 | `n : 2^n` |
| 8 | `7 : 4; 8 : 252` |
| 9 | `8 : 24; 9 : 488` |

Son las `1022` palabras posibles, no una muestra. Toda palabra de longitud
al menos nueve contiene un prefijo de nueve letras con al menos ocho
palíndromos distintos, que siguen presentes en la palabra completa.
Así queda demostrada la cota inferior para cualquier `n` grande.
Las construcciones siguientes alcanzan todas las cantidades restantes.

### Un período con un conjunto acotado de palíndromos

El período infinito `(aababb)…` tiene exactamente
`{a,b,aa,bb,aba,bab,abba,baab}`.
Inspecciona los seis residuos iniciales para cada longitud de uno a seis.
No hay palíndromos de longitud cinco o seis; cualquiera mayor contendría
uno central de longitud cinco o seis, por lo que tampoco existe.
El script también reproduce esta comprobación finita.

Para un objetivo `8≤i<n` toma `k=i−6≥2` copias de `a` y añade un prefijo
de `(babbaa)…` hasta completar exactamente `n` caracteres.
Hay `k` palíndromos solo de `a`: `a,a²,…,a^k`.
Un palíndromo que cruza la frontera y contiene `b` empieza con `t` letras `a`.
Su extremo simétrico contiene `t` letras `a` después de una `b`.
Los bloques de `a` del período miden como máximo dos, luego `t≤2`.
Tal palíndromo queda en el sufijo iniciado en las últimas dos `a` iniciales,
que es un prefijo de `(aababb)…`. Los enteramente contenidos en la cola
también obedecen la misma restricción periódica.
Solo quedan los seis valores adicionales `b,bb,aba,bab,abba,baab`.
Todos aparecen cuando la cola tiene al menos siete caracteres.
Como su longitud es `n−k=n−i+6≥7`, hay exactamente `k+6=i` valores distintos.

Para `i=n` utiliza `a^n`. El único caso factible restante, `n=8,i=7`,
usa `aababbaa`: tiene `a,aa` y los cinco valores adicionales
`b,bb,aba,bab,abba`; aún no aparece `baab`.
Los índices menores imposibles reciben `NO`.

En el ejemplo `n=4`, la enumeración completa descarta uno, dos y tres.
`aaaa` contiene exactamente `a,aa,aaa,aaaa`, cumpliendo la cuarta línea.
Construye e imprime una fila cada vez: tiempo `O(n²)`, acorde con el tamaño
de salida para `n` grande, y espacio auxiliar `O(n)`.

Trampas:

- Cuenta valores distintos, no ocurrencias ni el palíndromo vacío.
- Longitud ocho permite siete palíndromos y requiere un caso especial.
- Que falle un patrón no justifica imprimir `NO` para un índice factible.
- En el patrón periódico `k=i−6` y la cola comienza por `b`.
- Conserva índices y dos puntos incluso en las filas imposibles.

## Notas por lenguaje

C++, Go, Rust y Java usan salida con búfer; Java crea un arreglo de
caracteres por fila. Python imprime directamente cada fila. Ningún
solucionador crea un árbol de palíndromos ni guarda toda la salida
cuadrática. Solo se usan índices pequeños, sin riesgo de desbordamiento.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2037_constructive.cpp](2037_constructive.cpp) | G++ 13.2 x64 | constructive | O(n^2) | AC | 0.046 s | 744 KB |
| [2037_constructive.go](2037_constructive.go) | Go 1.14 x64 | constructive | O(n^2) | AC | 0.031 s | 6220 KB |
| [2037_constructive.java](2037_constructive.java) | Java 1.8 | constructive | O(n^2) | AC | 0.156 s | 5076 KB |
| [2037_constructive.py](2037_constructive.py) | Python 3.12 x64 | constructive | O(n^2) | AC | 0.140 s | 592 KB |
| [2037_constructive.rs](2037_constructive.rs) | Rust 1.75 x64 | constructive | O(n^2) | AC | 0.046 s | 1020 KB |
