# 1340. Cucaracha

[Timus 1340](https://acm.timus.ru/problem.aspx?space=1&num=1340) · dificultad 4914 · geometry

Problema original de Pavel Egorov, del USU Championship 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una cucaracha está en (X, Y) mirando en la dirección A, en grados en
sentido antihorario desde el eje x, y no puede girar más cerrado que
por una circunferencia de radio R. Hay que hallar la longitud del
camino más corto hasta una miga en (KX, KY), con cualquier dirección
final, con cuatro cifras tras el punto. Todas las coordenadas y R valen
como mucho 10 000 en valor absoluto.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

X, Y, A y R en la primera línea, KX y KY en la segunda.

## Salida

La longitud del camino más corto.

## Ejemplos

### Ejemplo 1

Entrada:

```
1 2 90 10
21 2
```

Salida:

```
31.4159
```

## Solución

Es el camino más corto de un coche que solo avanza con un radio de giro
acotado, el coche de Dubins, hasta un punto con cualquier rumbo final.
Se sabe que ese camino es o bien un arco seguido de un segmento recto, o
bien dos arcos que giran en sentidos opuestos. Ambos tipos empiezan en
una de las dos circunferencias de radio R que tocan el inicio, la
izquierda o la derecha.

- Arco y segmento: si la miga no está dentro de la circunferencia, la
  cucaracha gira hasta quedar de cara a la miga por una tangente. Con la
  miga a distancia d del centro, el segmento mide √(d² − R²), y el punto
  de tangencia está acos(R / d) antes de la dirección de la miga vista
  desde el centro.
- Dos arcos: la segunda circunferencia toca la primera, así que su
  centro está a 2R del primer centro, y pasa por la miga, así que su
  centro está a R de la miga. Cada uno de los como mucho dos puntos que
  cumplen ambas condiciones da un camino; los dos ángulos de arco salen
  de los ángulos alrededor de los centros.

Todos los ángulos de arco se miden en el sentido del giro y se toman
módulo 2π. Un ángulo que se queda a un error de redondeo de la vuelta
completa se toma como ningún giro, o una miga justo delante costaría un
círculo entero. La respuesta es el más corto de los como mucho seis
candidatos. `O(1)`.

Detalles a tener en cuenta:

- con la miga dentro de una circunferencia de giro, el camino de arco y
  segmento de ese lado no existe, y dos arcos pueden ser lo más corto
  (prueba 06);
- una miga justo delante debe dar la distancia simple, no un círculo
  completo (prueba 03);
- la miga bajo la cucaracha se alcanza enseguida, 0 (prueba 05);
- R = 0 permite girar en el sitio (prueba 02).

Las respuestas se compararon, en 300 casos aleatorios, con una búsqueda
sobre el rumbo final que prueba los seis caminos estándar de Dubins
para cada rumbo; esos caminos se comprobaron recorriéndolos paso a
paso. La mayor diferencia fue de 5 · 10⁻⁵, el paso de la búsqueda.

## Notas por lenguaje

- Las cinco soluciones prueban los mismos candidatos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1340_geometry.cpp](1340_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 204 KB |
| [1340_geometry.go](1340_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1104 KB |
| [1340_geometry.java](1340_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.156 s | 2008 KB |
| [1340_geometry.py](1340_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 736 KB |
| [1340_geometry.rs](1340_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.015 s | 272 KB |
