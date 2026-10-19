# 1960. Palíndromos distintos en cada prefijo

[Timus 1960](https://acm.timus.ru/problem.aspx?space=1&num=1960) · difficulty 435 · strings

Original problem from Ural FU contest. Kontur Cup. Petrozavodsk training camp. Winter 2013 | by Mikhail Rubinchik (prepared by Grigory Nazarov).

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Para cada prefijo no vacío de una palabra, contar sus subcadenas contiguas
palindrómicas distintas y no vacías. Valores iguales cuentan una sola vez
aunque aparezcan repetidamente. Un palíndromo coincide con su reverso.
Límites: 1 s, 64 MB.

## Entrada

Una palabra de n letras inglesas minúsculas, 1≤n≤100000. No hay un entero
de longitud separado.

## Salida

n enteros separados por espacios: respuestas para longitudes 1…n.
No contar el palíndromo vacío, ocurrencias ni longitud máxima.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
aba
```

```
1 2 3
```

## Solución

En el ejemplo, `a` contiene solo `a`; `ab` contiene `a,b`; `aba` añade `aba`. Por eso los conteos son 1,2,3.

### Como máximo uno nuevo

Tras añadir c, toda subcadena nueva termina en c. Sea P el sufijo palíndromo
más largo del nuevo prefijo. Un sufijo palíndromo más corto Q también es
prefijo propio de P, por lo que apareció antes de c. Solo P puede ser nuevo:
cada paso añade cero o un valor distinto, como máximo n en total.

### Árbol palindrómico

Usamos el eertree estándar; véase [Rubinchik–Shur, 2015](https://arxiv.org/abs/1506.04862).
La explicación es autosuficiente. Un nodo real representa un palíndromo
y guarda longitud, enlace a su sufijo palíndromo propio más largo y
transiciones de envoltura Q→cQc. Dos raíces artificiales tienen longitudes
−1 y 0, índices 0 y 1; sus enlaces apuntan a 0. Un nodo de longitud uno
enlaza a la raíz vacía. Interior y letra exterior identifican unívocamente
cada palíndromo, así que tiene una única transición entrante.

last mantiene el sufijo palíndromo más largo antes de añadir. Seguimos
enlaces hasta que el carácter anterior al candidato sea c. En la raíz
de longitud −1 se compara el propio nuevo carácter: siempre se detiene.
El mayor Q extensible da el nuevo máximo sufijo P=cQc. Si existe su
transición c, se reutiliza; si no, se crea longitud |Q|+2.

Un nodo nuevo de longitud uno enlaza a la raíz vacía. En otro caso,
partimos de link[Q], buscamos el siguiente sufijo extensible y seguimos
su transición c ya existente. Es el mayor sufijo palíndromo propio de P.
Ya existía porque también es prefijo propio de P y apareció antes.
Actualizamos last a P e imprimimos nodos_totales−2.

### Corrección y complejidad

Los enlaces enumeran sufijos palíndromos en longitud decreciente: el
primero extensible produce el mayor sufijo nuevo. Interior y letra
identifican su valor; falta de transición equivale a un valor nuevo.
Los demás ya existían por el primer lema. La inducción mantiene exactamente
los palíndromos distintos del prefijo.

Ambas búsquedas tienen trabajo total lineal. Sean ℓ_old,ℓ_new las longitudes
de last antes/después. Un fallo reduce longitud y envolver suma dos:
pasos fallidos ≤ℓ_old−ℓ_new+2, cuyas sumas se cancelan telescópicamente.
Para la segunda, q_old,q_new son longitudes de sufijos propios máximos;
comienza en ≤q_old y termina en q_new−2. La cota q_old−q_new+2 también
se cancela. Sin nodo nuevo no hay segunda búsqueda y q_new≤q_old+2.

Versiones nativas usan transiciones densas de 26 letras: inicialización
y memoria `O(26n)`, ambas `O(n)` con alfabeto fijo. Python usa diccionario
disperso y claves exactas parent*26+letter_code: tiempo esperado `O(n)`,
espacio `O(n)`. Es una codificación inyectiva, no una huella probabilística
de subcadenas. Hay como máximo n+2 nodos.

No contar las raíces, sumar ocurrencias, omitir palíndromos pares ni
suponer un aumento en cada paso: `abca` termina en 3. Comprobar límite
izquierdo antes de indexar; índices negativos de Python leen silenciosamente
otra posición. Enumerar todas las ocurrencias puede ser cuadrático.

## Notas por lenguaje

C++ guarda arrays dentro de nodos. Go 1.14 y Rust 1.75 usan índices enteros
nativos. Java 8 usa un array int plano, sin objetos por nodo. Python usa
bytes y claves enteras dispersas. Rust solo emplea la biblioteca estándar.
Se selecciona CPython mediante pruebas de recursos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1960_strings.cpp](1960_strings.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.031 s | 11464 KB |
| [1960_strings.go](1960_strings.go) | Go 1.14 x64 | strings | O(n) | AC | 0.062 s | 26104 KB |
| [1960_strings.java](1960_strings.java) | Java 1.8 | strings | O(n) | AC | 0.125 s | 15252 KB |
| [1960_strings.py](1960_strings.py) | Python 3.12 x64 | strings | O(n) | AC | 0.296 s | 23012 KB |
| [1960_strings.rs](1960_strings.rs) | Rust 1.75 x64 | strings | O(n) | AC | 0.046 s | 22956 KB |
