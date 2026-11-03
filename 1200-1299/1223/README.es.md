# 1223. El menor número de lanzamientos de huevos que halla el piso crítico

[Timus 1223](https://acm.timus.ru/problem.aspx?space=1&num=1223) · dificultad 292 · dp

Problema original del folclore, propuesto por Alexander Klepinin, del séptimo concurso universitario de programación de la Universidad Estatal de los Urales.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay `f` pisos, numerados del 1 al `f`, y `e` huevos iguales,
con `1 ≤ e, f ≤ 1000`. El valor desconocido `E` pertenece a `0..f`:
un huevo resiste desde cualquier piso no superior a `E` y se rompe por encima.
Si se rompe desde el primer piso, `E = 0`; si resiste desde el piso `f`, `E = f`.

Halla el mínimo número de lanzamientos que determina `E` en el peor caso.
Se pueden reutilizar los huevos intactos. Hay como máximo 1000 consultas;
el par `0 0` termina la entrada y no cuenta como consulta.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Una consulta por línea: el número de huevos y el número de pisos.

## Salida

Para cada consulta, el menor número de lanzamientos en el peor caso.

## Comprobación

Comparar tokens enteros en orden; 0 0 no recibe respuesta. Cada
nueva fuente didáctica superó13 entradas Docker y tiene Accepted propio
de SHA exacto. El Python real se verificó con21000 consultas, en lotes
de hasta1000: todos los pisos1..1000 con huevos1..20 y1000 consultas
aleatorias con hasta1000 huevos. El oráculo independiente usa la suma
cerrada `Σ C(d,i)` y búsqueda binaria, no las DP. No son21000 ejecuciones
de cada fuente nativa. Incluir un huevo/un piso, diez y mil huevos,
fronteras exactas de capacidad,1000 consultas y el centinela.

## Ejemplos

### Ejemplo 1

Entrada:

```
1 10
2 5
0 0
```

Salida:

```
10
3
```

## Solución

Las nuevas fuentes didácticas usan el minimax literal. Sea D(e,f)
el mínimo peor caso con e huevos y f pisos. Cero pisos necesita cero
intentos, D(1,f)=f. Un primer lanzamiento desde x deja x−1 pisos y un
huevo menos si se rompe; si resiste, f−x pisos con los mismos huevos.
Así `D(e,f)=1+min₁≤ₓ≤f max(D(e−1,x−1),D(e,f−x))`. Toda estrategia debe
elegir un primer piso y afrontar ambos resultados, dando la cota inferior;
elegir el mejor y continuar óptimamente alcanza la cota.

Recorrer huevos y pisos crecientes deja disponibles la fila anterior y
los pisos menores. Hay F+1 umbrales y dos resultados por intento: hacen
falta al menos `ceil(log₂(F+1))` lanzamientos. Diez huevos alcanzan esa
cota por búsqueda binaria para F≤1000, con hasta diez intentos y una
pérdida por intento; más huevos no ayudan. El límite de diez filas está
demostrado. Con E=10,F=1000: `O(EF²)` preparación, `O(EF)` celdas, `O(1)`
por consulta. Las cinco fuentes nuevas tienen Accepted propio y son las
bases didácticas; Python usa PyPy3.10. Las cinco antiguas conservan todos
sus bytes; no se crean copias optimized idénticas.

## Notas por lenguaje

La instantánea del 2 de noviembre de 2026 usa los filtros acordados
de compilador,fecha y otros autores: C++ exige15% superior o primeros
diez en ambas medidas; las demás familias, primero en ambas. Base C++:
1/2 frente a85 entradas; base Java:1/1 frente a5; Python rápido:1/1 frente
a14. Go/Rust no tienen rivales filtrados: cobertura formal no demuestra
superioridad. Las cinco bases y el Python antiguo admitido cubren el
criterio actual, sin inventar etiquetas rápidas para las alternativas.
Las medidas pertenecen a fuentes Accepted exactas.

## Soluciones optimizadas

El antiguo `dp` invierte la pregunta: R(d,e) pisos resolubles con
d intentos y e huevos. El primer intento divide en rama rota, su piso y
rama superviviente: `R(d,e)=R(d−1,e−1)+1+R(d−1,e)`, con bordes cero.
La división es necesaria y alcanzable, por lo que el primer d con
R(d,e)≥f es D(e,f). Incrementar d y escribir cada respuesta cuando se
cubre por primera vez. Saturar capacidades en F es seguro por monotonía;
valores mayores son indistinguibles para consultas legales. Hay hasta F
rondas, pues un huevo mide d pisos con d intentos, y se escribe una vez
cada celda: `O(EF)` preparación/memoria, `O(1)` por consulta. Cada suma
es como máximo `2F+1=2001`, segura en los enteros nativos.

Solo el antiguo Python se admite como optimizado: CPython0,078s/812KB
frente al PyPy didáctico0,265s/2916KB, ahorro70,6% de tiempo y72,2% de
memoria. Es otro algoritmo y conserva `dp`. El Java antiguo mejora solo
28,4% en tiempo y consume más memoria; C++/Go/Rust tampoco llegan al30%,
por lo que se conservan como alternativas sin etiqueta rápida. El Java
sencillo ya cumple la meta de clasificación.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1223_bruteforce_dp.cpp](1223_bruteforce_dp.cpp) | G++ 13.2 x64 | bruteforce, dp | O(EF^2 + Q) | AC | 0.015 s | 152 KB | 11308226 |
| [1223_bruteforce_dp.go](1223_bruteforce_dp.go) | Go 1.14 x64 | bruteforce, dp | O(EF^2 + Q) | AC | 0.031 s | 1208 KB | 11308230 |
| [1223_bruteforce_dp.java](1223_bruteforce_dp.java) | Java 1.8 | bruteforce, dp | O(EF^2 + Q) | AC | 0.109 s | 584 KB | 11308235 |
| [1223_bruteforce_dp.py](1223_bruteforce_dp.py) | PyPy 3.10 x64 | bruteforce, dp | O(EF^2 + Q) | AC | 0.265 s | 2916 KB | 11308219 |
| [1223_bruteforce_dp.rs](1223_bruteforce_dp.rs) | Rust 1.75 x64 | bruteforce, dp | O(EF^2 + Q) | AC | 0.015 s | 344 KB | 11308239 |

### Otros algoritmos (sin cumplir el30%)

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1223_dp.cpp](1223_dp.cpp) | G++ 13.2 x64 | dp | O(EF + Q) | AC | 0.015 s | 172 KB | 11283700 |
| [1223_dp.go](1223_dp.go) | Go 1.14 x64 | dp | O(EF + Q) | AC | 0.031 s | 1216 KB | 11283701 |
| [1223_dp.java](1223_dp.java) | Java 1.8 | dp | O(EF + Q) | AC | 0.078 s | 668 KB | 11283703 |
| [1223_dp.rs](1223_dp.rs) | Rust 1.75 x64 | dp | O(EF + Q) | AC | 0.015 s | 376 KB | 11283704 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1223_dp.py](1223_dp.py) | Python 3.12 x64 | dp | O(EF + Q) | AC | 0.078 s | 812 KB | 11283702 |
