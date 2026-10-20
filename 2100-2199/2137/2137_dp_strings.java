import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

public class Main {
    private static final int EXTENSION = 25;

    private static class Seed {
        final int state;
        final long score;

        Seed(int state, long score) {
            this.state = state;
            this.score = score;
        }
    }

    private final int[] text;
    private final int[] border;
    private final int[] rank;
    private final long[] answer = new long[EXTENSION + 1];
    private int length;

    private Main(int capacity) {
        text = new int[capacity];
        border = new int[capacity + 1];
        rank = new int[capacity + 1];
        Arrays.fill(answer, -1);
    }

    private int append(int symbol) {
        int matched = border[length];
        while (matched > 0 && text[matched] != symbol) {
            matched = border[matched];
        }
        if (length > 0 && text[matched] == symbol) {
            matched++;
        }
        text[length++] = symbol;
        border[length] = matched;
        int period = length - matched;
        int previous = matched - border[matched];
        rank[length] = rank[matched] + (period == previous ? 0 : 1);
        return rank[matched];
    }

    private void finish(int depth, long total) {
        int fixed = length;
        int remaining = EXTENSION - depth;
        int[] zero = new int[fixed];
        int[] one = new int[fixed];
        for (int state = 0; state < fixed; state++) {
            int fallback = border[state];
            if (text[state] == 0) {
                zero[state] = state + 1;
                one[state] = state == 0 ? 0 : one[fallback];
            } else {
                one[state] = state + 1;
                zero[state] = state == 0 ? 0 : zero[fallback];
            }
        }

        ArrayList<ArrayList<Seed>> seeds = new ArrayList<>();
        for (int step = 0; step <= remaining; step++) {
            seeds.add(new ArrayList<Seed>());
        }
        int ancestor = border[fixed];
        while (fixed - ancestor <= remaining) {
            int period = fixed - ancestor;
            long score = total;
            for (int step = 1; step <= remaining; step++) {
                int symbol = text[length - period];
                int matched = border[length];
                if (matched >= fixed) {
                    int other = symbol ^ 1;
                    while (matched >= fixed && text[matched] != other) {
                        matched = border[matched];
                    }
                    if (matched >= fixed) {
                        matched++;
                    } else {
                        matched = other == 0 ? zero[matched] : one[matched];
                    }
                    if (matched < fixed) {
                        seeds.get(step).add(new Seed(matched, score + rank[matched]));
                    }
                }
                score += append(symbol);
                answer[depth + step] = Math.max(answer[depth + step], score);
            }
            length = fixed;
            if (ancestor == 0) {
                break;
            }
            ancestor = border[ancestor];
        }

        long[] current = new long[fixed];
        long[] following = new long[fixed];
        Arrays.fill(current, -1);
        int[] active = new int[fixed];
        int[] nextActive = new int[fixed];
        active[0] = border[fixed];
        int count = 1;
        current[active[0]] = total;
        for (int step = 1; step <= remaining; step++) {
            Arrays.fill(following, -1);
            int nextCount = 0;
            for (Seed seed : seeds.get(step)) {
                if (following[seed.state] == -1) {
                    nextActive[nextCount++] = seed.state;
                }
                following[seed.state] = Math.max(following[seed.state], seed.score);
            }
            for (int index = 0; index < count; index++) {
                int state = active[index];
                for (int symbol = 0; symbol < 2; symbol++) {
                    int target = symbol == 0 ? zero[state] : one[state];
                    if (target < fixed) {
                        long value = current[state] + rank[target];
                        if (following[target] == -1) {
                            nextActive[nextCount++] = target;
                        }
                        following[target] = Math.max(following[target], value);
                    }
                }
            }
            for (int index = 0; index < nextCount; index++) {
                answer[depth + step] = Math.max(
                    answer[depth + step], following[nextActive[index]]);
            }
            long[] scores = current;
            current = following;
            following = scores;
            int[] states = active;
            active = nextActive;
            nextActive = states;
            count = nextCount;
        }
    }

    private void search(int depth, int split, long total) {
        if (depth == split) {
            finish(depth, total);
            return;
        }
        int fixed = length;
        for (int symbol = 0; symbol < 2; symbol++) {
            long score = total + append(symbol);
            answer[depth + 1] = Math.max(answer[depth + 1], score);
            search(depth + 1, split, score);
            length = fixed;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        String source = input.readLine();
        if (source == null) {
            source = "";
        }
        Main solver = new Main(source.length() + EXTENSION);
        long total = 0;
        for (int index = 0; index < source.length(); index++) {
            total += solver.append(source.charAt(index) == 'X' ? 1 : 0);
        }
        int split = Math.max(0, (EXTENSION - solver.length + 1) / 2);
        solver.search(0, split, total);
        StringBuilder output = new StringBuilder();
        for (int step = 1; step <= EXTENSION; step++) {
            output.append(solver.answer[step]).append('\n');
        }
        System.out.print(output);
    }
}
