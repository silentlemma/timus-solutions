# 1959. Restaurar símbolos con modas de ventanas superpuestas

[Timus 1959](https://acm.timus.ru/problem.aspx?space=1&num=1959) · difficulty 1063 · two_pointers

Original problem from Ural FU contest. Kontur Cup. Petrozavodsk training camp. Winter 2013 | by Mikhail Rubinchik (prepared by Bulat Zaynullin).

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Para texto s de longitud n y patrón p de longitud m<n, sumar la distancia
de Hamming entre p y cada subcadena contigua de s de longitud m. Hamming
cuenta posiciones distintas. Como máximo una secuencia tiene símbolos
desconocidos; ambas pueden estar intactas. Restaurar minimizando la suma
y conservando lo conocido. Límites: 1 s, 64 MB.

## Entrada

Primero n, 1≤n≤100000, seguido de n enteros del texto. Luego m, 1≤m<n,
y m enteros del patrón. Juntas las restricciones implican n≥2. Valores
0…100000: positivos son ID de símbolos y cero es desconocido. Nunca hay
ceros simultáneamente en ambas secuencias.

## Salida

Texto restaurado en la primera línea, patrón en la segunda. Cada ID debe
estar en 1…100000 y los conocidos no cambian. Se admite cualquier mínimo;
no se imprime la distancia.

## Evaluación

Un comprobador verifica que los símbolos conocidos se conservan y que
cada símbolo restaurado es uno de los más frecuentes entre sus
comparaciones; por el argumento de abajo cualquier elección así es
óptima, así que los empates son libres.

## Ejemplos

```
5
1 2 3 1 2
3
1 2 0
```

```
1 2 3 1 2
1 2 1
```

## Solución

### Decisiones independientes

Solo un lado tiene incógnitas, así que cada comparación de un hueco tiene
un símbolo fijo al otro lado. Las comparaciones entre conocidos son una
constante. Un hueco comparado con t símbolos aporta t−frequency(v) al elegir
v. Sirve cualquier moda de sus oponentes. Los huecos no interactúan: la
suma de mínimos locales es globalmente mínima. Toda ventana es no vacía
y contiene ID positivos, por lo que existe un relleno óptimo legal.

Sea g=n−m, con posiciones desde cero. Un hueco j del patrón compara con
s[j…j+g], ventana de ancho g+1. Al avanzar j, quitamos el extremo izquierdo
anterior y añadimos el nuevo derecho.

Un hueco i del texto compara con j del patrón cuando i=j+offset,
0≤offset≤g y 0≤j<m: ventana p[max(0,i−g)…min(m−1,i)]. Ambos extremos
avanzan monótonamente. Para cada i, añadir p[i] si i<m, quitar p[i−g−1]
si i>g y consultar la moda si s[i]=0. La ventana crece, puede deslizarse
o permanecer y finalmente decrece. El lado intacto nunca cambia.

### Modas en tiempo constante

Guardamos frequency[v]. Los símbolos con frecuencia f>0 forman una lista
doblemente enlazada intrusiva: previous[v], following[v] y head[f]. Cero
solo representa enlace nulo; frecuencias cero no pertenecen a listas.
También guardamos la mayor frecuencia no vacía maximum.

Actualizar quita el símbolo de su lista antigua, cambia la frecuencia en
uno y lo inserta en la cabeza nueva si sigue positiva. Si crece sobre
maximum, elevamos maximum; si su lista queda vacía, lo reducimos. Una
actualización válida baja el máximo como mucho en uno: el símbolo conserva
frecuencia f−1, salvo f=1. Cada actualización y consulta es O(1).
head[maximum] es una moda válida.

Con patrón dañado basta capacidad g+1 para cabezas. Con texto dañado se
usa m: añadir antes de quitar puede superar temporalmente en uno el ancho
final de la ventana deslizante.

Tiempo y memoria O(n+m+σ), con σ el mayor ID de entrada, σ≤100000.
Hay O(n+m) cambios de extremos y acceso directo a arrays. No usar moda
global, olvidar el ancho inclusivo g+1, contar ceros, cambiar conocidos
ni considerar solo la mejor alineación. La independencia depende de que
solo un lado esté dañado.

Los programas no calculan el objetivo numérico. Cada contador cabe en
32 bits, pero puede haber 2 500 050 000 pares comparados, más de 2³¹−1.
La verificación de distancia usa enteros amplios.

## Notas por lenguaje

C++, Go 1.14, Java 8 y Rust 1.75 usan arrays/vectores primitivos; Java evita
objetos por símbolo. Rust solo usa la biblioteca estándar. Python usa
listas indexadas y CPython conserva margen. Si no hay ceros, todas las
versiones devuelven la entrada sin construir contadores.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1959_two_pointers.cpp](1959_two_pointers.cpp) | G++ 13.2 x64 | two_pointers | O(n+m+sigma) | AC | 0.046 s | 2300 KB |
| [1959_two_pointers.go](1959_two_pointers.go) | Go 1.14 x64 | two_pointers | O(n+m+sigma) | AC | 0.171 s | 7228 KB |
| [1959_two_pointers.java](1959_two_pointers.java) | Java 1.8 | two_pointers | O(n+m+sigma) | AC | 0.171 s | 10212 KB |
| [1959_two_pointers.py](1959_two_pointers.py) | Python 3.12 x64 | two_pointers | O(n+m+sigma) | AC | 0.453 s | 17424 KB |
| [1959_two_pointers.rs](1959_two_pointers.rs) | Rust 1.75 x64 | two_pointers | O(n+m+sigma) | AC | 0.046 s | 6792 KB |
