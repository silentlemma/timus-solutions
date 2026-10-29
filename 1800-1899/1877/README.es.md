# 1877. Códigos de bicicleta

[Timus 1877](https://acm.timus.ru/problem.aspx?space=1&num=1877) · dificultad 19 · implementation

Problema original de Denis Mukhametianov, del Concurso Regional por Equipos de Programación de los Urales 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Den tiene dos candados de bicicleta de cuatro cifras y los alterna cada
noche, empezando por el primero la noche en que llega un ladrón. El
ladrón prueba el código 0000 esa noche, 0001 la siguiente, y así
sucesivamente. ¿Abrirá alguna vez el candado?

## Entrada

Los códigos del primer y del segundo candado, de cuatro cifras cada
uno.

## Salida

"yes" si el ladrón abre un candado alguna noche, "no" en caso
contrario.

## Ejemplos

### Ejemplo 1

Entrada:

```
0001
0000
```

Salida:

```
no
```

### Ejemplo 2

Entrada:

```
0002
0001
```

Salida:

```
yes
```

## Solución

La noche k (contando desde 0) el ladrón prueba el código k, y la
bicicleta está en el primer candado si k es par y en el segundo si es
impar. Así que el primer candado cae si su código es par, el segundo si
su código es impar, y si no la bicicleta está a salvo. `O(1)`.

En el primer ejemplo el primer código es impar y el segundo par, así
que ningún candado se prueba nunca con su propio código.

Trampas:

- los códigos con ceros a la izquierda deben leerse como decimales;
  `fmt.Scan` de Go puede leer "0009" como 0 y 9, así que la solución
  en Go lee cadenas;
- solo importa la paridad de cada código, no cuál es menor.

Las respuestas coinciden con una implementación aceptada independiente
en todas las pruebas.

## Soluciones optimizadas

La solución optimizada en Java analiza los números byte a byte desde
`System.in` en lugar de usar `Scanner`: 336 KB en lugar de 1572 KB, con
el mismo tiempo.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1877_implementation.cpp](1877_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.015 s | 116 KB | 11303804 |
| [1877_implementation.go](1877_implementation.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.031 s | 1064 KB | 11291005 |
| [1877_implementation.java](1877_implementation.java) | Java 1.8 | implementation | O(1) | AC | 0.109 s | 1572 KB | 11291007 |
| [1877_implementation.py](1877_implementation.py) | Python 3.12 x64 | implementation | O(1) | AC | 0.093 s | 404 KB | 11291006 |
| [1877_implementation.rs](1877_implementation.rs) | Rust 1.75 x64 | implementation | O(1) | AC | 0.031 s | 232 KB | 11303805 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1877_implementation_optimized.java](1877_implementation_optimized.java) | Java 1.8 | implementation | O(1) | AC | 0.109 s | 336 KB | 11303782 |
