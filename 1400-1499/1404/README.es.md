# 1404. ¡Fácil de descifrar!

[Timus 1404](https://acm.timus.ru/problem.aspx?space=1&num=1404) · dificultad 80 · implementation

Problema original de Vladimir Yakovlev, del Duodécimo Campeonato por Equipos de Programación para Escolares de la Región de Sverdlovsk, 15 de octubre de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una palabra de a lo sumo 100 letras minúsculas se cifra así: las letras
se convierten en números de 0 a 25, al primero se le suma 5, a cada
siguiente se le suma el nuevo valor del anterior, y todos los valores se
toman módulo 26 y vuelven a ser letras. Dada la palabra cifrada, hay que
imprimir la original.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

La palabra cifrada.

## Salida

La palabra original.

## Ejemplos

### Ejemplo 1

Entrada:

```
xbduyr
```

Salida:

```
secret
```

## Solución

El k-ésimo valor cifrado es el (k − 1)-ésimo más la k-ésima letra, y
tomar módulo 26 no estropea esa relación. Así que cada letra es la
diferencia entre su código y el código anterior, módulo 26, con un 5
delante del primer código. `O(n)`.

Detalles a tener en cuenta:

- la diferencia puede ser negativa, así que se devuelve a 0 … 25 (prueba
  03, donde la z se cifra como e y vuelve);
- las sumas del cifrado pasan de 25 antes del módulo, pero los códigos de
  la entrada ya están reducidos, y con eso basta.

Las pruebas se obtuvieron cifrando palabras y se juzgan por comparación
exacta.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1404_implementation.cpp](1404_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 360 KB |
| [1404_implementation.go](1404_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.031 s | 1068 KB |
| [1404_implementation.java](1404_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.093 s | 1612 KB |
| [1404_implementation.py](1404_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.078 s | 352 KB |
| [1404_implementation.rs](1404_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.015 s | 208 KB |
