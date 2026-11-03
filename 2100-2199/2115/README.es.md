# 2115. Ordenar una fila con a lo sumo un intercambio

[Timus 2115](https://acm.timus.ru/problem.aspx?space=1&num=2115) · dificultad 228 · sorting

Problema original de Ivan Smirnov, de la Olimpiada Académica Universitaria Escolar de Informática 2019.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dada una secuencia de `1≤n≤100000` alturas `0≤a[i]≤10⁹`, determina
si ya es no decreciente o no creciente. Si no, encuentra un intercambio
de dos posiciones distintas que produzca cualquiera de los órdenes, o
demuestra que uno no basta. Se permiten iguales. Límites: 1 s y 256 MB.

## Entrada

Primera línea n; segunda línea las n alturas en el orden actual.

## Salida

Si ya es monótona en algún sentido, imprime `Nothing to do here`.
En otro caso, si es posible, imprime `Yes` y en la línea siguiente dos
posiciones distintas desde 1 cuyo intercambio sirva. Cualquiera es válido.
Si no existe, imprime `No hope`.

## Evaluación

Se comprueba el veredicto obligatorio, o se aplica el intercambio de
dos posiciones distintas desde 1 y se verifica cualquiera de los órdenes.
Distintos intercambios válidos se aceptan. Cada programa elegido pasó 15
entradas del repositorio y 100 extra en su entorno objetivo. Se releyeron
las 500 salidas extra y códigos con un checker independiente de objetivos
ordenados, sin la regla de fronteras de inversión. El Python exacto
seleccionado ejecutó además 10876 entradas anfitrionas: todos los 9840
arrays de longitudes 1..8 sobre `{0,1,10⁹}`, 1000 aleatorios, extremos
duplicados y casos de 99999/100000, con línea larga, tokens multilínea y
EOF. No son ejecuciones nativas. Las cinco fuentes rápidas y tres revisiones
de formato tienen Accepted de sus bytes exactos.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
150 160 170
```

Salida:

```
Nothing to do here
```

### Ejemplo 2

Entrada:

```
4
140 160 150 170
```

Salida:

```
Yes
2 3
```

## Solución

Las bases ordenan una copia para obtener el objetivo no decreciente;
su inversa es el no creciente. Coincidir con uno implica no cambiar nada.
Si no, se enumeran diferencias con cada objetivo. Un intercambio solo
cambia dos posiciones: deben ser exactamente i,j y cumplir
`a[i]=target[j]`, `a[j]=target[i]`. También es suficiente, pues el resto
ya coincide. Probar ambos objetivos es completo. Tiempo `O(n log n)`,
arrays `O(n)` más la entrada retenida.

Se conservan las cinco ordenaciones. Go y Python quedan idénticos;
C++, Java y Rust solo reciben la salida exacta del formateador, cada uno
con nuevo Accepted propio. Los bytes anteriores quedan en copias locales
de publicación. Cada métrica corresponde a los bytes reales.

## Soluciones optimizadas

Los `two_pointers` evitan ordenar y copiar objetivos. Para no decrecer,
se halla la primera inversión `a[p]>a[p+1]` y se extiende p a la izquierda
por valores iguales hasta l; se halla la última `a[q-1]>a[q]` y se
extiende q a la derecha por iguales hasta r. Se intercambian l,r y se
verifica todo. Si falla, se restaura el array y se repite para no crecer,
comparando `direction*a[i]` con direction=−1. Los valores quedan en
`[-10⁹,10⁹]`, dentro de 32 bits con signo. Si ya era monótono, primero
se devuelve la frase obligatoria de no cambiar nada.

¿Por qué son necesarios esos extremos? Si intercambiar i<j arregla el
orden creciente, allí había H>L y todos los valores intermedios sin
cambiar están entre L y H. La primera inversión está al final de la
racha H que empieza en i; no puede extenderse antes de i, porque ese H
sin cambiar excedería el nuevo L. Extender a la izquierda recupera i.
La última inversión está al principio de la racha L que acaba en j;
no puede seguir después de j, pues el nuevo H excedería su sucesor L.
Extender a la derecha recupera j. Todo intercambio posible es el probado;
la comprobación completa prueba suficiencia y fallar ambos sentidos,
imposibilidad. Las rachas iguales importan, como en `1,2,2,1`.

Hay un número constante de recorridos: `O(n)` tiempo, `O(1)` estado de
búsqueda más la secuencia de `O(n)` celdas. Go y Rust retienen toda la
entrada; el split de Python puede retener una línea entera de tokens.
Ese espacio cuenta, no es constante. C++ usa búfer de bytes y un vector
de 32 bits; Java un int[]; Python `array('i')` en vez de enteros objeto.
No se construyen objetivos ordenados o invertidos.

Frente a las bases Accepted actuales: C++ 0,109→0,015 s (86,2% menos)
y 2532→520 KB (79,5% menos). Go 0,140→0,046 s (67,1% menos); memoria
5696→4052 KB solo baja 28,9%, así que se admite por tiempo. Java baja
3644→848 KB (76,7%). Rust baja 3504→2140 KB (38,9%); 0,062→0,046 s
es una unidad del reloj, sin usarla como prueba de aceleración. Python
baja 15740→8564 KB (45,6%), pero sube 0,140→0,203 s (45,0% peor).
Se admite por memoria y conserva el asterisco de ranking pendiente.

## Notas por lenguaje

Es otro algoritmo lineal: se llama `two_pointers` junto al sencillo
`sorting`. Se eligen las revisiones Accepted más fuertes C++ y Python de
009; las anteriores de 002 con los mismos nombres propuestos solo quedan
en instantáneas e informes locales, sin duplicados públicos.

C++, Java, Go y Rust cumplen el perfil actual; Go y Rust no tienen otros
autores elegibles: cobertura formal, no superioridad demostrada. CPython
3.12 es primero en memoria y 17.º en tiempo, con asterisco. Las comparaciones
nativas usan bases recién aceptadas tras formato cuando corresponde,
sin atribuir métricas antiguas a bytes nuevos. Se cubre todo el dominio,
incluidos n=1, todos iguales, cero y 10⁹.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [2115_sorting.cpp](2115_sorting.cpp) | G++ 13.2 x64 | sorting | O(n log n) | AC | 0.109 s | 2532 KB | 11308132 |
| [2115_sorting.go](2115_sorting.go) | Go 1.14 x64 | sorting | O(n log n) | AC | 0.140 s | 5696 KB | 11294785 |
| [2115_sorting.java](2115_sorting.java) | Java 1.8 | sorting | O(n log n) | AC | 0.140 s | 3644 KB | 11308139 |
| [2115_sorting.py](2115_sorting.py) | Python 3.12 x64 | sorting | O(n log n) | AC | 0.140 s | 15740 KB | 11294788 |
| [2115_sorting.rs](2115_sorting.rs) | Rust 1.75 x64 | sorting | O(n log n) | AC | 0.062 s | 3504 KB | 11308149 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [2115_two_pointers.cpp](2115_two_pointers.cpp) | G++ 13.2 x64 | two_pointers | O(n) | AC | 0.015 s | 520 KB | 11308152 |
| [2115_two_pointers.go](2115_two_pointers.go) | Go 1.14 x64 | two_pointers | O(n) | AC | 0.046 s | 4052 KB | 11307992 |
| [2115_two_pointers.java](2115_two_pointers.java) | Java 1.8 | two_pointers | O(n) | AC | 0.125 s | 848 KB | 11307994 |
| [2115_two_pointers.py](2115_two_pointers.py) \* | Python 3.12 x64 | two_pointers | O(n) | AC | 0.203 s | 8564 KB | 11308151 |
| [2115_two_pointers.rs](2115_two_pointers.rs) | Rust 1.75 x64 | two_pointers | O(n) | AC | 0.046 s | 2140 KB | 11307999 |

\* Aceptada; aún no cumple el objetivo de clasificación. Puede optimizarse más.
