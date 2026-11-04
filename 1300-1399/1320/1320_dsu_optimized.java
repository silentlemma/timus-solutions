public class Main {
    static final int VERTICES = 1000;
    static final int BUFFER_SIZE = 512;
    // A positive parent link, zero even root or minus one odd root.
    static final short[] parent = new short[VERTICES + 1];
    static final byte[] input = new byte[BUFFER_SIZE];
    static int position, available;

    static int refill() throws java.io.IOException {
        available = Math.max(0, System.in.read(input));
        position = 0;
        return available;
    }

    static int next() throws java.io.IOException {
        while (true) {
            if (position == available && refill() == 0)
                return -1;
            if (input[position] > ' ')
                break;
            position++;
        }
        int value = input[position++] - '0';
        // At most four digits, refilling safely even inside a vertex label.
        if (position == available && refill() == 0)
            return value;
        if (input[position] <= ' ')
            return value;
        value = value * 10 + input[position++] - '0';
        if (position == available && refill() == 0)
            return value;
        if (input[position] <= ' ')
            return value;
        value = value * 10 + input[position++] - '0';
        if (position == available && refill() == 0)
            return value;
        if (input[position] <= ' ')
            return value;
        value = value * 10 + input[position++] - '0';
        return value;
    }

    static int find(int vertex) {
        while (parent[vertex] > 0) {
            int next = parent[vertex];
            if (parent[next] > 0)
                parent[vertex] = parent[next];
            vertex = next;
        }
        return vertex;
    }

    public static void main(String[] args) throws java.io.IOException {
        int endpoint;
        while ((endpoint = next()) >= 0) {
            int a = find(endpoint), b = find(next());
            if (a == b) {
                parent[a] = (short)~parent[a];
            } else {
                int parity = ~(parent[a] ^ parent[b]);
                parent[a] = (short)b;
                parent[b] = (short)parity;
            }
        }
        int answer = '1';
        for (int vertex = 1; vertex <= VERTICES; vertex++) {
            if (parent[vertex] < 0)
                answer = '0';
        }
        System.out.write(answer);
        System.out.write('\n');
    }
}
