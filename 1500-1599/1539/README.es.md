# 1539. Datos de inteligencia

[Timus 1539](https://acm.timus.ru/problem.aspx?space=1&num=1539) · dificultad 1050 · number_theory

Problema original de Stanislav Vasiliev, del Octavo Campeonato Personal Abierto de la Universidad Estatal de los Urales, 3 de marzo de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un informe da N promedios (1 ≤ N ≤ 100) sobre el mismo grupo de
trasgos, cada uno un número positivo de hasta 1000 redondeado a
exactamente d decimales (1 ≤ d ≤ 5). Hay que hallar el menor tamaño
posible del grupo.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

d y N, y luego los N promedios, uno por línea.

## Salida

El menor tamaño del grupo.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 3
52.29
0.71
170.86
```

Salida:

```
7
```

## Solución

Se trabaja en unidades de 10^−d: un promedio escrito como v unidades
sale de un total de p objetos entre q trasgos cuando 10^d·p / q se redondea a
v, es decir, cuando v − 1/2 ≤ 10^d·p / q < v + 1/2, o
(2v − 1)·q ≤ 2·10^d·p < (2v + 1)·q (la mitad se redondea hacia arriba).
Para un q dado la pregunta es si un intervalo semiabierto contiene un
entero: se toma el menor p que permite el extremo izquierdo y se
comprueba el derecho, todo con enteros.

Solo importa la parte fraccionaria de cada promedio, porque a cada total
se le puede sumar un número entero de objetos por trasgo, y un promedio
entero vale para cualquier grupo; los repetidos también sobran. Para
q = 10^d el intervalo mide al menos 1, así que la respuesta es como
mucho 10^d ≤ 10⁵: se prueba q = 1, 2, … y se para en el primero que
sirve para todos los promedios. Un promedio que descarta un q suele
descartar los siguientes, así que pasa al principio de la lista.
`O(10^d·N)` en el peor caso.

Detalles a tener en cuenta:

- la mitad se redondea hacia arriba: 1/4 = 0,25 se escribe 0.3, así que
  cuatro trasgos explican a la vez 0.3 y 0.8 (prueba 05);
- 0.00001 por sí solo ya exige 66667 trasgos (prueba 04);
- las partes enteras no cambian nada: en la prueba 08, 999.99999 cuenta
  como 0.99999, que necesita al menos 66667 trasgos igual que 0.00001, y
  la mitad hace que el grupo sea par, 66668;
- los números de coma flotante no son lo bastante exactos cerca de los
  extremos de los intervalos, así que los promedios se leen como
  enteros.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1539_number_theory.cpp](1539_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(10^d * N) | AC | 0.015 s | 400 KB |
| [1539_number_theory.go](1539_number_theory.go) | Go 1.14 x64 | number_theory | O(10^d * N) | AC | 0.046 s | 1140 KB |
| [1539_number_theory.java](1539_number_theory.java) | Java 1.8 | number_theory | O(10^d * N) | AC | 0.109 s | 644 KB |
| [1539_number_theory.py](1539_number_theory.py) | Python 3.12 x64 | number_theory | O(10^d * N) | AC | 0.250 s | 516 KB |
| [1539_number_theory.rs](1539_number_theory.rs) | Rust 1.75 x64 | number_theory | O(10^d * N) | AC | 0.015 s | 228 KB |
