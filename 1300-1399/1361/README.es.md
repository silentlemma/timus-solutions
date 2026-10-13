# 1361. Espaciología contra cronística

[Timus 1361](https://acm.timus.ru/problem.aspx?space=1&num=1361) · dificultad 1858 · graphs

Problema original con idea de Alexander Klepinin, preparado por Evgeny Krokhalev, del Noveno Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 19–24 de abril de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una ciudad tiene N ≤ 100 000 cruces, y cada cruce enumera sus
carreteras de salida de izquierda a derecha. Dos profesores salen a la
vez de los cruces A y B. En cada cruce el primero toma siempre la
carretera de más a la izquierda y el segundo la de más a la derecha;
cada carretera dura un minuto. Solo pueden encontrarse en un cruce y en
el mismo momento. Hay que imprimir el minuto del primer encuentro, o −1
si nunca se encuentran.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N, luego N líneas, cada una una lista de cruces terminada en 0, de la
carretera de más a la izquierda a la de más a la derecha. La última
línea tiene A y B. Cada lista contiene al menos un cruce distinto de
0; se permiten bucles. Todas las carreteras de salida parten del mismo
lado del cruce.

## Salida

El minuto del encuentro, o −1.

## Ejemplos

### Ejemplo 1

Entrada:

```
7
2 4 0
3 1 0
4 2 0
5 1 6 3 0
6 4 0
2 5 4 0
6 0
1 7
```

Salida:

```
7
```

## Solución

Cada conductor tiene una sola salida de cada cruce, así que cada
recorrido es una cola seguida de un ciclo. Se recorre cada uno hasta que
un cruce se repite. Entonces cada cruce v del recorrido se visita o una
vez, en el momento r, o en los momentos r, r + L, r + 2L, … si está en
el ciclo de longitud L.

Para cada cruce que visitan ambos recorridos se cortan los dos
conjuntos de momentos:

- dos momentos sueltos coinciden solo si son iguales;
- un momento suelto t está en r + kL si t ≥ r y L divide a t − r;
- dos ciclos piden t ≡ r₁ (mod L₁) y t ≡ r₂ (mod L₂). Por el teorema
  chino del resto hay solución solo si gcd(L₁, L₂) divide a r₂ − r₁. La
  solución se obtiene eligiendo el menor k ≥ 0 tal que t = r₁ + L₁k
  satisfaga la segunda congruencia, mediante un inverso modular tras
  dividir por el máximo común divisor (k = 0 si L₂ / gcd(L₁, L₂) = 1).
  Si t < r₂, se suman suficientes múltiplos enteros de lcm(L₁, L₂).

La respuesta es el menor momento sobre todos los cruces.
`O(M + N log N)`, donde M es el número total de carreteras de las
listas, que hay que leer completas.

Detalles a tener en cuenta:

- simular paso a paso es demasiado lento: dos ciclos de 49 999 y 50 001
  cruces que comparten un cruce pueden encontrarse por primera vez tras
  2 499 999 998 minutos (prueba generada 2), más de lo que cabe en enteros
  con signo de 32 bits;
- dos ciclos de 50 000 cruces con un único cruce compartido nunca dan
  un encuentro si las llegadas a ese cruce están desfasadas un minuto
  (prueba generada 3);
- ambos pueden salir del mismo cruce, y entonces la respuesta es 0
  (prueba 02);
- solo importan la primera y la última carretera de cada lista, pero
  hay que leerlas todas.

Las respuestas se compararon con una simulación paso a paso, lo
bastante larga para cubrir las colas y ambos ciclos, en 3 000 ciudades
aleatorias de hasta 9 cruces, 985 de ellas sin encuentro.

## Notas por lenguaje

- Python usa `pow(x, -1, m)` para el inverso modular; los demás
  lenguajes usan el algoritmo de Euclides extendido.
- Go y Java leen la entrada byte a byte.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1361_graphs.cpp](1361_graphs.cpp) | G++ 13.2 x64 | graphs | O(M + N log N) | AC | 0.187 s | 4608 KB |
| [1361_graphs.go](1361_graphs.go) | Go 1.14 x64 | graphs | O(M + N log N) | AC | 0.062 s | 12740 KB |
| [1361_graphs.java](1361_graphs.java) | Java 1.8 | graphs | O(M + N log N) | AC | 0.109 s | 7420 KB |
| [1361_graphs.py](1361_graphs.py) | Python 3.12 x64 | graphs | O(M + N log N) | AC | 0.343 s | 49584 KB |
| [1361_graphs.rs](1361_graphs.rs) | Rust 1.75 x64 | graphs | O(M + N log N) | AC | 0.046 s | 7588 KB |
