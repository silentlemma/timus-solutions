public class Main {
    static final int MAX_DECIMAL_DIGITS = 10, OUTPUT_BUFFER_SIZE = 4096;
    static final byte[] output = new byte[OUTPUT_BUFFER_SIZE];
    static int outputCount;

    static void flushOutput() throws java.io.IOException {
        System.out.write(output, 0, outputCount);
        outputCount = 0;
    }

    static void emit(int value, int delimiter) throws java.io.IOException {
        if (outputCount + MAX_DECIMAL_DIGITS + 1 > output.length)
            flushOutput();
        int first = outputCount;
        do {
            output[outputCount++] = (byte)('0' + value % 10);
            value /= 10;
        } while (value != 0);
        for (int left = first, right = outputCount - 1; left < right; left++, right--) {
            byte temporary = output[left];
            output[left] = output[right];
            output[right] = temporary;
        }
        output[outputCount++] = (byte)delimiter;
    }

    static void finishOutput() throws java.io.IOException {
        flushOutput();
        System.out.flush();
    }

    static int[] head, to, next, edge, weights, after;
    static int count, used;
    static final int BUFFER_SIZE = 4096, BYTE_MASK = 255;
    static final byte[] buffer = new byte[BUFFER_SIZE];
    static int position, available;

    static int read() throws java.io.IOException {
        if (position == available) {
            available = System.in.read(buffer);
            position = 0;
            if (available < 0)
                return -1;
        }
        return buffer[position++] & BYTE_MASK;
    }
    static long nextLong() throws java.io.IOException {
        int c = read();
        while (c >= 0 && c <= ' ')
            c = read();
        long value = 0;
        while (c >= '0' && c <= '9') {
            value = 10 * value + c - '0';
            c = read();
        }
        return value;
    }

    static int nextInt() throws Exception { return (int)nextLong(); }
    static void add(int a, int b, int weight) {
        to[count] = b;
        edge[count] = weight;
        next[count] = head[a];
        head[a] = count++;
    }
    static void visit(int vertex, int parent, int weight) {
        int position = used++;
        weights[position] = weight;
        for (int e = head[vertex]; e != -1; e = next[e])
            if (to[e] != parent)
                visit(to[e], vertex, edge[e]);
        after[position] = used;
    }
    public static void main(String[] args) throws Exception {
        int n = nextInt(), keep = nextInt(), total = 0;
        head = new int[n + 1];
        for (int i = 0; i <= n; i++)
            head[i] = -1;
        to = new int[2 * (n - 1)];
        next = new int[to.length];
        edge = new int[to.length];
        weights = new int[n];
        after = new int[n];
        for (int i = 1; i < n; i++) {
            int a = nextInt(), b = nextInt(), weight = nextInt();
            add(a, b, weight);
            add(b, a, weight);
            total += weight;
        }
        int immediate = shortcut(n, keep, total);
        if (immediate >= 0) {
            emit(immediate, '\n');
            finishOutput();
            return;
        }
        visit(1, 0, 0);
        int removed = n - 1 - keep, limit = Math.min(keep, removed), stride = limit + 1;
        boolean minimize = removed < keep;
        int unreachable = minimize ? total + 1 : -1;
        int[] best = new int[(n + 1) * stride], prefix = new int[n + 1];
        for (int i = 0; i < best.length; i++)
            best[i] = unreachable;
        for (int i = 0; i <= n; i++)
            best[i * stride] = 0;
        for (int i = 0; i < n; i++)
            prefix[i + 1] = prefix[i] + weights[i];
        for (int position = n - 1; position > 0; position--) {
            int here = position * stride, following = (position + 1) * stride,
                skipped = after[position] * stride;
            int size = after[position] - position, cost =
                                                       prefix[after[position]] - prefix[position];
            for (int amount = 1; amount <= Math.min(limit, n - position); amount++) {
                int answer;
                if (minimize) {
                    answer = best[following + amount];
                    // A cut must discard every descendant together with its edge.
                    if (amount >= size) {
                        int rest = best[skipped + amount - size];
                        if (rest < unreachable)
                            answer = Math.min(answer, rest + cost);
                    }
                } else {
                    answer = best[skipped + amount];
                    int rest = best[following + amount - 1];
                    if (rest >= 0)
                        answer = Math.max(answer, rest + weights[position]);
                }
                best[here + amount] = answer;
            }
        }
        int answer = best[stride + limit];
        emit(minimize ? total - answer : answer, '\n');
        finishOutput();
    }

    static int shortcut(int n, int keep, int total) {
        if (total == 0 || keep == 0)
            return 0;
        if (keep == n - 1)
            return total;
        if (keep == 1) {
            int answer = 0;
            for (int e = head[1]; e != -1; e = next[e])
                answer = Math.max(answer, edge[e]);
            return answer;
        }
        if (keep == n - 2) {
            int smallest = total;
            // Discarding exactly one edge preserves root connectivity only at a leaf.
            for (int vertex = 2; vertex <= n; vertex++)
                if (next[head[vertex]] == -1)
                    smallest = Math.min(smallest, edge[head[vertex]]);
            return total - smallest;
        }
        if (keep == 2) {
            int answer = 0, largest = -1, second = -1;
            for (int e = head[1]; e != -1; e = next[e]) {
                int weight = edge[e];
                if (weight > largest) {
                    second = largest;
                    largest = weight;
                } else if (weight > second) {
                    second = weight;
                }
                int child = to[e];
                for (int following = head[child]; following != -1; following = next[following])
                    if (to[following] != 1)
                        answer = Math.max(answer, weight + edge[following]);
            }
            // Two retained edges are either two root children or one two-edge chain.
            return second < 0 ? answer : Math.max(answer, largest + second);
        }
        return -1;
    }
}
