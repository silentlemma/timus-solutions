# 1916. Fragmentos cortos de palabras exponencialmente largas

[Timus 1916](https://acm.timus.ru/problem.aspx?space=1&num=1916) · difficulty 3024 · strings

Problema original de Ivan Burmistrov (preparado por Dmitry Ivankov), de la subregión oriental del NEERC 2012.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada uno de n tipos de símbolo es estable o tiene una única palabra fija
de reemplazo, ordenada desde abajo hacia arriba. Reemplazar los inestables
hasta obtener solo estables; se garantiza terminación para cada tipo.
Desde cualquier tipo inicial, considerar sus fragmentos contiguos de
longitud exactamente k. Contar las palabras distintas entre todas las
expansiones; las apariciones repetidas cuentan una vez. Límites: 1 segundo, 64 MB.

## Entrada

n,k en [2,100]. Después una descripción por tipo 1..n: −1 si es estable;
si no, longitud 1≤kᵢ≤100 y kᵢ índices en [1,n], conservando el orden.
La suma E de longitudes de reemplazo no supera 100.

## Salida

Cantidad de fragmentos distintos de longitud k módulo 1 000 000 007.
Escribir cero si ninguna palabra es suficientemente larga.

## Evaluación

Comparación exacta de un token entero.

## Ejemplos

```
7 3
3 3 2 2
3 4 5 5
1 7
-1
-1
3 7 7 7
-1
```

```
5
```

## Solución

El grafo de dependencias es acíclico: un ciclo de reemplazos no vacíos
no terminaría. Procesar con búsqueda en profundidad y memoria. Guardar
solo prefijo y sufijo de hasta k−1 símbolos de cada tipo; uno estable
aporta su propio símbolo. No expandir palabras completas: 50 duplicaciones
producen longitud 2⁵⁰.

Concatenar los hijos de cada regla de izquierda a derecha. Al añadir B
a la parte acumulada A, formar suffix(A,k−1)+prefix(B,k−1) e insertar
todas sus subcadenas de longitud k en un conjunto global. Cada mitad es
más corta que k, así que todo candidato cruza una unión verdadera.
Actualizar el prefijo con los primeros k−1 símbolos de ambos prefijos,
y el sufijo con los últimos k−1 de ambos sufijos. Usar el sufijo del
hijo en esta última actualización, no su prefijo.

### Corrección

Una subcadena de A+B está dentro de A, dentro de B o cruza la unión.
Las dos primeras clases ya se recogen antes o recursivamente. La tercera
usa como máximo k−1 símbolos de cada lado, así que está en la ventana.
Recíprocamente, toda subcadena de longitud k de esa ventana cruza la unión
y es real. Las actualizaciones conservan los resúmenes exactos. La inducción
por dependencias y concatenaciones demuestra que se recoge exactamente
el conjunto válido. Visitar todos los tipos incluye cualquier comienzo,
y el conjunto global elimina duplicados.

### Coste y representación

Cada unión aporta como máximo k−1 candidatos y hay a lo sumo E conexiones.
Como mucho E(k−1)≤9900 inserciones. Copiar y calcular el hash de una palabra
cuesta `O(k)`: tiempo esperado `O(Ek² + nk)` y memoria `O(Ek² + nk)`, contando
el contenido real de las claves. El resultado ya es menor que el módulo,
pero se aplica el resto solicitado.

Los índices≤100 caben en un byte. Las claves son palabras completas de
bytes o caracteres; las colisiones de hash se resuelven con igualdad exacta.
La memoria de resultados maneja referencias adelantadas y descendientes compartidos.

El ejemplo produce 777,455,745,554,545; otra aparición de 455 no cambia el resultado.

Contar palabras distintas, no apariciones ni caminos. Incluir todos los
tipos iniciales. Acumular el resumen izquierdo: una palabra puede cruzar
varios hijos cortos, no solo dos vecinos. Respetar el orden, distinguir
tipos estables, tratar alias y k excesivo, y separar prefijo de sufijo del hijo.

## Notas por lenguaje

Python usa `bytes`, C++/Go cadenas de bytes, Java cadenas de caracteres y
Rust vectores de bytes. Todos usan conjuntos exactos. La recursión tiene
profundidad≤100. Go puede compartir la memoria de una ventana corta;
Rust copia sus claves. Ningún puerto expande las palabras exponenciales
ni identifica palabras solamente por un hash rodante.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1916_strings.cpp](1916_strings.cpp) | G++ 13.2 x64 | strings | O(E k^2 + n k) | AC | 0.015 s | 672 KB |
| [1916_strings.go](1916_strings.go) | Go 1.14 x64 | strings | O(E k^2 + n k) | AC | 0.031 s | 1332 KB |
| [1916_strings.java](1916_strings.java) | Java 1.8 | strings | O(E k^2 + n k) | AC | 0.093 s | 2160 KB |
| [1916_strings.py](1916_strings.py) | Python 3.12 x64 | strings | O(E k^2 + n k) | AC | 0.078 s | 976 KB |
| [1916_strings.rs](1916_strings.rs) | Rust 1.75 x64 | strings | O(E k^2 + n k) | AC | 0.015 s | 724 KB |
