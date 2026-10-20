# 2197. El prefijo repetido más corto de una cadena bajo sobrescrituras de bloques

[Timus 2197](https://acm.timus.ru/problem.aspx?space=1&num=2197) · dificultad 1669 · hashing, fenwick

Problema original de Konstantin Rychkov, de la clasificatoria del Campeonato Regional de los Urales ICPC 2024.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una cadena S de longitud N se imprime como varias copias de uno de sus
prefijos, e imprimir una vez un prefijo de longitud l cuesta l²
segundos. Q veces un patrón t_k de un conjunto fijo sobrescribe S desde
la posición p. Imprimir el menor tiempo de impresión para la cadena
inicial y tras cada sobrescritura. Los límites son 3 segundos y 256 MB.

## Entrada

N, M y Q, 1 ≤ N ≤ 2 · 10⁵, 0 ≤ M, Q ≤ 2 · 10⁵, luego S, luego los M
patrones de longitud total hasta 10⁶, y luego las sobrescrituras p k.

## Salida

Q + 1 tiempos.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 3 3
abab
be
ebb
ee
3 1
1 2
2 3
```

Salida:

```
8
16
16
4
```

## Solución

Imprimir N / l copias de un prefijo de longitud l cuesta N · l segundos,
así que se busca la menor l que divide a N y genera S.

Las longitudes que dividen a N y generan S son cerradas bajo el mcd, así
que la menor divide a todas las demás. Empezando en l = N, la solución
intenta dividir l por cada factor primo de N mientras el prefijo más
corto siga generando S; lo que queda es el periodo más corto. Un prefijo
de longitud c se comprueba comparando el hash de S con el del prefijo
repetido N / c veces, una suma geométrica
h(prefix) · (B^N − 1) / (B^c − 1), comparada tras multiplicar por el
denominador. En cada ejecución se elige independientemente una base
para cada módulo entre 257 y módulo − 2. Si alguna cumple B^N = 1 en
su módulo, se repite la elección; como c divide a N, B^c − 1 tampoco
se anula. La igualdad de hashes es probabilística, no una comparación
exacta de cadenas.

Trampa: las bases públicas fijas permiten construir colisiones a propósito.
Los tests 17 y 18 contienen cadenas no constantes de longitud prima 17
que colisionan con una cadena constante con los parámetros anteriores,
incluso teniendo igual suma de códigos. La respuesta es 289, no 17.
Las mismas bases aleatorias se usan para comprobar períodos, guardar
respuestas y detectar sobrescrituras sin cambios; sigue existiendo una
probabilidad de colisión distinta de cero.

Lo difícil es calcular el hash de una cadena que cambia con
sobrescrituras largas. Todo el texto que puede aparecer, S y cada
patrón, se pone en una cadena fuente con hashes de prefijo. La S actual
es una lista de fragmentos, cada uno apuntando a un trozo de la fuente,
y cada fragmento guarda su hash ya desplazado a su posición en S, en un
árbol de Fenwick según la posición de inicio. Una sobrescritura corta
los fragmentos en sus dos extremos, quita los de dentro y añade un
fragmento para el patrón, así que cada sobrescritura crea solo un número
constante de fragmentos. El hash de un prefijo es una suma de prefijo de
Fenwick sobre fragmentos completos más el hash de la parte del último
fragmento, leído de la fuente. Las respuestas además se guardan por el
hash de la cadena entera.

En el ejemplo "abab" tiene periodo 2, así que el tiempo es 4 · 2 = 8, y
"eeee" tiene periodo 1, así que es 4.

Sea L la longitud total del diccionario. Cada respuesta requiere O(log N)
comprobaciones de candidatos, incluidas las divisiones repetidas por el
mismo primo; cada comprobación cuesta O(log N). Una sobrescritura cuesta
O(log N) por fragmento creado o eliminado, y se crean O(N + Q) fragmentos
en total. Incluyendo entrada y preprocesamiento, el tiempo total esperado
es O(L + (N + Q + 1) log² N) y el espacio O(L + N + Q), tomando log N
como mínimo igual a 1.

## Notas por lenguaje

- Python también descarta los períodos cuyo número de copias no divide
  la suma de los códigos de los caracteres, porque repetir un prefijo
  repite esa suma. La tabla conserva las mediciones publicadas de PyPy;
  no se han repetido para la versión con bases aleatorias. CPython 3.12
  y PyPy 3.10 no estaban disponibles para la verificación local.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2197_hashing_fenwick.cpp](2197_hashing_fenwick.cpp) | G++ 13.2 x64 | hashing, fenwick | O(L + (N + Q + 1) log² N) | AC | 0.390 s | 33876 KB |
| [2197_hashing_fenwick.go](2197_hashing_fenwick.go) | Go 1.14 x64 | hashing, fenwick | O(L + (N + Q + 1) log² N) | AC | 0.468 s | 65620 KB |
| [2197_hashing_fenwick.java](2197_hashing_fenwick.java) | Java 1.8 | hashing, fenwick | O(L + (N + Q + 1) log² N) | AC | 1.390 s | 71404 KB |
| [2197_hashing_fenwick.py](2197_hashing_fenwick.py) | PyPy 3.10 x64 | hashing, fenwick | O(L + (N + Q + 1) log² N) | AC | 2.859 s | 95636 KB |
| [2197_hashing_fenwick.rs](2197_hashing_fenwick.rs) | Rust 1.75 x64 | hashing, fenwick | O(L + (N + Q + 1) log² N) | AC | 0.312 s | 45676 KB |
