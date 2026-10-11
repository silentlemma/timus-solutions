# 1231. Una máquina de Turing que juega a echar a suertes

[Timus 1231](https://acm.timus.ru/problem.aspx?space=1&num=1231) · dificultad 2192 · constructive

Problema original del cuarto de final de la región central de Rusia del ACM ICPC 2002–2003, Rybinsk, octubre de 2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una cinta contiene n signos menos (1 ≤ n ≤ 200), número desconocido de
antemano, y `#` en todas las demás celdas. Los menos forman un círculo;
empezando por el primero, se tacha cada k-ésimo menos que sigue en pie,
hasta que queda uno. Dado k (1 ≤ k ≤ 200), hay que imprimir la tabla de
control de una máquina de Turing que, para cualquier n, convierta en `+`
todos los menos salvo ese.

La máquina empieza en el estado 1 sobre el menos de más a la izquierda.
Una fila de la tabla `estado símbolo nuevo-estado nuevo-símbolo
movimiento` dice qué hacer al leer un símbolo en un estado; el movimiento
es `<`, `>` o `=`, y la máquina se detiene cuando ninguna fila coincide.
Puede escribir `+`, `#` y `A`–`Z`, las celdas de los menos solo pueden
contener `-` y `+`, el menos que queda nunca debe cambiar y el cabezal
debe terminar sobre él. Límites: como mucho 1 000 000 de pasos, menos de
10 000 filas, estados de 1 a 30 000 y como mucho 5000 celdas a cada lado
del inicio.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

El entero k.

## Salida

El número de filas p (1 < p < 10 000) y luego las p filas, cada una con
cinco elementos separados por espacios simples.

## Evaluación

Se acepta cualquier tabla que funcione para todo n. El verificador de
referencia la ejecuta para cada n de 1 a 200 y comprueba los pasos, los
símbolos escritos, el menos que queda y la posición final del cabezal.

## Ejemplos

El enunciado solo muestra el formato: para k = 2 da una tabla de cinco
filas que tacha el segundo menos, correcta solo para n = 2.

## Solución

La máquina no tiene que simular el juego: k se conoce al imprimir la
tabla, así que el programa resuelve el juego por sí mismo para cada n con
la recurrencia de Josefo `pos(n) = (pos(n−1) + k) mod n` y mete las
respuestas en la tabla.

- **Contar.** El estado i significa «el cabezal está en la celda i». Con
  `-` avanza a la derecha al estado i+1, así que al llegar al `#` tras los
  menos el estado es n+1 y n ya se conoce.
- **Buscar.** Esa fila retrocede al último menos y entra en el estado
  «faltan d celdas», con d = n−1−pos(n); estos estados avanzan a la
  izquierda hasta que d vale 0, y el cabezal queda sobre el menos que se
  salva.
- **Tachar.** Cinco estados fijos lo rebasan, convierten en `+` todo lo
  que hay a su derecha hasta el `#`, vuelven pasando por él, tachan todo
  lo de su izquierda y por último van a la derecha sobre los `+` de vuelta
  a él, donde ninguna fila coincide y la máquina se detiene.

Son 609 filas y como mucho 6n pasos. `O(N)` con `N = 200`.

Detalles a tener en cuenta:

- la celda del menos que se salva debe conservar su `-`, así que los
  recorridos pasan por ella y escriben de nuevo el mismo `-`;
- n = 1 también debe funcionar: entonces la máquina no tacha nada y se
  detiene en el único menos.

El verificador ejecuta la tabla para cada n y compara el menos que queda
con el que deja el juego.

## Notas por lenguaje

- Todos los lenguajes imprimen la misma tabla, fila a fila y en el mismo
  orden.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1231_constructive.cpp](1231_constructive.cpp) | G++ 13.2 x64 | constructive | O(N) | AC | 0.015 s | 152 KB |
| [1231_constructive.go](1231_constructive.go) | Go 1.14 x64 | constructive | O(N) | AC | 0.015 s | 1172 KB |
| [1231_constructive.java](1231_constructive.java) | Java 1.8 | constructive | O(N) | AC | 0.093 s | 576 KB |
| [1231_constructive.py](1231_constructive.py) | Python 3.12 x64 | constructive | O(N) | AC | 0.062 s | 604 KB |
| [1231_constructive.rs](1231_constructive.rs) | Rust 1.75 x64 | constructive | O(N) | AC | 0.015 s | 240 KB |
