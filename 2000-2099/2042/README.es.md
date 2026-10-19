# 2042. Palíndromos de longitud acotada con asignaciones de subcadenas

[Timus 2042](https://acm.timus.ru/problem.aspx?space=1&num=2042) · difficulty 3245 · strings, segment_tree

Problema original de Nikita Sivukhin, del concurso Dandelion de la UrFU, campamento de Petrozavodsk, verano de 2014.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Mantenga una cadena de letras latinas minúsculas. Una actualización
reemplaza todos los caracteres de un intervalo inclusivo por una misma
letra. Una consulta cuenta las apariciones de subcadenas palíndromas
completamente contenidas en su intervalo y de longitud como máximo un
`k` fijo. Las palabras iguales en posiciones diferentes se cuentan por
separado.

## Entrada

La primera línea contiene la cadena inicial y `k`, con `1≤n≤100000` y
`1≤k≤50`. Sigue `1≤m≤100000` operaciones. `1 l r c` asigna la letra
minúscula `c` a las posiciones `l..r`; `2 l r` pide la cuenta de ese
intervalo. Los índices empiezan en uno y cumplen `1≤l≤r≤n`. Ni la
longitud ni `k` cambian. Límites: 3 segundos y 64 MB.

## Salida

Imprima un entero por consulta, en orden; si no hay consultas, la salida
es vacía. Se comparan los enteros como tokens. Se cuentan pares de
extremos, no valores de palíndromos distintos. Cada respuesta es como
máximo `nk≤5000000`.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
abacaba 4
3
2 1 3
1 1 3 c
2 1 4
```

```
4
10
```

Al principio las tres primeras letras son `aba`: tres letras
individuales y el palíndromo de longitud tres dan `4` apariciones. Tras
asignar `c` a `1..3`, las primeras cuatro letras son `cccc`. Sus
`4+3+2+1=10` subcadenas son palíndromas de longitud no mayor que `4`.

## Solución

### Una cuenta por centro

Usamos índices desde cero. Sean `O=(k+1)//2` y `E=k//2`. `odd[i]` es el
radio impar centrado en el carácter `i`, incluyendo el centro y limitado
a `O`; `even[i]` es el radio par centrado en el hueco justo antes de `i`
y limitado a `E`. Un radio `d` representa `d` longitudes positivas de su
paridad. Por tanto, `p[i]=odd[i]+even[i]` cuenta todas las apariciones
permitidas asignadas al índice de centro `i`.

Calcule radios con Manacher. La inicialización por espejo sigue siendo
válida con un tope: un radio reflejado menor que el tope es exacto hasta
el borde derecho conocido; alcanzar el tope ya entrega el máximo
permitido. Las nuevas comparaciones exitosas avanzan el borde derecho,
así que cada recorrido es lineal.

Mantenga dos árboles de segmentos perezosos. Uno asigna caracteres y
extrae una ventana consecutiva corta. El otro asigna constantes a `p`,
suma intervalos y reemplaza un tramo corto por valores explícitos en un
solo recorrido. Hacer una actualización puntual por centro añadiría un
logaritmo innecesario.

### Reparar solo los bordes de una asignación

Primero asigne los caracteres de `[l,r]`. Un radio solo cambia si su
mayor ventana permitida intersecta ese intervalo. Todos los centros
afectados están en `A=[l-O+1,r+E]`, recortado a la cadena. En
`I=[l+E,r-O+1]`, ambas ventanas máximas quedan totalmente dentro del
intervalo asignado. Todas sus subcadenas son constantes, por lo que se
asigna perezosamente `p=k`.

El resto de `A` tiene como máximo dos partes de hasta `k-1` centros cada
una. Si `I` es vacío, repare todo `A` una sola vez: las partes nominales
pueden solaparse. Para reparar centros `[u,v]`, extraiga caracteres
`[u-E,v+O-1]` recortados globalmente, calcule sus radios acotados y
reemplace solo esos centros. La ventana contiene todos sus posibles
palíndromos permitidos, por lo que sus extremos no recortan una
respuesta válida. Su longitud es `O(k)` aunque la asignación sea larga.

### Contar en una consulta

Si `r-l+1<k`, extraiga todo el intervalo y sume los radios locales
acotados. En otro caso, los centros `[l+E,r-O+1]` tienen todas sus
ventanas dentro de la consulta: use la suma almacenada de `p`. Quedan
`l..l+E-1` y `r-O+2..r`.

Para la parte izquierda extraiga los primeros `k-1` caracteres y sume
solo sus primeros `E` centros. Para la derecha extraiga los últimos
`k-1` caracteres y sume solo sus últimos `O-1` centros. Estas ventanas
cubren todos los palíndromos relevantes y respetan los extremos
consultados. El interior y los dos bordes particionan los índices de
centro, y cada aparición tiene un único centro y paridad. Así se cuenta
cada aparición solicitada exactamente una vez y ninguna que salga del
intervalo. Con `k=1` los dos bordes son vacíos y solo quedan letras
individuales.

### Corrección y complejidad

Tras una construcción inicial correcta, cada asignación restaura todos
los centros que cambian y conserva los demás. La inducción sobre
operaciones prueba el invariante almacenado; la partición de centros
prueba cada consulta. Una ventana corta y su reemplazo cuestan `O(k+log
n)`, y el interior constante largo usa una asignación perezosa. Tiempo
total `O(n+m(k+log n))` y espacio `O(n)`.

Python mantiene otro invariante: `s[i]` y `e[i]` cuentan los palíndromos
permitidos que empiezan y terminan en la posición `i`. En esta
descripción de Python los intervalos son semiabiertos. Un recorrido
guarda una máscara que cabe en una palabra de máquina; el bit `d`
representa un palíndromo de longitud `d+1` que termina en la posición
actual. La máscara anterior se desplaza dos bits, se añaden los
candidatos de longitudes uno y dos y se aplica la intersección con la
máscara de posiciones cuya letra coincide con la actual. En esta última,
el bit `d` está activo exactamente cuando coincide el carácter situado
`d` posiciones atrás. Así, un candidato más largo sobrevive si y solo si
su interior es palíndromo y sus letras extremas coinciden. Se descartan
las longitudes mayores que `k`; una pequeña tabla de conteo de bits da
`e[i]`. El historial de cada letra se desplaza según la distancia desde
su aparición anterior. Recorrer la ventana invertida da `s[i]`.

En una ventana uniforme, las cuentas de extremos son `min(k,t)`, donde
`t` es la cantidad de caracteres disponibles hacia el borde
correspondiente. Las ventanas cortas con dos o tres tramos máximos de
letras iguales también permiten un cálculo directo, empezando por las
cuentas internas de cada tramo. En una ventana de dos tramos, ningún
palíndromo contiene ambas letras. Con tres, un palíndromo con letras
distintas debe contener todo el tramo central y tomar igual cantidad de
letras de los dos tramos exteriores, cuyas letras deben coincidir. Se
añaden exactamente las extensiones que caben a ambos lados y respetan el
límite de longitud. Las demás ventanas usan el recorrido con máscaras.
Las cachés exactas de tamaño acotado reutilizan cadenas cortas de bytes
y sus cuentas inmutables de extremos o sus totales de consulta;
recuperar un resultado no altera su exactitud.

Si la consulta mide menos de `k-1`, todas sus subcadenas ya cumplen el
límite de longitud. Se cuentan las subcadenas internas de cada tramo de
letras iguales mediante su número triangular, y después se expande
simétricamente alrededor de cada tramo completo. Todo palíndromo con
letras distintas tiene un único tramo central de este tipo, así que cada
aparición se cuenta una vez. Si el trabajo de expansión supera un
presupuesto lineal, se descarta el total parcial y se usa el recorrido
con máscaras. El cálculo de una consulta corta sigue siendo lineal.

Los caracteres y las cuentas de extremos se guardan en bytearrays
divididos en bloques de tamaño fijo, con un árbol de segmentos perezoso
sobre las sumas de los bloques. Las sumas de las cuentas de inicios y
finales ocupan campos separados de un mismo entero; cada campo admite la
máxima suma posible, por lo que las adiciones no producen acarreo entre
campos. Una asignación etiqueta los bloques completos con la nueva letra
y fija provisionalmente ambas cuentas en `k`. Antes de leer sus
caracteres o editar parcialmente un bloque etiquetado, se materializa su
contenido. La cuenta vale `k` donde todas las longitudes permitidas
caben en el tramo recién asignado; las demás cuentas afectadas se
reparan en ventanas de longitud `O(k)` junto a los bordes, uniendo las
ventanas si se solapan. Todo palíndromo que cambia intersecta la
asignación y mide como máximo `k`, de modo que estas ventanas contienen
todos los caracteres necesarios y las demás cuentas siguen siendo
válidas. Solo se recalculan las sumas de los bloques reparados.

Para una consulta `[l,r)` de longitud al menos `k-1`, la respuesta es
`sum(e[0:r])-sum(s[0:l])`, obtenida con dos sumas de prefijos del árbol.
Todo palíndromo permitido que empieza antes de `l` también termina antes
de `r`, pues su longitud no supera `k`. La resta elimina exactamente las
apariciones que salen por el borde izquierdo de la consulta; las
restantes quedan completamente dentro. Una consulta de toda la cadena
usa directamente el total almacenado.

Las asignaciones se aplazan hasta que una consulta necesita la
estructura de extremos. Antes del primer uso, se aplican las
asignaciones pendientes a los caracteres y se construyen las cuentas una
sola vez. En lotes posteriores se puede omitir una asignación cubierta
por completo por otras posteriores: solo los caracteres finales importan
para la siguiente consulta aún sin resolver. Un recorrido hacia atrás
registra solo la cobertura de asignaciones largas; ignorar las cortas
puede dejar una escritura redundante, pero nunca eliminar una necesaria.
Los lotes grandes de asignaciones cortas modifican primero los
caracteres en orden, recortando prefijos y sufijos que ya coinciden con
la nueva letra. Un cambio real en `[l,r)` solo afecta las cuentas de
finales en `[l,r+k-1)` y las de inicios en `[l-k+1,r)`, recortadas a la
cadena. Estos intervalos se ordenan y se unen los cercanos; se añaden
los `k-1` caracteres de contexto necesarios y cada región unida se
recalcula una vez sobre la cadena final. El cálculo es exacto incluso si
las asignaciones se solapan, porque todas las reparaciones usan los
caracteres definitivos. Los demás lotes reparan los bordes de cada
asignación por separado. No hace falta procesar asignaciones posteriores
a la última consulta.

Algunas consultas no necesitan reparaciones. Además del último intervalo
asignado, Python mantiene un intervalo que se sabe uniforme: une
asignaciones solapadas o adyacentes de la misma letra o conserva una
nueva asignación o una parte uniforme que sigue intacta. Estas
elecciones mantienen la garantía de que todos sus caracteres son
iguales. Si una consulta queda dentro de cualquiera de los dos
intervalos uniformes conocidos, su respuesta es `dL-d(d-1)/2`, donde `L`
es su longitud y `d=min(k,L)`: se suman `L-j+1` apariciones para cada
longitud `j` de uno a `d`. Con `k=1`, la fórmula vale para toda
consulta, sean cuales sean los caracteres. Estas consultas dejan
aplazadas las asignaciones pendientes.

La cota de Python incluye también el trabajo fuera del árbol. Sea `B` el
tamaño fijo de bloque, al menos `k`. Una asignación puede escribir
`O(n/B)` etiquetas de bloque y reparar `O(B+k)` caracteres; los caminos
del árbol cuestan `O(log n)`. Al filtrar un lote, mantener la unión de
intervalos ya cubiertos también puede recorrer `O(n/B+1)` partes con los
umbrales fijos de la implementación. Ordenar los intervalos afectados
cuesta como máximo `O(m log m)` entre todos los lotes. Una cota total
conservadora es `O(n+m(n/B+B+k+log n+log m))` en tiempo. Caracteres,
cuentas y árboles ocupan `O(n)` espacio; con la entrada almacenada, las
asignaciones pendientes y las respuestas, el espacio total es `O(n+m)`.
Estos costes difieren de la cota anterior para las cuentas por centro.

El centro par está antes de `i`. Recorte ventanas globales, una
reparaciones solapadas y distinga radio de longitud. Cuente apariciones
e incluya todas las letras individuales. Trate `k>n` y la salida vacía.
Restaure la etiqueta de un bloque antes de editarlo parcialmente. No
sustituya el reemplazo corto conjunto por `k` actualizaciones puntuales
separadas.

## Notas por lenguaje

C++, Go y Rust usan arreglos planos y recursión de profundidad
logarítmica. Rust usa aritmética saturada para límites izquierdos e
interiores vacíos. Go 1.14 usa su propio analizador de enteros y salida
con búfer. Java 8 reutiliza los búferes de ventanas, radios y
reemplazos. Python usa máscaras de extremos, un árbol perezoso por
bloques y reparaciones de bordes aplazadas. Las cuentas caben en 32 bits
con signo; Rust usa sumas sin signo de 32 bits. Todas las versiones
convierten los índices una sola vez.

La solución actual de Python se ejecuta con PyPy y obtuvo Accepted en
Timus con PyPy 3.10 x64 en 2,39 s, usando 26 300 KB, dentro del límite
de 3 s. Las versiones anteriores superaron el límite de tiempo en la
prueba 9 del juez con CPython y en las pruebas 14 y 17 con PyPy.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2042_strings_segment_tree.cpp](2042_strings_segment_tree.cpp) | G++ 13.2 x64 | strings, segment_tree | O(n+m(k+log n)) | AC | 0.781 s | 2980 KB |
| [2042_strings_segment_tree.go](2042_strings_segment_tree.go) | Go 1.14 x64 | strings, segment_tree | O(n+m(k+log n)) | AC | 0.921 s | 16428 KB |
| [2042_strings_segment_tree.java](2042_strings_segment_tree.java) | Java 1.8 | strings, segment_tree | O(n+m(k+log n)) | AC | 0.890 s | 8844 KB |
| [2042_strings_segment_tree.py](2042_strings_segment_tree.py) | PyPy 3.10 x64 | strings, segment_tree | O(n+m(n/B+B+k+log n+log m)) | AC | 2.390 s | 26300 KB |
| [2042_strings_segment_tree.rs](2042_strings_segment_tree.rs) | Rust 1.75 x64 | strings, segment_tree | O(n+m(k+log n)) | AC | 0.640 s | 5788 KB |
