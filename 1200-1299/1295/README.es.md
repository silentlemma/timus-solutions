# 1295. Delirio

[Timus 1295](https://acm.timus.ru/problem.aspx?space=1&num=1295) · dificultad 151 · number_theory

Problema original de Den Raskovalov, de la Novena Competición Abierta por Equipos de Programación para Escolares, 13 de marzo de 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

¿En cuántos ceros termina el número decimal 1ⁿ + 2ⁿ + 3ⁿ + 4ⁿ, para
1 ≤ n ≤ 300 000?

Límite de tiempo: 0.5 segundos. Límite de memoria: 64 MB.

## Entrada

Un entero n, `1 ≤ n ≤ 300000`.

## Salida

La cantidad de ceros finales.

## Evaluación

Las pruebas del repositorio comparan exactamente los tokens de salida; los espacios entre tokens no son significativos.

## Ejemplos

### Ejemplo 1

Entrada:

```
8
```

Salida:

```
0
```

### Ejemplo 2

Entrada:

```
7
```

Salida:

```
2
```

## Solución

Para el mayor n la suma tiene más de 180 000 cifras, pero sus ceros
finales están limitados por la potencia de 2 que contiene. Sea
S = 1ⁿ + 2ⁿ + 3ⁿ + 4ⁿ.

- n = 1: S = 10, un cero.
- n par: 1ⁿ + 3ⁿ ≡ 1 + 1 = 2 (mod 4), y 2ⁿ, 4ⁿ son múltiplos de 4, así
  que S es divisible por 2 pero no por 4.
- n impar, n ≥ 3: 3ⁿ ≡ 3 (mod 8), luego 1ⁿ + 3ⁿ ≡ 4 (mod 8), mientras
  que 2ⁿ y 4ⁿ son múltiplos de 8; S es divisible por 4 pero no por 8.

Así que S nunca termina en tres ceros, y S mod 100 lo decide todo: dos
ceros si vale 0, un cero si termina en 0 y ninguno en otro caso. Las
cuatro potencias módulo 100 salen de la exponenciación rápida.
`O(log n)`.

De hecho la respuesta solo depende de n mod 20: 0 cuando 4 divide a n,
2 cuando n deja resto 3 módulo 4 o 5 módulo 20, y 1 en los demás
casos. Las soluciones la calculan directamente sin apoyarse en esta
tabla.

Detalles a tener en cuenta:

- un n con resto 1 módulo 4 suele dar un cero, pero n = 5, 25, … dan
  dos (pruebas 05 y 06);
- la suma completa se puede construir con enteros grandes, pero nunca
  hace falta: solo importan sus dos últimas cifras.

Los resultados se compararon con la suma exacta en enteros grandes para
todos los n hasta 3000.

Las revisiones de los fuentes descritas arriba ya obtuvieron sus propios Accepted. Las tablas de soluciones indican los envíos finales que corresponden a cada fuente y sus mediciones conjuntas de tiempo y memoria; las observaciones anteriores describen revisiones previas. Se conservan todas las implementaciones sencillas con valor didáctico.

## Soluciones optimizadas

`1295_math.java`. Una fórmula de congruencias sustituye potencias modulares: n divisible por 4 da cero ceros finales; n mod 4=3 o n mod 20=5 da dos; los demás uno. Módulo 5 decide existencia, expansión impar módulo 25 el segundo, módulo 8 excluye tercero; n=1 da 10 aparte. Sin tabla de respuestas. Aritmética y espacio O(1), más lectura decimal. Algoritmo distinto llamado math; conserva potencia modular y enseñanza. Fórmula real contrastada para todo n=1..300000 con potencias independientes.

Java 1.8 exacto #11327403 mide `0.078 s / 340 KB`, con puestos
guardados del 20 de noviembre de 2026 de 2/67 en tiempo y memoria.
Bajo 1024 KB solo se exige tiempo: la fórmula cumple. La variante
distinta de potencias modulares #11305839 mide `0.109 s / 324 KB`;
su tiempo 12/67 no entra en diez primeros ni 15% con corte 11, por
eso conserva asterisco. No hay meta separada de primer puesto por lenguaje.

- `1295_math.java`: 0.078 s / 340 KB; base didáctica conservada `1295_number_theory.java` (Java 1.8): 0.125 s / 1600 KB.

Python intacto selecciona CPython 3.12 #11327024 `0.062 s / 660 KB`,
tiempo 1/57 y memoria 30/57, cumpliendo solo por tiempo. Base
#11284644 `0.093 s / 464 KB`: más rápido pero más memoria. Su PyPy
3.10 anterior documentado #11325070 es `0.125 s / 200 KB`, más lento
con menos memoria. No se mezclan pares de compiladores/ejecuciones;
las notas posteriores de ahorro se refieren al PyPy histórico. Se
reutiliza el archivo sin copia ni otra meta de admisión por lenguaje.

La solución optimizada en Java analiza `n` a mano desde un búfer de 4 KB
que se llena desde `System.in`, en lugar de crear un `Scanner`, así que
la JVM no carga el escáner ni sus expresiones regulares; las potencias
módulo 100 son las mismas: {1295_number_theory_optimized.java}.

### Mejora medida

Los pares siguientes son cambios medidos individuales, no una mejora
universal del 30% ni otra admisión. Go #11328536 frente a base
#11284638 mantiene `0.031 s`; memoria de 1080 a 936 KB, solo 13.3%
menos. Cumple por comparación temporal del grupo pequeño, no por
ahorrar un 30%. Reducción negativa indica mayor coste; se conservan
bases didácticas y versiones anteriores distintas.

- `1295_number_theory_optimized.java`: reducción de tiempo +12.80%;
  reducción de memoria +79.75%; base: `1295_number_theory.java`.

`1295_number_theory_optimized.py`. Conserva el argumento módulo 100 para los ceros finales. Calcula directamente 1+pow(2,n,100)+pow(3,n,100)+pow(4,n,100), sin generador sobre cuatro bases. Las potencias modulares no construyen valores enormes. La cota demostrada de dos ceros hace que resto cero dé dos, divisibilidad por diez dé uno y lo demás cero. Tiempo O(log n) operaciones modulares acotadas y estado O(1). El programa independiente para el juez vacía stdout antes de os._exit(0), omitiendo la finalización normal del intérprete. Su propio Accepted acredita la mejora de memoria. El cambio de salida por sí solo no mejora la complejidad asintótica y su beneficio de ejecución no se garantiza en otras plataformas. La versión sencilla no cambia.

Frente a `1295_number_theory.py`: tiempo 0.093 s → 0.125 s; memoria 464 KB → 200 KB.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1295_number_theory_optimized.go`. Se conservan el algoritmo y sus casos límite. Se sustituye fmt por conversión de números y palabras y un búfer de salida reutilizable. La entrada completa se guarda en bytes: se intercambia ese espacio por un menor coste de la E/S general.

Accepted #11328536 (Go 1.14 x64): **0.031 s / 936 KB**. Comparación archivada: `1295_number_theory.go` (Go 1.14 x64) — 0.031 s / 1080 KB (#11284638).

## Notas por lenguaje

Los [criterios compartidos](../../RATING_CRITERIA.md) rigen todos los lenguajes:
diez primeros o 15% superior en métricas necesarias, sustituidos por
referencia con 1–10 rivales válidos del mismo compilador. Bajo 1024 KB
solo se exige tiempo. Se excluyen rivales menores de `0.015 s`; solo
nuestro tiempo se eleva a ese mínimo. Empates comparten puesto y corte
porcentual redondea arriba. No hay corte ID/fecha, primer puesto
separado ni admisión solo por mejorar 30%. Algoritmos, comentarios y
celdas Accepted emparejadas siguen intactos.

Los puestos PyPy anteriores del 18 de noviembre (tiempo 37/57, memoria
1/57) son históricos. La auditoría congelada ligada a fuentes admite
C++, fórmula Java, CPython seleccionado, Go rápido y Rust sencillo.
El límite temporal Go de tres rivales es `0.062 s`; Go base supera
su límite de memoria 1076.40 KB. Rust cumple `0.062 s` frente a un
rival. Go, Java y Python sencillos se conservan para enseñanza
aunque no cumplan las comparaciones necesarias.

El Go actual solo extrae el ancho de conversión64 a `numericBits` por
lint estricto. #11328536 y las comparaciones anteriores corresponden
a los bytes previos.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1295_number_theory.cpp](1295_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(log n) | AC | 0.015 s | 128 KB | 11284634 |
| [1295_number_theory.go](1295_number_theory.go) | Go 1.14 x64 | number_theory | O(log n) | AC | 0.031 s | 1080 KB | 11284638 |
| [1295_number_theory.java](1295_number_theory.java) | Java 1.8 | number_theory | O(log n) | AC | 0.125 s | 1600 KB | 11284648 |
| [1295_number_theory.py](1295_number_theory.py) | Python 3.12 x64 | number_theory | O(log n) | AC | 0.093 s | 464 KB | 11284644 |
| [1295_number_theory.rs](1295_number_theory.rs) | Rust 1.75 x64 | number_theory | O(log n) | AC | 0.046 s | 240 KB | 11284651 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1295_number_theory_optimized.java](1295_number_theory_optimized.java) \* | Java 1.8 | number_theory | O(log n) | AC | 0.109 s | 324 KB | 11305839 |
| [1295_math.java](1295_math.java) | Java 1.8 | math | O(1) arithmetic/storage + decimal input | AC | 0.078 s | 340 KB | 11327403 |
| [1295_number_theory_optimized.py](1295_number_theory_optimized.py) | Python 3.12 x64 | number_theory | O(log n) | AC | 0.062 s | 660 KB | 11327024 |
| [1295_number_theory_optimized.go](1295_number_theory_optimized.go) | Go 1.14 x64 | number_theory | O(log n) | AC | 0.031 s | 932 KB | 11331007 |

\* Accepted; aún no se alcanza el objetivo de [RATING_CRITERIA.md](../../RATING_CRITERIA.md). Esta versión puede optimizarse más.
