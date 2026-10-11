#include <cstdio>

// The PIBAS program keeps the quote characters in C and B, so its printing
// statement needs no single quote and fits inside the single-quoted A; the
// statement prints the start of the program, then A in quotes, then A again.
const char *HEAD = R"(C="'";B='"';A=')";
const char *TAIL = R"(;?"C="+B+C+B+";B="+C+B+C+";A="+C+A+C+A)";

int main() { printf("%s%s'%s\n", HEAD, TAIL, TAIL); }
