# 1937. Un palíndromo formado por dos cadenas cíclicas

[Timus 1937](https://acm.timus.ru/problem.aspx?space=1&num=1937) · difficulty 1217 · suffix_structures

Original problem from Open Ural FU Championship 2012 | by Olga Soboleva (prepared by Egor Shchelkonogov).

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Elegir una rotación cíclica independiente de cada cadena A,B. Concatenar
primero A rotada y después B rotada; el resultado debe ser igual a su
reverso. Hallar cualquier pareja de inicios o decidir que no existe.
Límites: 1 segundo, 64 MB.

## Entrada

Dos líneas de letras latinas minúsculas: A de longitud n y B de longitud
m, con 1≤m<n≤100000. Una rotación comienza en el carácter elegido y
continúa cíclicamente conservando el orden original.

## Salida

No si es imposible; en otro caso Yes y, en la línea siguiente, inicios
de A y B numerados desde 1 y limitados por n y m. Cualquier pareja que
forme un palíndromo es válida.

## Evaluación

Un comprobador verifica que las rotaciones impresas forman de verdad un
palíndromo; para `No` decide por su cuenta que no existe ninguna pareja.
Se acepta cualquier pareja válida.

## Ejemplos

```
cdedab
bac
```

```
Yes
5 3
```

```
aaaa
bbb
```

```
No
```

## Solución

Usar índices desde cero. Dividir una rotación de A en U V, con |U|=m
y |V|=L=n−m. U V Brot es palíndromo exactamente si V lo es y
Brot=reverse(U). Así se separan las dos condiciones sin probar n·m parejas.

Sean C=reverse(B), P=C+C[:-1]. Las ventanas de longitud m de P son
exactamente todas las rotaciones de C. Construir su autómata de sufijos.
Recorrer los primeros n+m−1 caracteres de A+A manteniendo el sufijo
más largo presente en P. Seguir transiciones existentes; si faltan,
seguir enlaces de sufijo y ajustar la longitud al máximo del estado
hasta poder avanzar. Una coincidencia de al menos m certifica U en
a=position−m+1. Se cubren los n inicios posibles de A.

Cada estado guarda longitud máxima, enlace, transiciones y un final
de aparición f. Al añadir un carácter, crear estado y completar las
transiciones ausentes siguiendo enlaces. En el primer p→q existente,
enlazar a q si len(q)=len(p)+1. Si no, clonar q con longitud len(p)+1,
copiar transiciones/enlace/final, redirigir las transiciones afectadas
por los enlaces al clon y enlazar tanto q como el estado nuevo al clon.
Se conserva exactamente el lenguaje de subcadenas de P. Los últimos
m caracteres coincidentes terminan también en f, por lo que j=f−m+1,
0≤j<m, es un inicio de rotación de C. Al invertirla, el inicio en B
es (−j mod m). Devolver a+1 y ese segundo inicio+1.

Para el centro, calcular Manacher sobre A+A solo con la paridad de L.
El radio impar cuenta parejas sin el centro; el par cuenta parejas
alrededor del hueco anterior al centro. La condición de V que empieza
en a+m es radius[a+m+floor(L/2)]≥floor(L/2). Manacher reutiliza el radio
espejo dentro del palíndromo más a la derecha y extiende su frontera,
con trabajo total lineal. Si no hay centro posible, rechazar antes
de construir el autómata. Cada respuesta satisface ambas condiciones
necesarias y suficientes. Si el recorrido no encuentra ninguna,
se han descartado todas las rotaciones posibles de A.

Tiempo y espacio O(n+m) para el alfabeto fijo de 26 letras. La tabla
densa usa O(26m) enteros, con menos de 2|P| estados. Los retrocesos
por enlaces se amortizan con pasos exitosos. Java recorre como máximo
26 aristas dispersas, conservando la misma cota.

Invertir B antes de buscar y negar su inicio recuperado. Basta coincidir
en al menos m caracteres, aunque el autómata conozca un sufijo mayor.
Incluir el último inicio n−1. Las cadenas periódicas permiten varias
coordenadas correctas. El centro palíndromo y el exterior coincidente
deben corresponder al mismo inicio. m<n garantiza centro no vacío;
su paridad determina la convención de radios.

## Notas por lenguaje

C++, Go, Rust y Python usan transiciones y estados de 32 bits; int32
de Go e i32 de Rust evitan duplicar la mayor reserva. Con m=99999,
los datos Python ocupan 46 399 304 bytes, más 800 000 para radios.
Java usa arreglos primitivos head/next/destination/letter, como máximo
3|P|+1 transiciones y letras byte, dejando margen para la JVM.
Todos los índices y desplazamientos caben en 32 bits.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1937_suffix_structures.cpp](1937_suffix_structures.cpp) | G++ 13.2 x64 | suffix_structures | O(n+m) | AC | 0.046 s | 46824 KB |
| [1937_suffix_structures.go](1937_suffix_structures.go) | Go 1.14 x64 | suffix_structures | O(n+m) | AC | 0.062 s | 49928 KB |
| [1937_suffix_structures.java](1937_suffix_structures.java) | Java 1.8 | suffix_structures | O(n+m) | AC | 0.218 s | 16404 KB |
| [1937_suffix_structures.py](1937_suffix_structures.py) | Python 3.12 x64 | suffix_structures | O(n+m) | AC | 0.796 s | 47932 KB |
| [1937_suffix_structures.rs](1937_suffix_structures.rs) | Rust 1.75 x64 | suffix_structures | O(n+m) | AC | 0.046 s | 46428 KB |
