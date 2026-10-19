# 2059. Comparar frecuencias de palíndromos

[Timus 2059](https://acm.timus.ru/problem.aspx?space=1&num=2059) · difficulty 1487 · strings

Problema original de Mikhail Rubinchik, del Concurso Palindrómico del 11 de julio de 2015.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Para dos palabras A y B, considerar cada palíndromo distinto que
aparezca en alguna de ellas. Contar los palíndromos que aparecen más
veces en A, los que aparecen igual número de veces en ambas y los que
aparecen más veces en B. Las apariciones pueden solaparse y las
mayúsculas importan. Los límites son 1 segundo y 64 MB.

## Entrada

El número de pruebas T y después, para cada prueba, dos líneas con A y
B. Cada palabra no está vacía y tiene a lo sumo 200 000 caracteres; la
entrada completa ocupa como mucho 8 MB.

## Salida

Para la prueba i, la línea `Case #i: x y z` con los tres números.

## Evaluación

Un comprobador compara los tres números de cada caso; los espacios entre
ellos no importan.

## Ejemplos

```
3
abacab
abccab
faultydogeuniversity
hasnopalindromeatall
abbacabbaccab
youmayexpectedstrongsamplesbutnow
```

```
Case #1: 4 1 2
Case #2: 8 3 9
Case #3: 13 0 15
```

En la primera pareja, `a,aba,aca,bacab` aparecen más en `abacab`; `b`
aparece dos veces en ambas; `c` y `cc` aparecen más en `abccab`. Resulta
`4 1 2`. La segunda pareja contiene 20 palíndromos distintos en la
unión, repartidos como `8+3+9`, y la tercera contiene 28, como
`13+0+15`. Hay que contar solapamientos: `aaaa` contiene `aa` tres
veces, y comparar `aaaa` con `aaa` da `4 0 0`.

## Solución

### Un árbol palindrómico compartido

Cada nodo real representa un palíndromo distinto; hay además dos raíces
auxiliares de longitudes `−1` y `0`. Una transición con carácter `c`
transforma el palíndromo interior `P` en `cPc`; desde la raíz impar crea
una sola letra `c`. Cada nodo guarda su longitud, `link` al mayor sufijo
palindrómico propio y una lista dispersa de hijos.

Recorrer `A` de izquierda a derecha. Desde el anterior mayor sufijo
palindrómico, seguir enlaces hasta que el carácter nuevo pueda rodear el
palíndromo. Seguir o crear la transición correspondiente. Para un nodo
nuevo, buscar su enlace de la misma forma desde el enlace de su padre.
Comprobar el límite izquierdo de la palabra actual antes de leer el
carácter anterior.

Después recorrer `B` conservando nodos y transiciones, pero reiniciar el
sufijo activo en la raíz vacía y usar el límite de `B`. Así los
palíndromos iguales comparten nodos sin crear apariciones que crucen la
frontera entre palabras. Las versiones compiladas tienen dos contadores
por nodo inicialmente cero. En cada posición incrementar solo el contador
del sufijo máximo, correspondiente a la palabra actual.

### Recuperar todas las frecuencias

Procesar los nodos reales en orden decreciente de creación. Añadir ambos
contadores de `v` a los correspondientes de `link[v]`. Comparar después
los dos contadores de `v` e incrementar una de `x,y,z`. Las raíces
auxiliares nunca se clasifican.

Python guarda la diferencia con signo en lugar de dos contadores:
suma `+1` al recorrer `A` y `−1` al recorrer `B`, y propaga esa
diferencia por los enlaces en el mismo orden inverso. Su signo elige
`x,y,z`. La resta conmuta con la propagación, de modo que equivale a
comparar las dos frecuencias completas.

El palíndromo interior y los dos caracteres exteriores iguales
determinan una única cadena. Por ello un nodo compartido corresponde a
un palíndromo distinto, no a una aparición. Solo el mayor sufijo
palindrómico puede ser nuevo en una posición: todo sufijo menor también
aparece antes como prefijo de ese mayor palíndromo. Hay como máximo
`|A|+|B|+2` nodos, y el sufijo propio de un nodo nuevo ya tiene un
identificador anterior.

Fijar una posición final. Cada aparición palindrómica terminada allí
figura una vez en la cadena de enlaces desde el sufijo máximo. Colocamos
inicialmente una marca solo en la cabeza; la propagación la envía una
vez a cada ancestro. Cada nodo recibe así una marca por cada posición
final de su palíndromo, que es exactamente su número de apariciones.
Posiciones finales distintas siguen separadas aunque sus apariciones se
solapen. Los enlaces apuntan a nodos anteriores, así que el orden
decreciente procesa descendientes antes que ancestros y demuestra ambos
contadores. Todo nodo real apareció en alguna palabra, por lo que
contadores iguales son positivos. La clasificación final cuenta
exactamente las cadenas requeridas.

### Varias pruebas y detalles

Reutilizar los arreglos entre pruebas. Limpiar las cabezas de hijos y
los contadores de las raíces; al asignar cada nuevo identificador
activo, inicializar todos sus campos, incluidos hijos y ambos
contadores. Las posiciones antiguas inaccesibles no afectan al árbol
nuevo. Python reinicia un contador de diferencia por nodo, guarda la
longitud más uno en `span`, antepone un byte cero a cada palabra y usa
transiciones indexadas directamente por byte para las dos raíces.
Una pareja de letras es un caso base: letras iguales dan `0 1 0`;
distintas, `1 0 1`.

Python también trata directamente parejas de palabras formadas por una
sola letra repetida o parejas de palabras alternantes de período dos.
En una palabra alternante, cada letra inicial define una familia de
palíndromos impares cuyas frecuencias disminuyen en uno cuando la longitud
aumenta en dos. Alfabetos iguales de dos letras
comparten esas familias; alfabetos distintos solo pueden compartir
palíndromos de una letra. Si ninguna palabra contiene un palíndromo de
longitud dos o tres, basta contar letras: todo palíndromo mayor tiene
uno de esos palíndromos en el centro. Para palabras idénticas, Python
construye solo un árbol y cuenta sus nodos reales, todos empatados.
También reutiliza la respuesta anterior si se repite la pareja, o
intercambia `x,z` si se invierte. Estos atajos conservan las frecuencias
y no cambian la complejidad en el peor caso.

Con un alfabeto de tamaño `σ`, buscar una transición examina como máximo
`σ` hijos. Una pareja cuesta `O(σ(|A|+|B|))`: las búsquedas de sufijos
suman trabajo lineal por amortización de las disminuciones de longitud,
ya que una extensión aumenta las longitudes pertinentes como máximo dos.
La propagación también es lineal. Para un alfabeto fijo de bytes es
`O(|A|+|B|)`, con `O(|A|+|B|)` nodos activos. Las versiones compiladas
reservan una vez hasta `400002` posiciones; Python crece hasta la mayor
pareja encontrada. La inicialización no se repite en cada prueba
diminuta. Todos los contadores caben en enteros con signo de 32 bits.

C++ lee líneas del flujo de entrada. Python conserva la entrada en
`BytesIO` y lee sus palabras por líneas. Go y Java mantienen un búfer de
entrada de hasta 8 MiB; Rust también conserva la entrada. La salida se
divide en bloques acotados, evitando guardar casi dos millones de
respuestas a la vez. Python reutiliza arreglos compactos.

No comparar identificadores de dos árboles separados, porque no
identifican la misma cadena entre árboles distintos. Reiniciar el sufijo
activo al comenzar `B`. Marcar solo el sufijo máximo: incrementar toda
su cadena y luego propagar contaría dos veces. Respetar el orden
topológico inverso, excluir raíces vacías, contar solapamientos y
comparar frecuencias completas en lugar de solo presencia. Reiniciar
ambos contadores al reciclar un nodo. Considerar los 8 MB totales,
además de la longitud individual.
Con el contador con signo de Python, cero significa frecuencias iguales,
no ausencia: solo se clasifican nodos reales creados. Por ejemplo, la
prueba `002` compara `abba` consigo misma y exige `0 4 0`. El generador
debe emitir LF también en Windows: la expansión a CRLF hace que
`max_many_single_letters` y `max_many_varied_single_letters` superen el
límite total de entrada.

## Notas por lenguaje

La solución en Python se ejecuta con PyPy: con CPython 3.12 supera el
límite de tiempo en la prueba 2 del juez, mientras que con PyPy 3.10 se
acepta en 0.75 s.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2059_strings.cpp](2059_strings.cpp) | G++ 13.2 x64 | strings | O(n + m) | AC | 0.250 s | 12020 KB |
| [2059_strings.go](2059_strings.go) | Go 1.14 x64 | strings | O(n + m) | AC | 0.218 s | 20668 KB |
| [2059_strings.java](2059_strings.java) | Java 1.8 | strings | O(n + m) | AC | 0.296 s | 24520 KB |
| [2059_strings.py](2059_strings.py) | PyPy 3.10 x64 | strings | O(n + m) | AC | 0.750 s | 30004 KB |
| [2059_strings.rs](2059_strings.rs) | Rust 1.75 x64 | strings | O(n + m) | AC | 0.125 s | 22364 KB |
