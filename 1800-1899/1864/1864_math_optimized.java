public class Main {
    static final class Input {
        private final java.io.BufferedReader reader =
            new java.io.BufferedReader(new java.io.InputStreamReader(System.in));
        private java.util.StringTokenizer words = new java.util.StringTokenizer("");

        String next() throws java.io.IOException {
            while (!words.hasMoreTokens()) {
                String line = reader.readLine();
                if (line == null)
                    return null;
                words = new java.util.StringTokenizer(line);
            }
            return words.nextToken();
        }
        int nextInt() throws java.io.IOException { return Integer.parseInt(next()); }
    }

    static final int MONEY = 100;

    // buffered tokens avoid scanner regex initialization and temporary match objects.
    public static void main(String[] args) throws java.io.IOException {
        Input in = new Input();
        int n = in.nextInt();
        int[] bought = new int[n];
        int total = 0;
        for (int i = 0; i < n; i++) {
            bought[i] = in.nextInt();
            total += bought[i];
        }
        // everybody, Den too, drinks total / (n + 1); in units of 1 / (n + 1)
        // litre, friend i paid for bought[i] (n + 1) - total litres of others
        int[] over = new int[n];
        int all = 0;
        for (int i = 0; i < n; i++) {
            over[i] = Math.max(0, bought[i] * (n + 1) - total);
            all += over[i];
        }
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < n; i++) {
            out.append(i > 0 ? " " : "").append(MONEY * over[i] / all);
        }
        System.out.println(out);
    }
}
