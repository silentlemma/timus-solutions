# 1611. Decimación

[Timus 1611](https://acm.timus.ru/problem.aspx?space=1&num=1611) · dificultad 695 · dp

Problema original de Alexander Ipatov (idea de Stanislav Vasiliev), del XII Campeonato de los Urales de Programación Competitiva, 29 de marzo de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

n ≤ 10000 revisores forman una fila, cada uno bueno (`1`) o malo (`0`);
se multa a toda persona cuyo puesto es múltiplo de 10. Antes de las
multas se pueden meter en la fila, donde se quiera, hasta k ≤ 50 amigos
de los revisores. Hay que minimizar el número de amigos multados más el
de revisores buenos multados, e imprimirlo con los puestos de los amigos
en la nueva fila. Vale cualquier fila óptima.

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

n y k, y luego la fila como una cadena de `0` y `1`.

## Salida

El menor número de esas multas, luego m y los m puestos de los amigos.

## Ejemplos

### Ejemplo 1

Entrada:

```
10 2
0000000001
```

Salida:

```
0
2 5 12
```

### Ejemplo 2

Entrada:

```
10 2
1111111111
```

Salida:

```
1
0
```

## Solución

Se construye la nueva fila desde delante. Tras i revisores y j amigos,
la siguiente persona está en el puesto i + j + 1, sea quien sea. Así que
cost[i][j], el menor número de multas hasta ahí, tiene dos movimientos:
entra un amigo, multado si ese puesto es múltiplo de 10, o entra el
revisor i + 1, que suma una multa solo si es bueno y está en un puesto
así. Los amigos tras el último revisor solo podrían recibir multas, así
que nunca hacen falta. La respuesta es el menor cost[n][j] con j ≤ k, y
recorrer la tabla hacia atrás da los puestos de los amigos: `O(n·k)`.

Las pruebas usan un verificador que reconstruye la fila a partir de los
puestos impresos y cuenta sus multas. Los números se contrastaron con
probar todos los conjuntos de puestos para los amigos en filas cortas.

Detalles a tener en cuenta:

- un amigo desplaza un puesto a todos los revisores que tiene detrás,
  así que un amigo delante puede salvar de golpe a todos los revisores
  buenos (prueba 05), y un segundo amigo puede solo añadir una multa;
- los propios amigos se multan en los puestos décimos, y la fila más
  larga puede alcanzar un nuevo puesto décimo (prueba 08);
- la respuesta no es única: en el primer ejemplo se ponen dos amigos,
  pero uno delante es igual de bueno.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1611_dp.cpp](1611_dp.cpp) | G++ 13.2 x64 | dp | O(n·k) | AC | 0.015 s | 2428 KB |
| [1611_dp.go](1611_dp.go) | Go 1.14 x64 | dp | O(n·k) | AC | 0.031 s | 6200 KB |
| [1611_dp.java](1611_dp.java) | Java 1.8 | dp | O(n·k) | AC | 0.109 s | 2812 KB |
| [1611_dp.py](1611_dp.py) | Python 3.12 x64 | dp | O(n·k) | AC | 0.328 s | 12976 KB |
| [1611_dp.rs](1611_dp.rs) | Rust 1.75 x64 | dp | O(n·k) | AC | 0.015 s | 4524 KB |
