# 1978. Suma vectorial máxima para cada cantidad

[Timus 1978](https://acm.timus.ru/problem.aspx?space=1&num=1978) · dificultad 3231 · geometry, sorting

Problema original de Alexander Ipatov, del Campeonato de Programación Deportiva de los Urales 2013.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dados `n` vectores planos, elija exactamente `k` posiciones distintas de
la entrada y maximice la longitud euclídea de su suma. Calcule el
resultado para cada `k=1,…,n`. Los vectores iguales son entradas
distintas; se permiten coordenadas negativas y cero.

Límites: `1≤n≤1000` y coordenadas enteras `−10⁶≤x,y≤10⁶`. Tiempo: 2
segundos; memoria: 64 MB.

## Entrada

La primera línea contiene `n`. Cada una de las siguientes `n` líneas
contiene las coordenadas `x y`.

## Salida

Escriba `n` líneas: la línea `k` da la mayor longitud con exactamente
`k` entradas.

## Evaluación

Los números se comparan con error absoluto o relativo 10⁻⁶.

## Ejemplos

Entrada:

```
3
3 -2
-3 -2
0 4
```

Salida:

```
4.000000
4.000000
0.000000
```

## Solución

Para una dirección `u`, tome los `k` vectores con mayores proyecciones.
Al girar la dirección, estos conjuntos incluyen un óptimo para cada
cantidad. Si una suma óptima es `s≠0`, cualquier conjunto con mayor
proyección sobre `s/|s|` tendría longitud mayor que `|s|`, una
contradicción. Ante empates se puede perturbar ligeramente la dirección
y conservar la proyección óptima en el límite. Los óptimos nulos tampoco
se pierden.

Mantenga el orden ascendente de proyecciones sobre `(1,t)` mientras `t`
va de menos a más infinito. Inicialmente ordene por `y` decreciente y
luego por `x` creciente. Un prefijo contiene las proyecciones menores;
su complemento contiene las mayores. Registrar ambos cubre también el
semicírculo opuesto.

Dos vectores con diferentes `y` intercambian posiciones en
`t=(x_low−x_high)/(y_high−y_low)`, donde `high` tiene mayor `y`. Ordene
los eventos mediante productos cruzados enteros exactos. Los pares con
igual `y` no se cruzan dentro del semicírculo abierto; los vectores
idénticos no necesitan eventos.

Un evento aislado intercambia dos elementos adyacentes y modifica solo
el prefijo que termina entre ellos. Guarde las sumas de coordenadas de
cada prefijo, actualice el máximo de su longitud al cuadrado y también
el tamaño complementario mediante la suma total menos el prefijo.

Los eventos simultáneos se procesan juntos. Cada grupo de proyecciones
iguales forma un bloque contiguo que se invierte al pasar el evento.
Para cada par del lote, forme el intervalo entre sus posiciones
actuales. Fusione intervalos que se solapen, manteniendo separados los
que solo sean adyacentes. Invierta cada bloque, reconstruya sus prefijos
internos y registre los candidatos. Los prefijos exteriores conservan
sus sumas. Esto también maneja vectores repetidos.

Entre direcciones consecutivas de eventos, el orden no cambia. El estado
inicial y todas las inversiones por lotes visitan los conjuntos de
proyección necesarios. Cada prefijo o complemento registrado es un
subconjunto real, de modo que no sobreestima el óptimo. El argumento de
proyecciones completa la prueba.

Hay `O(n²)` eventos y ordenarlos cuesta `O(n² log n)`. La longitud total
de los bloques invertidos es `O(n²)`: un bloque no trivial está
conectado por sus eventos y su longitud no supera el doble de su número.
Ordenar los inicios dentro de los lotes respeta la misma cota. Memoria:
`O(n²)`.

En el ejemplo, `(0,4)` tiene longitud 4. Los primeros dos vectores suman
`(0,−4)`, también de longitud 4. La suma de los tres es cero.

Trampas:

- Se exigen exactamente `k` entradas; el óptimo puede disminuir al aumentar `k`.
- Una dirección puede tener varios grupos de proyección distintos; no
  fusione grupos adyacentes.
- Un par de un lote simultáneo no tiene por qué ser adyacente antes de
  procesarlo.
- Direcciones enteras muy próximas pueden diferir por un determinante de
  uno; compare las pendientes exactamente.
- Las longitudes al cuadrado alcanzan `2·10¹⁸`; use enteros de 64 bits
  para productos y normas.

## Notas por lenguaje

C++, Go, Java y Rust ordenan índices de pares empaquetados con productos
cruzados exactos de 64 bits. Java usa arreglos primitivos y ordenación
por mezcla.

Python no guarda los O(n²) eventos. Un conjunto óptimo se separa de cada
otro vector distinto por una recta, y esa recta puede girarse hasta
pasar por uno de los vectores. Así, para cada vector distinto como
pivote ordena los demás por la pendiente de su recta con el pivote, gira
la recta alrededor del pivote y en cada paso registra el conjunto de un
lado y su complemento, añadiendo las copias del propio pivote una a una.
Las cotas de las coordenadas separan las pendientes distintas mucho más
que el redondeo de los double, y los vectores con igual pendiente pueden
pasarse en cualquier orden, porque cada conjunto intermedio es un
subconjunto real. Las normas al cuadrado siguen siendo enteros exactos;
solo las raíces finales usan coma flotante. `O(n² log n)` de tiempo y
`O(n)` de memoria. Se ejecuta con PyPy, 0,80 s de los 2 s en el juez; la
versión anterior, con todos los eventos de pares, superaba el límite de
tiempo en la prueba 7 del juez con CPython y en la 33 con PyPy.

Las respuestas coinciden con probar todos los subconjuntos en 14 139
casos pequeños.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1978_geometry.cpp](1978_geometry.cpp) | G++ 13.2 x64 | geometry | O(n^2 log n) | AC | 0.078 s | 2048 KB |
| [1978_geometry.go](1978_geometry.go) | Go 1.14 x64 | geometry | O(n^2 log n) | AC | 0.218 s | 6416 KB |
| [1978_geometry.java](1978_geometry.java) | Java 1.8 | geometry | O(n^2 log n) | AC | 0.453 s | 7792 KB |
| [1978_geometry.py](1978_geometry.py) | PyPy 3.10 x64 | geometry | O(n^2 log n) | AC | 0.796 s | 9808 KB |
| [1978_geometry.rs](1978_geometry.rs) | Rust 1.75 x64 | geometry | O(n^2 log n) | AC | 0.093 s | 4092 KB |
