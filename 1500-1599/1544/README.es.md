# 1544. Compañeros de clase 3

[Timus 1544](https://acm.timus.ru/problem.aspx?space=1&num=1544) · dificultad 1252 · graphs

Problema original del folclore, preparado por Sergey Pupyrev para el XI Campeonato Universitario por Equipos de Programación de los Urales, Ekaterimburgo, 21 de abril de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N ≤ 50 ordenadores forman una red conexa; cada uno usa el protocolo
europeo (E) o el japonés (J). Pedir a un ordenador que cambie de
protocolo lo cambia junto con todo lo alcanzable desde él a través de
ordenadores con su protocolo antiguo. Hay que hallar el menor número de
peticiones que deje todos los ordenadores con un mismo protocolo, y
listarlas como «ordenador protocolo».

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y M, los N protocolos y luego los M enlaces.

## Salida

K y luego las K peticiones. Se acepta cualquier lista óptima.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 5
E E E J J
1 2
1 3
1 4
4 2
5 2
```

Salida:

```
1
1 J
```

## Solución

Se juntan los ordenadores enlazados con el mismo protocolo en regiones.
Una petición recolorea una región, que se funde con todas las regiones
vecinas, ya que todas tienen el otro protocolo. En el grafo de regiones,
cambiar la misma región una y otra vez absorbe cada vez un anillo más de
regiones, así que una región de excentricidad e termina en e
peticiones; lo mejor es elegir un centro del grafo de regiones, y la
respuesta es su radio. Una búsqueda en anchura desde cada región lo
encuentra en `O(R·(R + M))` para R regiones.

Que ningún plan mejora el radio se comprobó con una búsqueda en anchura
sobre los 2^N estados de protocolos en 300 redes aleatorias de hasta 10
ordenadores; todas las respuestas coincidieron.

Detalles a tener en cuenta:

- en esta construcción, las peticiones deben alternar el protocolo
  del ordenador elegido, empezando por el otro (pruebas 04, 07);
- la mejor región puede usar cualquiera de los dos protocolos
  (prueba 06);
- una red con un solo protocolo necesita 0 peticiones (pruebas 02, 03);
- hay varios planes óptimos, así que las pruebas usan un verificador
  (todas las pruebas).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1544_graphs.cpp](1544_graphs.cpp) | G++ 13.2 x64 | graphs | O(R * (R + M)) | AC | 0.015 s | 208 KB |
| [1544_graphs.go](1544_graphs.go) | Go 1.14 x64 | graphs | O(R * (R + M)) | AC | 0.031 s | 1192 KB |
| [1544_graphs.java](1544_graphs.java) | Java 1.8 | graphs | O(R * (R + M)) | AC | 0.109 s | 776 KB |
| [1544_graphs.py](1544_graphs.py) | Python 3.12 x64 | graphs | O(R * (R + M)) | AC | 0.093 s | 748 KB |
| [1544_graphs.rs](1544_graphs.rs) | Rust 1.75 x64 | graphs | O(R * (R + M)) | AC | 0.015 s | 260 KB |
