# 2038. Pertenencia a todos los recubrimientos mínimos bipartitos

[Timus 2038](https://acm.timus.ru/problem.aspx?space=1&num=2038) · dificultad 2284 · matching, bitmask

Problema original de Alexey Danilyuk, del concurso Dandelion de la UrFU, campamento de Petrozavodsk, verano de 2014.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Considera todos los recubrimientos de vértices de cardinalidad mínima de
un grafo bipartito. Cada arista debe tener al menos un extremo elegido.
Clasifica cada vértice como `N` si no aparece en ninguno, `A` si aparece
en todos, o `E` si aparece en algunos pero no en todos.
Límites: 1 segundo y 64 MB.

## Entrada

Una instancia `n m k`, con `1≤n,m≤1000` y `0≤k≤1000000`, seguida de
`k` aristas `u v`, `1≤u≤n`, `1≤v≤m`.
Cada parte se numera desde uno de forma independiente. No se repiten aristas,
así que `k≤nm`. No hay cantidad inicial de pruebas.

## Salida

Dos cadenas sin espacios: `n` clasificaciones de la parte izquierda y
`m` de la derecha, por número de vértice. Usa mayúsculas `N,E,A`.
Se pide cardinalidad mínima, no solo minimalidad por inclusión.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
11 9 22
1 1
1 2
1 3
1 8
1 9
2 1
2 3
3 2
3 4
4 3
4 5
5 2
5 4
5 6
6 6
6 7
7 5
7 7
8 7
9 7
10 7
11 7
```

```
AEEEEEENNNN
EEEEEEANN
```

## Solución

Calcula un emparejamiento máximo y propaga decisiones obligatorias desde
sus vértices libres. Guarda ambas direcciones de adyacencia como máscaras
de bits, sin crear un objeto por cada arista.

### Emparejamiento por búsquedas alternantes

Procesa los vértices izquierdos en orden, manteniendo un máximo para el
prefijo procesado. Si el nuevo vértice tiene un vecino derecho libre,
emparéjalo directamente. En otro caso usa BFS: desde un izquierdo visita
vecinos derechos aún no vistos y desde un derecho emparejado visita su pareja.
Registra el predecesor izquierdo de cada derecho descubierto.
Un derecho libre termina un camino aumentante; invierte las parejas por
esos predecesores y las parejas anteriores.

Cada derecho se visita una vez por búsqueda. Un izquierdo emparejado solo
puede entrar por su único derecho emparejado, también como máximo una vez;
su propia arista de pareja ya fue vista al extraerlo.
Las máscaras enumeran solo derechos nuevos.
Si toda la parte derecha está emparejada, puede terminar la construcción.

Añadir un izquierdo eleva el óptimo como máximo en uno. Todo camino
aumentante nuevo debe empezar en ese nuevo vértice libre, que no puede
ser interno en un camino alternante. Un éxito alcanza el nuevo óptimo y
un fracaso conserva el anterior. El criterio aumentante se obtiene
descomponiendo la diferencia simétrica con cualquier emparejamiento
mayor en componentes alternantes.

### Presupuesto de parejas en un recubrimiento mínimo

Sea `ν` el tamaño del emparejamiento. Sus aristas disjuntas exigen al menos
`ν` vértices en cualquier recubrimiento.
Desde todos los izquierdos libres recorre aristas hacia la derecha y
parejas hacia la izquierda; llama `D_L,D_R` a los conjuntos alcanzados.
No alcanza un derecho libre, pues eso daría un camino aumentante.

`(L fuera de D_L) unido con D_R` cubre toda arista: un izquierdo alcanzado
hace alcanzable cualquier vecino derecho. Cada pareja tiene ambos extremos
alcanzados o ninguno, por lo que el conjunto toma exactamente uno.
Excluye los izquierdos libres y no contiene derechos libres.
Su tamaño es `ν`, demostrando que se alcanza la cota.
Por tanto todo recubrimiento mínimo elige exactamente un extremo de cada
arista emparejada fija y ningún vértice libre.

### Decisiones obligatorias y opciones restantes

Los vértices libres están obligatoriamente ausentes: `N`.
Todos los vecinos de un ausente deben estar elegidos: `A`.
La pareja de un elegido obligatorio debe estar ausente.
Dos recorridos alternantes propagan esas reglas:

- Desde izquierdos libres: izquierdos alcanzados `N`, derechos alcanzados `A`.
- Desde derechos libres: derechos alcanzados `N`, izquierdos alcanzados `A`.

No hay contradicciones porque existe un recubrimiento mínimo.
Todo vértice sin marcar está emparejado y su pareja tampoco está marcada.
Forma un recubrimiento con todos los `A` y todos los izquierdos sin marcar;
otro con todos los `A` y todos los derechos sin marcar.
Una arista con extremo `N` ya tiene un extremo `A`; las demás tocan `A`
o unen dos extremos sin marcar y quedan cubiertas por la parte elegida.
Ambos conjuntos toman un extremo por pareja y tienen tamaño `ν`.
Cada vértice restante pertenece a uno y no al otro, justificando `E`.
No se enumeran recubrimientos ni hacen falta componentes fuertemente conexas.

En el ejemplo, `L1` y `R7` son obligatorios. `L8…L11` y `R8,R9` nunca aparecen.
Los seis `L2…L7` y los seis `R1…R6` pueden variar:
`L1…L7` con `R7` y, alternativamente, `L1` con `R1…R7`
son dos recubrimientos mínimos de tamaño ocho que muestran las opciones.

### Complejidad y representación

Sea `B=ceil(max(n,m)/w)` para anchura de palabra `w`.
Los lenguajes compilados usan `w=64` y como máximo dieciséis palabras por fila;
consumen `O(k+n²B+nm+(n+m)B)` operaciones de palabra.
En Python las máscaras son enteros arbitrarios; una cota conservadora,
incluyendo actualizaciones de entrada y extracción del bit inferior, es
`O((k+n(n+m))B)`. Todas las búsquedas y propagaciones son iterativas.

Máscaras, parejas y colas ocupan `O((n+m)B+n+m)`. C++ y Java leen flujos
con búfer; Python lee una arista por línea. Go y Rust conservan el búfer
de entrada, añadiendo `O(k)` bytes con estas cotas numéricas.

Trampas:

- Un aislado es `N`; un grafo sin aristas tiene el recubrimiento vacío
  como único mínimo.
- Basta un emparejamiento máximo; sus vértices libres nunca están en un mínimo.
- Si un emparejamiento perfecto cubre ambas partes, todos son `E`.
- Propaga desde ambas partes y desde todos los vértices libres.
- Separa numeraciones y elimina bits sobrantes de la última palabra.
- Cuenta ceros finales únicamente en palabras no nulas.

## Notas por lenguaje

C++, Go y Rust usan palabras sin signo de 64 bits. Java usa filas
primitivas `long`; la representación con signo no altera las máscaras.
Python precalcula los bits individuales y convierte solo los dos valores
de cada línea, evitando una lista de todos los tokens de un millón de
aristas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2038_matching_bitmask.cpp](2038_matching_bitmask.cpp) | G++ 13.2 x64 | matching, bitmask | O((k+n(n+m))B) | AC | 0.265 s | 620 KB |
| [2038_matching_bitmask.go](2038_matching_bitmask.go) | Go 1.14 x64 | matching, bitmask | O((k+n(n+m))B) | AC | 0.062 s | 35920 KB |
| [2038_matching_bitmask.java](2038_matching_bitmask.java) | Java 1.8 | matching, bitmask | O((k+n(n+m))B) | AC | 0.109 s | 5540 KB |
| [2038_matching_bitmask.py](2038_matching_bitmask.py) | Python 3.12 x64 | matching, bitmask | O((k+n(n+m))B) | AC | 0.984 s | 1536 KB |
| [2038_matching_bitmask.rs](2038_matching_bitmask.rs) | Rust 1.75 x64 | matching, bitmask | O((k+n(n+m))B) | AC | 0.062 s | 17488 KB |
