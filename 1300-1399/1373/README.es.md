# 1373. Pictura ex Machina

[Timus 1373](https://acm.timus.ru/problem.aspx?space=1&num=1373) · dificultad 837 · geometry

Problema original de Pavel Egorov, del Noveno Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 19–24 de abril de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un trazador pinta N ≤ 100 000 trazos. Cada trazo avanza X milímetros en
una dirección, gira 90° en sentido horario y avanza X milímetros más; se
da por su inicio y su final, enteros de valor absoluto a lo sumo
10 000. Hay que imprimir el ancho y el alto del menor marco con lados
paralelos a los ejes que contiene todos los trazos, con 4 decimales.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Hasta el final de la entrada, líneas de cuatro enteros: el inicio y el
final de un trazo.

## Salida

El ancho y el alto del marco.

## Ejemplos

### Ejemplo 1

Entrada:

```
0 0 1 1
1 1 2 0
2 0 0 0
2 0 3 0
```

Salida:

```
3.0000 2.0000
```

## Solución

Un trazo son dos segmentos, así que el marco solo tiene que contener su
inicio, su final y su esquina. Si el primer tramo es (p, q), el giro en
sentido horario hace que el segundo sea (q, −p), y juntos dan el
desplazamiento del inicio al final: p + q = dx y q − p = dy. Así que la
esquina es el inicio más ((dx − dy) / 2, (dx + dy) / 2). La respuesta es
el rectángulo envolvente de todos esos puntos. Duplicar todas las
coordenadas mantiene enteras las mitades, y al final el rectángulo se
divide otra vez entre dos. `O(N)`.

Detalles a tener en cuenta:

- el eje y apunta hacia arriba: así el ejemplo da 3 × 2, y con el giro
  contrario daría 3 × 1,5;
- las esquinas pueden caer fuera del rango de la entrada, hasta 20 000
  del origen (prueba 06);
- puede no haber ningún trazo, y entonces la respuesta es 0 × 0
  (prueba 02);
- no se da el número de trazos: hay que leer hasta el final de la
  entrada.

## Notas por lenguaje

- Go lee con un escáner de palabras, más rápido que `fmt.Fscan` para
  400 000 números.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1373_geometry.cpp](1373_geometry.cpp) | G++ 13.2 x64 | geometry | O(N) | AC | 0.218 s | 144 KB |
| [1373_geometry.go](1373_geometry.go) | Go 1.14 x64 | geometry | O(N) | AC | 0.093 s | 10332 KB |
| [1373_geometry.java](1373_geometry.java) | Java 1.8 | geometry | O(N) | AC | 0.187 s | 5024 KB |
| [1373_geometry.py](1373_geometry.py) | Python 3.12 x64 | geometry | O(N) | AC | 0.312 s | 41448 KB |
| [1373_geometry.rs](1373_geometry.rs) | Rust 1.75 x64 | geometry | O(N) | AC | 0.031 s | 14464 KB |
