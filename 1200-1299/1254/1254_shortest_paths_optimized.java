import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Locale;
import java.util.StringTokenizer;

public class Main {
    private static final double DIAGONAL = Math.sqrt(2);
    private static final double[] COST = {1, 1, 1, 1, DIAGONAL, DIAGONAL, DIAGONAL, DIAGONAL};

    private static final class Search {
        final int width;
        final boolean[] free;
        final int[] steps, heap, position, seen;
        final double[] distance, priority;
        int size, generation;

        Search(int width, boolean[] free, int[] steps) {
            this.width = width;
            this.free = free;
            this.steps = steps;
            heap = new int[free.length];
            position = new int[free.length];
            seen = new int[free.length];
            distance = new double[free.length];
            priority = new double[free.length];
        }

        double estimate(int cell, int targetX, int targetY) {
            int dx = Math.abs(cell % width - targetX);
            int dy = Math.abs(cell / width - targetY);
            return Math.abs(dx - dy) + DIAGONAL * Math.min(dx, dy);
        }

        boolean earlier(int a, int b) { return priority[a] < priority[b]; }

        void place(int slot, int cell) {
            heap[slot] = cell;
            position[cell] = slot;
        }

        void offer(int cell, double length, double estimate) {
            int slot = seen[cell] == generation ? position[cell] : -1;
            if (slot < 0) {
                slot = size++;
            }
            seen[cell] = generation;
            distance[cell] = length;
            priority[cell] = length + estimate;
            while (slot > 0) {
                int parent = (slot - 1) / 2;
                if (!earlier(cell, heap[parent])) {
                    break;
                }
                place(slot, heap[parent]);
                slot = parent;
            }
            place(slot, cell);
        }

        int pop() {
            int first = heap[0];
            int last = heap[--size];
            position[first] = -1;
            if (size == 0) {
                return first;
            }
            int slot = 0;
            for (int child = 1; child < size; child = 2 * slot + 1) {
                if (child + 1 < size && earlier(heap[child + 1], heap[child])) {
                    child++;
                }
                if (!earlier(heap[child], last)) {
                    break;
                }
                place(slot, heap[child]);
                slot = child;
            }
            place(slot, last);
            return first;
        }

        double walk(int from, int to, boolean open) {
            int targetX = to % width, targetY = to / width;
            if (open) {
                return estimate(from, targetX, targetY);
            }
            generation++;
            size = 0;
            offer(from, 0, estimate(from, targetX, targetY));
            while (size > 0) {
                int cell = pop();
                if (cell == to) {
                    return distance[cell];
                }
                for (int i = 0; i < steps.length; i++) {
                    int next = cell + steps[i];
                    double length = distance[cell] + COST[i];
                    if (free[next] && (seen[next] != generation || length < distance[next])) {
                        offer(next, length, estimate(next, targetX, targetY));
                    }
                }
            }
            throw new IllegalStateException();
        }
    }

    private static int[] components(boolean[] free, int[] steps) {
        int[] part = new int[free.length];
        int[] stack = new int[free.length];
        for (int cell = 0; cell < free.length; cell++) {
            if (!free[cell] || part[cell] != 0) {
                continue;
            }
            int size = 0;
            stack[size++] = cell;
            part[cell] = cell;
            while (size > 0) {
                int current = stack[--size];
                for (int step : steps) {
                    int next = current + step;
                    if (free[next] && part[next] == 0) {
                        part[next] = cell;
                        stack[size++] = next;
                    }
                }
            }
        }
        return part;
    }

    private static final class Input {
        final BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokens = new StringTokenizer("");

        String next() throws IOException {
            while (!tokens.hasMoreTokens()) {
                tokens = new StringTokenizer(reader.readLine());
            }
            return tokens.nextToken();
        }

        int number() throws IOException { return Integer.parseInt(next()); }

        int cell(int width) throws IOException { return number() + number() * width; }
    }

    public static void main(String[] args) throws IOException {
        Input input = new Input();
        int cols = input.number(), rows = input.number(), bombs = input.number();
        double speed = Double.parseDouble(input.next());
        int width = cols + 2;
        boolean[] free = new boolean[(rows + 2) * width];
        for (int row = 1; row <= rows; row++) {
            String line = input.next();
            for (int col = 1; col <= cols && col <= line.length(); col++) {
                free[row * width + col] = line.charAt(col - 1) == '.';
            }
        }
        int at = input.cell(width);
        free[at] = true;
        int[] steps = {1, -1, width, -width, width + 1, width - 1, 1 - width, -width - 1};
        int[] part = components(free, steps);
        int openCells = 0;
        for (boolean cell : free) {
            if (cell) {
                openCells++;
            }
        }
        boolean open = openCells == rows * cols;
        Search search = new Search(width, free, steps);
        HashMap<Integer, Double> known = new HashMap<>();
        double total = 0;
        for (int i = 0; i < bombs; i++) {
            int target = input.cell(width);
            if (part[target] != part[at] || target == at) {
                continue;
            }
            int key = Math.min(at, target) * free.length + Math.max(at, target);
            Double length = known.get(key);
            if (length == null) {
                length = search.walk(at, target, open);
                known.put(key, length);
            }
            total += length;
            at = target;
        }
        System.out.printf(Locale.ROOT, "%.2f%n", total / speed);
    }
}
