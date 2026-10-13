# 1408. Multiplicación de polinomios

[Timus 1408](https://acm.timus.ru/problem.aspx?space=1&num=1408) · dificultad 1184 · parsing

Problema original de Vladimir Yakovlev, del Duodécimo Campeonato por Equipos de Programación para Escolares de la Región de Sverdlovsk, 15 de octubre de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se dan dos polinomios en las variables a a z, uno por línea: términos
unidos por + y -, cada término un producto de un coeficiente opcional
(hasta 100, quizá con ceros a la izquierda, el primero quizá negativo) y
factores X o X^N, con espacios en cualquier lugar. Hay que imprimir su
producto en una forma fija: términos y factores semejantes juntados, sin
términos nulos ni potencias cero, sin coeficientes ni potencias iguales
a 1 salvo el término «1» y el polinomio «0», factores en orden
alfabético, términos por grado total decreciente y luego por potencia
decreciente de a, de b, etcétera.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Los dos polinomios.

## Salida

El producto en una línea, con los espacios como en el ejemplo.

## Ejemplos

### Ejemplo 1

Entrada:

```
x*y*z + 4*x^2*y - 2*z*y*y^4 - 1
x + 7*z
```

Salida:

```
-2*x*y^5*z - 14*y^5*z^2 + 4*x^3*y + 29*x^2*y*z + 7*x*y*z^2 - x - 7*z
```

## Solución

Primero se quitan todos los espacios; entonces un polinomio es un signo,
un término, un signo, un término, etcétera. Un término son factores
unidos por *: un número multiplica el coeficiente y una letra, con un ^
y un número opcionales, suma a la potencia de esa letra. Se guarda el
polinomio como un mapa de las 26 potencias al coeficiente, así que los
términos semejantes se suman al leerlos. Se multiplica cada par de
términos, sumando las potencias y multiplicando los coeficientes, se
quitan los coeficientes nulos y se ordena por grado total y luego por
las potencias de a a z, todo decreciente. El primer término lleva solo
«-» si es negativo, los siguientes « + » o « - »; el coeficiente se
imprime salvo que su valor absoluto sea 1 y el término tenga variables.
Incluyendo la ordenación, `O(T₁·T₂·26·log(T₁·T₂+1))` para T₁ y T₂ términos.

Detalles a tener en cuenta:

- puede haber espacios dentro de números y entre ^ y la potencia
  (pruebas 07 y 12);
- un producto nulo imprime «0», incluso si un factor ya es 0 antes de
  multiplicar (pruebas 03 y 11);
- una potencia 0 y un coeficiente 0 deben desaparecer, y una potencia 1
  no se escribe (pruebas 06 y 07);
- el foro habla de una prueba con líneas de más de 100 caracteres, así
  que las líneas se leen enteras.

Las pruebas incluyen los casos del foro y se juzgan por comparación
exacta.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1408_parsing.cpp](1408_parsing.cpp) | G++ 13.2 x64 | parsing | O(T1·T2·26·log(T1·T2+1)) | AC | 0.031 s | 504 KB |
| [1408_parsing.go](1408_parsing.go) | Go 1.14 x64 | parsing | O(T1·T2·26·log(T1·T2+1)) | AC | 0.031 s | 2412 KB |
| [1408_parsing.java](1408_parsing.java) | Java 1.8 | parsing | O(T1·T2·26·log(T1·T2+1)) | AC | 0.171 s | 6860 KB |
| [1408_parsing.py](1408_parsing.py) | Python 3.12 x64 | parsing | O(T1·T2·26·log(T1·T2+1)) | AC | 0.078 s | 1272 KB |
| [1408_parsing.rs](1408_parsing.rs) | Rust 1.75 x64 | parsing | O(T1·T2·26·log(T1·T2+1)) | AC | 0.015 s | 1132 KB |
