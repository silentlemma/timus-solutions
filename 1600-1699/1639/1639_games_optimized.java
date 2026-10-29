import java.io.IOException;

public class Main {
    // the two numbers are parsed by hand from System.in, much lighter than Scanner
    private static int readInt() throws IOException {
        int c;
        do {
            c = System.in.read();
        } while (c <= ' ' && c != -1);
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = System.in.read();
        }
        return value;
    }

    public static void main(String[] args) throws IOException {
        int m = readInt();
        int n = readInt();
        // every break adds one piece, so the game always lasts m * n - 1 moves
        // m * n even means an odd number of moves m * n - 1, so the first player wins
        System.out.println(m * n % 2 == 0 ? "[:=[first]" : "[second]=:]");
    }
}
