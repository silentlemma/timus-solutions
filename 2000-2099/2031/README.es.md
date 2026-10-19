# 2031. Una fila que gira hasta enteros consecutivos

[Timus 2031](https://acm.timus.ru/problem.aspx?space=1&num=2031) · dificultad 88 · bruteforce

Problema original de Nikita Sivukhin, del Concurso Regional Escolar de Programación de los Urales 2014.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Construye una fila de `n` números decimales que, al girar toda la fila
180 grados, produzca un segmento creciente de enteros positivos
consecutivos. Cada número impreso debe tener exactamente dos cifras: los
de una cifra llevan cero inicial. El giro invierte tanto el orden de los
números como las cifras dentro de cada uno. `0`, `1`, `8` quedan
iguales; `6` y `9` se intercambian. Las demás cifras quedan ilegibles.

Límite de entrada: `1 ≤ n ≤ 99`. Tiempo: 1 segundo. Memoria: 64 MB.

## Entrada

Un entero `n`, la cantidad de palabras numéricas en la fila.

## Salida

Cualquier fila válida de `n` números de dos cifras separados por
espacios. Si no existe, imprime exactamente `Glupenky Pierre`. Los
valores girados deben ser positivos, por lo que `00` no vale. Conserva
los ceros iniciales de las demás palabras.

## Evaluación

Un comprobador gira la fila impresa y verifica que se obtiene una serie
de enteros positivos consecutivos, cada uno con dos dígitos legibles; la
imposibilidad solo se acepta si no existe tal serie. Se acepta cualquier
fila válida.

## Ejemplos

```
2
```

```
11 01
```

```
99
```

```
Glupenky Pierre
```

## Solución

Busca primero la fila posterior al giro. Cada objetivo está entre 1 y 99 y sus
dos cifras, incluido un posible cero inicial, pertenecen a `0,1,6,8,9`. Recorre
los enteros en orden, manteniendo la longitud de la racha consecutiva legible;
un número ilegible la reinicia a cero. Cuando alcanza `n` al llegar a `r`, el
intervalo `[r-n+1,r]` está disponible.

Para construir la preimagen recorre los objetivos desde `r` hasta `r-n+1`.
Emite primero la unidad transformada y luego la decena transformada. Añadir
caracteres conserva dos cifras. Si el recorrido termina sin racha suficiente,
declara imposibilidad.

### Corrección

El mapa de cifras es una involución: aplicarlo dos veces recupera cada cifra
legible. La fila construida es el giro inverso del intervalo elegido. Invertir
la fila restaura el orden creciente, y la inversión y transformación dentro
de cada palabra recuperan las dos cifras objetivo. El giro produce por tanto
exactamente los enteros positivos consecutivos elegidos.

Recíprocamente, cualquier fila válida debe girar a un intervalo positivo
consecutivo dentro de `[1,99]` con cifras legibles. La búsqueda completa
visita esos enteros seguidos y su racha alcanzará `n`. Por ello, el
fracaso de la búsqueda demuestra que no existe respuesta.

Los objetivos positivos legibles son
`1,6,8,9,10,11,16,18,19,60,61,66,68,69,80,81,86,88,89,90,91,96,98,99`.
Las rachas máximas son `[8,11]` y `[88,91]`, de longitud cuatro: son factibles
exactamente las longitudes uno a cuatro. El programa encuentra las rachas sin
usar ese límite como caso especial.

El primer ejemplo `11 01` gira a `10 11`. El programa también puede imprimir
`60 80`, que gira a `08 09` y es igualmente válido. En el segundo ejemplo,
99 supera la longitud máxima y corresponde la frase indicada.

Se examinan como máximo 99 enteros y, con éxito, se emiten `n` palabras:
tiempo `O(100+n)`, estado de búsqueda `O(1)` y salida almacenada `O(n)`.
El universo fijo de dos cifras mantiene constante la enumeración.

Trampas:

- Invierte tanto el orden de las palabras como las cifras de cada palabra.
- Intercambia `6` y `9`; invertir caracteres solamente no basta.
- Conserva el cero inicial de cada representación de dos cifras.
- Excluye cero del intervalo positivo.
- Otro intervalo válido no tiene que coincidir con los tokens del ejemplo.

## Notas por lenguaje

Todos los programas añaden caracteres de cifras transformadas sin convertir
el resultado a entero, para conservar ceros. El mapa marca las cifras ilegibles.
Rust genera los objetivos descendentes como `r-offset`; encontrar la racha
garantiza `r ≥ n`, así que la resta sin signo es segura. No se necesitan enteros
grandes ni coma flotante.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2031_bruteforce.cpp](2031_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(100+n) | AC | 0.015 s | 372 KB |
| [2031_bruteforce.go](2031_bruteforce.go) | Go 1.14 x64 | bruteforce | O(100+n) | AC | 0.015 s | 1092 KB |
| [2031_bruteforce.java](2031_bruteforce.java) | Java 1.8 | bruteforce | O(100+n) | AC | 0.109 s | 472 KB |
| [2031_bruteforce.py](2031_bruteforce.py) | Python 3.12 x64 | bruteforce | O(100+n) | AC | 0.078 s | 472 KB |
| [2031_bruteforce.rs](2031_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(100+n) | AC | 0.015 s | 200 KB |
