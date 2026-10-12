# 1340. Cucaracha

[Timus 1340](https://acm.timus.ru/problem.aspx?space=1&num=1340) · dificultad 4615 · geometry

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

Se traslada el inicio al origen y se alinea el rumbo con el eje x
positivo, reduciendo el ángulo por cuadrantes. Sean (u, v) la miga
transformada, D² el desplazamiento original al cuadrado, s = ±1 el
sentido del giro y d la distancia de (0, sR) a la miga. Se calcula
q = D² − 2sRv = d² − R² directamente; se corrige el redondeo negativo
a cero solo dentro de 10⁻¹⁵D².

- Arco y segmento: si la miga no está dentro de la circunferencia, la
  cucaracha gira hasta quedar de cara a la miga por una tangente. Se
  exige q ≥ 0, el segmento mide √q y el giro se calcula como
  atan2(u, R − sv) − atan2(√q, R).
- Dos arcos: la segunda circunferencia toca la primera, así que su
  centro está a 2R del primer centro, y pasa por la miga, así que su
  centro está a R de la miga. Cada uno de los como mucho dos puntos que
  cumplen ambas condiciones da un camino; los dos ángulos de arco salen
  de los ángulos alrededor de los centros. Las intersecciones requieren
  0 ≤ q ≤ 8R²; su altura se calcula con
  √(q(8R² − q)) / (2d), evitando restar cuadrados casi iguales.

Todos los ángulos de arco se miden en el sentido del giro y se toman
módulo 2π; el segundo arco usa atan2 de los productos vectorial y
escalar de sus radios. No se amplían los intervalos de distancia con un
epsilon fijo ni se convierten giros casi completos en cero: un destino
interior puede exigir un rodeo largo. La respuesta es el más corto de los
como mucho seis candidatos. `O(1)`.

Detalles a tener en cuenta:

- con la miga dentro de una circunferencia de giro, el camino de arco y
  segmento de ese lado no existe, y dos arcos pueden ser lo más corto
  (prueba 06);
- una miga justo delante debe dar la distancia simple, no un círculo
  completo (prueba 03);
- si los extremos coinciden, se devuelve 0 antes de calcular círculos (pruebas 05, 10);
- incluso apenas dentro del círculo delantero, el atajo tangente es
  imposible; un epsilon no debe permitirlo (prueba 18);
- R = 0 permite girar en el sitio (prueba 02).

Las respuestas se comprobaron en 10 000 entradas aleatorias pequeñas
con un oráculo independiente que enumera exhaustivamente los ángulos
de cambio y verifica cada camino integrando el movimiento.

## Notas por lenguaje

- Las cinco soluciones prueban los mismos candidatos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1340_geometry.cpp](1340_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 196 KB |
| [1340_geometry.go](1340_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1200 KB |
| [1340_geometry.java](1340_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.093 s | 1976 KB |
| [1340_geometry.py](1340_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.093 s | 792 KB |
| [1340_geometry.rs](1340_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.015 s | 272 KB |
