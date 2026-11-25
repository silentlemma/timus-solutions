# 1941. Ventanas con un multiconjunto dado

[Timus 1941](https://acm.timus.ru/problem.aspx?space=1&num=1941) · difficulty 432 · two_pointers

Original problem from Open Ural FU Personal Contest 2012 | by Andrey Demidov (prepared by Alex Samsonov).

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada letra es una terna ordenada de símbolos ASCII de códigos 33 a 122
inclusive: hay 90³=729000 letras. Dado un patrón no vacío de m≤8000 letras
y un texto no vacío de n≤500000 letras, contar ventanas contiguas que
sean permutaciones del patrón. Importan las multiplicidades y el orden
interno de la terna; las ventanas pueden solaparse. Límites: 1 segundo, 64 MB.

## Entrada

La primera línea contiene el patrón y la segunda el texto. Una letra
son tres símbolos adyacentes; espacios separan letras. El final de la
primera línea fija m. No se proporcionan m ni n por separado.

## Salida

Un entero: número de ventanas válidas. Si m>n, la respuesta es 0.

## Evaluación

Se compara un entero; los espacios son insignificantes.

## Ejemplos

```
aaa bbb ccc
aaa aaa bbb ccc aaa zzz aaa bbb ccc
```

```
3
```

## Solución

Codificar (a,b,c) como ((a−33)·90+(b−33))·90+(c−33). Son dígitos
0..89, una biyección a 0..728999, no un hash. Iniciar una tabla con
signo D de 729000 déficits con las frecuencias del patrón, un anillo
de m códigos y missing=m.

Antes de insertar una letra, retirar la más antigua si el anillo está
lleno. Al retirar x, incrementar missing si D[x]≥0 antes del cambio;
después incrementar D[x]. Al insertar y, reducir missing si D[y]>0,
y después reducir D[y]. Reemplazar la posición del anillo y avanzar
cíclicamente. Contar cuando missing=0. Antes de llenar m posiciones,
menos de m letras no pueden cubrir m ocurrencias, por lo que no se cuenta.

El invariante es D[x]=frecuencia_patron[x]−frecuencia_ventana[x], y
missing=Σ max(D[x],0). Retirar crea un déficit exactamente si D[x]≥0;
insertar llena uno exactamente si D[y]>0. Se conserva el invariante.
En una ventana llena ambas sumas de frecuencias son m, por lo que
missing=0 equivale a todos los déficits nulos, es decir, multiconjuntos
iguales. Cada ventana se visita una vez, incluidos solapamientos y final.

Con U=729000, tiempo O(U+m+n), espacio del núcleo O(U+m). C++ y Java
procesan el texto como flujo; Python, Go y Rust conservan la entrada,
con espacio total O(U+m+n). La respuesta≤max(0, n−m+1)≤500000 cabe en 32 bits
con signo.

Las letras son ternas, no símbolos ASCII sueltos; reordenar una terna
la cambia. Un conjunto sin cantidades no basta. Retirada usa ≥0,
inserción >0, antes del cambio. Incluir solapamientos y ventana final;
no desplazar el anillo completo ni recorrer todo el alfabeto en cada paso.
Si m>n no hay ventanas (prueba 03), por lo que la cota superior debe
tomar el máximo con cero.

## Soluciones optimizadas

`1941_two_pointers_optimized.py`. Conserva códigos exactos de tripletes base90 y el mismo invariante de ocurrencias faltantes. Usa listas Python para los 729000 déficits y el anillo, en vez de celdas array compactas, evitando conversiones por actualización. Lee tokens con split en búfer de 16 KiB, sin retener todo el texto. Antes de actualizar, quitar comprueba deficit>=0 y añadir deficit>0. Tiempo O(U+m+n), estado O(U+m) más búfer acotado, U=90^3. Es un intercambio exacto de representación/E/S, no hash ni nuevo algoritmo de ventana; conserva las bases.

Accepted exacto PyPy 3.10 x64 #11326701: 0.234 s / 17756 KB. Comparación guardada del 2026-11-20 de compiladores Python actuales: tiempo 2/16, memoria 2/16; ambas metas estrictas de diez primeros pasan. Desde 1024 KB se exigen tiempo y memoria. No cumple la meta propia de primero en ambas: conserva el asterisco. Registro optimizado CPython 3.12 anterior #11314998: 0.89 s / 8604 KB. El PyPy elegido registra menor tiempo pero más memoria; son pares independientes en intérpretes distintos, sin atribuir toda mejora al algoritmo ni mezclar mínimos. La base CPython conservada tiene Accepted actual #11327563: 0.781 s / 33640 KB. No necesita copia extra ni reenvío.

Accepted propios tras cambiar solo formato: `1941_two_pointers.py` #11327563. Conserva algoritmos básicos y todos los demás fuentes.

Go, Python y Rust mantienen la codificación exacta base 90 y el invariante de ocurrencias faltantes. En Go y Rust, las frecuencias del patrón y ventana están en 0..m, m≤8000: déficits compactos de 16 bits con signo reducen la tabla de 729000 posiciones a 1458000 bytes; sus anillos usan códigos exactos de 32 bits. Go y Rust leen con búferes acotados: espacio total O(U+m). Python guarda déficits y anillo en listas de enteros, intercambiando más memoria por actualizaciones más rápidas; lee tokens con búfer acotado de 16 KiB, estado O(U+m) más entrada acotada. Antes de actualizar, quitar comprueba ≥0 y añadir >0. El primer salto sigue separando patrón y texto, también con CRLF. Se conservan las bases; C++ y Java reutilizan las admitidas en el conjunto rápido.

Las bases Accepted conservadas [1941_two_pointers.cpp](1941_two_pointers.cpp), [1941_two_pointers.java](1941_two_pointers.java) cumplen diez primeros o 15% superior en las métricas exigidas de la comparación guardada, sin copias optimizadas idénticas. La tabla contiene pares actuales exactos; el asterisco indica la meta propia del lenguaje. El formato no cambia algoritmos ni recibe crédito por mejoras de velocidad.

## Notas por lenguaje

Estas notas describen las implementaciones sencillas.

Los déficits necesitan signo para representar exceso. Python usa un
array compacto signed int; Go usa int32 y campos de bytes; Java analiza
ternas directamente sin un String por letra. Rust guarda la entrada
una vez e itera sus segmentos. No hay huellas probabilísticas ni mapas.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1941_two_pointers.cpp](1941_two_pointers.cpp) | G++ 13.2 x64 | two_pointers | O(U+m+n) | AC | 0.046 s | 2996 KB | 11291874 |
| [1941_two_pointers.go](1941_two_pointers.go) | Go 1.14 x64 | two_pointers | O(U+m+n) | AC | 0.062 s | 21096 KB | 11291875 |
| [1941_two_pointers.java](1941_two_pointers.java) \* | Java 1.8 | two_pointers | O(U+m+n) | AC | 0.187 s | 3336 KB | 11291879 |
| [1941_two_pointers.py](1941_two_pointers.py) | Python 3.12 x64 | two_pointers | O(U+m+n) | AC | 0.781 s | 33640 KB | 11327563 |
| [1941_two_pointers.rs](1941_two_pointers.rs) | Rust 1.75 x64 | two_pointers | O(U+m+n) | AC | 0.031 s | 6000 KB | 11291881 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1941_two_pointers_optimized.go](1941_two_pointers_optimized.go) | Go 1.14 x64 | two_pointers | O(U+m+n) | AC | 0.031 s | 1864 KB | 11315003 |
| [1941_two_pointers_optimized.py](1941_two_pointers_optimized.py) | PyPy 3.10 x64 | two_pointers | O(U+m+n) time; O(U+m) space plus bounded input | AC | 0.234 s | 17756 KB | 11326701 |
| [1941_two_pointers_optimized.rs](1941_two_pointers_optimized.rs) \* | Rust 1.75 x64 | two_pointers | O(U+m+n) | AC | 0.015 s | 1364 KB | 11315010 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
