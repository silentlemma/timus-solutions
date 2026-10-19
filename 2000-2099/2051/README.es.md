# 2051. Recuperar dos curvas de igual área desde sus envolventes

[Timus 2051](https://acm.timus.ru/problem.aspx?space=1&num=2051) · difficulty 3748 · meet_in_middle

Problema original de Viktor Kamashev, preparado por Bulat Zaynullin, del Campeonato de Programación Deportiva de los Urales 2015.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dos funciones ocultas, continuas y lineales a trozos en [0, T], tienen
integrales iguales. Solo se conocen su máximo puntual h y su mínimo
puntual g. Reconstruir dos funciones cualesquiera así. Los límites son 1
segundo y 64 MB.

## Entrada

Primero T, 2 ≤ T ≤ 10⁶. Luego h y después g, cada una con su número de
nodos (2 ≤ n, m ≤ 100 000) seguido de pares enteros t y. Los tiempos
crecen estrictamente de 0 a T, las alturas están entre 0 y 10⁶ y no hay
tres nodos consecutivos alineados. En todo punto g ≤ h, con igualdad en
treinta puntos como mucho, extremos incluidos, y nunca a lo largo de un
segmento. Se garantiza que hay solución.

## Salida

Dos funciones en el mismo formato: número de nodos y pares enteros t y,
con tiempos estrictamente crecientes de 0 a T y sin tres nodos
consecutivos alineados.

## Evaluación

Un comprobador verifica exactamente que el máximo y el mínimo puntuales
de las dos funciones son h y g y que sus integrales coinciden; se acepta
cualquier pareja válida.

## Ejemplos

```
6
6
0 2
1 1
2 2
3 1
4 2
6 0
6
0 0
1 1
2 0
3 1
4 0
6 0
```

```
5
0 2
1 1
2 2
4 0
6 0
5
0 0
1 1
2 0
4 2
6 0
```

Las envolventes se tocan en tiempos uno, tres y seis. Las áreas dobles
de separación de las tres regiones son `2,4,6`. La primera curva
mostrada toma la superior en las dos primeras regiones y la inferior en
la última; la segunda usa la elección opuesta. Cada integral vale cinco.
El nodo de tiempo tres desaparece de la primera salida por quedar
colineal con sus vecinos; no se permiten nodos colineales adicionales.

## Solución

### Dónde pueden intercambiarse los papeles

Dentro de un intervalo conexo con `h>g`, una función reconstruida
continua debe seguir una misma envolvente durante todo el intervalo.
Cambiar entre valores distintos produciría discontinuidad. Se puede
cambiar en cada contacto `h=g`. Recíprocamente, cualquier asignación
independiente de papeles entre contactos produce funciones continuas con
las envolventes correctas.

Todo contacto coincide con un tiempo de nodo de al menos una entrada. Si
no, la separación es localmente lineal: un cero interior aislado
cambiaría de signo o la igualdad persistiría en un segmento. Ambos
contradicen las condiciones. El tiempo es entero; la altura de un nodo
de una entrada es entera y la igualdad hace entera la altura común.

Fusionamos los tiempos de nodos y comparamos interpolaciones
exactamente. En una arista `(a,x),(b,y)` el valor en `t` se representa
por `(x(b-t)+y(t-a),b-a)`. Productos cruzados deciden la igualdad sin
redondeo. Guardamos contactos internos y usamos cero y `T` como límites
externos aunque no sean contactos. Quedan `R≤31` regiones de separación
positiva.

### Partición exacta del área

Insertamos los contactos internos que falten en ambas curvas; todas las
coordenadas añadidas son enteras. La integral doble de una curva en una
región es la suma `(y_i+y_next)(t_next-t_i)`. La diferencia `d_i` entre
superior e inferior es un entero positivo; sea `D=sum d_i`. Si la
primera salida sigue la superior en un subconjunto `S`, su área doble es
el área doble total inferior más `sum_S d_i`. La segunda es el total
superior menos esa misma suma. Coinciden exactamente si `sum_S d_i=D/2`.
La promesa de existencia garantiza `D` par y un subconjunto adecuado.

Dividimos los pesos en `L=floor(R/2)≤15` izquierdos y como máximo
dieciséis derechos. Enumeramos cada subconjunto izquierdo con un entero
`key=sum·2^L+mask`. Al añadir cada peso duplicamos la lista y finalmente
la ordenamos. Los `L` bits bajos guardan la máscara; así se ordena
primero por suma y las sumas repetidas conservan una máscara válida.

Enumeramos máscaras derechas en orden Gray. Entre máscaras consecutivas
cambia un solo bit, por lo que la suma derecha se actualiza sumando o
restando un peso. Para `need=D/2-right_sum` buscamos el primer valor no
menor que `need·2^L`. Su cociente por `2^L` es `need` precisamente
cuando existe un subconjunto izquierdo correspondiente. Recuperamos los
bits bajos y combinamos ambas máscaras. Como se enumeran todos los
subconjuntos de cada mitad, aparece la solución prometida.

La aritmética es exacta. Los numeradores interpolados no superan `10^12`
ni los productos cruzados `10^18`. Como `D≤2·10^12`, las claves son
menores que `6,6·10^16`. Bastan enteros con signo de sesenta y cuatro
bits, promoviendo operandos antes de multiplicar. La máscara completa
ocupa como máximo treinta y un bits.

### Reconstrucción canónica

Recorremos las regiones de izquierda a derecha y añadimos los nodos de
la envolvente elegida, incluidos contactos insertados, a la primera
salida; los de la otra, a la segunda. Se omiten copias repetidas de una
frontera. Mientras los tres últimos puntos sean colineales se elimina el
central mediante un producto cruzado exacto. Esto conserva la función y
deja nodos canónicos. La igualdad en los contactos garantiza
continuidad, el subconjunto elegido prueba igualdad de integrales y los
papeles complementarios conservan ambas envolventes. Las coordenadas
siguen siendo enteras dentro de los límites originales.

No hay que interpolar y añadir un valor en cada nodo ajeno de la otra
gráfica: podría ser no entero. Solo hacen falta los nodos propios de la
curva seleccionada y los contactos. Antes de simplificar, las dos
salidas contienen como máximo `n+m+30` nodos en total.

Un contacto no tiene que ser nodo de ambas entradas: una puede
atravesarlo linealmente. Los contactos en los extremos no son cortes
internos. Se necesitan áreas dobles y productos de sesenta y cuatro
bits. Las sumas izquierdas repetidas son válidas y deben conservar
máscara. En Gray se usa el bit que cambió, no el número de iteración.
Reconstruir en orden temporal y simplificar también después de cambiar
papeles. Comprobar envolventes solo en nodos puede omitir un cruce
ilegal interior; el comprobador revisa también los puntos medios de
todos los intervalos lineales conjuntos.

## Notas por lenguaje

Los barridos y la pila requieren `O(n+m)` tiempo. Con ordenación y
búsquedas, el total es `O(n+m+R·2^ceil(R/2))` tiempo y
`O(n+m+2^floor(R/2))` espacio auxiliar. Con `R≤31` se almacenan como
máximo 32768 claves y se enumeran 65536 subconjuntos derechos.

Los cinco programas usan enteros exactos y claves escalares
empaquetadas. Python guarda coordenadas en arrays compactos sin signo,
busca con bisect y escribe por bloques. Java usa arrays primitivos y
búferes de bytes. No hay geometría ni
integración en coma flotante.

La solución en Python se ejecuta con PyPy: con CPython 3.12 supera el
límite de tiempo en la prueba 19 del juez, mientras que con PyPy 3.10 se
acepta en 0.562 s.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2051_meet_in_middle.cpp](2051_meet_in_middle.cpp) | G++ 13.2 x64 | meet_in_middle | O(n+m+R*2^(R/2)) | AC | 0.125 s | 11344 KB |
| [2051_meet_in_middle.go](2051_meet_in_middle.go) | Go 1.14 x64 | meet_in_middle | O(n+m+R*2^(R/2)) | AC | 0.093 s | 19692 KB |
| [2051_meet_in_middle.java](2051_meet_in_middle.java) | Java 1.8 | meet_in_middle | O(n+m+R*2^(R/2)) | AC | 0.171 s | 7872 KB |
| [2051_meet_in_middle.py](2051_meet_in_middle.py) | PyPy 3.10 x64 | meet_in_middle | O(n+m+R*2^(R/2)) | AC | 0.562 s | 41668 KB |
| [2051_meet_in_middle.rs](2051_meet_in_middle.rs) | Rust 1.75 x64 | meet_in_middle | O(n+m+R*2^(R/2)) | AC | 0.046 s | 15200 KB |
