# 2039. Cuadrados formados por líneas negras completas

[Timus 2039](https://acm.timus.ru/problem.aspx?space=1&num=2039) · dificultad 5501 · two_pointers, bitmask

Problema original de Kirill  Borozdin , preparado por Oleg Merkurev, del concurso Dandelion de la UrFU, campamento de Petrozavodsk, verano de 2014.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dada una matriz binaria `n × m` y un entero positivo `k`, contar
regiones cuadradas contiguas con exactamente `k` filas totalmente negras
y exactamente `k` columnas totalmente negras. Todas las celdas fuera de
la unión de esas líneas deben ser blancas. Las líneas elegidas no tienen
que ser consecutivas. Dos cuadrados son distintos si cambia su esquina
superior izquierda o su lado.

## Entrada

La primera línea contiene `n,m,k`, cada uno entre 1 y 1000. Siguen `n`
líneas con exactamente `m` caracteres binarios: `0` es blanco y `1` es
negro. `k` puede superar cualquiera de las dimensiones. Límites: 0,5
segundos y 64 MB.

## Salida

Un entero: el número de cuadrados válidos. Un lado menor que `k` es
imposible; con lado `k` sólo sirven los cuadrados totalmente negros. Los
mayores deben contener blanco. Si `k>min(n,m)`, la respuesta es cero.
Hay como máximo 333833500 cuadrados en cualquier matriz permitida; un
acumulador de 64 bits resulta cómodo, aunque esta cota también cabe en
32 bits con signo.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
5 6 2
010100
111111
010100
111111
010100
```

```
7
```

En coordenadas desde uno `(fila,columna,lado)`, las siete regiones son
`(2,2,3)`, `(1,1,4)`, `(1,2,4)`, `(2,1,4)`, `(2,2,4)`, `(1,1,5)` y
`(1,2,5)`. En la de lado tres, la fila y columna centrales son blancas
salvo los cruces con las dos líneas negras completas de la otra
dirección. Las ventanas de lados cuatro y cinco siguen teniendo
exactamente dos líneas completas en cada dirección. No existe una
ventana totalmente negra de lado dos. Por tanto, `1+4+2=7`.

## Solución

### Una propiedad hereditaria

Llamamos correcta a la forma si las celdas blancas son un producto
cartesiano `R×C`, donde `R` son las filas con blanco y `C` las columnas
con blanco. En el caso totalmente negro ambos conjuntos están vacíos.
Equivalentemente, todas las filas con algún blanco tienen el mismo
patrón de columnas blancas. Esto describe precisamente la unión de
líneas negras completas antes de fijar sus cantidades.

Si el producto blanco no es vacío y el lado es `s`, las cantidades de
líneas negras son `s-|R|` y `s-|C|`. La propiedad `P` exige la forma
correcta y ambas cantidades como máximo `k`. Todo subcuadrado la hereda.
Si conserva blanco, sus líneas negras son subconjuntos de las del padre.
Si se vuelve totalmente negro, todas sus filas o todas sus columnas
deben ser líneas negras elegidas del padre: de otro modo una fila blanca
y una columna blanca se cruzarían dentro. Su lado es entonces como
máximo `k`, por lo que también cumple las cotas.

### Una ventana por diagonal

C++, Go, Rust y Java recorren las esquinas inferiores derechas por
diagonales de noroeste a sureste. Un puntero inicial representa el mayor
sufijo cuadrado con `P` y sólo avanza. Un cuadrado inválido no puede
repararse al crecer, por herencia; quitar la fila superior y columna
izquierda de la ventana anterior y reintentar encuentra la nueva ventana
máxima. Hay `O(nm)` ampliaciones y eliminaciones en total.

No hace falta guardar todos los conjuntos `R,C`: bastan la última fila
blanca `pr`, última columna blanca `pc` y las dos cantidades de líneas
negras; ambos pivotes están ausentes en la ventana totalmente negra. Al
añadir la fila inferior sobre las columnas anteriores, su patrón blanco
debe ser vacío o igual al de la fila pivote restringida. Si antes no
había blanco, cualquier patrón inicia un producto. Después se añade la
columna derecha sobre todas las filas, incluida la nueva, con la
comparación análoga contra la columna pivote. Se actualizan los pivotes
a las últimas posiciones blancas. Si el producto ya existía, la celda
del pivote opuesto clasifica la nueva fila o columna. Si aparece blanco
por primera vez, la única nueva fila o columna blanca y su cantidad de
unos determinan directamente las cuentas. Sólo se confirma la ampliación
cuando ambas cuentas son como máximo `k`.

Si falla, se reduce la ventana anterior, sin conservar una ampliación
parcial. Si se elimina la fila `pr` o columna `pc`, desaparece
completamente un factor del producto blanco y el resto queda negro. En
otro caso permanecen los pivotes y una cuenta disminuye exactamente
cuando la línea eliminada era negra en el pivote opuesto. Así se
conservan forma, últimas posiciones blancas y cuentas.

Sea `t` el desplazamiento del extremo por la diagonal y `a` el inicio de
su ventana máxima. Todas las respuestas con ese extremo están dentro. El
sufijo de lado `k` aporta uno si cabe y al menos un pivote blanco queda
antes de su frontera: entonces el producto blanco no lo intersecta.

Para lados mayores, reducir la ventana no añade líneas negras elegidas.
Sólo puede haber respuesta cuando ambas cuentas actuales son `k` y queda
blanco. Sean `fr,fc` las primeras líneas negras elegidas, medidas como
desplazamientos de la diagonal. El inicio debe cumplir
`a≤x≤min(t-k,fr,fc,pr,pc)`, convirtiendo también los pivotes a
desplazamientos. Conservar la primera fila elegida conserva todas;
conservar la última fila blanca deja al menos una blanca. Lo mismo vale
para columnas. Las condiciones son necesarias y suficientes: sumar el
número de enteros del intervalo cuenta las respuestas. Cada cuadrado
tiene un extremo único y se cuenta una vez.

Ambas cuentas deben ser exactamente `k`; una celda negra extra invalida
el cuadrado aunque las cuentas coincidan. Separar el lado negro `k` de
los cuadrados mixtos mayores. Comprobar la columna nueva después de
añadir la fila, y no conservar media ampliación fallida. Borrar ambos
pivotes al desaparecer un factor blanco.

### Python: reducir el tablero

Python empieza descartando dimensiones menores que `k`. En un tablero
negro sólo cuentan los cuadrados de lado `k`; en uno blanco, la
respuesta es cero. En los demás casos recorta al rectángulo que encierra
todas las celdas negras. Como `k` es positivo, cada fila y cada columna
de una respuesta contiene negro, así que ninguna respuesta puede salir
de ese rectángulo.

Si cada fila es totalmente negra o coincide con un único patrón común,
un cuadrado mayor se determina mediante dos ventanas independientes: una
de filas con exactamente `k` filas completas y otra de columnas con
exactamente `k` unos del patrón. Para cada lado se multiplican ambas
cantidades. Cada grupo de `k` unos consecutivos describe las ventanas
que incluyen sus extremos y excluyen los unos vecinos. La cantidad de
posiciones en función de la longitud tiene forma de trapecio y se
acumula con segundas diferencias. El lado `k` se cuenta aparte mediante
rachas de filas o columnas completas, restando su intersección una vez.

Con pocos patrones distintos y sin filas completas, el programa también
intenta separar las celdas negras en componentes de un grafo bipartito
cuyos vértices son filas y columnas. Sólo aplica la recursión si cada
componente ocupa filas consecutivas y columnas consecutivas. Las líneas
negras elegidas de un cuadrado válido conectan todos sus vértices de
fila y columna, de modo que pertenece a un único rectángulo. Por eso se
pueden sumar las respuestas de los componentes.

Otro atajo trata tableros anidados: tras invertir el orden de filas o
columnas si hace falta, cada fila es un prefijo negro seguido de blanco,
y las longitudes de los prefijos no decrecen. Los cuadrados negros de
lado `k` se cuentan a partir del prefijo más corto de cada ventana de
filas. En una respuesta mayor, varias filas mínimas iguales van seguidas
de exactamente `k` filas más largas. Exigir exactamente `k` columnas
negras fija el borde izquierdo. La cantidad de filas mínimas determina
el lado y está limitada por el tamaño de su grupo, la diferencia con la
siguiente longitud de prefijo y la anchura restante. Cada cantidad
admisible da un cuadrado, sin recorrer todos los lados.

El tablero restante puede transponerse si una estimación del trabajo
basada en los cambios de patrón favorece la otra orientación. La
transposición conserva los cuadrados y ambas cantidades de franjas. Tras
obtener una cota segura para el lado, los intervalos cortos usan
contadores paralelos; los largos con `k > 1`, una descomposición fuera
de línea; `k = 1` tiene un método propio.

### Python: contadores paralelos y cotas seguras

Fijado el lado `s`, un cuadrado sirve exactamente cuando tiene `k` filas
completas, `k` columnas completas y cada fila contiene `k` o `s` celdas
negras. Las columnas completas ya aportan las `k` celdas negras de cada
fila no completa, por lo que no puede haber ninguna celda negra
adicional.

Todo el tablero se guarda en un entero grande, con un bit por celda. Los
desplazamientos y AND encuentran segmentos horizontales y verticales
completos; duplicar la longitud evita examinar sus celdas una a una. Los
dígitos binarios de los contadores se guardan en enteros separados para
contar marcas en todas las ventanas a la vez. XOR da el dígito de la
suma y AND el acarreo: combinar bloques desplazados realiza la suma
binaria exacta de forma independiente en cada posición. Intersectar los
planos de bits según los dígitos de `k` comprueba la igualdad. Las
cuentas de filas y columnas completas, junto con la condición de cada
fila, producen una máscara exacta de respuestas. Otras máscaras
descartan inicios que salen del tablero; el recuento de bits suma las
respuestas.

Antes de contar, unas condiciones locales necesarias acotan el lado. Un
producto cartesiano blanco no admite tres celdas blancas ni dos blancas
en diagonal en un bloque adyacente `2×2`. Una respuesta mayor que `k` no
puede contener un cuadrado negro de lado `k+1`. Para `k` pequeño también
se excluyen bloques de lado `2k+1` con demasiadas filas o columnas
completas. Las tablas de cuadrados de lados potencia de dos comprueban
la ausencia de esos bloques mediante cuatro bloques de esquina
solapados. Se descartan las ventanas blancas porque `k` es positivo. La
existencia de un candidato mixto restante es monótona respecto al lado:
un cuadrado menor en una esquina puede conservar dos celdas adyacentes
de distinto color y hereda las exclusiones. Por tanto, la búsqueda
binaria da una cota superior segura, pero no decide si un candidato es
una respuesta.

Al procesar intervalos de lados, el recorte conserva todas las posibles
filas y columnas completas con longitud suficiente para el lado mínimo,
dejando margen para el máximo. Toda respuesta contiene esas líneas, así
que fuera del recorte no puede haber contribuciones. Las máscaras vacías
y las dimensiones insuficientes permiten terminar el recorrido sin
perder respuestas. Los contadores exactos siguen comprobando cada
candidato restante.

### Python: descomposición fuera de línea para `k > 1`

Para intervalos largos, el programa evita repetir los contadores en cada
lado. El lado `k` corresponde a cuadrados negros. El lado `k+1` exige
exactamente una celda blanca: las demás filas y columnas son
precisamente sus `k` franjas negras. Ambos casos se cuentan con máscaras
paralelas que, al combinar bloques disjuntos, registran si no hay blanco
o hay como máximo una celda blanca.

Para lados mayores, primero se certifica la forma de cada bloque
interior de lado `k+2`. Con `k` pequeño, cada par de filas debe tener el
mismo patrón blanco salvo que alguna sea completa, y se prohíben los
bloques negros de lado `k+1`. En el otro caso, la unión de columnas
blancas debe tener el mismo tamaño que cada fila con blanco, lo que
obliga a que esos conjuntos coincidan; al menos dos filas y dos columnas
deben contener blanco. Toda respuesta pasa la prueba correspondiente.
Los bloques certificados adyacentes comparten blanco en su solapamiento,
así que sus productos cartesianos concuerdan y se extienden a un solo
producto sobre todo el cuadrado. Una programación dinámica de cuadrados
da el mayor lado que satisface los certificados en cada inicio. Cada
fila de estados se calcula con mínimos empaquetados y distancias al
siguiente certificado fallido.

Entre las primeras `k+1` filas de una respuesta hay al menos una que no
es una franja. Su intersección de bits da, por tanto, exactamente las
columnas completas. La intersección de las primeras `k+1` columnas
identifica de igual modo las filas completas. Para cada inicio, la
posición de la línea elegida número `k` da una cota inferior inclusiva
del lado, y la siguiente línea da una cota superior inclusiva: la
ventana debe incluir la primera y excluir la siguiente. Se intersectan
los intervalos de filas y columnas con la cota de forma y el mínimo
`k+2`, y se suma la longitud del intervalo resultante. Cada lado contado
tiene la forma certificada y las cantidades exactas; cada respuesta
aparece en su único inicio.

Las posiciones sucesoras se obtienen de rachas o rangos empaquetados, y
los patrones repetidos reutilizan los mismos vectores exactos de
extremos. Los cambios pequeños pueden actualizar sólo los rangos
afectados. Extremos y cotas ocupan campos separados con bits de
protección dentro de enteros grandes, para calcular mínimos, máximos y
longitudes de intervalos de muchas columnas a la vez. Los campos admiten
todas las coordenadas permitidas y las máscaras evitan que un acarreo o
préstamo entre campos altere el resultado. Todo es exacto, sin
comparaciones probabilísticas. Si los certificados dejan un intervalo
corto, se vuelve a los contadores paralelos.

### Python: una franja y su cruce único

Para `k = 1`, cada celda negra aporta una respuesta de lado uno. Los
demás lados pequeños se agrupan en intervalos. En el lado mínimo de cada
intervalo, las máscaras encuentran exactamente una fila y una columna
completas, con certificados locales de forma para lados mayores que dos.
Estas condiciones bastan: la forma certificada obliga a que cada fila no
completa sólo tenga la celda negra de la columna completa. Todo cuadrado
mayor con una franja contiene otro menor con el mismo cruce, así que las
máscaras localizan todas las regiones que pueden contribuir en el
intervalo. Los grupos de filas con candidatos se amplían con los
márgenes necesarios; los recortes de grupos distintos son disjuntos.
Dentro de cada recorte, la fórmula del patrón común o los contadores
paralelos cuentan sólo los lados del intervalo.

Para lados grandes, un lado menor fijo proporciona los cruces
candidatos. Cada cuadrado que pasa las pruebas tiene un único cruce de
su fila y columna completas; mirar otra columna permite identificar la
fila completa. Un conjunto elimina los cruces repetidos que aparecen en
varios cuadrados menores. Toda respuesta mayor contiene uno de esos
cuadrados con el mismo cruce, así que no se pierde ningún cruce
necesario.

Para cada cruce, las rachas negras que lo atraviesan delimitan todas las
respuestas posibles. Dentro de esos límites se borran su fila y su
columna. Un cuadrado que contiene el cruce es válido exactamente cuando
las demás celdas son blancas. Una programación dinámica empaquetada
encuentra el mayor cuadrado vacío en cada esquina superior izquierda.
Las distancias necesarias para incluir el cruce dan la cota inferior del
lado; el tamaño del cuadrado vacío y el intervalo solicitado dan la
superior. Sumar las longitudes de los intervalos enteros cuenta todas
las respuestas de ese cruce. Borrar las líneas es correcto porque los
límites de las rachas ya garantizan que ambas eran negras. La unicidad
del cruce impide contar un cuadrado dos veces.

## Notas por lenguaje

Sea `L=min(n,m)`. La ventana hace `O(nm)` actualizaciones, pero
búsquedas y comparaciones de bytes pueden leer `O(L)` caracteres. La
cota conservadora de C++/Go/Rust es tiempo `O(nmL)` y espacio `O(nm)`.
Java usa bloques exactos de 64 bits, máscaras de bordes, cuentas de bits
y tablas prefijas de las últimas posiciones blancas: tiempo `O(nmB₆₄)` y
espacio `O(nm)`, con `B₆₄=ceil(max(n,m)/64)`. El desplazamiento de 64 se
trata por separado.

Para Python, sea `D=max(n,m)` y sea `B` el número de palabras de máquina
necesario para una fila empaquetada con `D` campos de coordenadas y sus
bits de protección. Con el límite de coordenadas del problema, ocupa
`O(D)` bits. Cobrando conservadoramente `O(B²)` por multiplicar o
dividir esos enteros, y usando el coste amortizado habitual de los
diccionarios, una cota para todas las ramas es tiempo `O(nm(nm+DB²))` y
espacio `O(nm+DB log(L+1))`.

Esta cota de tiempo, deliberadamente amplia, permite hasta `nm` cruces
distintos, cada uno con un recorrido de como máximo `nm` celdas y `D`
filas empaquetadas a coste `O(B²)` por fila. También cubre la
preparación fuera de línea, todos los recorridos por lados y la
aritmética cuadrática sobre enteros del tamaño del tablero. Sólo se
procesa un cruce a la vez; las máscaras, vectores de extremos, cachés y
tablas de potencias de dos caben en la memoria indicada. Las reducciones
y las operaciones empaquetadas disminuyen mucho el trabajo real en
muchos tableros.

La solución se ejecuta en CPython y obtuvo Accepted en Timus con Python
3.12 x64 en 0.359 s y 21 964 KB, dentro del límite de 0.5 s. Las
versiones anteriores superaron el límite en las pruebas 4, 26 y 24 del
juez; lo que hacía lenta la prueba 24 se encontró comparando los tiempos
de ejecución de dos versiones en muchos tableros generados.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2039_bitmask.py](2039_bitmask.py) | Python 3.12 x64 | bitmask | O(nm(nm+DB^2)) | AC | 0.359 s | 21964 KB |
| [2039_two_pointers.cpp](2039_two_pointers.cpp) | G++ 13.2 x64 | two_pointers | O(nmL) | AC | 0.218 s | 2276 KB |
| [2039_two_pointers.go](2039_two_pointers.go) | Go 1.14 x64 | two_pointers | O(nmL) | AC | 0.234 s | 4436 KB |
| [2039_two_pointers.java](2039_two_pointers.java) | Java 1.8 | two_pointers | O(nmB64) | AC | 0.312 s | 8088 KB |
| [2039_two_pointers.rs](2039_two_pointers.rs) | Rust 1.75 x64 | two_pointers | O(nmL) | AC | 0.265 s | 3368 KB |
