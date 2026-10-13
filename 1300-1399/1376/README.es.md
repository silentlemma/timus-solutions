# 1376. La pirámide del decano 2

[Timus 1376](https://acm.timus.ru/problem.aspx?space=1&num=1376) · dificultad 12875 · backtracking

Problema original de Alexander Mironenko, del Noveno Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 19–24 de abril de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una pirámide de base cuadrada de lado A1 y cuatro caras laterales
isósceles iguales de arista lateral A2 (ambas de 0,1 a 10, A2/A1 de 0,9
a 1,9) está sobre su base, centrada en el origen con los lados de la base
paralelos a los ejes. Se hace rodar sobre una arista de una cara a una
cara vecina, sin que la arista se mueva. En a lo sumo N vuelcos
(2 ≤ N ≤ 32) devuélvela a su base con el centro de la base lo más cerca
posible de (X, Y), que está al menos a 20,05·A1; entre finales igual de
cercanos usa el menor número de vuelcos. Imprime la distancia con 3
decimales, el número de vuelcos M y las M + 1 caras sobre las que
descansa: 0 es la base, 1 a 4 las caras laterales en sentido horario
desde la que mira a +y.

Límite de tiempo: 2,5 segundos. Límite de memoria: 64 MB.

## Entrada

A1, A2, X, Y y N.

## Salida

La distancia, M y las caras desde el 0 inicial.

## Ejemplos

### Ejemplo 1

Entrada:

```
10.0 10.0 1000.0 0.0 5
```

Salida:

```
972.679
5
0 2 3 4 1 0
```

## Solución

El estado es la cara sobre la mesa y sus vértices; un vuelco los refleja
o los despliega sobre la arista común. Cuatro reglas cubren todos los
vuelcos: de la base a la cara k sobre la arista de los vértices k y
k + 1; de una cara lateral a la base, que despliega un cuadrado; y de una
cara lateral a la vecina en sentido horario o antihorario sobre una
arista lateral, que refleja el tercer vértice.

La búsqueda es exacta. Un vuelco mueve el centro de la cara sobre la mesa
una cantidad fija: A1/2 + h/3 entre la base y una cara lateral (h la
altura de una cara lateral) y 2·A1·h/(3·A2) entre dos laterales, así que
una tabla da para cada estado y número de vuelcos restantes hasta dónde
puede llegar aún el centro terminando en la base. Una búsqueda en
profundidad sobre los vuelcos (sin volver nunca atrás de inmediato) poda
por la desigualdad triangular toda rama que no pueda mejorar la mejor
distancia y prueba primero las posiciones más cercanas. Una búsqueda en
haz con 4 000 estados por nivel da una buena primera respuesta, así que
las podas actúan enseguida. `O(3^N)` en el peor caso, mucho menos en la
práctica.

Detalles a tener en cuenta:

- la respuesta no es única: los vuelcos del ejemplo pueden hacerse en
  otro orden (prueba 01), así que un verificador los reproduce;
- con N = 2 no se puede acercar y la respuesta es 0 vuelcos (prueba 02);
- a igual distancia decide el número de vuelcos.

Las respuestas coinciden con una implementación independiente aceptada en
todas las pruebas de aquí y en 150 generadas, y con una búsqueda
exhaustiva sobre todas las secuencias de vuelcos en 240 casos con N hasta
8.

## Notas por lenguaje

- Python acota exactamente los primeros 8 vuelcos: desde un estado de
  cada uno de los 17 tipos juega todas las secuencias de hasta 8 vuelcos
  y guarda el final más lejano sobre la base; más allá suma los pasos
  fijos como los demás lenguajes. Base, cara y base siempre vuelve al
  sitio, así que la cota anterior era demasiado holgada: la búsqueda
  visita de 11 a 25 veces menos nodos y basta un haz de 200 estados. Las
  pruebas más grandes tardan 0,25 s con CPython; una primera versión sin
  las cotas exactas excedía 2,5 s en la prueba 5 del juez incluso con
  PyPy.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1376_backtracking.cpp](1376_backtracking.cpp) | G++ 13.2 x64 | backtracking | O(3^N) worst case | AC | 0.218 s | 7376 KB |
| [1376_backtracking.go](1376_backtracking.go) | Go 1.14 x64 | backtracking | O(3^N) worst case | AC | 0.375 s | 25964 KB |
| [1376_backtracking.java](1376_backtracking.java) | Java 1.8 | backtracking | O(3^N) worst case | AC | 1.203 s | 18948 KB |
| [1376_backtracking.py](1376_backtracking.py) | Python 3.12 x64 | backtracking | O(3^N) worst case | AC | 0.750 s | 2988 KB |
| [1376_backtracking.rs](1376_backtracking.rs) | Rust 1.75 x64 | backtracking | O(3^N) worst case | AC | 0.390 s | 11432 KB |
