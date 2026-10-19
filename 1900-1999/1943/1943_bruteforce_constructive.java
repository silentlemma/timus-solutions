import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.HashSet;

public class Main {
    private static final int LOCAL_LIMIT = 5;

    static boolean wins(int[] own, int[] opponent) {
        ArrayDeque<Integer> first = new ArrayDeque<>(), second = new ArrayDeque<>();
        for (int card : own)
            first.addLast(card);
        for (int card : opponent)
            second.addLast(card);
        HashSet<String> seen = new HashSet<>();
        while (!first.isEmpty() && !second.isEmpty()) {
            if (!seen.add(first.toString() + "|" + second.toString()))
                return false;
            int x = first.removeFirst(), y = second.removeFirst();
            if (x > y) {
                first.addLast(y);
                first.addLast(x);
            } else if (y > x) {
                second.addLast(x);
                second.addLast(y);
            }
        }
        return !first.isEmpty();
    }

    static boolean nextPermutation(int[] values) {
        int pivot = values.length - 2;
        while (pivot >= 0 && values[pivot] >= values[pivot + 1])
            --pivot;
        if (pivot < 0)
            return false;
        int successor = values.length - 1;
        while (values[successor] <= values[pivot])
            --successor;
        int swap = values[pivot];
        values[pivot] = values[successor];
        values[successor] = swap;
        for (int left = pivot + 1, right = values.length - 1; left < right; ++left, --right) {
            swap = values[left];
            values[left] = values[right];
            values[right] = swap;
        }
        return true;
    }

    static int[] construct(int[] opponent) {
        int size = Math.min(opponent.length, LOCAL_LIMIT);
        int[] local = Arrays.copyOf(opponent, size), candidate = local.clone();
        Arrays.sort(candidate);
        do {
            if (wins(candidate, local)) {
                int[] answer = opponent.clone();
                System.arraycopy(candidate, 0, answer, 0, size);
                return answer;
            }
        } while (nextPermutation(candidate));
        return null;
    }

    static int nextInt(BufferedInputStream in) throws IOException {
        int symbol;
        do {
            symbol = in.read();
        } while (symbol <= ' ' && symbol != -1);
        int value = 0;
        while (symbol > ' ') {
            value = value * 10 + symbol - '0';
            symbol = in.read();
        }
        return value;
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream in = new BufferedInputStream(System.in);
        int size = nextInt(in);
        int[] opponent = new int[size];
        for (int index = 0; index < size; ++index)
            opponent[index] = nextInt(in);
        int[] answer = construct(opponent);
        if (answer == null)
            System.out.println("NO");
        else {
            StringBuilder out = new StringBuilder("YES\n");
            for (int index = 0; index < size; ++index) {
                if (index != 0)
                    out.append(' ');
                out.append(answer[index]);
            }
            System.out.println(out);
        }
    }
}
