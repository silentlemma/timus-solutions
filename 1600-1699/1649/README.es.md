# 1649. Abstraccionismo para todos

[Timus 1649](https://acm.timus.ru/problem.aspx?space=1&num=1649) · dificultad 6429 · backtracking

Problema original de Eugene Krokhalev, del cuarto de final de la subregión oriental del NEERC 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un lienzo de n × m empieza vacío. Las bacterias se colocan de una en una,
cada una en una celda vacía; una bacteria nueva suma uno a cada celda
vecina ya poblada (arriba, abajo, izquierda, derecha), y una celda que
llega a 5 vuelve a 1. Dados los recuentos finales (de 1 a 4 en cada
celda), hay que hallar un orden de poblar todas las celdas que los
produzca, o decir que no existe.

## Entrada

n y m (1 ≤ n, m ≤ 20) y luego n filas de m números de 1 a 4.

## Salida

`No`, o `Yes` y las celdas en orden de población, una «fila columna» por
línea. Se acepta cualquier orden válido.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 3
2 2 1
3 1 3
1 2 2
```

Salida:

```
Yes
2 2
2 1
1 1
1 2
2 3
1 3
3 3
3 2
3 1
```

## Solución

Una celda empieza en 1 y gana uno por cada vecina poblada después, módulo
4. Un orden funciona exactamente cuando cada celda v tiene entre 0 y deg(v)
vecinas posteriores, en número congruente con need(v) − 1 módulo 4.
Está fijado salvo en un caso: una celda interior (cuatro vecinas) que
muestra 1 puede tener 0 o 4 vecinas posteriores.

Se pela desde los dos extremos del orden. Una celda cuyas vecinas libres
deben ir todas después puede pasar al principio de cualquier orden válido
sin estropearlo, así que se puebla la primera y se retira. Igualmente,
una celda que no debe tener vecinas libres posteriores se puebla la
última; sus vecinas esperan entonces una vecina posterior menos, módulo 4.
Cada retirada puede forzar más celdas, así que una pila sigue pelando, y
una celda que pide más vecinas posteriores de las que le quedan demuestra
que el cuadro es imposible. Las partes independientes del lienzo se
resuelven por separado.

Cuando nada está forzado, la primera celda de cualquier orden válido sigue
teniendo todas sus vecinas después, así que debe ser una de las celdas
interiores indecisas que muestran 1. Una celda así, en cualquier orden
válido, va antes o después de todas sus vecinas, por lo que ramificar en
una sola de ellas, primera o última, no pierde nada. Dos comprobaciones de
recuento podan la búsqueda: los recuentos de vecinas posteriores deben
sumar el número de aristas, lo que fija cuántas celdas indecisas van
primero, y las indecisas que se tocan deben alternar (dos primeras o dos
últimas no pueden ser vecinas), así que cada grupo aporta uno de sus dos
colores de tablero; una suma de subconjuntos sobre los grupos dice si se
puede alcanzar el número. En la práctica cualquier rama desata una
cascada de movimientos forzados, así que la búsqueda queda diminuta.
Exponencial en el peor caso, pelado lineal por rama.

Detalles a tener en cuenta:

- solo un 1 interior es ambiguo; un 1 en el borde siempre es el último
  entre sus vecinas libres;
- tras una vecina poblada la última, un recuento de 1 pasa a 4 (todavía
  se requieren tres vecinas posteriores);
- la respuesta puede ser `No` aunque todos los recuentos estén en rango,
  como en un bloque de 2 × 2 de unos (prueba 07).

Un verificador reproduce el orden; las respuestas coinciden con una
implementación aceptada independiente en Yes o No y pasan el verificador
en 400 lienzos aleatorios y adversos, incluidos órdenes de tablero donde
toda celda interior muestra 1.

Complejidad: `O(2^U·(nm)^2)`, donde U es el número inicial de celdas
interiores que muestran 1, cada una probada primera o última.

## Notas por lenguaje

- Python eleva el límite de recursión: cada rama anida una llamada.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1649_backtracking.cpp](1649_backtracking.cpp) | G++ 13.2 x64 | backtracking | O(2^U·(nm)^2) | AC | 0.015 s | 276 KB |
| [1649_backtracking.go](1649_backtracking.go) | Go 1.14 x64 | backtracking | O(2^U·(nm)^2) | AC | 0.031 s | 1388 KB |
| [1649_backtracking.java](1649_backtracking.java) | Java 1.8 | backtracking | O(2^U·(nm)^2) | AC | 0.218 s | 3508 KB |
| [1649_backtracking.py](1649_backtracking.py) | Python 3.12 x64 | backtracking | O(2^U·(nm)^2) | AC | 0.125 s | 1136 KB |
| [1649_backtracking.rs](1649_backtracking.rs) | Rust 1.75 x64 | backtracking | O(2^U·(nm)^2) | AC | 0.062 s | 376 KB |
