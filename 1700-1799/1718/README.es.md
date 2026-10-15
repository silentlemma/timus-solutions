# 1718. Rejuzgado

[Timus 1718](https://acm.timus.ru/problem.aspx?space=1&num=1718) · dificultad 309 · implementation

Problema original de Alexander Ipatov, preparado por Alex Samsonov, de la subregión oriental del NEERC 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un problema tenía siete tests. Se añadieron diez tests nuevos tras
ellos, luego se quitó el test 6, y se vuelven a juzgar todas las
soluciones anteriores. Cada autor cuya lista de veredictos cambiados no
está vacía recibe una carta. Dados los veredictos antiguos, hallar el
menor y el mayor número posible de cartas.

## Entrada

n (1 ≤ n ≤ 1000) y luego n líneas con el nombre de un autor y un
veredicto antiguo: AC, CE, o ML X, TL X o WA X con 1 ≤ X ≤ 7. Un
veredicto con test X pasó los tests 1 … X − 1 y falló el test X. Los
veredictos que solo difieren en X son distintos.

## Salida

El menor y el mayor número de autores que reciben cartas.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
[SPbSU_ITMO]_WiNGeR TL 6
Milanin_(TNU) WA 6
Vladimir_Yakovlev_(USU) AC
Sandro_(USU) WA 1
Sandro_(USU) ML 3
```

Salida:

```
0 3
```

## Solución

Tras el cambio, los tests 1 … 5 se quedan, el antiguo test 7 pasa a ser
el 6 y los nuevos son 7 … 16. Cada veredicto antiguo o cambia seguro, o
puede cambiar, o se queda seguro:

- CE y los fallos en los tests 1 … 5 se quedan, pues van primero los
  mismos tests;
- un fallo en el test 7 debe cambiar: ese test es ahora el número 6,
  así que en el mejor caso el veredicto dice 6 en vez de 7;
- AC puede cambiar, pues un test nuevo puede fallar, y un fallo en el
  test 6 puede cambiar, pues ese test ya no está y la ejecución sigue
  con el antiguo test 7. Si falla el antiguo test 7 del mismo modo, el
  veredicto queda igual, ya que ese test es ahora el número 6.

Así, el menor número de cartas es el de autores con un fallo en el
test 7. El mayor añade los que tienen un AC o un fallo en el test 6.
Los nombres se cuentan en conjuntos: `O(n log n)` en C++, `O(n)`
esperado en los demás.

Trampas:

- un autor cuenta una vez, cambien cuantas soluciones cambien;
- un fallo en el antiguo test 6 puede conservar exactamente el mismo
  veredicto, así que no obliga a una carta;
- los nombres tienen corchetes y paréntesis, pero no espacios, así que
  leer por palabras funciona.

Las respuestas coinciden con una implementación aceptada independiente
en 600 casos aleatorios.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1718_implementation.cpp](1718_implementation.cpp) | G++ 13.2 x64 | implementation | O(n log n) | AC | 0.015 s | 596 KB |
| [1718_implementation.go](1718_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.031 s | 1344 KB |
| [1718_implementation.java](1718_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.078 s | 1140 KB |
| [1718_implementation.py](1718_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.078 s | 724 KB |
| [1718_implementation.rs](1718_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.046 s | 532 KB |
