# 1977. Crecimiento de energía y reparto triangular

[Timus 1977](https://acm.timus.ru/problem.aspx?space=1&num=1977) · dificultad 2366 · segment_tree, simulation

Problema original de Denis Dublennykh, del Campeonato de Programación Deportiva de los Urales 2013.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay `n` secciones numeradas y un almacén, todos inicialmente sin
energía. Cada sección gana `p` unidades de energía por unidad de tiempo.
Los eventos ocurren en instantes enteros distintos y estrictamente
crecientes. `save l r` traslada al almacén toda la energía del intervalo
inclusivo `[l,r]` e informa del nuevo total almacenado. `enforce i d`
consume todo el almacén: la sección `j` recibe `x(d−|j−i|)` cuando
`|j−i|<d`, con `x=energía almacenada/d²`. Esta energía se suma a la que
ya tenía la sección; después el almacén queda vacío.

Los límites son `1≤n≤10⁹`, `1≤p≤100`, `1≤q≤10⁵` y `0≤t≤10⁹`. Una
recogida cumple `1≤l≤r≤n`; un reparto cumple `1≤d≤min(i,n+1−i)`. Tiempo:
2 segundos. Memoria: 64 MB.

## Entrada

La primera línea contiene `n p`; la segunda, `q`. Siguen `q` líneas `t
save l r` o `t enforce i d`, ordenadas por tiempo.

## Salida

Imprima el total del almacén después de cada recogida. Los repartos no
producen salida.

## Evaluación

Los números se comparan con error absoluto o relativo 10⁻⁶.

## Ejemplos

Entrada:

```
5 1
4
2 save 4 5
3 enforce 2 2
4 save 3 5
5 enforce 3 3
```

Salida:

```
4.000000
9.000000
```

## Solución

Primero leemos los eventos y comprimimos las fronteras donde cambia la
fórmula de una operación. Incluimos `1,n+1`; una recogida aporta
`l,r+1`, y un reparto aporta `i−d+1,i+1,i+d`. Cada hoja representa todas
las secciones enteras entre dos fronteras consecutivas, conservando su
longitud física.

Un árbol de segmentos mantiene las sumas de energía. Cada nodo tiene una
marca de borrado y una función afín pendiente de sumar, representada por
sus valores en la primera y la última sección. Con extremos `a,b` y
longitud `L`, la suma aumenta en `(a+b)L/2`. Entre eventos en tiempos
`s,t`, sumamos la constante `p(t−s)` a la raíz.

Si las longitudes de los hijos son `A,B`, el último valor del hijo
izquierdo es `(aB+b(A−1))/(A+B−1)` y el primero del derecho es
`(a(B−1)+bA)/(A+B−1)`. Estas fórmulas combinan términos no negativos;
las funciones constantes se tratan directamente. La marca de borrado se
propaga antes que las sumas. Representar los extremos evita la
cancelación entre un término de pendiente grande y un término
independiente grande.

Una recogida acumula los totales de los nodos completamente cubiertos y
los borra. Tras visitar solo parte de un nodo, reconstruimos su total
sumando los hijos. Un reparto se divide en una progresión creciente
sobre `[i−d+1,i]` y otra decreciente sobre `[i+1,i+d−1]`. Calculamos
primero los pesos enteros y después los multiplicamos por `energía
almacenada/d²`. Finalmente vaciamos el almacén.

Los pesos suman `1+…+d+(d−1)+…+1=d²`, de modo que se reparte exactamente
toda la energía almacenada. El invariante del árbol establece que el
total de un nodo ya incluye su marca pendiente, que los hijos reciben al
visitarlos. El crecimiento uniforme, la suma de progresiones y la
recogida con borrado preservan ese invariante; por tanto, los totales
comunicados son correctos.

En el ejemplo, la primera recogida suma dos secciones con energía 2 y
obtiene 4. Tras una unidad de crecimiento y el reparto de radio dos, las
energías son `(4,5,4,1,1)`. Una unidad de tiempo después, recoger las
secciones 3–5 aporta `5+2+2=9`. El último reparto no imprime nada.

Con `m=O(q)` intervalos comprimidos, las cuatro versiones compiladas
usan `O(q log q)` tiempo y `O(q)` memoria. El almacenamiento en preorden
necesita exactamente `2m−1` nodos: el hijo izquierdo sigue al padre y el
derecho aparece después de todo el subárbol izquierdo.

### Python: enviar energía a futuras recogidas

El archivo Python `1977_segment_tree_simulation.py` separa el
crecimiento natural de la energía repartida. Solo comprime `1,n+1` y las
fronteras de las recogidas, `l,r+1`. Una recogida siempre toma una celda
comprimida entera o no la toca. Un reparto puede cubrir solo parte de
una celda: basta sumar ese tramo de la progresión aritmética, pues
ninguna recogida posterior distingue sus secciones interiores.

Para la energía repartida, recorremos los eventos hacia atrás y
etiquetamos cada sección con la primera recogida futura que la alcanza,
o sin destino si no vuelve a recogerse. Una recogida sustituye las
etiquetas de su intervalo por la del evento actual. Es correcto porque,
para cualquier evento anterior, esta recogida precede a todos los
destinos ya registrados en ese intervalo. Un árbol de segmentos
persistente comparte las rutas que no cambian entre versiones y condensa
un nodo cuando todo su intervalo tiene el mismo destino. Guardamos la
versión necesaria para cada reparto.

Después procesamos los eventos hacia delante con el saldo real del
almacén. Dividimos cada reparto en sus dos mitades afines y enviamos la
energía por la versión guardada. Un destino único recibe directamente la
suma aritmética; en otro caso, un nodo cubierto por completo acumula los
valores de los extremos. Cuando una recogida pone fin a esa ruta,
distribuimos la función acumulada entre los hijos registrados mediante
la interpolación positiva descrita antes, y luego procesamos los hijos.
Cada aporte llega exactamente a su primera recogida; los aportes sin
destino se pueden descartar. Las versiones sucesivas de un mismo nodo
espacial pueden compartir los búferes numéricos: la versión anterior se
vacía antes de que la siguiente reciba energía.

El crecimiento natural solo necesita un mapa de intervalos con el mismo
instante de última recogida, inicialmente cero. Un tramo de longitud
`L`, recogido por última vez en `s`, aporta `pL(t−s)` en el instante
`t`; después su marca temporal pasa a ser `t`. Dividimos en las dos
fronteras de la recogida y eliminamos las fronteras interiores
sobrescritas. Así contamos exactamente el crecimiento desde la recogida
anterior. Unos conjuntos de bits jerárquicos localizan las fronteras
activas. Cada recogida crea como máximo dos fronteras y cada borrado se
atribuye a su inserción. Si ningún reparto mueve energía no nula, basta
con este mapa.

Antes de construir las rutas persistentes, el programa intenta crear una
lista explícita de transferencias aprovechando que todos los eventos se
conocen de antemano. Un recorrido inverso del mapa de intervalos
encuentra la primera recogida futura de cada tramo de un reparto.
Guardamos una arista hacia esa recogida cuyo peso es la suma entera de
los pesos triangulares del tramo. El mismo recorrido asigna el
crecimiento natural entre recogidas consecutivas, o desde el instante
cero hasta la primera recogida. En orden temporal, multiplicamos cada
peso por el saldo actual del almacén dividido por `d²`. Se envía así la
misma energía a las mismas recogidas que con el árbol de rutas. El
intento tiene límites de trabajo y almacenamiento; si la fragmentación
lo encarece demasiado, se descarta y se usa el método general.

Las partes espaciales pequeñas se simulan directamente. Excluimos las
recogidas de toda la pared al agrupar los intervalos de operaciones que
se solapan en componentes. Si cada componente contiene pocas celdas
comprimidas, guardamos el total de energía repartida y el instante de
última recogida de cada celda, procesando todos los eventos en orden con
un almacén común. Para un reparto sumamos los pesos de su intersección
con la celda. Los totales bastan porque las recogidas no dividen celdas;
entre recogidas de toda la pared, los componentes no tienen interacción
espacial.

Otra vía rápida trata las recogidas que abarcan pocas celdas comprimidas
con un árbol de extremos que acumula sumas pendientes sin mantener
totales de subárboles. Una recogida propaga las marcas, recorre y vacía
su intervalo corto, y calcula el crecimiento a partir de los tiempos de
las celdas visitadas. Obtiene la misma energía que una consulta de suma
y borrado. Al recoger toda la pared, la conservación de energía permite
fijar el almacén en `npt`, toda la energía generada hasta entonces, y
reiniciar el estado de la pared. La simulación por componentes puede
aplazar ese reinicio hasta la próxima visita al componente. La vía para
recogidas estrechas solo se usa si el coste total de los reinicios
completos también está acotado.

Con `m=O(q)` celdas comprimidas, el método general usa `O(q log q)`
tiempo y `O(q log q)` memoria. Cada recogida crea como máximo `O(log m)`
nodos de rutas; cada reparto inserta dos intervalos afines en `O(log
m)`, y cada nodo de rutas propaga su energía una sola vez. Los búferes
numéricos ocupan `O(q)` memoria. Los límites del intento de
transferencias y las comprobaciones de tamaño y trabajo de la simulación
directa conservan estas cotas en el peor caso bajo las restricciones
dadas. Los totales se combinan mediante sumas no negativas y las
funciones afines se dividen por interpolación de extremos. Así se evita
restar grandes cantidades de energía casi iguales.

Trampas:

- El almacén acumula varias recogidas y solo se vacía al repartir.
- El crecimiento precede al evento de ese instante; el tiempo cero es válido.
- El radio uno afecta únicamente al centro; la mitad decreciente puede
  estar vacía.
- La compresión debe conservar las longitudes físicas de las hojas.
- Reconstruya los totales sumando los hijos: restar cantidades grandes
  cercanas puede perder un pequeño resto.
- Una pendiente e intercepto globales en coma flotante pueden sufrir
  cancelación con coordenadas grandes.

## Notas por lenguaje

C++, Go, Java y Rust usan doble precisión y el árbol basado en extremos.
Java recorre el árbol con una pila explícita reutilizable y escribe
notación científica con diez cifras significativas, evitando crear una
cadena de formato para cada número real.

Python usa doble precisión con los métodos de rutas y simulación
descritos arriba. La solución actual está aceptada en PyPy 3.10 x64 con
1.484 s y 37 252 KB, dentro de los límites de 2 segundos y 64 MB. Las
versiones anteriores superaron el límite de tiempo en la prueba 7 del
juez con CPython y en la prueba 12 con PyPy.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1977_segment_tree.cpp](1977_segment_tree.cpp) | G++ 13.2 x64 | segment_tree | O(q log q) | AC | 0.500 s | 17412 KB |
| [1977_segment_tree.go](1977_segment_tree.go) | Go 1.14 x64 | segment_tree | O(q log q) | AC | 0.375 s | 21908 KB |
| [1977_segment_tree.java](1977_segment_tree.java) | Java 1.8 | segment_tree | O(q log q) | AC | 0.546 s | 22224 KB |
| [1977_segment_tree.rs](1977_segment_tree.rs) | Rust 1.75 x64 | segment_tree | O(q log q) | AC | 0.375 s | 19520 KB |
| [1977_segment_tree_simulation.py](1977_segment_tree_simulation.py) | PyPy 3.10 x64 | segment_tree, simulation | O(q log q) | AC | 1.484 s | 37252 KB |
