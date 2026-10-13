# 1394. Barcos. Versión 2

[Timus 1394](https://acm.timus.ru/problem.aspx?space=1&num=1394) · dificultad 27928 · backtracking

Problema original preparado por Vladimir Yakovlev.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

La misma tarea que el [problema 1115](../../1100-1199/1115/README.es.md)
con pruebas mucho más difíciles: N < 100 barcos de longitudes de 1 a 100
deben llenar exactamente 1 < M < 10 filas de longitud dada, con al menos
un barco por fila. Existe una colocación; hay que imprimir una. El juez
guarda a lo sumo 20 pruebas, cada una elegida contra algún tipo de
heurística, y ninguna pensada para vencerlas todas.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y M, luego N líneas con las longitudes de los barcos y M líneas con
las longitudes de las filas.

## Salida

Para cada fila, en el orden de la entrada, dos líneas: el número de
barcos que tiene y sus longitudes.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 2
4
10
2
5
3
11
13
```

Salida:

```
3
5 4 2
2
10 3
```

## Solución

La partición exacta en varias partes es difícil en general, y las pruebas
del juez están elegidas para vencer heurísticas aisladas. Las soluciones
ejecutan por turnos cuatro búsquedas exactas, cada una en una porción de
tiempo que crece 1,6 veces por ronda, con los órdenes algo barajados en
las rondas posteriores, y paran en cuanto una coloca todos los barcos.

- B, filas una a una. Los barcos van de más largo a más corto; dentro de
  una fila cada barco se toma o se salta, y las copias de una longitud
  saltada se saltan juntas. Cada fila abierta debe seguir siendo suma de
  un subconjunto de los barcos sin usar (bitsets de sumas de sufijos,
  recalculados al abrir una fila). Un estado fallido, los barcos sin usar
  más las filas abiertas, va a una tabla hash que sobrevive a los
  reinicios, porque no depende del orden. Una ronda de cada dos, B hace
  también la comprobación de restos de abajo con módulos pequeños.
- C, B solo sobre las longitudes raras (de una a tres copias): una fila
  necesita entonces un resto que formen los barcos comunes, y un B anidado
  coloca los comunes al final. Así se evitan las muchas formas
  intercambiables de llenar filas con barcos comunes.
- D, C donde «raro» significa no divisible por un módulo K que divide a
  muchos barcos, más una comprobación exacta de restos: los no múltiplos
  restantes de cada resto deben repartirse entre las filas restantes de
  modo que cada fila obtenga su longitud módulo K. Lo responde una DP
  sobre filas y vectores de cantidades (en base mixta), con un
  presupuesto por consulta y una caché que sobrevive a los reinicios.
- A, barcos uno a uno en filas, las longitudes más raras primero. La
  longitud restante de cada fila debe ser suma de barcos sin colocar; una
  fila que no puede completarse sin el barco actual lo recibe; las filas
  con igual longitud restante se prueban una vez; los barcos iguales van a
  filas en orden; y las cantidades de barcos por fila deben poder sumar
  (bitsets de las sumas de exactamente c barcos).

`O(M^N)` en el peor caso, como toda búsqueda exacta.

Detalles a tener en cuenta:

- con la flota de la prueba 70 del foro, con una fila de 820, los
  reinicios simples no encuentran nada en 20 segundos (prueba 03); la
  prueba 80 del foro es difícil para otros órdenes (prueba 04);
- acertijos de restos: casi todos los barcos múltiplos de algún k y un
  barco especial por fila cuyo resto fija su fila (pruebas generadas 7 y
  8);
- las filas se imprimen en el orden de la entrada.

Las colocaciones pasan el verificador en todas las pruebas de aquí, en 200
flotas generadas de ocho tipos y en unas pocas flotas difíciles conocidas,
cada una muy por debajo del límite; una implementación independiente
aceptada resuelve el mismo conjunto.

## Notas por lenguaje

- No hay solución en Python: en la prueba 03 PyPy necesita unos 5 s y
  CPython más de 10 s, frente a un límite de 1 s.
- Java necesitó un port más ajustado para pasar la prueba 8 del juez en
  1 s: la rama de saltar en una fila es un bucle y no una llamada de
  cola; los bitsets de A terminan en la fila más larga; los índices usan
  desplazamientos y máscaras. Una primera versión sin esto excedía 1 s en
  esa prueba.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1394_backtracking.cpp](1394_backtracking.cpp) | G++ 13.2 x64 | backtracking | O(M^N) worst case | AC | 0.406 s | 26956 KB |
| [1394_backtracking.go](1394_backtracking.go) | Go 1.14 x64 | backtracking | O(M^N) worst case | AC | 0.515 s | 35124 KB |
| [1394_backtracking.java](1394_backtracking.java) | Java 1.8 | backtracking | O(M^N) worst case | AC | 0.859 s | 49668 KB |
| [1394_backtracking.rs](1394_backtracking.rs) | Rust 1.75 x64 | backtracking | O(M^N) worst case | AC | 0.406 s | 32072 KB |
