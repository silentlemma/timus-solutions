import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    private static final int ORIENTATIONS = 4;
    private static final int INITIAL_QUEUE_CAPACITY = 1024;

    private static final class IntDeque {
        int[] values = new int[INITIAL_QUEUE_CAPACITY];
        int head;
        int size;

        void ensureSpace() {
            if (size < values.length) {
                return;
            }
            int[] next = new int[values.length * 2];
            for (int index = 0; index < size; index++) {
                next[index] = values[(head + index) & (values.length - 1)];
            }
            values = next;
            head = 0;
        }

        void addFirst(int value) {
            ensureSpace();
            head = (head - 1) & (values.length - 1);
            values[head] = value;
            size++;
        }

        void addLast(int value) {
            ensureSpace();
            values[(head + size) & (values.length - 1)] = value;
            size++;
        }

        int removeFirst() {
            int value = values[head];
            head = (head + 1) & (values.length - 1);
            size--;
            return value;
        }
    }

    private static final class Transition {
        final int player;
        final int mask;
        final int change;
        final int offset;

        Transition(int player, int mask, int change, int offset) {
            this.player = player;
            this.mask = mask;
            this.change = change;
            this.offset = offset;
        }
    }

    private static int minimumPassages(int rows, int columns, String[] scheme) {
        int height = rows + 2;
        int width = columns + 2;
        int size = height * width;
        int[][] moves = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
        int[] offsets = {-width, 1, width, -1};
        boolean[] outside = new boolean[size];
        byte[] masks = new byte[size];
        int[] starts = new int[2];
        int startCount = 0;
        for (int position = 0; position < size; position++) {
            int r = position / width;
            int c = position % width;
            outside[position] = r == 0 || r == height - 1 || c == 0 || c == width - 1;
        }
        for (int row = 1; row <= rows; row++) {
            for (int column = 1; column <= columns; column++) {
                int position = row * width + column;
                int r = 2 * row - 1;
                int c = 2 * column - 1;
                char room = scheme[r].charAt(c);
                if (room == '1' || room == '2') {
                    starts[startCount++] = position;
                }
                char[] walls = {scheme[r - 1].charAt(c), scheme[r].charAt(c + 1),
                        scheme[r + 1].charAt(c), scheme[r].charAt(c - 1)};
                for (int direction = 0; direction < moves.length; direction++) {
                    if (walls[direction] == '.') {
                        masks[position] |= 1 << direction;
                    }
                }
            }
        }
        for (int position = 0; position < size; position++) {
            if (!outside[position]) {
                continue;
            }
            int row = position / width;
            int column = position % width;
            for (int direction = 0; direction < moves.length; direction++) {
                int nr = row + moves[direction][0];
                int nc = column + moves[direction][1];
                if (nr < 0 || nr >= height || nc < 0 || nc >= width) {
                    continue;
                }
                int neighbor = nr * width + nc;
                int opposite = (direction + 2) % moves.length;
                if (outside[neighbor] || (masks[neighbor] & (1 << opposite)) != 0) {
                    masks[position] |= 1 << direction;
                }
            }
        }
        int[][] relative = {{0, 1}, {1, -1}, {1, 0}, {1, 1}};
        int[] deltas = new int[ORIENTATIONS];
        Transition[][] transitions = new Transition[ORIENTATIONS][];
        for (int orientation = 0; orientation < ORIENTATIONS; orientation++) {
            deltas[orientation] = relative[orientation][0] * width + relative[orientation][1];
            List<Transition> choices = new ArrayList<>();
            for (int player = 0; player < 2; player++) {
                for (int direction = 0; direction < moves.length; direction++) {
                    int[][] positions = {{0, 0},
                            {relative[orientation][0], relative[orientation][1]}};
                    positions[player][0] += moves[direction][0];
                    positions[player][1] += moves[direction][1];
                    if (positions[1][0] < positions[0][0]
                            || positions[1][0] == positions[0][0]
                            && positions[1][1] < positions[0][1]) {
                        int[] temporary = positions[0];
                        positions[0] = positions[1];
                        positions[1] = temporary;
                    }
                    int dr = positions[1][0] - positions[0][0];
                    int dc = positions[1][1] - positions[0][1];
                    int next = -1;
                    for (int index = 0; index < ORIENTATIONS; index++) {
                        if (relative[index][0] == dr && relative[index][1] == dc) {
                            next = index;
                            break;
                        }
                    }
                    if (next < 0) {
                        continue;
                    }
                    int shift = positions[0][0] * width + positions[0][1];
                    choices.add(new Transition(player, 1 << direction,
                            shift * ORIENTATIONS + next - orientation, offsets[direction]));
                }
            }
            transitions[orientation] = choices.toArray(new Transition[0]);
        }
        Arrays.sort(starts);
        int orientation = 0;
        for (int index = 0; index < ORIENTATIONS; index++) {
            if (deltas[index] == starts[1] - starts[0]) {
                orientation = index;
            }
        }
        int initial = starts[0] * ORIENTATIONS + orientation;
        int[] distance = new int[size * ORIENTATIONS];
        Arrays.fill(distance, -1);
        boolean[] finished = new boolean[distance.length];
        distance[initial] = 0;
        IntDeque pending = new IntDeque();
        pending.addLast(initial);
        while (pending.size != 0) {
            int state = pending.removeFirst();
            if (finished[state]) {
                continue;
            }
            finished[state] = true;
            int current = distance[state];
            int first = state / ORIENTATIONS;
            int dir = state % ORIENTATIONS;
            int second = first + deltas[dir];
            if (outside[first] && outside[second]) {
                return current;
            }
            for (Transition action : transitions[dir]) {
                int position = action.player == 0 ? first : second;
                if ((masks[position] & action.mask) == 0) {
                    continue;
                }
                int neighbor = position + action.offset;
                int cost = outside[position] && outside[neighbor] ? 0 : 1;
                int following = state + action.change;
                int candidate = current + cost;
                if (distance[following] == -1 || candidate < distance[following]) {
                    distance[following] = candidate;
                    if (cost == 0) {
                        pending.addFirst(following);
                    } else {
                        pending.addLast(following);
                    }
                }
            }
        }
        return -1;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer header = new StringTokenizer(in.readLine());
        int rows = Integer.parseInt(header.nextToken());
        int columns = Integer.parseInt(header.nextToken());
        String[] scheme = new String[2 * rows + 1];
        for (int index = 0; index < scheme.length; index++) {
            scheme[index] = in.readLine();
        }
        int answer = minimumPassages(rows, columns, scheme);
        System.out.println(answer < 0 ? "Death" : Integer.toString(answer));
    }
}
