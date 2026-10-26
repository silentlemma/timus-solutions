# 1394. Barcos. Versión 2

[Timus 1394](https://acm.timus.ru/problem.aspx?space=1&num=1394) · dificultad 14802 · backtracking, linear_programming

Problema original preparado por Vladimir Yakovlev.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

La misma tarea que el [problema 1115](../../1100-1199/1115/README.es.md)
con pruebas mucho más difíciles: N < 100 barcos de longitudes enteras
de 1 a 100 deben llenar exactamente 1 < M < 10 filas de longitud dada,
con al menos un barco por fila. Existe una colocación; hay que imprimir
una. El juez
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

La partición exacta en varias partes es difícil en general, y las
pruebas del juez están elegidas para vencer heurísticas aisladas. Hay
dos soluciones: backtracking, con tres búsquedas exactas por turnos
(C++, Go, Java, Rust), y programación lineal, que ve todas las filas a
la vez y es mucho más rápida (los cinco lenguajes).

El backtracking alterna tres búsquedas exactas en cinco turnos: B, B con
las filas de menor a mayor longitud, C, D y B otra vez. Las porciones de
tiempo crecen 1,6 veces hasta un tope y las rondas posteriores alteran
los órdenes, hasta que una búsqueda coloca todos los barcos o se agota
el presupuesto interno.

- B, filas una a una. Los barcos van de más largo a más corto; dentro de
  una fila cada barco se toma o se salta, y las copias de una longitud
  saltada se saltan juntas. Cada fila abierta debe seguir siendo suma de
  un subconjunto de los barcos sin usar (bitsets de sumas de sufijos,
  recalculados al abrir una fila). Un estado fallido, los barcos sin
  usar más las filas abiertas, va a una tabla hash que sobrevive a los
  reinicios, porque no depende del orden. Uno de cada dos turnos de B
  también comprueba los restos con los módulos de D y módulos pequeños.
- C, B solo sobre las longitudes raras (de una a tres copias): una fila
  necesita entonces un resto que formen los barcos comunes, y un B
  anidado coloca los comunes al final. Así se evitan las muchas formas
  intercambiables de llenar filas con barcos comunes.
- D, C donde «raro» significa no divisible por un módulo K que divide a
  muchos barcos, más una comprobación exacta de restos: los no múltiplos
  restantes de cada resto deben repartirse entre las filas restantes de
  modo que cada fila obtenga su longitud módulo K. Lo responde una DP
  sobre filas y vectores de cantidades (en base mixta), con un
  presupuesto por consulta y una caché que sobrevive a los reinicios.

Hacen falta las tres: sin C se acaba el tiempo en la prueba 8 del juez,
sin D en la 10, y con B en dos turnos de cuatro en vez de tres de cinco,
en la 7. Una cuarta búsqueda, barcos uno a uno en filas, no hizo falta.

La programación lineal trabaja con cantidades: los barcos tienen k
longitudes distintas, y un relleno de una fila es un vector de
cantidades que suma la longitud de la fila. Tres etapas van de las
baratas a las caras; gana la primera colocación encontrada.

- Voraz: las filas van desde la más corta, y cada una toma, en un orden
  fijo, todo barco que aún deja completarla con los barcos siguientes
  (bitsets de sumas de sufijos); la fila más larga se queda con el
  resto. Se prueban seis órdenes: barcos por longitud decreciente y
  creciente, luego barcos y filas barajados.
- Generación de columnas: un PL sobre pares (fila, relleno), con como
  mucho un relleno por fila y no más barcos de cada longitud de los que
  hay, maximiza el número de filas llenas. Empieza vacío; el método
  símplex da precios duales de las longitudes y de las filas, y para
  cada fila una DP halla el relleno más barato con esos precios (una
  suma de subconjunto de coste mínimo con multiplicidades). Un relleno
  con coste reducido negativo entra en el PL. Cuando el PL llena todas
  las filas, se fija la fila con el mayor valor en el PL, sus rellenos
  se prueban por valor decreciente, y el resto se resuelve igual. Los
  precios dicen qué longitudes escasean, justo lo que las búsquedas por
  filas no ven: en la prueba 03 esta etapa necesita 9 estados. Se
  detiene tras 160 resoluciones del PL.
- Búsqueda exacta: va primero la fila con menos rellenos (los cuenta una
  DP), sus rellenos se enumeran con bitsets de sumas de sufijos, y los
  estados fallidos se recuerdan. El presupuesto se duplica hasta hallar
  una colocación, con intentos voraces entre medias. Esta búsqueda es
  completa, así que la respuesta nunca depende de la coma flotante: el
  PL solo ordena la búsqueda.

S es la longitud total de los barcos.

Detalles a tener en cuenta:

- con la flota de la prueba 70 del foro, con una fila de 820, los
  reinicios simples no encuentran nada en 20 segundos (prueba 03); la
  prueba 80 del foro es difícil para otros órdenes (prueba 04);
- acertijos de restos: casi todos los barcos múltiplos de algún k y un
  barco especial por fila cuyo resto restringe la asignación de filas
  (pruebas generadas 7 y 8);
- flotas que solo resuelve la búsqueda por filas B, y solo en un orden
  afortunado, mientras C y D fallan (pruebas 14 y 15);
- las filas se imprimen en el orden de la entrada.

Las colocaciones pasan el verificador en todas las pruebas de aquí, en
130 flotas difíciles y en 11 000 flotas generadas (6 000 de ellas con
filas iguales): el backtracking en como mucho 0,55 s y 0,08 s, la
programación lineal en como mucho 0,02 s y 0,24 s, en las flotas
difíciles y en las generadas respectivamente.

## Notas por lenguaje

- Python ejecuta la programación lineal con PyPy con 64 órdenes voraces
  en vez de seis y la búsqueda exacta sin presupuesto. El PL conserva su
  base cuando entran rellenos nuevos, así que el método símplex sigue
  desde donde se detuvo en vez de empezar de nuevo.
- Go, Java y Rust reproducen mt19937 y el barajado de libstdc++ de los
  reintentos voraces, así que sus colocaciones por programación lineal
  son byte a byte las de C++.
- El backtracking en Python excedía el límite en la prueba 7 del juez en
  cuatro versiones, cada una con su búsqueda principal, así que en
  Python solo está la solución por programación lineal.
- El Java con backtracking necesitó un port más ajustado para pasar la
  prueba 8 del juez en 1 s: la rama de saltar en una fila es un bucle y
  no una llamada de cola, y los índices usan desplazamientos y máscaras.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1394_backtracking.cpp](1394_backtracking.cpp) | G++ 13.2 x64 | backtracking | O(M^N · poly(N, M, S)) per search | AC | 0.406 s | 26108 KB |
| [1394_backtracking.go](1394_backtracking.go) | Go 1.14 x64 | backtracking | O(M^N · poly(N, M, S)) per search | AC | 0.468 s | 28492 KB |
| [1394_backtracking.java](1394_backtracking.java) | Java 1.8 | backtracking | O(M^N · poly(N, M, S)) per search | AC | 0.546 s | 26652 KB |
| [1394_backtracking.rs](1394_backtracking.rs) | Rust 1.75 x64 | backtracking | O(M^N · poly(N, M, S)) per search | AC | 0.453 s | 27520 KB |
| [1394_linear_programming.cpp](1394_linear_programming.cpp) | G++ 13.2 x64 | linear_programming | O(M^N · poly(N, M, S)) worst case | AC | 0.015 s | 6812 KB |
| [1394_linear_programming.go](1394_linear_programming.go) | Go 1.14 x64 | linear_programming | O(M^N · poly(N, M, S)) worst case | AC | 0.031 s | 5244 KB |
| [1394_linear_programming.java](1394_linear_programming.java) | Java 1.8 | linear_programming | O(M^N · poly(N, M, S)) worst case | AC | 0.140 s | 3300 KB |
| [1394_linear_programming.py](1394_linear_programming.py) | PyPy 3.10 x64 | linear_programming | O(M^N · poly(N, M, S)) worst case | AC | 0.343 s | 11144 KB |
| [1394_linear_programming.rs](1394_linear_programming.rs) | Rust 1.75 x64 | linear_programming | O(M^N · poly(N, M, S)) worst case | AC | 0.015 s | 6964 KB |
