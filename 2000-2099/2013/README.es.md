# 2013. Valores Determinados Antes y Después de Cada Vértice

[Timus 2013](https://acm.timus.ru/problem.aspx?space=1&num=2013) · dificultad 941 · graphs

Problema original de Alex Samsonov, preparado por Egor Shchelkonogov, de la subregión oriental del NEERC 2014.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un recorrido empieza en el vértice 1 de un grafo dirigido con valor 0.
Al entrar se registra el valor. Si el parámetro del vértice `k>0`, lo
sustituye por `k`; si `k=0`, se conserva. Se registra el valor de salida
y se sigue cualquier arista saliente. Se permiten visitas repetidas.
Para cada vértice, determina por separado si su entrada y su salida son
iguales en todos los recorridos posibles hasta esa visita. Todos los
vértices son alcanzables desde 1.

## Entrada

Primero `n`, `1 ≤ n ≤ 100 000`. Por cada vértice, una línea contiene `k
m` y sus `m` destinos distintos en orden creciente. `0 ≤ k ≤ 100 000`,
`0 ≤ m ≤ n`; los destinos pertenecen a `1..n`, con posibles bucles
propios. Hay como máximo 100 000 aristas en total. Tiempo límite 1
segundo, memoria 64 MB.

## Salida

Una línea por vértice en orden, con dos respuestas: antes y después de
sustituir el valor. Escribe `sober` si siempre es cero, el entero si
siempre es el mismo positivo, y `unknown` si hay varios valores
posibles. Las palabras son minúsculas. La respuesta única se compara por
tokens.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
5
0 2 2 3
6 1 4
5 2 4 5
5 1 5
0 0
```

```
sober sober
sober 6
sober 5
unknown 5
5 5
```

```
2
0 2 1 2
0 2 1 2
```

```
sober sober
sober sober
```

En el primer ejemplo, el vértice 4 puede recibir 6 o 5: su entrada es
desconocida, pero su propia sustitución fija la salida en 5. Las dos
maneras de llegar al vértice 5 llevan entonces 5. En el segundo, ningún
vértice sustituye el cero inicial, que persiste incluso en los ciclos.

## Solución

Resume cada entrada como no alcanzada, un valor conocido (incluido
cero), o desconocida. Usa códigos negativos distintos para no alcanzada
y desconocida. Inicializa la entrada del vértice 1 con cero e
introdúcelo en una cola de cambios. Ese cero inicial sigue siendo
posible aunque el recorrido regrese a 1.

Al sacar un vértice, su salida es el `k` positivo fijo, o su entrada
actual si `k=0`. Ofrece ese estado a todos sus sucesores. Un sucesor no
alcanzado toma la oferta. Valores conocidos iguales permanecen iguales;
estados distintos se unen como desconocido. Lo desconocido absorbe toda
oferta posterior. Encola al sucesor únicamente si cambia su entrada. Al
vaciar la cola, calcula cada salida con la misma regla.

El resumen basta: una sustitución elimina toda la historia anterior,
mientras que un vértice cero la conserva. Unir dos valores factibles
distintos, o un estado que ya tiene varios, certifica correctamente la
ambigüedad. El mismo número procedente de vértices distintos sigue
siendo igual. Toda posibilidad propagada procede de un recorrido real,
así que no se inventa ambigüedad. Al terminar, cada arista ha
transmitido la salida final de su origen; por inducción sobre la
longitud del recorrido finito, todas las posibilidades están
representadas. Un valor único es común a todos, y desconocido implica al
menos dos. Los ciclos no requieren orden topológico.

Un ciclo formado solo por vértices con `k=0` conserva los valores que
recibe; no los convierte en cero. En el test [004](tests/004.in), el bucle
del vértice 2 conserva el valor 1 recibido del vértice 1. Un ciclo así
permanece en cero solo si todos los recorridos que entran llevan cero.

Una entrada cambia como máximo dos veces: de no alcanzada a conocida y
luego a desconocida, o directamente a desconocida. Cada cambio causa a
lo sumo una inserción en la cola; cada lista de adyacencia se recorre
como máximo dos veces. Tiempo `O(n+m)` y espacio `O(n+m)`. Guarda las
aristas en arrays planos con offsets y usa una cola iterativa, sin
recursión ni enumeración de rutas.

## Notas por lenguaje

La primera visita no fija la respuesta: un conflicto posterior debe
propagarse por vértices cero. Un vértice positivo restablece incluso una
entrada desconocida. Regresar a 1 puede volver desconocida su entrada.
Un ciclo sin sustituciones conserva los valores recibidos; etiquetas
positivas iguales no chocan. La alcanzabilidad garantiza que no se imprime el estado no
alcanzado. La cola de Java admite `2n` elementos; Go, C++ y Rust usan
arrays crecientes. Python usa arrays compactos con signo para grafo y
estados, deque para la cola y libera los tokens antes de construir la
salida; se ejecuta en CPython.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2013_graphs.cpp](2013_graphs.cpp) | G++ 13.2 x64 | graphs | O(n + m) | AC | 0.078 s | 2752 KB |
| [2013_graphs.go](2013_graphs.go) | Go 1.14 x64 | graphs | O(n + m) | AC | 0.234 s | 11180 KB |
| [2013_graphs.java](2013_graphs.java) | Java 1.8 | graphs | O(n + m) | AC | 0.140 s | 14336 KB |
| [2013_graphs.py](2013_graphs.py) | Python 3.12 x64 | graphs | O(n + m) | AC | 0.453 s | 15644 KB |
| [2013_graphs.rs](2013_graphs.rs) | Rust 1.75 x64 | graphs | O(n + m) | AC | 0.031 s | 6608 KB |
