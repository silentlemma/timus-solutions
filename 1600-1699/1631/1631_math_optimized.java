import java.io.IOException;

public class Main {
    static int readInt() throws IOException {
        int c;
        do {
            c = System.in.read();
        } while (c <= ' ' && c >= 0);
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = System.in.read();
        }
        return value;
    }

    public static void main(String[] args) throws IOException {
        int m = readInt(), n = readInt();
        int diagonal = m + n + 1;
        double length = m * n + diagonal * (Math.sqrt(2) - 1);
        System.out.println(length);
    }
}
