public class Main {
    static int[] head, to, next, edge, weights, after;
    static int count, used;
    static int nextInt() throws Exception {
        int c = System.in.read();
        while (c <= ' ')
            c = System.in.read();
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = System.in.read();
        }
        return value;
    }
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
        if (keep == n - 1) {
            System.out.println(total);
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
        System.out.println(minimize ? total - answer : answer);
    }
}
