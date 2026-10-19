# 1971. Clasificar un producto dinámico sin desbordamiento

[Timus 1971](https://acm.timus.ru/problem.aspx?space=1&num=1971) · difficulty 675 · number_theory

Problema original de Denis Dublennykh, del Campeonato de Programación Deportiva de los Urales 2013.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un fotograma de ancho W y alto H cuesta W·H operaciones sin efectos.
Cada opción activada multiplica el coste por su factor entero k. El
equipo ejecuta p operaciones por segundo; los FPS son p dividido por el
coste resultante. Todas las opciones empiezan activadas. Clasificar la
tasa tras cada cambio de opción o resolución, además del estado inicial.

Por debajo de 10 FPS: Slideshow; desde 60 inclusive: Perfect; en otro
caso: So-so. Límites: 2 segundos, 64 MB.

## Entrada

n, 0≤n≤100000, seguido de n nombres y factores 2≤k≤100. Los nombres
tienen 1…10 letras latinas minúsculas. Después W,H,p con 320≤W≤2560,
200≤H≤1600, 1≤p≤10⁹. Sigue m, 1≤m≤100000, y m órdenes On s, Off s o
Resolution w h con iguales límites de dimensiones. On siempre encuentra
la opción desactivada y Off activada. p no cambia.

## Salida

m+1 líneas: clasificación inicial y tras cada orden. Usar exactamente
Slideshow, So-so o Perfect. La igualdad con 10 pertenece a So-so y la
igualdad con 60 a Perfect.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
1
vsync 10
640 480 10000000
2
Off vsync
Resolution 320 240
```

```
Slideshow
So-so
Perfect
```

## Solución

### Guardar exponentes exactos

Solo hay 25 primos hasta 100. Precalcular la factorización de cada factor
permitido. Para cada primo q mantener E[q], suma de exponentes en las
opciones activadas. On añade la factorización y Off la resta; cambiar
la resolución no altera exponentes. El mapa de nombres a factores permanece.

Así la representación sigue siendo exacta aunque el producto sea enorme.
Limitar el producto almacenado pierde información necesaria al desactivar
muchas opciones después. Los logaritmos flotantes pueden fallar justo
en los umbrales de FPS.

### Calcular solo hasta el umbral inferior

Sea A=W·H y L=floor(p/(10A)). Si L=0, incluso el producto vacío queda
por debajo de 10 FPS: Slideshow. En otro caso iniciar Q=1 y expandir las
potencias primas. Antes de multiplicar por q, comprobar Q>floor(L/q).
Si ocurre, el producto completo supera L: devolver Slideshow inmediatamente.
En otro caso multiplicar y seguir.

El retorno temprano no modifica ningún exponente. Si se consumen todas
las potencias, Q es el producto exacto y hay al menos 10 FPS. Responder
Perfect si Q≤floor(p/(60A)); de lo contrario So-so.

Como A≥64000 y p≤10⁹, L≤1562. Cada multiplicación correcta al menos
duplica Q, de modo que hay como máximo diez y un intento fallido,
independientemente de E[q]. Recorrer los 25 primos también es constante;
los exponentes enormes no provocan bucles largos.

### Corrección y cotas

Los exponentes representan inicialmente el producto exacto de opciones
activadas. Sumar o restar una factorización conserva el invariante, y
la resolución no lo afecta. Durante una consulta Q es un prefijo de la
factorización. Un fallo demuestra que el producto completo supera L,
equivalente a p<10A·producto. Sin fallo, el producto es exacto y su
comparación con floor(p/(60A)) equivale al umbral superior. Así todas
las categorías y ambas igualdades se deciden correctamente tras cada cambio.

El exponente máximo es 600000, 60A≤245760000 y Q nunca supera 1562.
Excepto nombres codificados, bastan enteros de 32 bits. Con límite fijo
de factores y acceso hash esperado constante, tiempo total `O(n+m)`.
Espacio `O(n+m)` incluidos búferes de entrada/salida, o `O(n)` para
el estado mantenido.

En el ejemplo el coste inicial es 640·480·10=3072000: menos de 10 FPS,
Slideshow. Desactivar la opción deja 307200, unos 32.55 FPS, So-so.
A 320×240 el coste es 76800, unos 130.21 FPS: Perfect.

Imprimir m+1 respuestas. Preservar todos los exponentes al clasificar;
la consulta no debe consumir el estado. No dividir en Off un producto
previamente limitado. Para n=0 el producto es uno. Usar desigualdades
enteras en 10 y 60. Cambiar resolución mantiene p fijo. Evitar millones
de tokens temporales y distinguir nombres que sean prefijos de otros.

## Notas por lenguaje

Python lee líneas y usa claves de bytes. C++ y Go usan flujos con búfer;
Rust guarda una cadena de entrada y presta subcadenas para nombres. Java
usa búfer de bytes y codifica nombres en long con base 27 y dígitos
1…26: hasta diez letras caben y los dígitos no nulos distinguen
prefijos. Java recorre 25 primos al actualizar; las otras versiones usan
factores dispersos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1971_number_theory.cpp](1971_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(n+m) | AC | 0.093 s | 7212 KB |
| [1971_number_theory.go](1971_number_theory.go) | Go 1.14 x64 | number_theory | O(n+m) | AC | 0.328 s | 12744 KB |
| [1971_number_theory.java](1971_number_theory.java) | Java 1.8 | number_theory | O(n+m) | AC | 0.187 s | 14272 KB |
| [1971_number_theory.py](1971_number_theory.py) | Python 3.12 x64 | number_theory | O(n+m) | AC | 0.375 s | 16372 KB |
| [1971_number_theory.rs](1971_number_theory.rs) | Rust 1.75 x64 | number_theory | O(n+m) | AC | 0.046 s | 10220 KB |
