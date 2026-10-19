# 2040. Nuevos valores palíndromos tras cada letra

[Timus 2040](https://acm.timus.ru/problem.aspx?space=1&num=2040) · dificultad 861 · strings

Problema original de Mikhail Rubinchik, preparado por Kirill Borozdin, del concurso Dandelion de la UrFU, campamento de Petrozavodsk, verano de 2014.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Para cada prefijo no vacío de una palabra, indicar cuántos valores
distintos de subcadenas palíndromas no vacías aparecieron al añadir su
última letra. La misma cadena en posiciones distintas es un solo valor;
no se cuentan apariciones.

## Entrada

Una palabra formada sólo por `a` y `b` minúsculas, con `1≤n≤5000000`.
Límite de tiempo: 0,5 segundos; memoria: 100 MB. La nota oficial
garantiza una solución C++ suficientemente rápida, pero no garantiza tal
solución en otros lenguajes, incluido Java.

## Salida

Exactamente `n` dígitos consecutivos sin espacios. El dígito `i` es la
cantidad de palíndromos distintos no vacíos del prefijo de longitud `i`
menos la del prefijo anterior. El primero es `1`. Se demuestra abajo que
cada dígito es `0` o `1`.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
abbbba
```

```
111111
```

Los nuevos valores son `a`, `b`, `bb`, `bbb`, `bbbb` y `abbbba`; los
seis dígitos son uno. No ocurre con cualquier palabra binaria:
`aababbaa` produce `11111110`, pues su última letra no introduce ningún
valor palíndromo nuevo.

## Solución

### Como máximo un palíndromo nuevo

Una subcadena nueva debe terminar en la nueva posición. Si hubiera dos
sufijos palíndromos nuevos `U,V` con `|U|>|V|`, el sufijo palíndromo `V`
también sería prefijo de `U`. Esa aparición acaba antes, contradiciendo
su novedad. Por tanto, como máximo aparece un valor nuevo y sólo puede
ser el mayor sufijo palíndromo. Hay como máximo `n` nodos de palíndromos
no vacíos.

### Árbol palindrómico binario

Cada nodo representa un palíndromo y guarda su longitud, un enlace a su
mayor sufijo palíndromo propio y dos transiciones: `c` lleva de `P` a
`cPc`. Dos raíces tienen longitud cero y longitud artificial menos uno.
La artificial permite crear palíndromos de una letra y su autoenlace
termina toda búsqueda de ampliación. El nodo cero es artificial y el uno
vacío; una transición cero significa ausente, mientras que los
palíndromos reales empiezan en dos.

Mantener `last`, el mayor sufijo palíndromo del prefijo procesado. Al
añadir `c` en la posición `p`, recorrer enlaces desde `last` hasta el
primer `P` que cumple `p-1-length(P)≥0` y tiene `c` en esa posición. La
raíz artificial siempre funciona. Los candidatos decrecen en longitud,
así que el primer acierto da el nuevo mayor sufijo `cPc`.

Si la transición existe, ese valor ya apareció: emitir cero y reutilizar
el nodo. Si no, crear exactamente un nodo de longitud `length(P)+2`,
registrar la transición y emitir uno. Un nodo de longitud uno enlaza con
la raíz vacía. Para uno mayor, iniciar la misma búsqueda desde
`link(P)`; la transición `c` del candidato hallado es su nuevo enlace.
El interior de cualquier sufijo palíndromo propio es un sufijo
palíndromo propio de `P`, por lo que se encuentra el mayor. El destino
existe, ya que no pueden aparecer dos palíndromos nuevos en un paso.

El interior de cada palíndromo apareció antes de su última letra. Junto
con la representación única `cPc`, esto prueba que las transiciones
identifican exactamente los valores vistos. Por inducción, las búsquedas
mantienen el mayor sufijo y todos sus enlaces correctos. Crear un nodo
equivale a introducir un valor nuevo, de modo que los dígitos son la
respuesta.

### Las dos búsquedas cuestan tiempo lineal total

Sea `F_i` la longitud del mayor sufijo palíndromo tras `i` letras,
`F_0=0`. La primera búsqueda va de `F_(i-1)` a `F_i-2`. Cada enlace
disminuye al menos uno y hay como máximo `F_(i-1)+2-F_i` pasos. La suma
telescópica no supera `2n`.

Sea `G_i` la longitud del mayor sufijo palíndromo propio del actual
mayor, con `G_0=-1`. Un sufijo propio `W` del nuevo mayor, si mide al
menos dos, tiene como interior un sufijo palíndromo del prefijo
anterior. Como `|W|<F_i≤F_(i-1)+2`, el interior es propio del mayor
anterior, de donde `G_i≤G_(i-1)+2`. Las longitudes cero y uno también
cumplen la cota. La segunda búsqueda empieza en longitud como máximo
`G_(i-1)` y termina en `G_i-2`; cuesta como máximo `G_(i-1)+2-G_i`. Los
pasos sin esta búsqueda tienen coste cero, también acotado por esa
expresión no negativa. La suma es `O(n)`. Con transiciones binarias
constantes, todo el árbol, incluida la creación, cuesta `O(n)`.

### Representación y recursos

C++ usa cuatro campos de 32 bits por nodo, no cuatro índices
del tamaño de máquina. Con `n=5000000` los nodos ocupan hasta
`16(n+2)=80000032` bytes; también deben caber entrada, salida y entorno.
Python usa cuatro arrays de enteros fijos, evitando millones de objetos,
y escribe su bytearray sin otra copia completa.

Java usa cuatro campos sin signo de tres bytes, `12(n+2)` bytes. Los
identificadores y `length+1` son menores que `2^23`; longitud más uno
codifica la raíz artificial como cero. Reutiliza los bytes de entrada
para la salida: el bit de valor cuatro no aparece en ASCII `a` ni `b`.
Se activa al crear un palíndromo, se enmascara en comparaciones
posteriores y sólo al terminar toda la palabra se transforma cada marca
en `0`/`1` sobre el mismo espacio. Ya no se necesitan letras originales.
Se escribe únicamente el intervalo original, sin espacios ni capacidad
sin usar.

El árbol, la entrada y la respuesta ocupan O(n); Java reserva un búfer
fijo de 5 000 002 bytes para la entrada. La cadena de dígitos se lee y
escribe entera como bytes, sin formatear millones de números por
separado.

La solución en Python se ejecuta con PyPy: con CPython 3.12 supera el
límite de tiempo en la prueba 9 del juez, mientras que con PyPy 3.10 se
acepta en 0.375 s con 92 MB de los 100 MB. Go y Rust leen la palabra en
un único búfer de tamaño fijo, marcan en él la respuesta como los demás
y guardan el árbol en cuatro arreglos de enteros de 32 bits, unos 85 MB
en total; sus versiones anteriores no compilaban en el juez.

Contar valores distintos, no apariciones, y excluir el palíndromo vacío.
Crear una transición aporta un uno; reencontrarla no. La segunda
búsqueda empieza en el enlace del padre. La longitud artificial lógica
es menos uno; el formato compacto usa un desplazamiento explícito.
Evitar campos de índices de 64 bits, una copia UTF-16 de toda la palabra
y otra copia completa de la salida Python. Ejemplos pequeños con sólo
unos no reemplazan casos con ceros y cadenas largas de fallos de
enlaces.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2040_strings.cpp](2040_strings.cpp) | G++ 13.2 x64 | strings | O(n+N) | AC | 0.125 s | 88880 KB |
| [2040_strings.go](2040_strings.go) | Go 1.14 x64 | strings | O(n+N) | AC | 0.109 s | 87324 KB |
| [2040_strings.java](2040_strings.java) | Java 1.8 | strings | O(n+N) | AC | 0.390 s | 69240 KB |
| [2040_strings.py](2040_strings.py) | PyPy 3.10 x64 | strings | O(n+N) | AC | 0.375 s | 93844 KB |
| [2040_strings.rs](2040_strings.rs) | Rust 1.75 x64 | strings | O(n+N) | AC | 0.109 s | 83068 KB |
