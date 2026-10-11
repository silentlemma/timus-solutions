# 1307. Archivador

[Timus 1307](https://acm.timus.ru/problem.aspx?space=1&num=1307) · dificultad 1293 · strings

Problema original con idea de Leonid Volkov, preparado por Pavel Egorov y Leonid Volkov, del Octavo Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 11–16 de marzo de 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

La entrada es un fragmento de literatura inglesa de 20 000 a 200 000
caracteres. Hay que imprimir un «archivo» de él: un programa en Pascal,
C o C++, cuya primera línea, `{PAS}`, `/*C*/` o `//CPP`, nombra el
lenguaje, que al compilarse y ejecutarse imprime exactamente el texto
original y que es estrictamente más corto que el texto.

Límite de tiempo: 1 segundo. Límite de memoria: 4 MB.

## Entrada

El texto.

## Salida

El archivo.

## Evaluación

Timus compila el archivo y compara lo que imprime con el texto. Nuestro
verificador no puede compilar C++, así que solo acepta archivos con la
única forma que imprimen estas soluciones (se ve abajo) y ejecuta esa
forma por su cuenta: comprueba las líneas fijas, descodifica las
cadenas y la tabla y compara el resultado con la entrada. Para entradas
de al menos 20 000 caracteres comprueba además que el archivo es más
corto. La entrada del ejemplo es más corta, así que para ella vale
cualquier archivo correcto, aunque sea más largo.

## Ejemplos

### Ejemplo 1

Entrada:

```
123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657
```

Salida:

```
//CPP
#include <cstdio>
const char *d[] = {
"123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657\n",
0};
int main() {
    const char *t[256] = {0};
    for (int k = 0; d[k]; k++)
        for (const char *p = d[k]; *p; p++)
            if (t[(unsigned char)*p]) fputs(t[(unsigned char)*p], stdout);
            else putchar(*p);
    return 0;
}
```

## Solución

El archivo es un pequeño programa en C++ alrededor del texto, guardado
en literales de cadena, y tiene que ahorrar más de lo que cuesta el
programa (unos cientos de caracteres más una línea por código).

El inglés está lleno de los mismos trozos cortos: « the », «and», «th»,
«e », etc. En cambio, un texto literario nunca usa muchos de los
caracteres imprimibles, como `#`, `$`, `@` o `~`. Así que el
codificador recorre una lista fija de trozos frecuentes, empezando por
el salto de línea. Cada trozo cuyos usos ahorrarían más que la línea de
tabla que cuesta recibe el siguiente carácter imprimible sin usar, y
cada aparición del trozo en el texto se sustituye por ese carácter. Los
trozos son texto normal y los códigos nunca son letras ni espacios, así
que los trozos posteriores nunca coinciden dentro de códigos ya puestos,
y la descodificación es una sola pasada sin anidamiento.

El archivo contiene entonces:

- el texto codificado en literales de cadena de 1000 caracteres cada
  uno, para no tocar ningún límite del compilador sobre su longitud;
- una tabla `t[code] = "piece";` para los códigos en uso;
- un bucle que imprime `t[c]` para un código y el propio `c` en otro
  caso.

`"`, `\` y `?` se escapan en los literales (el último para que no
aparezca ningún trigrafo `??`), y los saltos de línea sin código se
escriben como `\n`. Los retornos de carro de la entrada se descartan:
el archivo imprime `\n`, y el modo texto del juez lo convierte de nuevo
en un fin de línea.

En nuestros textos de prueba parecidos al inglés el archivo ocupa un
55–60 % de la entrada. `O(P · L)` para P trozos y un texto de longitud L,
con solo el texto y la salida en memoria.

Detalles a tener en cuenta:

- 4 MB no es mucho: crear un objeto cadena por carácter (una forma fácil
  de escapar el texto) no cabría, así que el texto se codifica en su
  sitio y se escribe trozo a trozo;
- los archivos se compilaron con g++ y se ejecutaron, y reprodujeron los
  textos de prueba exactamente, barras invertidas y signos de
  interrogación incluidos.

## Notas por lenguaje

- Los cinco lenguajes imprimen byte a byte el mismo archivo, y su
  primera línea es `//CPP` sea cual sea el lenguaje del codificador.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1307_strings.cpp](1307_strings.cpp) | G++ 13.2 x64 | strings | O(P * L) | AC | 0.062 s | 368 KB |
| [1307_strings.go](1307_strings.go) | Go 1.14 x64 | strings | O(P * L) | AC | 0.062 s | 1724 KB |
| [1307_strings.java](1307_strings.java) | Java 1.8 | strings | O(P * L) | AC | 0.140 s | 1072 KB |
| [1307_strings.py](1307_strings.py) | Python 3.12 x64 | strings | O(P * L) | AC | 0.046 s | 928 KB |
| [1307_strings.rs](1307_strings.rs) | Rust 1.75 x64 | strings | O(P * L) | AC | 0.031 s | 736 KB |
