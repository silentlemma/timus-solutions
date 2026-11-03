public class Main {
    static final int MAX_LENGTH = 100;

    public static void main(String[] args) throws Exception {
        byte[] text = new byte[MAX_LENGTH];
        int n = 0, c;
        while ((c = System.in.read()) >= 0 && c != '\n')
            if (c > ' ')
                text[n++] = (byte)c;
        int[] row = new int[n + 1];
        for (int i = 0; i <= n; i++)
            row[i] = i * (2 * n + 1 - i) / 2;
        // Include empty intervals; only j>=i is stored, at row[i]+j.
        byte[] cost = new byte[(n + 1) * (n + 2) / 2];
        for (int i = 0; i < n; i++)
            cost[row[i] + i + 1] = 1;
        for (int length = 2; length <= n; length++)
            for (int i = 0; i + length <= n; i++) {
                int j = i + length, best = 1 + cost[row[i + 1] + j];
                if ((text[i] == '(' && text[j - 1] == ')') ||
                    (text[i] == '[' && text[j - 1] == ']'))
                    best = cost[row[i + 1] + j - 1];
                for (int k = i + 1; k < j && best > length % 2; k++)
                    best = Math.min(best, cost[row[i] + k] + cost[row[k] + j]);
                cost[row[i] + j] = (byte)best;
            }
        byte[] output = new byte[2 * n + 1];
        int[] pending = new int[2 * n + 1];
        int top = 0, used = 0, stride = n + 1;
        pending[top++] = n;
        while (top != 0) {
            int job = pending[--top];
            // Negative tasks emit a closing bracket after their nested interval.
            if (job < 0) {
                output[used++] = (byte)-job;
                continue;
            }
            int i = job / stride, j = job % stride;
            if (i == j)
                continue;
            if (j == i + 1) {
                boolean round = text[i] == '(' || text[i] == ')';
                output[used++] = (byte)(round ? '(' : '[');
                output[used++] = (byte)(round ? ')' : ']');
            } else if (((text[i] == '(' && text[j - 1] == ')') ||
                        (text[i] == '[' && text[j - 1] == ']')) &&
                       cost[row[i] + j] == cost[row[i + 1] + j - 1]) {
                output[used++] = text[i];
                pending[top++] = -text[j - 1];
                pending[top++] = (i + 1) * stride + j - 1;
            } else {
                for (int k = i + 1; k < j; k++)
                    if (cost[row[i] + j] == cost[row[i] + k] + cost[row[k] + j]) {
                        pending[top++] = k * stride + j;
                        pending[top++] = i * stride + k;
                        break;
                    }
            }
        }
        output[used++] = '\n';
        System.out.write(output, 0, used);
    }
}
