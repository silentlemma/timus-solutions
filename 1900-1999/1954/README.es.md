# 1954. Cinco palíndromos mediante paridad de factorización

[Timus 1954](https://acm.timus.ru/problem.aspx?space=1&num=1954) · difficulty 3455 · dp

Original problem from Ural FU contest. Kontur Cup. Petrozavodsk training camp. Winter 2013 | by Mikhail Rubinchik (prepared by Kirill Borozdin).

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dividir toda la cadena en exactamente cinco palíndromos contiguos no
vacíos, conservando el orden. Un palíndromo coincide con su reverso.
Cualquier división válida sirve. Límites: 1 segundo, 64 MB.

## Entrada

Una cadena s de letras inglesas minúsculas, 5≤n=|s|≤100000.

## Salida

Si es imposible, `NO`. Si es posible, `YES` y los cinco palíndromos,
uno por línea. Su concatenación debe reproducir s exactamente.

## Evaluación

Un comprobador verifica que `YES` o `NO` es correcto y, para `YES`, que
las cinco palabras impresas son palíndromos no vacíos que forman la
cadena; se acepta cualquier división válida.

## Ejemplos

```
aaabbcdcaa
```

```
YES
aa
a
bb
cdc
aa
```

```
spaaaaaaarta
```

```
NO
```

```
abacdcxyxzpz
```

```
NO
```

## Solución

Hallar el mínimo número impar r de partes palíndromas. Hay cinco partes
si y solo si r≤5. Necesidad inmediata. Para suficiencia, r es 1,3 o 5.
Mientras r<5, hay al menos dos caracteres más que partes. Entonces alguna
parte tiene longitud al menos tres, o dos partes tienen longitud dos.
En el primer caso separar primera letra, centro no vacío y última letra:
los tres son palíndromos. En el segundo dividir ambos palíndromos de dos
letras en letras individuales. Cada operación añade dos partes no vacías
y conserva la cadena. A lo sumo dos operaciones alcanzan cinco. Es
esencial la condición n≥5.

Guardar E[i],O[i], mínimos números par e impar de partes para cada prefijo.
Inicialmente E[0]=0, O[0]=∞. Para cada sufijo palíndromo s[j:i], actualizar
O[i] con E[j]+1 y E[i] con O[j]+1, guardando j para reconstruir. Añadir una
parte invierte paridad; toda división tiene un último sufijo de esta forma,
por lo que las transiciones son necesarias y suficientes. Valores mayores
que cinco se representan por seis: el número de partes solo aumenta.
Un mínimo sin paridad no basta; la otra paridad puede ser más cara o imposible.

Un eertree tiene un nodo por palíndromo distinto. Una arista añade la misma
letra en ambos extremos; el enlace de sufijo lleva al mayor sufijo palíndromo
propio. Raíces de longitudes −1 y 0 tratan las longitudes impares y pares.
Al añadir una letra seguir enlaces hasta poder rodear el sufijo actual;
reutilizar o crear el nodo y su enlace. Hay como máximo n+2 nodos. Usar
26 transiciones por nodo da acceso determinista para el alfabeto fijo.

Enumerar todos los sufijos es cuadrático en una cadena uniforme. Agrupar
nodos consecutivos con igual diferencia d[v]=len[v]−len[link[v]], y saltar
al grupo siguiente mediante series[v]. Para un líder v en posición i,
el predecesor nuevo es b=i−len[series[v]]−d[v]. Inicializar los dos mínimos
del grupo con E[b],O[b]. Si link[v] tiene igual diferencia, tomar mínimos
por componente con sus valores recordados, conservando también el índice.
Cada grupo añade uno e invierte paridad al actualizar E[i],O[i].

Invariante periódico: el grupo anterior en i−d[v] tiene las mismas posiciones
predecesoras salvo la nueva b. El índice recordado sigue describiendo un
sufijo palíndromo real y el mínimo correcto. No borrar datos del grupo en
cada carácter ni desplazar el índice recordado por d[v]. Hay O(log n)
líderes por prefijo. El lema y construcción estándar aparecen en el
[artículo del eertree](https://arxiv.org/pdf/1506.04862), sección 4;
aplicar el mínimo independientemente a las dos componentes de paridad.

Si O[n]>5 imprimir NO. Si no, seguir predecesores alternando paridad,
recuperar una división impar mínima, invertirla y añadir dos partes por
las operaciones demostradas hasta llegar a cinco. Cada paso es un sufijo
palíndromo no vacío; terminar en prefijo cero garantiza reconstrucción total.

O(n log n) tiempo y O(26n)=O(n) espacio, incluidos transiciones y padres.
Construcción y salida/refinamiento lineales para alfabeto fijo. El factor
logarítmico es el número de grupos de series.

Como máximo cinco no equivale a exactamente cinco sin paridad. Una cadena
alternante de longitud par solo tiene palíndromos impares y no admite cinco.
No producir centros vacíos: separar extremos solo si longitud≥3. Guardar
el predecesor del mínimo en caché. Reservar dos raíces además de n nodos
y estados para el prefijo vacío.

## Notas por lenguaje

Solo biblioteca estándar. Python usa arrays tipados para transiciones e
índices y bytearray para costes, evitando diccionarios y muchos enteros
encapsulados por nodo. Java usa arrays planos y BufferedReader. C++, Go
y Rust reservan una sola vez la capacidad de nodos. Longitudes de raíces
con signo. Las cinco subcadenas suman n caracteres, sin concatenaciones
repetidas cuadráticas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1954_dp.cpp](1954_dp.cpp) | G++ 13.2 x64 | dp | O(n log n) | AC | 0.031 s | 15368 KB |
| [1954_dp.go](1954_dp.go) | Go 1.14 x64 | dp | O(n log n) | AC | 0.046 s | 33204 KB |
| [1954_dp.java](1954_dp.java) | Java 1.8 | dp | O(n log n) | AC | 0.140 s | 17020 KB |
| [1954_dp.py](1954_dp.py) | Python 3.12 x64 | dp | O(n log n) | AC | 0.656 s | 14836 KB |
| [1954_dp.rs](1954_dp.rs) | Rust 1.75 x64 | dp | O(n log n) | AC | 0.031 s | 30280 KB |
