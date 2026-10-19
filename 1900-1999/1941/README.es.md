# 1941. Ventanas con un multiconjunto dado

[Timus 1941](https://acm.timus.ru/problem.aspx?space=1&num=1941) · difficulty 431 · two_pointers

Original problem from Open Ural FU Personal Contest 2012 | by Andrey Demidov (prepared by Alex Samsonov).

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada letra es una terna ordenada de símbolos ASCII de códigos 33 a 122
inclusive: hay 90³=729000 letras. Dado un patrón no vacío de m≤8000 letras
y un texto no vacío de n≤500000 letras, contar ventanas contiguas que
sean permutaciones del patrón. Importan las multiplicidades y el orden
interno de la terna; las ventanas pueden solaparse. Límites: 1 segundo, 64 MB.

## Entrada

La primera línea contiene el patrón y la segunda el texto. Una letra
son tres símbolos adyacentes; espacios separan letras. El final de la
primera línea fija m. No se proporcionan m ni n por separado.

## Salida

Un entero: número de ventanas válidas. Si m>n, la respuesta es 0.

## Evaluación

Se compara un entero; los espacios son insignificantes.

## Ejemplos

```
aaa bbb ccc
aaa aaa bbb ccc aaa zzz aaa bbb ccc
```

```
3
```

## Solución

Codificar (a,b,c) como ((a−33)·90+(b−33))·90+(c−33). Son dígitos
0..89, una biyección a 0..728999, no un hash. Iniciar una tabla con
signo D de 729000 déficits con las frecuencias del patrón, un anillo
de m códigos y missing=m.

Antes de insertar una letra, retirar la más antigua si el anillo está
lleno. Al retirar x, incrementar missing si D[x]≥0 antes del cambio;
después incrementar D[x]. Al insertar y, reducir missing si D[y]>0,
y después reducir D[y]. Reemplazar la posición del anillo y avanzar
cíclicamente. Contar cuando missing=0. Antes de llenar m posiciones,
menos de m letras no pueden cubrir m ocurrencias, por lo que no se cuenta.

El invariante es D[x]=frecuencia_patron[x]−frecuencia_ventana[x], y
missing=Σ max(D[x],0). Retirar crea un déficit exactamente si D[x]≥0;
insertar llena uno exactamente si D[y]>0. Se conserva el invariante.
En una ventana llena ambas sumas de frecuencias son m, por lo que
missing=0 equivale a todos los déficits nulos, es decir, multiconjuntos
iguales. Cada ventana se visita una vez, incluidos solapamientos y final.

Con U=729000, tiempo O(U+m+n), espacio del núcleo O(U+m). C++ y Java
procesan el texto como flujo; Python, Go y Rust conservan la entrada,
con espacio total O(U+m+n). La respuesta≤n−m+1≤500000 cabe en 32 bits
con signo.

Las letras son ternas, no símbolos ASCII sueltos; reordenar una terna
la cambia. Un conjunto sin cantidades no basta. Retirada usa ≥0,
inserción >0, antes del cambio. Incluir solapamientos y ventana final;
no desplazar el anillo completo ni recorrer todo el alfabeto en cada paso.

## Notas por lenguaje

Los déficits necesitan signo para representar exceso. Python usa un
array compacto signed int; Go usa int32 y campos de bytes; Java analiza
ternas directamente sin un String por letra. Rust guarda la entrada
una vez e itera sus segmentos. No hay huellas probabilísticas ni mapas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1941_two_pointers.cpp](1941_two_pointers.cpp) | G++ 13.2 x64 | two_pointers | O(U+m+n) | AC | 0.046 s | 2996 KB |
| [1941_two_pointers.go](1941_two_pointers.go) | Go 1.14 x64 | two_pointers | O(U+m+n) | AC | 0.062 s | 21096 KB |
| [1941_two_pointers.java](1941_two_pointers.java) | Java 1.8 | two_pointers | O(U+m+n) | AC | 0.187 s | 3336 KB |
| [1941_two_pointers.py](1941_two_pointers.py) | Python 3.12 x64 | two_pointers | O(U+m+n) | AC | 0.734 s | 33664 KB |
| [1941_two_pointers.rs](1941_two_pointers.rs) | Rust 1.75 x64 | two_pointers | O(U+m+n) | AC | 0.031 s | 6000 KB |
