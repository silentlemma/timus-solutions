# 1546. Ordenación japonesa

[Timus 1546](https://acm.timus.ru/problem.aspx?space=1&num=1546) · dificultad 888 · sorting

Problema original de Vladimir Yakovlev, del XI Campeonato Universitario por Equipos de Programación de los Urales, Ekaterimburgo, 21 de abril de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay que ordenar cadenas de letras minúsculas y cifras (como mucho
100 KB en total) en orden «japonés», donde los números dentro de las
cadenas se comparan por su valor: photox2 va antes que photox10. El
enunciado no detalla las reglas; ofrece un programa de muestra que
ordena entradas pequeñas.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Las cadenas, una por línea.

## Salida

Las mismas cadenas en orden japonés.

## Ejemplos

### Ejemplo 1

Entrada:

```
photox10
photox1
photo2
photox2
```

Salida:

```
photo2
photox1
photox2
photox10
```

## Solución

Las reglas son las de la ordenación natural de un gestor de archivos, y
los detalles de abajo coinciden con el programa de muestra tal como se
cita en el foro del juez:

- la cadena se parte en letras y tramos máximos de cifras;
- se compara trozo a trozo: un número va antes que una letra, los
  números se comparan por valor (por longitud sin ceros a la izquierda y
  luego cifra a cifra, pues pueden ser muy largos) y las letras por su
  código;
- la cadena que termina antes va primero;
- solo si todos los trozos son iguales se comparan los ceros a la
  izquierda de los números, tramo a tramo, y más ceros van antes:
  000 < 00 < 0, a001 < a01 y 01w01 < 01w1.

Cada cadena recibe una clave: la lista de trozos y la lista de los
ceros con signo menos; una ordenación estable por la clave hace el
resto. `O(L log n)` para una longitud total L.

Detalles a tener en cuenta:

- los ceros solo deshacen empates: z001pp00 va después de z0pp01
  (prueba 02);
- una cadena de ceros es un número, y 000 va antes que 0 (prueba 03);
- los números pueden pasar de 64 bits (prueba 04);
- las cifras van antes que las letras: 1, 2, 10, a, a1, aa (prueba 06).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1546_sorting.cpp](1546_sorting.cpp) | G++ 13.2 x64 | sorting | O(L log n) | AC | 0.031 s | 5476 KB |
| [1546_sorting.go](1546_sorting.go) | Go 1.14 x64 | sorting | O(L log n) | AC | 0.093 s | 7628 KB |
| [1546_sorting.java](1546_sorting.java) | Java 1.8 | sorting | O(L log n) | AC | 0.312 s | 11504 KB |
| [1546_sorting.py](1546_sorting.py) | Python 3.12 x64 | sorting | O(L log n) | AC | 0.140 s | 9448 KB |
| [1546_sorting.rs](1546_sorting.rs) | Rust 1.75 x64 | sorting | O(L log n) | AC | 0.031 s | 4692 KB |
