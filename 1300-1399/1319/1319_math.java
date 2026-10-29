public class Main {
    // no table: each number is computed from the length of its diagonal,
    // counted from the start above the main diagonal and from the end below it
    public static void main(String[] args) throws java.io.IOException {
        // n is parsed by hand from System.in, lighter than Scanner
        int c = System.in.read();
        while (c >= 0 && c <= ' ')
            c = System.in.read();
        int n = 0;
        while (c >= '0' && c <= '9') {
            n = n * 10 + c - '0';
            c = System.in.read();
        }
        StringBuilder output = new StringBuilder();
        for (int row = 0; row < n; row++) {
            output.setLength(0);
            for (int col = 0; col < n; col++) {
                // the diagonal of this cell has n - |col - row| cells
                int length = n - Math.abs(col - row);
                int value = col >= row ? length * (length - 1) / 2 + row + 1
                                       : n * n - length * (length + 1) / 2 + col + 1;
                if (col > 0)
                    output.append(' ');
                output.append(value);
            }
            System.out.println(output);
        }
    }
}
