# 2199. Dos días de un rango cuyos cambios suman lo más cerca de cero

[Timus 2199](https://acm.timus.ru/problem.aspx?space=1&num=2199) · dificultad 1123 · sqrt_decomposition, sorting

Problema original de Vadim Barinov, de la clasificatoria del Campeonato Regional de los Urales ICPC 2024.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un arreglo d de N enteros recibe Q consultas de rango [l, r]: dar dos
posiciones distintas i, j del rango con el menor |dᵢ + dⱼ|, cualquiera
si hay varias mejores. Los límites son 3 segundos y 256 MB.

## Entrada

N y Q, 2 ≤ N ≤ 30 000, 1 ≤ Q ≤ 30 000, luego d con |dᵢ| ≤ 10⁹, y luego las
consultas con 1 ≤ l < r ≤ N.

## Salida

Dos posiciones por consulta.

## Ejemplos

### Ejemplo 1

Entrada:

```
6 4
17 11 -1 -4 20 -24
1 2
3 4
2 3
1 6
```

Salida:

```
1 2
3 4
2 3
5 6
```

## Solución

Se ordenan los elementos por valor absoluto. Existe al menos un par
óptimo de vecinos en ese orden. Sean a, c, b con |a| ≤ |c| ≤ |b|.
Si a y b tienen el mismo signo, (a, c) no es peor que (a, b).
En caso contrario, si c tiene el signo de b, sirve (a, c); si tiene el
de a, sirve (c, b). El cero puede tomar cualquiera de los signos.
Repitiendo la sustitución se obtiene un par óptimo adyacente, por lo que
al insertar basta examinar el predecesor y el sucesor.

Las consultas se procesan fuera de línea, agrupadas por el bloque del
extremo izquierdo. En cada bloque de B días se ordenan por extremo
derecho. El núcleo a la derecha del bloque solo crece. C++, Java y Rust
guardan los rangos por valor absoluto en conjuntos ordenados; Go usa un
árbol de Fenwick de ocupación con búsquedas por número de orden. Cada
búsqueda o actualización cuesta O(log N). Para una consulta que cruza
el borde del bloque, se comparan el mejor par del núcleo, el mejor par
precalculado del sufijo del bloque y los pares cruzados, buscando en el
núcleo los rangos vecinos de cada elemento del sufijo. El sufijo no se
inserta en el núcleo. Las consultas dentro del bloque usan un conjunto
temporal que se vacía después de cada consulta.

Las versiones compiladas usan dos cotas. Una tabla de prefijos encuentra
un par que alcanza el mínimo global cuando la consulta contiene alguno.
Además, se puede omitir un elemento si ni siquiera su mejor compañero
de todo el arreglo mejora la respuesta actual. Estas cotas aceleran la
ejecución práctica, pero no cambian la cota del peor caso.

Python usa la misma descomposición en bloques con otro preprocesamiento,
sin esas dos podas. Insertar en el orden por valor absoluto equivale a
borrar del orden completo en sentido inverso. Una lista enlazada permite
registrar los vecinos de cada inserción, tanto para el núcleo creciente
como para los sufijos del bloque. Las consultas dentro del bloque recorren
su orden por valor absoluto, filtrando por los extremos de la consulta.
Para los pares cruzados, cada valor x del borde necesita el valor del
núcleo más cercano a −x. El borrado inverso en orden numérico da el
intervalo de valores reflejados para los que un nuevo valor del núcleo
pasa a estar estrictamente más cerca; los empates conservan al compañero
anterior. Búsquedas binarias localizan ese intervalo entre los valores
reflejados del borde. Las asignaciones se aplican por orden de llegada
a un árbol sobre grupos de 16 elementos del borde, con actualizaciones
individuales en los extremos. Gana la última marca temporal y cada
consulta lee los compañeros de su sufijo.

En el ejemplo todo el arreglo da |20 − 24| = 4 en los días 5 y 6.

Con 1 ≤ B ≤ N y B aproximadamente N / √Q, las versiones compiladas tardan
O(N log N + Q log Q + (N²/B + QB) log N). Python tarda
O(N log N + Q log Q + (N²/B) log(B+1) + QB). Las cinco usan O(N + Q) de
espacio auxiliar. La tabla usa B para la longitud del bloque.

Trampas: Q puede ser 1 (tests 02–04); estos tests son válidos y no
necesitan reemplazo. La adyacencia se refiere al orden por valor absoluto,
no a las fechas (test 06), y basta con que un par óptimo sea adyacente.
Las operaciones de conjuntos y de Fenwick tienen coste logarítmico,
no el coste constante atribuido a las operaciones de bitset.

## Notas por lenguaje

- La tabla conserva resultados históricos de PyPy 3.10. El rendimiento
  de CPython depende del entorno y del hardware; esos tiempos no garantizan
  su velocidad ni corresponden a números de tests locales.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2199_sqrt_decomposition_sorting.cpp](2199_sqrt_decomposition_sorting.cpp) | G++ 13.2 x64 | sqrt_decomposition, sorting | O(N log N + Q log Q + (N²/B + QB) log N) | AC | 0.656 s | 3472 KB |
| [2199_sqrt_decomposition_sorting.go](2199_sqrt_decomposition_sorting.go) | Go 1.14 x64 | sqrt_decomposition, sorting | O(N log N + Q log Q + (N²/B + QB) log N) | AC | 1.234 s | 12004 KB |
| [2199_sqrt_decomposition_sorting.java](2199_sqrt_decomposition_sorting.java) | Java 1.8 | sqrt_decomposition, sorting | O(N log N + Q log Q + (N²/B + QB) log N) | AC | 1.812 s | 11324 KB |
| [2199_sqrt_decomposition_sorting.py](2199_sqrt_decomposition_sorting.py) | PyPy 3.10 x64 | sqrt_decomposition, sorting | O(N log N + Q log Q + (N²/B) log(B+1) + QB) | AC | 1.125 s | 17704 KB |
| [2199_sqrt_decomposition_sorting.rs](2199_sqrt_decomposition_sorting.rs) | Rust 1.75 x64 | sqrt_decomposition, sorting | O(N log N + Q log Q + (N²/B + QB) log N) | AC | 0.703 s | 7536 KB |
