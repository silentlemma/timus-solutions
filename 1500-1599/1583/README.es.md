# 1583. Queso

[Timus 1583](https://acm.timus.ru/problem.aspx?space=1&num=1583) · dificultad 1820 · binary_search

Problema original de Alexander Mironenko, preparado por Denis Musin, de la subregión oriental del NEERC del ACM ICPC 2007–2008, Ekaterimburgo, 27 de octubre de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una barra de queso de 10 × 100 × 10 cm pesa un gramo por centímetro
cúbico y tiene hasta 100 agujeros esféricos que no se tocan entre sí ni
con los lados. Una máquina la corta de través, un trozo de 500 gramos
tras otro: desde el último corte halla la marca donde el siguiente trozo
llega a 500 gramos, la redondea a micrómetros enteros y corta ahí. Se
detiene cuando quedan menos de 500 gramos y nunca corta exactamente en
el metro. Hay que imprimir los cortes en micrómetros.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

El número de agujeros y luego cada agujero como x, y, z y su radio, en
centímetros; y va a lo largo de la barra.

## Salida

El número de cortes y luego cada corte en micrómetros desde el inicio
de la barra.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
3.2 37.2 1.8 1
4.2 66.6 5.5 2.5
```

Salida:

```
19
50000
100000
150000
200000
250000
300000
350000
400419
450419
500419
550419
600419
651114
706964
756964
806964
856964
906964
956964
```

## Solución

El peso de la barra hasta una marca y es 100·y menos, por cada agujero,
la parte de la esfera por debajo de la marca: un casquete esférico de
altura h (entre 0 y 2r) con volumen π·h²·(3r − h)/3. Este peso crece con
y, ya que cada sección conserva algo de queso, así que la marca donde el
siguiente trozo llega a 500 gramos se halla por bisección, 100
divisiones desde el último corte hasta el final de la barra. La marca se
redondea a la rejilla de micrómetros y el siguiente trozo empieza en ese
corte redondeado, como hace la máquina. Como mucho 20 trozos, cada
búsqueda O(100·n). Los resultados se contrastaron con un programa
independiente en 60 barras aleatorias.

Detalles a tener en cuenta:

- cada trozo se mide desde el corte realmente hecho, tras redondear, y
  no desde la marca exacta, así que los errores no se acumulan;
- sin agujeros el vigésimo corte caería exactamente en el metro y no se
  hace (prueba 02);
- las coordenadas están en centímetros y los cortes en micrómetros: un
  centímetro son 10000 µm.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1583_binary_search.cpp](1583_binary_search.cpp) | G++ 13.2 x64 | binary_search | O(n) | AC | 0.015 s | 216 KB |
| [1583_binary_search.go](1583_binary_search.go) | Go 1.14 x64 | binary_search | O(n) | AC | 0.031 s | 1120 KB |
| [1583_binary_search.java](1583_binary_search.java) | Java 1.8 | binary_search | O(n) | AC | 0.140 s | 2956 KB |
| [1583_binary_search.py](1583_binary_search.py) | Python 3.12 x64 | binary_search | O(n) | AC | 0.187 s | 556 KB |
| [1583_binary_search.rs](1583_binary_search.rs) | Rust 1.75 x64 | binary_search | O(n) | AC | 0.031 s | 280 KB |
