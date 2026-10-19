import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
    private static final class Input {
        private final BufferedInputStream stream = new BufferedInputStream(System.in);

        String word() throws IOException {
            int character;
            do {
                character = stream.read();
            } while (character <= ' ' && character != -1);
            StringBuilder token = new StringBuilder();
            while (character > ' ') {
                token.append((char)character);
                character = stream.read();
            }
            return token.toString();
        }

        long number() throws IOException {
            int character;
            do {
                character = stream.read();
            } while (character <= ' ' && character != -1);
            long result = 0;
            while (character > ' ') {
                result = result * 10 + character - '0';
                character = stream.read();
            }
            return result;
        }
    }

    private static final class Fenwick {
        private final long[] linear;
        private final long[] constant;

        Fenwick(long[] values) {
            linear = new long[values.length];
            constant = new long[values.length];
            for (int i = 1; i < values.length; ++i) {
                long difference = values[i] - values[i - 1];
                linear[i] = difference;
                constant[i] = difference * (i - 1);
            }
            for (int i = 1; i < values.length; ++i) {
                int ancestor = i + (i & -i);
                if (ancestor < values.length) {
                    linear[ancestor] += linear[i];
                    constant[ancestor] += constant[i];
                }
            }
        }

        void suffixAdd(int index, long amount) {
            long weighted = amount * (index - 1);
            for (; index < linear.length; index += index & -index) {
                linear[index] += amount;
                constant[index] += weighted;
            }
        }

        long prefixSum(int index) {
            long coefficient = 0;
            long offset = 0;
            for (int at = index; at > 0; at -= at & -at) {
                coefficient += linear[at];
                offset += constant[at];
            }
            return coefficient * index - offset;
        }

        long point(int index) {
            long result = 0;
            for (; index > 0; index -= index & -index) {
                result += linear[index];
            }
            return result;
        }

        long[] values() {
            // Undo the linear Fenwick build, then integrate the differences.
            for (int i = linear.length - 1; i > 0; --i) {
                int ancestor = i + (i & -i);
                if (ancestor < linear.length) {
                    linear[ancestor] -= linear[i];
                }
            }
            for (int i = 1; i < linear.length; ++i) {
                linear[i] += linear[i - 1];
            }
            return linear;
        }
    }

    public static void main(String[] args) throws IOException {
        Input in = new Input();
        int n = (int)in.number();
        int q = (int)in.number();
        int[] parent = new int[n];
        int[] size = new int[n];
        int[] tin = new int[n];
        int[] cursor = new int[n];
        long[] salary = new long[n];
        salary[0] = in.number();
        for (int vertex = 0; vertex < n; ++vertex) {
            size[vertex] = 1;
            tin[vertex] = 1;
            cursor[vertex] = 2;
            if (vertex > 0) {
                parent[vertex] = (int)in.number();
                salary[vertex] = in.number();
            }
        }
        for (int vertex = n - 1; vertex > 0; --vertex) {
            size[parent[vertex]] += size[vertex];
        }
        // Reserve consecutive child blocks; every parent has a smaller number.
        for (int vertex = 1; vertex < n; ++vertex) {
            int boss = parent[vertex];
            tin[vertex] = cursor[boss];
            cursor[boss] += size[vertex];
            cursor[vertex] = tin[vertex] + 1;
        }
        long[] initial = new long[n + 1];
        for (int vertex = 0; vertex < n; ++vertex) {
            initial[tin[vertex]] = salary[vertex];
        }
        Fenwick tree = new Fenwick(initial);
        for (int query = 0; query < q; ++query) {
            String kind = in.word();
            int vertex = (int)in.number();
            long threshold = in.number();
            long amount = in.number();
            int left = tin[vertex];
            int length = kind.equals("employee") ? 1 : size[vertex];
            long total = length == 1 ? tree.point(left)
                                     : tree.prefixSum(left + length - 1) - tree.prefixSum(left - 1);
            if (total < threshold * length) {
                tree.suffixAdd(left, amount);
                tree.suffixAdd(left + length, -amount);
            }
        }
        long[] finalSalary = tree.values();
        StringBuilder output = new StringBuilder();
        for (int vertex = 0; vertex < n; ++vertex) {
            output.append(finalSalary[tin[vertex]]).append('\n');
        }
        System.out.print(output);
    }
}
