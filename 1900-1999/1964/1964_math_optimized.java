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
        long nextLong() throws java.io.IOException { return Long.parseLong(next()); }
    }

    static long minimumCommon(long population, long[] lowerBounds) {
        long answer = population;
        for (long lower : lowerBounds)
            answer -= population - lower;
        return Math.max(0, answer);
    }

    // buffered tokens avoid scanner regex initialization and temporary match objects.
    public static void main(String[] args) throws java.io.IOException {
        Input input = new Input();
        long population = input.nextLong();
        int count = input.nextInt();
        long[] lowerBounds = new long[count];
        for (int i = 0; i < count; i++)
            lowerBounds[i] = input.nextLong();
        System.out.println(minimumCommon(population, lowerBounds));
    }
}
