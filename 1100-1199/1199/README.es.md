# 1199. El camino menos expuesto del ratón hasta el queso

[Timus 1199](https://acm.timus.ru/problem.aspx?space=1&num=1199) · dificultad 3906 · geometry

Problema original de Nikita Rybak.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una cocina tiene hasta 100 muebles, cada uno un polígono convexo de 3 a
10 vértices, y dos muebles cualesquiera están a más de 20 cm. Un punto es
peligroso si está a más de 10 cm de todos los muebles. Hay que hallar una
poligonal del ratón al queso con la menor longitud total de tramos
peligrosos. Cada segmento debe ser entero peligroso o entero seguro, salvo
sus extremos, y la poligonal puede tener como mucho 1000 vértices.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

El ratón y el queso como `x y x y`, luego `N` y luego cada polígono como
`K` seguido de `K` vértices. Las coordenadas están en metros, con como
mucho tres decimales y valor absoluto hasta `10⁵`; ni el ratón ni el
queso están dentro de un polígono.

## Salida

El número de vértices de la poligonal, contando ambos extremos, y luego
los vértices, uno por línea, con precisión `10⁻⁴`.

## Evaluación

Se acepta cualquier poligonal que empiece en el ratón, termine en el
queso, tenga como mucho 1000 vértices, no tenga segmentos en parte
seguros y en parte peligrosos, y tenga la menor longitud peligrosa; el
verificador de referencia calcula exactamente la parte segura de cada
segmento y admite 1 mm de holgura.

## Ejemplos

### Ejemplo 1

Entrada:

```
1.0 1.5 0.0 1.5
1
4
0.0 0.0
0.0 1.0
1.0 1.0
1.0 0.0
```

Salida:

```
4
1.0 1.5
1.0 1.1
0.0 1.1
0.0 1.5
```

## Solución

La zona segura alrededor de un mueble es el polígono ensanchado 10 cm,
una zona convexa, y las zonas no se tocan porque los muebles están a más
de 20 cm. Moverse dentro de una zona no cuesta nada, así que un camino es
una cadena de zonas unidas por tramos peligrosos, y cada tramo cuesta al
menos la separación entre lo que une. Eso da un grafo cuyos nodos son el
ratón, el queso y las zonas: la separación entre dos zonas es la
distancia entre los polígonos menos 20 cm, la del ratón o el queso a una
zona es su distancia al polígono menos 10 cm (o 0 si ya está a salvo), y
del ratón al queso cuesta la distancia en línea recta. El algoritmo de
Dijkstra sobre este grafo completo da la respuesta.

Cada separación se puede recorrer exactamente. Entre dos polígonos se
toma su par de puntos más cercanos; el segmento entre ellos, acortado
10 cm por cada extremo, es peligroso de punta a punta. Un segmento
peligroso que cortara una tercera zona daría un camino más barato a
través de ella, así que el camino más corto nunca lo necesita. Dentro de
una zona el ratón pasa al punto más cercano del polígono, recorre el
borde en el sentido que pasa por menos vértices y sale por el punto más
cercano a la zona siguiente; nunca atraviesa los muebles, y cada zona
añade como mucho nueve vértices, muy por debajo del límite.

La distancia entre dos polígonos es la menor distancia de un vértice de
uno a un lado del otro. Un par se omite cuando ni siquiera la cota de sus
circunferencias envolventes puede mejorar la distancia al destino, lo
que descarta la mayoría de los pares en la práctica. `O(N²K²)` en el peor
caso.

Detalles a tener en cuenta:

- no se promete que los vértices vengan en orden, así que primero se
  ordena cada polígono por ángulo alrededor de su centro;
- los puntos a exactamente 10 cm cuentan como seguros, por eso la
  respuesta del ejemplo va por el borde de la zona segura;
- el ratón o el queso pueden estar ya a menos de 10 cm de un mueble;
- el camino recto del ratón al queso también debe ser un candidato.

Las longitudes peligrosas se compararon con una solución escrita aparte
en 320 cocinas aleatorias y en todas las pruebas, con el verificador en
ambos sentidos.

## Notas por lenguaje

- Todos los lenguajes hacen la misma búsqueda con la misma cota de
  circunferencias e imprimen nueve decimales.
- Java formatea los números con `Locale.US`, porque la configuración
  regional por defecto podría imprimir comas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1199_geometry.cpp](1199_geometry.cpp) | G++ 13.2 x64 | geometry | O(N²K²) | AC | 0.015 s | 352 KB |
| [1199_geometry.go](1199_geometry.go) | Go 1.14 x64 | geometry | O(N²K²) | AC | 0.031 s | 1360 KB |
| [1199_geometry.java](1199_geometry.java) | Java 1.8 | geometry | O(N²K²) | AC | 0.234 s | 6572 KB |
| [1199_geometry.py](1199_geometry.py) | Python 3.12 x64 | geometry | O(N²K²) | AC | 0.640 s | 1892 KB |
| [1199_geometry.rs](1199_geometry.rs) | Rust 1.75 x64 | geometry | O(N²K²) | AC | 0.031 s | 376 KB |
