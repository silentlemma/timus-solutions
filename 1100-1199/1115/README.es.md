# 1115. Repartir longitudes en filas de longitud total dada

[Timus 1115](https://acm.timus.ru/problem.aspx?space=1&num=1115) · dificultad 409 · backtracking

Problema original de la primera competición de selección del equipo búlgaro para la IOI.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay `N < 100` objetos con longitudes enteras de 1 a 100 y `M` filas
(`1 < M < 10`) de longitudes dadas. Reparte todos los objetos en las filas
de modo que las longitudes de cada fila sumen exactamente la longitud de
la fila; cada fila recibe al menos un objeto. Se sabe que existe un
reparto. Imprime uno.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N M`, luego `N` líneas con las longitudes de los objetos y luego `M`
líneas con las longitudes de las filas.

## Salida

Para cada fila, en el orden de la entrada, dos líneas: el número de
objetos que tiene y sus longitudes.

## Evaluación

Se acepta cualquier reparto válido. El comprobador verifica que cada fila
suma su longitud y que los objetos usados son exactamente los dados.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 2
4
10
2
5
3
11
13
```

Salida:

```
3
5 4 2
2
10 3
```

## Solución

Es una partición exacta en varias partes, un problema difícil en general,
así que las soluciones usan búsqueda con poda. Al principio se llenan las
filas de menor a mayor longitud y se prueban los objetos por longitud
decreciente. Es solo una heurística: una fila corta no tiene necesariamente
menos formas de llenarse. La última fila toma todos los objetos restantes.
Cada longitud igual se prueba una sola vez en cada posición, ya que los
objetos iguales son intercambiables.

Antes de llenar una fila, el conjunto de bits `reach[k]` guarda las sumas
que pueden formar los objetos libres desde la posición `k`. Se construye
desde el final con `reach[k] = reach[k+1] | reach[k+1] << len`. Si el
objetivo de cualquier fila pendiente es inalcanzable, la rama se descarta.
Solo se toma un objeto si el resto de la fila actual puede completarse
con los objetos posteriores.

Un orden fijo todavía puede perder mucho tiempo en llenados incompatibles.
Cada uno de los primeros 128 intentos permite 256 llamadas a la búsqueda
de subconjuntos; después deshace todas las asignaciones y permuta las
filas y el orden de las longitudes distintas. Las longitudes iguales
permanecen juntas. Todos los lenguajes usan el mismo generador entero con
estado inicial fijo, por lo que producen salidas idénticas. Si estos
intentos fallan, una búsqueda final sin límite de llamadas examina todas
las posibilidades; agotar el presupuesto no significa que no haya
reparto. Se conservan los índices originales de las filas para la salida.

Con longitud total `S` y ancho de palabra del conjunto de bits `W`, una
cota conservadora de tiempo es `O(M^N * N^2 * ceil(S/W))` en el peor caso,
y la memoria auxiliar es `O(M * N * ceil(S/W))` palabras. Los reinicios no
eliminan el peor caso exponencial; los tiempos medidos no garantizan la
misma rapidez para toda entrada válida.

Detalles a tener en cuenta:

- probar objetos iguales en todos los órdenes hace explotar la búsqueda
  cuando hay muchas longitudes repetidas;
- sin comprobar las sumas, permanecen ramas con filas actuales o futuras
  inalcanzables;
- la prueba **07** provoca millones de llamadas con el orden fijo de
  menor a mayor longitud; las filas cortas no siempre tienen menos
  llenados (objetos `[1,1,2,5]`, objetivos `[2,2,5]`: dos formas para 2,
  pero solo una para 5);
- un intento interrumpido debe deshacer todas las asignaciones, y la
  búsqueda final debe ejecutarse sin límite de llamadas;
- las filas deben imprimirse en el orden de la entrada, aunque se llenan
  en otro.

La solución de Python se comprobó en las 7 pruebas guardadas, los
5 casos declarados del generador, 1.500 casos aleatorios pequeños frente
a un oráculo exacto independiente y 406 casos grandes o de frontera.

Las revisiones de los fuentes descritas arriba ya obtuvieron sus propios Accepted. Las tablas de soluciones indican los envíos finales que corresponden a cada fuente y sus mediciones conjuntas de tiempo y memoria; las observaciones anteriores describen revisiones previas. Se conservan todas las implementaciones sencillas con valor didáctico.

## Soluciones optimizadas

`1115_backtracking_optimized.java`. Mantiene retroceso completo de subconjuntos, poda por longitudes iguales y 128 reinicios deterministas limitados seguidos de búsqueda completa sin límite: el peor caso sigue exponencial. Reutiliza por profundidad bitsets sufijos long planos e índices libres. Para filas posteriores consulta min(t,total-t), por la equivalencia con el complemento; la fila actual conserva su objetivo completo para reconstruir. Longitudes positivas permiten truncar en la mayor consulta real; limpia las celdas usadas y separa las áreas por profundidad. Inserción estable primitiva sustituye ordenación con objetos, y entrada/salida de 1024 bytes sustituye Scanner/StringBuilder. Cota conservadora O(M^N*N^2*ceil(S/64)) tiempo y O(M*N*ceil(S/64)) palabras más estado, S máximo objetivo. Se comprobaron 30935 instancias pequeñas y 10000 ordenaciones estables; la búsqueda final sin límite conserva completitud.

Accepted exacto Java 1.8 #11327476: 0.093 s / 420 KB. Puestos
guardados del 2026-11-20: tiempo 2/25, memoria 1/25; bajo 1024 KB
solo se aplica tiempo. Cumple, sin meta separada de primer puesto
ni asterisco en su fila. El anterior #11325125 (0.14 s / 2928 KB)
es otro par histórico, no la medición de este fuente.

- `1115_backtracking_optimized.java`: 0.093 s / 420 KB; base didáctica conservada `1115_backtracking.java`: 0.125 s / 4464 KB.

La versión C++ reserva solo las palabras de 64 bits que necesita la tabla de sumas de sufijos. Si los barcos libres suman U, una futura fila con objetivo T tiene un subconjunto válido exactamente cuando existe uno de longitud U − T. La comprobación usa el valor menor. La fila actual conserva su objetivo completo para reconstruir los barcos elegidos. La búsqueda final sin límite mantiene la completitud.

La caché de revisiones aceptadas confirma Python/Rust simples por
tiempo de cohorte pequeña del compilador exacto bajo 1 MiB. Go/Java
simples fallan; los cubren fuentes optimizados distintos. Ambas
versiones C++ cumplen puesto temporal ordinario. Son resultados
concretos, no admisión universal de bases. Se conservan versiones
simples significativas sin asteriscos de optimización.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1115_implementation_parsing_optimized.go`. Los arreglos acotados de barcos y filas usan inserción especializada, sin ordenación por reflexión. Se conservan heurísticas, bitsets de sufijos, reinicios reproducibles y búsqueda final completa sin límite. Las asignaciones se escriben sin listas temporales de cadenas. Se especializan la conversión de tokens y la salida numérica para los tipos usados, eliminando ramas generales innecesarias y conservando algoritmo y comentarios.

Las notas del 18 de noviembre de 2026 son una instantánea histórica.
Hoy se excluyen tiempos rivales bajo 0.015 s antes de elegir cohorte;
nuestros tiempos menores solo se elevan para comparar. Se conservan
pares Accepted originales y se usa la política común actual.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Conserva los algoritmos didácticos. Las filas básicas revalidadas usan sus nuevas métricas e IDs de Accepted de fuente exacta; estas pruebas no cuentan como optimizaciones.

La admisión actual usa los [criterios compartidos](../../RATING_CRITERIA.md):
puestos top diez/top 15% o referencia pequeña del compilador exacto
cuando corresponde; bajo 1 MiB solo tiempo. Mejorar 30% o una meta
aparte de primer puesto no da admisión. Se conservan bases significativas
sin asteriscos de objetivos de optimización.

Cuatro revisiones mueven el comentario existente de longitud
total a MAX_SUM/maxSum, desde el multiplicador aleatorio. Recibos
anteriores en tabla: C++ #11325586, Go simple #11325575, Rust
#11325611 y Go optimizado #11329250. No se inició la cola.

Go optimizado también nombra la reserva inicial intacta de 4 bytes
por artículo y el búfer entero de 24 bytes. Valores y salida no cambian;
esta revisión también requiere nuevo Accepted del fuente exacto.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1115_backtracking.cpp](1115_backtracking.cpp) | G++ 13.2 x64 | backtracking | O(M^N * N^2 * ceil(S/W)) worst case | AC | 0.015 s | 424 KB | 11331146 |
| [1115_backtracking.go](1115_backtracking.go) | Go 1.14 x64 | backtracking | O(M^N * N^2 * ceil(S/W)) worst case | AC | 0.015 s | 1884 KB | 11331025 |
| [1115_backtracking.java](1115_backtracking.java) | Java 1.8 | backtracking | O(M^N * N^2 * ceil(S/W)) worst case | AC | 0.125 s | 4464 KB | 11325558 |
| [1115_backtracking.py](1115_backtracking.py) | Python 3.12 x64 | backtracking | O(M^N * N^2 * ceil(S/W)) worst case | AC | 0.078 s | 844 KB | 11325596 |
| [1115_backtracking.rs](1115_backtracking.rs) | Rust 1.75 x64 | backtracking | O(M^N * N^2 * ceil(S/W)) worst case | AC | 0.031 s | 740 KB | 11331122 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1115_backtracking_optimized.cpp](1115_backtracking_optimized.cpp) | G++ 13.2 x64 | backtracking | O(M^N * N^2 * ceil(S/W)) worst case | AC | 0.015 s | 232 KB | 11310422 |
| [1115_backtracking_optimized.java](1115_backtracking_optimized.java) | Java 1.8 | backtracking | O(M^N*N^2*ceil(S/64)) worst case; exponential | AC | 0.093 s | 420 KB | 11327476 |
| [1115_implementation_parsing_optimized.go](1115_implementation_parsing_optimized.go) | Go 1.14 x64 | implementation, parsing | O(M^N * N^2 * ceil(S/W)) worst case | AC | 0.015 s | 928 KB | 11331026 |
