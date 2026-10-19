# 2017. Dos grupos coherentes

[Timus 2017](https://acm.timus.ru/problem.aspx?space=1&num=2017) · dificultad 1332 · graphs, bitmask, bfs

Problema original de Oleg Dolgorukov, de la subregión oriental del NEERC 2014.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada una de `n` personas indica un lugar y una lista de personas vistas allí.
La declaración atribuye ese lugar tanto a quien declara como a todas las
personas de la lista. Hay que elegir un grupo **no vacío** de tamaño mínimo
cuyas declaraciones sean compatibles entre sí, y tal que las declaraciones
del complemento también sean compatibles. Los dos grupos pueden describir
ubicaciones distintas para una misma persona. Una omisión no implica ausencia:
alguien pudo pasar inadvertido. Se garantiza una partición válida.

Hay `2 ≤ n ≤ 400` personas. Cada lugar es una cadena no vacía de hasta
20 letras latinas minúsculas. Una lista contiene `0 ≤ m ≤ n−1` índices
distintos entre 1 y `n`, en orden creciente, sin incluir a quien declara.
Límites: 1 segundo y 64 MB.

## Entrada

La primera línea contiene `n`. Las siguientes `n` líneas describen, en orden,
el lugar, la longitud `m` de la lista y los `m` índices vistos en ese lugar.

## Salida

Imprima el tamaño mínimo positivo en la primera línea y los índices desde uno
en la segunda. Se admite cualquier grupo óptimo y cualquier orden de índices.

## Evaluación

Un comprobador verifica que el grupo no está vacío, que tanto el grupo
como el resto son consistentes y que el tamaño es el menor posible; se
acepta cualquier grupo óptimo.

## Ejemplos

```
3
bar 0
bar 1 1
pool 2 1 2
```

```
1
3
```

```
3
pool 2 2 3
pool 2 1 3
pool 2 1 2
```

```
1
1
```

## Solución

Construya un conjunto de bits `C_i` con la propia persona `i` y su
lista. Dos declaraciones se contradicen exactamente cuando sus lugares
difieren y `C_i ∩ C_j` no está vacío. Una arista no dirigida une a
quienes hacen tales declaraciones. También hay conflicto cuando dos
personas sitúan a una **tercera** en lugares distintos: comprobar
solamente observaciones directas entre ambas pierde esas aristas. Listas
distintas en un mismo lugar no se contradicen.

Un conjunto de declaraciones es coherente si y solo si no contiene una
arista interna. Una arista asigna dos lugares a alguien; sin aristas,
todas las afirmaciones sobre cada persona coinciden y pueden completarse
hasta una asignación total. Por tanto ambos grupos son coherentes
exactamente cuando cada arista cruza la partición: se necesita una
coloración propia con dos colores, no basta una cobertura de vértices.
La garantía implica un grafo bipartito.

Coloree cada componente mediante búsqueda en anchura iterativa. En una
componente bipartita conexa, el color de un vértice determina los restantes;
las dos posibilidades intercambian sus clases. Elija la clase menor de cada
componente, con cualquier desempate. Como no hay restricciones entre
componentes, la suma de esos mínimos independientes es mínima globalmente.

Un vértice aislado tiene clases de tamaños uno y cero, así que no aporta
personas. Si al final no se eligió a nadie, el grafo entero carece de aristas;
cualquier persona forma un grupo no vacío óptimo. En otro caso cada
componente con aristas ya aporta al menos una persona y el mínimo es positivo.

En el primer ejemplo las declaraciones de `bar` coinciden, mientras que la de
`pool` contradice a ambas: se elige el índice 3. En el segundo todos los
lugares coinciden, no hay aristas y cualquier grupo de una persona es óptimo.

Sea `M` la suma de las longitudes de las listas y `w` el ancho de palabra.
Crear las máscaras y comparar todas las parejas cuesta
`O(M + n² ceil(n / w))`; colorear añade `O(n²)`.
El espacio es `O(n² + M)`, incluida la entrada almacenada.
Para 400 personas bastan siete palabras de 64 bits por máscara.

Trampas:

- Incluir siempre a quien declara en su máscara.
- Detectar conflictos sobre una tercera persona aunque no haya
  observación directa.
- El grupo elegido también debe ser coherente: una cobertura mínima de
  vértices no basta.
- Intercambiar clases por componente y omitir aislados salvo que el
  resultado quede vacío.
- No exigir observaciones recíprocas ni deducir ausencia por omisión.

## Notas por lenguaje

C++ usa `std::bitset`; Go y Rust, arreglos de palabras de 64 bits; Java,
`BitSet`; Python, enteros de precisión arbitraria. Las cinco versiones
recorren el grafo sin recursión y eligen las clases con la misma regla.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2017_graphs_bitmask.cpp](2017_graphs_bitmask.cpp) | G++ 13.2 x64 | graphs, bitmask | O(M + n^2 ceil(n / w)) | AC | 0.015 s | 728 KB |
| [2017_graphs_bitmask.go](2017_graphs_bitmask.go) | Go 1.14 x64 | graphs, bitmask | O(M + n^2 ceil(n / w)) | AC | 0.046 s | 4208 KB |
| [2017_graphs_bitmask.java](2017_graphs_bitmask.java) | Java 1.8 | graphs, bitmask | O(M + n^2 ceil(n / w)) | AC | 0.125 s | 5092 KB |
| [2017_graphs_bitmask.py](2017_graphs_bitmask.py) | Python 3.12 x64 | graphs, bitmask | O(M + n^2 ceil(n / w)) | AC | 0.125 s | 5920 KB |
| [2017_graphs_bitmask.rs](2017_graphs_bitmask.rs) | Rust 1.75 x64 | graphs, bitmask | O(M + n^2 ceil(n / w)) | AC | 0.031 s | 1692 KB |
