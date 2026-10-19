# 1980. Exceso de velocidad mínimo y una ruta

[Timus 1980](https://acm.timus.ru/problem.aspx?space=1&num=1980) · dificultad 639 · binary_search, dijkstra

Problema original de Denis Dublennykh, del Campeonato de Programación Deportiva de los Urales 2013.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada carretera no dirigida tiene longitud `l` kilómetros y límite de
velocidad `s` kilómetros por hora. Un exceso común no negativo `S`
permite circular hasta `s+S` en cualquier carretera. Halle el menor
exceso que permita llegar del vértice 1 al `n` en como máximo `T` horas
y escriba los índices originales de una ruta correspondiente.

Límites: `2≤n≤10000`, `1≤m≤10000`, `1≤s≤300`, `1≤l≤1000` y entero
`1≤T≤10⁶`. Los extremos cumplen `1≤a<b≤n`. Se garantiza que el destino
es alcanzable; se manejan carreteras paralelas y componentes
irrelevantes. Tiempo: 1 segundo; memoria: 64 MB.

## Entrada

Todos los valores de entrada son enteros. Lea `n m`, luego `m` líneas `a
b s l` y finalmente `T`. Las carreteras se numeran de 1 a `m` por orden
de entrada.

## Salida

Escriba `S k` en la primera línea y los `k` índices de carretera por
orden de recorrido en la segunda. Se permite cualquier ruta óptima
válida.

## Evaluación

Un comprobador verifica que las carreteras impresas forman un camino de
1 a n que llega a tiempo con el margen impreso y que el margen es óptimo
con error absoluto o relativo 10⁻⁶; se acepta cualquier ruta así.

## Ejemplos

Entrada:

```
3 3
1 3 50 150
1 2 80 100
2 3 80 100
2
```

Salida:

```
20.000000 2
2 3
```

Entrada:

```
2 1
1 2 60 60
1
```

Salida:

```
0.000000 1
1
```

## Solución

Para un `S` fijo, el menor tiempo de una carretera es `l/(s+S)`. Todos
los pesos son positivos, por lo que Dijkstra decide si el destino puede
alcanzarse dentro de `T`. Ignore las entradas obsoletas del montículo y
termine al extraer el destino con su distancia actual. Descarte tiempos
candidatos mayores que `T`, pues las carreteras posteriores solo añaden
tiempo.

Al aumentar `S`, todos los tiempos disminuyen: la factibilidad es
monótona. Compruebe primero `S=0`; si es factible, el óptimo es cero. En
otro caso, busque entre el cero no factible y la cota factible `U=Σl/T`.
Cualquier ruta simple tiene longitud total como máximo `Σl`, y con
exceso `U` tarda estrictamente menos que `Σl/U=T`.

Mantenga factible el extremo superior y haga como máximo 60 bisecciones.
Python también termina cuando el ancho es como máximo `10⁻⁹
max(1,upper)`. Repita Dijkstra en la cota superior final. El predecesor
guarda el índice original de carretera, distinguiendo aristas paralelas.
Desde `n`, pase al otro extremo de cada carretera predecesora y luego
invierta la lista.

Cada prueba es correcta por el invariante de Dijkstra con pesos
positivos. La monotonía mantiene el óptimo dentro del intervalo. La
cadena final de predecesores certifica la factibilidad del extremo
superior, demostrando tanto el valor numérico como la ruta.

Antes de imprimir, añada `10⁻⁸ max(1,upper)` como pequeño margen
ascendente. Compensa errores de suma y formato y sigue muy por debajo
del error permitido. Un óptimo cero puede aparecer como un número
positivo muy pequeño. Una ruta simple contiene como máximo `n−1`
términos positivos, cuyo error acumulado en binary64 es mucho menor que
este margen. El error de parada de Python también es menor. Incluyendo
divisiones, el error relativo de hasta 9999 términos positivos es
inferior a `1,2·10⁻¹²`. Como `s≤300`, el margen reduce cada tiempo al
menos `3,3·10⁻¹¹` relativamente, superando el error de suma y de
formato.

Con `B≤62` ejecuciones de Dijkstra, incluidas la inicial y la
reconstrucción final, y entradas obsoletas en el montículo, el tiempo es
`O(B(n+m) log(n+m))` y la memoria `O(n+m)`. Las carreteras paralelas
pueden producir más de `n` entradas en la cola.

En el primer ejemplo, las carreteras 2 y 3 tardan `200/(80+20)=2`,
mientras que la carretera directa necesita `150/(50+20)>2`; el mínimo
exceso es 20. En el segundo, el límite original basta para llegar en una
hora y el óptimo es cero.

Trampas:

- El tiempo es longitud entre velocidad; aumentar la velocidad no resta
  un tiempo fijo.
- Compruebe el exceso cero antes de buscar.
- Conserve los índices de carretera, incluidas las paralelas, y
  escríbalos desde el inicio hasta el destino.
- El último punto medio puede no ser factible: repita la prueba del
  extremo superior.
- Use la cota factible y suficientes decimales; redondear hacia abajo
  puede invalidar una ruta ajustada.

## Notas por lenguaje

C++, Go, Python y Rust usan montículos binarios estándar. Java almacena
la adyacencia y el montículo en arreglos primitivos reutilizados entre
pruebas. Cada coste de carretera se calcula una vez por prueba. Python
detiene bisecciones innecesarias según el ancho del intervalo. Todas las
versiones guardan los índices predecesores y añaden el pequeño margen
numérico ascendente.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1980_binary_search_dijkstra.cpp](1980_binary_search_dijkstra.cpp) | G++ 13.2 x64 | binary_search, dijkstra | O(B(n+m)log(n+m)) | AC | 0.031 s | 1064 KB |
| [1980_binary_search_dijkstra.go](1980_binary_search_dijkstra.go) | Go 1.14 x64 | binary_search, dijkstra | O(B(n+m)log(n+m)) | AC | 0.093 s | 7196 KB |
| [1980_binary_search_dijkstra.java](1980_binary_search_dijkstra.java) | Java 1.8 | binary_search, dijkstra | O(B(n+m)log(n+m)) | AC | 0.109 s | 2008 KB |
| [1980_binary_search_dijkstra.py](1980_binary_search_dijkstra.py) | Python 3.12 x64 | binary_search, dijkstra | O(B(n+m)log(n+m)) | AC | 0.406 s | 8356 KB |
| [1980_binary_search_dijkstra.rs](1980_binary_search_dijkstra.rs) | Rust 1.75 x64 | binary_search, dijkstra | O(B(n+m)log(n+m)) | AC | 0.046 s | 1948 KB |
