# 1312. Platos

[Timus 1312](https://acm.timus.ru/problem.aspx?space=1&num=1312) · dificultad 2925 · geometry

Problema original con idea de Alexander Petrov, preparado por Alexander Petrov y Alexander Mironenko, del Octavo Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 11–16 de marzo de 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay que colocar tres platos redondos de radios R1, R2, R3 en una
bandeja rectangular H × W de modo que ninguno sobresalga y que no se
solapen dos (tocarse está permitido). Todos los números son enteros
positivos hasta 10⁶. Se imprimen los tres centros con cuatro decimales,
en el orden de los radios, o `0` si no caben.

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

H, W, R1, R2 y R3.

## Salida

Seis coordenadas, o `0`.

## Evaluación

Se acepta cualquier colocación válida. El verificador comprueba que
cada plato está sobre la bandeja y que no se solapan dos, con una
tolerancia de 10⁻³ + 10⁻⁹ × (H + W) por el redondeo y los errores de
cálculo en coma flotante. Si la respuesta esperada es `0`, la salida
también debe ser `0`.

## Ejemplos

### Ejemplo 1

Entrada:

```
800 400 200 200 50
```

Salida:

```
200.0000 200.0000 600.0000 200.0000 400.0000 50.0000
```

### Ejemplo 2

Entrada:

```
800 400 200 200 51
```

Salida:

```
0
```

## Solución

Probemos los seis órdenes de los tres platos con búsqueda con retroceso.

Para cada plato se generan centros candidatos a partir de los
siguientes pares de contactos con las cuatro paredes y los platos ya
colocados:

- tocando dos paredes: las cuatro esquinas (r, r), (H − r, r), …;
- tocando una pared y un plato colocado de radio s: en una recta x = r
  o x = H − r (o y = …), a distancia r + s del centro de ese plato;
- tocando dos platos colocados: la intersección de dos circunferencias
  con centro en los suyos, de radios r + s₁ y r + s₂.

Un candidato solo se conserva si el plato está sobre la bandeja y no
solapa a los ya colocados. Seis órdenes, como mucho unas decenas de
candidatos por plato: toda la búsqueda es diminuta. Las comparaciones
admiten 10⁻⁹ × (H + W) para los errores de cálculo en
coma flotante en los contactos exactos.

Detalles a tener en cuenta:

- a menudo solo hay respuesta con platos que se tocan exactamente, como
  en el ejemplo; una unidad más y desaparece (pruebas 01 y 02);
- los huecos de las esquinas junto a un plato que llena la bandeja
  admiten un radio de unos (√2 − 1)/(√2 + 1) del suyo: 8 cabe junto a
  50 y 9 no (pruebas 10 y 11);
- un plato más ancho que la bandeja lo hace imposible de entrada
  (prueba 08).

Cada colocación impresa en 250 bandejas aleatorias pequeñas se comprobó
válida, y para cada bandeja respondida con `0`, una búsqueda por
descenso de penalización desde 60 inicios aleatorios tampoco encontró
colocación.

## Notas por lenguaje

- C++, Python y Rust prueban los órdenes en orden creciente, Go y Java
  con el algoritmo de Heap, así que los lenguajes pueden imprimir
  colocaciones válidas distintas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1312_geometry.cpp](1312_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 212 KB |
| [1312_geometry.go](1312_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1204 KB |
| [1312_geometry.java](1312_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.140 s | 2072 KB |
| [1312_geometry.py](1312_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.093 s | 860 KB |
| [1312_geometry.rs](1312_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.031 s | 292 KB |
