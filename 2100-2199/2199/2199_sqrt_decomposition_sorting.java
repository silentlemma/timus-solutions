import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.TreeSet;

public class Main {
    private static final int VALUE_LIMIT = 1000000000;
    private static final int INFINITY = 2 * VALUE_LIMIT + 1;
    private static final int BUFFER_BITS = 16;

    private static class Input {
        private final byte[] buffer = new byte[1 << BUFFER_BITS];
        private int position;
        private int size;

        private int read() throws IOException {
            if (position == size) {
                size = System.in.read(buffer);
                position = 0;
                if (size < 0) {
                    return -1;
                }
            }
            return buffer[position++];
        }

        int nextInt() throws IOException {
            int c;
            do {
                c = read();
            } while (c <= ' ' && c != -1);
            int sign = 1;
            if (c == '-') {
                sign = -1;
                c = read();
            }
            int value = 0;
            while (c > ' ') {
                value = value * 10 + c - '0';
                c = read();
            }
            return value * sign;
        }
    }

    private static class Answer {
        int score;
        int first;
        int second;

        Answer(int score, int first, int second) {
            this.score = score;
            this.first = first;
            this.second = second;
        }
    }

    private static class Query implements Comparable<Query> {
        final int right;
        final int left;
        final int id;

        Query(int right, int left, int id) {
            this.right = right;
            this.left = left;
            this.id = id;
        }

        public int compareTo(Query other) {
            int result = Integer.compare(right, other.right);
            if (result == 0) {
                result = Integer.compare(left, other.left);
            }
            return result == 0 ? Integer.compare(id, other.id) : result;
        }
    }

    private static int[] values;
    private static int[] potential;
    private static Integer[] order;
    private static TreeSet<Integer> active;

    private static void consider(int rank, int other, Answer best) {
        int score = Math.abs(values[rank] + values[other]);
        if (score < best.score) {
            best.score = score;
            best.first = order[rank];
            best.second = order[other];
        }
    }

    private static boolean add(int rank, Answer best) {
        if (potential[rank] >= best.score) {
            return false;
        }
        Integer below = active.lower(rank);
        Integer above = active.ceiling(rank);
        if (below != null) {
            consider(rank, below, best);
        }
        if (above != null) {
            consider(rank, above, best);
        }
        active.add(rank);
        return true;
    }

    public static void main(String[] args) throws IOException {
        Input in = new Input();
        int n = in.nextInt();
        int q = in.nextInt();
        int[] days = new int[n];
        order = new Integer[n];
        for (int i = 0; i < n; ++i) {
            days[i] = in.nextInt();
            order[i] = i;
        }
        Arrays.sort(order, (a, b) -> {
            int result = Integer.compare(Math.abs(days[a]), Math.abs(days[b]));
            return result == 0 ? Integer.compare(a, b) : result;
        });
        int[] ranks = new int[n];
        values = new int[n];
        potential = new int[n];
        Integer[] numeric = new Integer[n];
        for (int rank = 0; rank < n; ++rank) {
            ranks[order[rank]] = rank;
            values[rank] = days[order[rank]];
            numeric[rank] = rank;
        }
        Arrays.sort(numeric, (a, b) -> {
            int result = Integer.compare(values[a], values[b]);
            return result == 0 ? Integer.compare(a, b) : result;
        });
        for (int rank = 0; rank < n; ++rank) {
            int low = 0;
            int high = n;
            while (low < high) {
                int middle = (low + high) / 2;
                if (values[numeric[middle]] < -values[rank]) {
                    low = middle + 1;
                } else {
                    high = middle;
                }
            }
            potential[rank] = INFINITY;
            for (int other = Math.max(0, low - 2); other < Math.min(n, low + 2); ++other) {
                if (numeric[other] != rank) {
                    int score = Math.abs(values[rank] + values[numeric[other]]);
                    potential[rank] = Math.min(potential[rank], score);
                }
            }
        }
        int blockSize = Math.max(1, 2 * n / Math.max(1, (int) Math.sqrt(q)));
        int blockCount = (n + blockSize - 1) / blockSize;
        ArrayList<ArrayList<Query>> buckets = new ArrayList<>();
        for (int block = 0; block < blockCount; ++block) {
            buckets.add(new ArrayList<>());
        }
        Answer[] answers = new Answer[q];
        Answer[] globalPairs = new Answer[n];
        HashMap<Long, Integer> last = new HashMap<>();
        Answer globalPair = new Answer(0, -1, -1);
        int globalScore = Arrays.stream(potential).min().getAsInt();
        for (int day = 0; day < n; ++day) {
            long target = -(long) days[day];
            for (long value : new long[] {target - globalScore, target + globalScore}) {
                Integer first = last.get(value);
                if (first != null && first > globalPair.first) {
                    globalPair = new Answer(globalScore, first, day);
                }
            }
            globalPairs[day] = globalPair;
            last.put((long) days[day], day);
        }
        for (int id = 0; id < q; ++id) {
            int left = in.nextInt() - 1;
            int right = in.nextInt();
            if (globalPairs[right - 1].first >= left) {
                answers[id] = globalPairs[right - 1];
            } else {
                buckets.get(left / blockSize).add(new Query(right, left, id));
            }
        }
        for (int block = 0; block < blockCount; ++block) {
            ArrayList<Query> queries = buckets.get(block);
            queries.sort(null);
            int boundary = Math.min(n, (block + 1) * blockSize);
            int end = boundary;
            active = new TreeSet<>();
            Answer coreBest = new Answer(INFINITY, 0, 0);
            int start = block * blockSize;
            Answer[] suffixBest = new Answer[boundary - start + 1];
            Answer fringeBest = new Answer(INFINITY, 0, 0);
            for (int day = boundary - 1; day >= start; --day) {
                add(ranks[day], fringeBest);
                suffixBest[day - start] =
                        new Answer(fringeBest.score, fringeBest.first, fringeBest.second);
            }
            active.clear();
            for (Query query : queries) {
                while (end < query.right && coreBest.score != 0) {
                    add(ranks[end++], coreBest);
                }
                Answer best = new Answer(coreBest.score, coreBest.first, coreBest.second);
                if (query.right <= boundary) {
                    for (int day = query.left; day < query.right; ++day) {
                        add(ranks[day], best);
                    }
                    active.clear();
                } else {
                    fringeBest = suffixBest[query.left - start];
                    if (fringeBest.score < best.score) {
                        best = new Answer(fringeBest.score, fringeBest.first, fringeBest.second);
                    }
                    // The two internal answers leave only cross pairs to examine.
                    for (int day = query.left; day < boundary; ++day) {
                        int rank = ranks[day];
                        if (potential[rank] >= best.score) {
                            continue;
                        }
                        Integer below = active.lower(rank);
                        Integer above = active.ceiling(rank);
                        if (below != null) {
                            consider(rank, below, best);
                        }
                        if (above != null) {
                            consider(rank, above, best);
                        }
                    }
                }
                answers[query.id] = best;
            }
        }
        StringBuilder output = new StringBuilder();
        for (Answer best : answers) {
            output.append(Math.min(best.first, best.second) + 1).append(' ');
            output.append(Math.max(best.first, best.second) + 1).append('\n');
        }
        System.out.print(output);
    }
}
