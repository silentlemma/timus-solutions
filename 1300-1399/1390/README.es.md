# 1390. Disparos contra muros

[Timus 1390](https://acm.timus.ru/problem.aspx?space=1&num=1390) · dificultad 8947 · geometry

Problema original de Andrew Rumyantsev, del campus de entrenamiento de verano de Petrozavodsk, agosto de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Ocurren en orden hasta 50 000 sucesos. Un muro es un segmento cuya
recta no pasa por el origen; los muros pueden cruzarse. Un disparo se
hace desde el origen con velocidad no nula (vx, vy), y la bala vuela
en línea recta a velocidad constante. Para cada disparo hay que
imprimir el tiempo hasta que da en el muro más cercano construido antes
que él, o Infinite. Todas las coordenadas son enteros de valor absoluto
hasta 10 000.

Límite de tiempo: 3 segundos. Límite de memoria: 64 MB.

## Entrada

Líneas «shot vx vy» y «wall x1 y1 x2 y2», terminadas con «end».

## Salida

Para cada disparo el tiempo de vuelo con un error de hasta 10⁻⁶, o
Infinite.

## Ejemplos

### Ejemplo 1

Entrada:

```
shot 1 0
wall 1 0 0 1
shot 1 1
shot -1 3
wall 1 0 -1 2
shot -1 3
wall 1 1 -1 1
shot -1 3
wall 2 3 2 -3
wall 3 -2 -3 -2
shot 1 -1
shot 40 -39
shot 9999 -10000
shot -1 -1
shot -3000 -2000
shot -3001 -2000
shot -3000 -2001
shot 1 0
shot 1 1
wall -1 2 10 -10
shot -1 1
shot 0 1
shot 1 1
shot 1 0
shot 1 -1
wall 0 -10000 -10000 0
shot -2 -1
end
```

Salida:

```
Infinite
0.50000000000000000000
Infinite
0.50000000000000000000
0.33333333333333333333
2.00000000000000000000
0.05000000000000000000
0.00020000000000000000
2.00000000000000000000
0.00100000000000000000
Infinite
0.00099950024987506247
1.00000000000000000000
0.50000000000000000000
1.00000000000000000000
0.90909090909090909091
0.43478260869565217391
0.83333333333333333333
2.00000000000000000000
3333.33333333333333333
```

## Solución

Se escribe la recta de un muro como n · p = c con c > 0. Una bala de
velocidad v llega a la recta en el instante c / (n · v), así que el muro
más cercano en una dirección es el de mayor (n · v) / c entre los muros
que cubren esa dirección. Un muro cubre las direcciones de un extremo al
otro, un arco menor que π. Para dos muros, la diferencia de (n · v) / c
sobre los vectores unitarios v es una sinusoide, que cambia de signo a
lo sumo una vez en un arco así.

Esa es la condición de un árbol de Li Chao. Primero se leen todos los
sucesos, se toman como hojas las direcciones distintas de los disparos
ordenadas por ángulo, y se procesan los sucesos en orden. Un muro se
inserta en el rango de hojas que cubre, partido en dos si cruza el
semieje x positivo: en cada nodo del rango se queda el muro mejor en el
punto medio, y el otro baja a la mitad donde aún puede ganar. Un
disparo va de su hoja a la raíz y toma el mejor muro encontrado. Los
muros se comparan de forma exacta, (n₁ · v)·c₂ frente a (n₂ · v)·c₁, en
enteros de 64 bits, y el tiempo c / (n · v) se imprime por división
entera exacta con nueve cifras. `O(n log² n)`.

Detalles a tener en cuenta:

- una bala que roza el extremo de un muro da en él (prueba 04);
- un muro que cruza el semieje x positivo cubre los dos extremos de las
  direcciones ordenadas (prueba 05);
- una misma dirección llega con distintas velocidades, así que las hojas
  son direcciones y el tiempo usa la velocidad del disparo (prueba 07);
- un muro posterior más lejano no tapa a uno anterior más cercano
  (prueba 06), y los muros pueden cruzarse;
- los muros sin ningún disparo también deben leerse (prueba 02).

Las respuestas se compararon con una comprobación de cada muro para cada
disparo en fracciones exactas en 400 casos pequeños aleatorios y, con
enteros, en todas las pruebas generadas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1390_geometry.cpp](1390_geometry.cpp) | G++ 13.2 x64 | geometry | O(n log^2 n) | AC | 0.218 s | 5452 KB |
| [1390_geometry.go](1390_geometry.go) | Go 1.14 x64 | geometry | O(n log^2 n) | AC | 0.125 s | 11156 KB |
| [1390_geometry.java](1390_geometry.java) | Java 1.8 | geometry | O(n log^2 n) | AC | 0.281 s | 11420 KB |
| [1390_geometry.py](1390_geometry.py) | Python 3.12 x64 | geometry | O(n log^2 n) | AC | 1.937 s | 32172 KB |
| [1390_geometry.rs](1390_geometry.rs) | Rust 1.75 x64 | geometry | O(n log^2 n) | AC | 0.062 s | 8744 KB |
