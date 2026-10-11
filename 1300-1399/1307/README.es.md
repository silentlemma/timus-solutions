# 1307. Archivador

[Timus 1307](https://acm.timus.ru/problem.aspx?space=1&num=1307) · dificultad 1275 · strings

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
corto. Para el ejemplo más corto solo se omite la comprobación del tamaño.

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

El inglés repite trozos cortos como « the », «and», «th», «e », además
de palabras enteras. Un texto literario suele dejar sin usar algunos
caracteres imprimibles, como `#`, `$`, `@` o `~`. El codificador ordena
trozos frecuentes y hasta 300 variantes de palabras, con y sin espacio
anterior, por ahorro esperado. Un trozo recibe el siguiente carácter
imprimible sin usar si sustituir sus apariciones sin solapamiento ahorra
más que una estimación conservadora del coste de su línea de tabla.

Los candidatos solo contienen caracteres presentes en el texto, y los
códigos no aparecen en él, así que las sustituciones posteriores no
consumen códigos anteriores y la descodificación es una pasada sin
anidamiento.

El archivo contiene entonces:

- el texto codificado en literales de cadena de hasta 1000 caracteres
  codificados cada uno, para no tocar ningún límite del compilador sobre
  su longitud;
- una tabla `t[code] = "piece";` para los códigos en uso;
- un bucle que imprime `t[c]` para un código y el propio `c` en otro
  caso.

`"`, `\` y `?` se escapan en los literales (el último para que no
aparezca ningún trigrafo `??`), y los saltos de línea sin código se
escriben como `\n`. Los retornos de carro de la entrada se descartan,
convirtiendo CRLF en LF.

En nuestros textos de prueba, salvo el ejemplo, el archivo ocupa
aproximadamente el 26,3–61,3 % de la entrada.

Detalles a tener en cuenta:

- 4 MB no es mucho: un objeto cadena por carácter puede superar el límite.
  C++, Go, Java y Rust codifican el texto en su sitio; Python sustituye
  cadenas. Los cinco escriben la salida trozo a trozo;
- los archivos se compilaron con g++ y se ejecutaron, y reprodujeron los
  textos de prueba exactamente, barras invertidas y signos de
  interrogación incluidos.

## Notas por lenguaje

- Los cinco lenguajes imprimen byte a byte el mismo archivo, y su
  primera línea es `//CPP` sea cual sea el lenguaje del codificador.
- El límite de memoria es de 4 MB. Go y Java guardan una palabra solo
  como su inicio (llega hasta el final de sus letras) en un arreglo cuyo
  tamaño da una primera pasada de conteo, y solo convierten en cadenas
  las 300 palabras elegidas. Go además baja el umbral del recolector de
  basura; Java ordena con su propio heapsort y clases anónimas, porque
  los pares como objetos, el búfer de `TimSort` y la maquinaria de las
  lambdas lo sacaban del límite.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1307_strings.cpp](1307_strings.cpp) | G++ 13.2 x64 | strings | O(L * K * (log L + P)) | AC | 0.078 s | 1068 KB |
| [1307_strings.go](1307_strings.go) | Go 1.14 x64 | strings | O(L * K * (log L + P)) | AC | 0.125 s | 2576 KB |
| [1307_strings.java](1307_strings.java) | Java 1.8 | strings | O(L * K * (log L + P)) | AC | 0.281 s | 1516 KB |
| [1307_strings.py](1307_strings.py) | Python 3.12 x64 | strings | O(L * K * (log L + P)) | AC | 0.156 s | 2696 KB |
| [1307_strings.rs](1307_strings.rs) | Rust 1.75 x64 | strings | O(L * K * (log L + P)) | AC | 0.093 s | 2352 KB |
