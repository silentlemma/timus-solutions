# 1901. Ascensores espaciales

[Timus 1901](https://acm.timus.ru/problem.aspx?space=1&num=1901) · dificultad 524 · greedy

Problema original de Alex Samsonov, del Ural Championship 2012.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Ordenar n pesos positivos en una cola. Un ascensor de dos plazas la
procesa así: si los dos primeros pesos suman como máximo s, comparten
viaje. En otro caso sale el primero solo y el segundo queda al frente.
Un último peso viaja solo.

Maximizar el número de viajes y construir una cola que lo alcance.
Cada peso cabe individualmente. Los límites son 1 segundo y 64 MB.

## Entrada

La primera línea contiene n y s, con 1 ≤ n ≤ 100 000 y 1 ≤ s ≤ 10⁹.
La segunda contiene n pesos vᵢ, con 1 ≤ vᵢ ≤ s.

## Salida

Escribir el máximo de viajes y después los n pesos en una cola que lo
produzca. Conservar el multiconjunto original, incluidas repeticiones.
Se acepta cualquier cola óptima.

## Evaluación

Un verificador comprueba el multiconjunto, simula el embarque y exige
que el número declarado coincida con la simulación y con el óptimo.
La cola no tiene que ser igual a la del ejemplo.

## Ejemplos

### Ejemplo 1

Entrada:

```
6 6
1 2 3 3 4 5
```

Salida:

```
5
2 5 1 3 4 3
```

## Solución

Ordenar los pesos y mantener dos extremos. Si mínimo + máximo > s,
añadir mínimo, máximo, eliminarlos y contar dos viajes. El máximo
tampoco cabe con el siguiente mínimo, así que ambos salen solos.
En otro caso, añadir los dos menores como un viaje. Un último peso
impar aporta un viaje.

Probamos el intercambio de los dos menores y la cota óptima de la
otra rama. Una pareja es incompatible si su suma supera s. Si hay
q viajes compartidos, el total es n − q.

Existe una cola óptima canónica: los 2q menores van emparejados al
principio y los restantes forman un camino de vecinos incompatibles.
Además, esos 2q pesos son compatibles entre sí. Para demostrarlo,
marcar al segundo miembro de cada viaje compartido. Dos posiciones
no marcadas adyacentes son incompatibles. Intercambiar pesos para que
los q menores ocupen las marcas; los no marcados solo aumentan y sus
cadenas incompatibles se conservan. Así, los n − q mayores se cubren
con como máximo q + 1 caminos incompatibles.

Todo vecino del mínimo en este grafo es incompatible con cualquier
otro vértice. Al borrar el mínimo, su vecino universal puede unir otro
camino, o sus dos vecinos universales insertar otro camino en su lugar,
reduciendo en uno la cantidad si hay varios. Si solo hay un camino,
se omite el mínimo enlazando sus vecinos. Borrando los q menores no
marcados, los n − 2q mayores forman un camino, quizá vacío.

Los 2r menores, r ≤ q, admiten r parejas compatibles: elegir r parejas
originales y sustituir sus participantes ordenados por pesos globalmente
menores. Si los dos mayores entre los primeros 2q fueran incompatibles,
se podrían anteponer al camino final y emparejar los primeros 2q − 2.
Habría solo q − 1 viajes compartidos, contradicción. Por tanto, el
prefijo pequeño es mutuamente compatible y la forma canónica existe.

Si mínimo + máximo ≤ s, el mínimo cabe con cualquiera. Con al menos
dos pesos no pueden ser todos viajes individuales, así que q ≥ 1.
El óptimo canónico empieza con los dos menores juntos. Quitar ese
viaje completo deja un subproblema óptimo.

Si la suma de extremos supera s, anteponerlos da dos viajes solos.
Para la cota inversa, tomar un óptimo canónico. Si q > 0, borrar el
mínimo del prefijo y el máximo del camino final. Mantener q − 1
parejas pequeñas y poner el peso liberado entre los como máximo dos
caminos restantes. En esas fronteras aparece como máximo una pareja:
al emparejarse por un lado, ese peso se consume. La cola restante
usa como máximo q parejas y pierde como máximo dos viajes.

Si q = 0, borrar los extremos del camino incompatible deja hasta tres
fragmentos. Los vecinos supervivientes del mínimo son extremos
universales que permiten unirlos. Si los vértices borrados eran
adyacentes, basta uno; los casos de extremo o cola vacía son inmediatos.
Los restantes todavía viajan solos. Ambas elecciones voraces preservan
por tanto un óptimo.

Ordenar cuesta `O(n log n)` y el recorrido `O(n)`. La entrada y la
cola construida ocupan `O(n)` memoria.

En el ejemplo, los grupos son [2], [5, 1], [3], [4], [3]: cinco viajes.
Al menos un viaje compartido es inevitable, porque el peso 1 cabe con
cualquier otro.

Trampas:

- igualdad con s significa compartir viaje;
- tras emitir los dos extremos incompatibles, ambos deben salir solos;
- se maximiza el número de viajes, no se minimiza;
- conservar las multiplicidades de todos los pesos repetidos.

El voraz coincide con una búsqueda sobre las 2 601 556 colas de 4998
multiconjuntos pequeños y con una DP aparte en 5003 casos aleatorios.

## Notas por lenguaje

Cada versión ordena una vez y acumula la cola construida. Python usa
CPython 3.12. La suma de dos pesos máximos cabe en un entero de 32 bits
con signo; el número de viajes nunca supera n.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1901_greedy.cpp](1901_greedy.cpp) | G++ 13.2 x64 | greedy | O(n log n) | AC | 0.031 s | 1224 KB |
| [1901_greedy.go](1901_greedy.go) | Go 1.14 x64 | greedy | O(n log n) | AC | 0.046 s | 5640 KB |
| [1901_greedy.java](1901_greedy.java) | Java 1.8 | greedy | O(n log n) | AC | 0.125 s | 6444 KB |
| [1901_greedy.py](1901_greedy.py) | Python 3.12 x64 | greedy | O(n log n) | AC | 0.281 s | 11644 KB |
| [1901_greedy.rs](1901_greedy.rs) | Rust 1.75 x64 | greedy | O(n log n) | AC | 0.031 s | 2108 KB |
