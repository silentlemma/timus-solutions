public class Main {
    public static void main(String[] args) throws java.io.IOException {
        int c = System.in.read();
        while (c >= 0 && c <= ' ')
            c = System.in.read();
        // the number is parsed byte by byte from System.in instead of Scanner
        int size = 0;
        while (c >= '0' && c <= '9') {
            size = size * 10 + c - '0';
            c = System.in.read();
        }
        int total = size * (size + 1) / 2;
        System.out.println(total % 2 == 0 ? "black" : "grimy");
    }
}
