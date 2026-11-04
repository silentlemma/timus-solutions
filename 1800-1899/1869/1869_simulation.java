public class Main {
    static final int SEATS = 36;
    static final int BUFFER_SIZE = 4096;
    static final byte[] input = new byte[BUFFER_SIZE];
    static int position, available;

    static int read() throws java.io.IOException {
        if (position == available) {
            available = System.in.read(input);
            position = 0;
            if (available < 0)
                return -1;
        }
        return input[position++];
    }

    static int nextInt() throws java.io.IOException {
        int c = read();
        while (c <= ' ')
            c = read();
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = read();
        }
        return value;
    }

    public static void main(String[] args) throws Exception {
        int n = nextInt();
        int[] east = new int[n - 1], west = new int[n - 1];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++) {
                int people = nextInt();
                if (people == 0)
                    continue;
                int[] load = i < j ? east : west;
                for (int leg = Math.min(i, j); leg < Math.max(i, j); leg++)
                    load[leg] += people;
            }
        int peak = 0;
        for (int leg = 0; leg < n - 1; leg++)
            peak = Math.max(peak, Math.max(east[leg], west[leg]));
        System.out.println((peak + SEATS - 1) / SEATS);
    }
}
