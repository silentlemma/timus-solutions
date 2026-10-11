# 1308. La pirámide del decano

[Timus 1308](https://acm.timus.ru/problem.aspx?space=1&num=1308) · dificultad 2881 · bfs

Problema original con idea de Stanislav Vasiliev, preparado por Pavel Egorov y Alexander Mironenko, del Octavo Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 11–16 de marzo de 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una pirámide con base cuadrada unidad y cuatro caras laterales que son
triángulos equiláteros está sobre su base, centrada en el origen, con
los lados de la base paralelos a los ejes. Un movimiento la hace rodar
sobre una arista de la cara en la que está apoyada, sin que la arista se
mueva sobre la mesa. Hay una regla más: tras rodar hasta quedar sobre la
base por una arista, el siguiente giro debe ser por la arista opuesta
de la base. En 70 giros como mucho hay que dejar de nuevo la pirámide
sobre la base con el centro de la base lo más cerca posible de un punto
dado a distancia no mayor que 25 del origen. Se imprime esa distancia
con cuatro decimales.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Las coordenadas del punto objetivo.

## Salida

La menor distancia.

## Ejemplos

### Ejemplo 1

Entrada:

```
2.3660254037 1.3660254038
```

Salida:

```
0.0000
```

## Solución

Al hacer rodar un sólido sobre una arista, la cara siguiente queda al
otro lado de esa arista, así que conviene seguir las caras sobre la
mesa.

- De una cara lateral a la siguiente, el giro es sobre una arista que
  pasa por el vértice superior. Ese vértice no se mueve, y el triángulo
  nuevo es el viejo girado 60° a su alrededor.
- De una cara lateral a la base, el cuadrado queda más allá del lado
  inferior del triángulo, y por la regla el siguiente giro sigue recto
  hasta la cara lateral opuesta. Así, ese par de giros mueve el vértice
  dos alturas del triángulo más el lado del cuadrado, 1 + √3 en la
  dirección del vértice al lado inferior, y esa dirección se invierte.

Así que un triángulo apoyado queda descrito por su vértice y una de seis
direcciones. Los movimientos son un giro de ±60° (un giro) y un salto
de 1 + √3 (dos giros), y parar es un giro más hasta la base, cuyo
centro queda entonces a (1 + √3) / 2 más allá del vértice.

El primer giro saca la pirámide de la base por una de sus cuatro
aristas. Con giros de 60°, las aristas a 0° y 180° llevan a las mismas
seis direcciones, y las de 90° y 270° a otras seis. Así que el vértice,
medido en medios saltos, siempre está en una red hexagonal, y todas las
posiciones se pueden escribir exactamente como pares de enteros. Una
búsqueda de caminos mínimos por número de giros (cada movimiento cuesta
1 o 2, así que bastan cubetas por coste) visita todos los estados
alcanzables en 70 giros, unos miles por clase. Cada estado se prueba
como el último antes de rodar hasta la base, y gana el centro más
cercano; también vale no rodar nada.

`O(S)` para S estados alcanzables.

Detalles a tener en cuenta:

- muchos puntos se alcanzan exactamente, como el del ejemplo y el que
  está a un salto completo (pruebas 01 y 08), pero no todos los puntos
  de la red: medio salto a lo largo de un eje nunca se alcanza
  (prueba 07);
- la posición inicial también cuenta, sin girar nada (prueba 02).

El modelo se comparó con una simulación 3D real de la pirámide rodando,
girando el sólido sobre cada arista hasta que la cara siguiente queda
plana, con la regla del decano. Hasta 10 giros ambos dieron exactamente
el mismo conjunto de posiciones de la base.

## Notas por lenguaje

- (1 + √3) / 2 se calcula como 1/2 + sen 60°, con los mismos 60° que las
  direcciones.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1308_bfs.cpp](1308_bfs.cpp) | G++ 13.2 x64 | bfs | O(S) for S reachable states | AC | 0.015 s | 960 KB |
| [1308_bfs.go](1308_bfs.go) | Go 1.14 x64 | bfs | O(S) for S reachable states | AC | 0.031 s | 2996 KB |
| [1308_bfs.java](1308_bfs.java) | Java 1.8 | bfs | O(S) for S reachable states | AC | 0.171 s | 3912 KB |
| [1308_bfs.py](1308_bfs.py) | Python 3.12 x64 | bfs | O(S) for S reachable states | AC | 0.125 s | 1556 KB |
| [1308_bfs.rs](1308_bfs.rs) | Rust 1.75 x64 | bfs | O(S) for S reachable states | AC | 0.015 s | 1544 KB |
