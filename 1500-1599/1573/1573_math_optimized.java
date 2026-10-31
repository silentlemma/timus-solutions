public class Main {
    // parse positive decimal tokens directly to avoid scanner allocations.
    private static int nextInt() throws java.io.IOException {
        int c;
        do {
            c = System.in.read();
        } while (c <= ' ' && c != -1);
        int value = 0;
        while (c > ' ') {
            value = value * 10 + c - '0';
            c = System.in.read();
        }
        return value;
    }

    public static void main(String[] args) throws java.io.IOException {
        int blue = nextInt(), red = nextInt(), yellow = nextInt();
        int count = nextInt();
        // one reagent from each needed bag, chosen independently
        // three distinct colors with at most 100 choices give at most 1000000.
        int ways = 1;
        for (int i = 0; i < count; i++) {
            int c;
            do {
                c = System.in.read();
            } while (c <= ' ' && c != -1);
            // the three color names have different initials.
            if (c == 'B')
                ways *= blue;
            else if (c == 'R')
                ways *= red;
            else
                ways *= yellow;
            while (c > ' ')
                c = System.in.read();
        }
        System.out.println(ways);
    }
}
