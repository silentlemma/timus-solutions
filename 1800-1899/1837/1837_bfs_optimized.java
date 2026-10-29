import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.Arrays;
import java.util.Map;
import java.util.TreeMap;

public class Main {
    private static final int TEAM_SIZE = 3;
    private static final int MAX_NAME = 20;
    private static final int BUFFER_SIZE = 1024;
    private static final BufferedInputStream INPUT =
        new BufferedInputStream(System.in, BUFFER_SIZE);
    private static final char[] TOKEN = new char[MAX_NAME];

    // the names are read byte by byte, lighter than Scanner
    private static String next() throws IOException {
        int ch;
        do {
            ch = INPUT.read();
        } while (ch <= ' ' && ch != -1);
        int length = 0;
        while (ch > ' ') {
            TOKEN[length++] = (char)ch;
            ch = INPUT.read();
        }
        return new String(TOKEN, 0, length);
    }

    public static void main(String[] args) throws IOException {
        int teams = Integer.parseInt(next());
        int capacity = TEAM_SIZE * teams;
        TreeMap<String, Integer> ids = new TreeMap<>();
        // the teammates of each name form a linked list of edges in int arrays
        int[] first = new int[capacity];
        Arrays.fill(first, -1);
        int[] neighbor = new int[capacity * (TEAM_SIZE - 1)];
        int[] nextEdge = new int[neighbor.length];
        int edges = 0;
        int[] team = new int[TEAM_SIZE];
        for (int t = 0; t < teams; t++) {
            for (int i = 0; i < TEAM_SIZE; i++) {
                String name = next();
                Integer id = ids.get(name);
                if (id == null) {
                    id = ids.size();
                    ids.put(name, id);
                }
                team[i] = id;
            }
            for (int a : team) {
                for (int b : team) {
                    if (a != b) {
                        neighbor[edges] = b;
                        nextEdge[edges] = first[a];
                        first[a] = edges++;
                    }
                }
            }
        }
        // breadth-first search from the champion over shared teams
        int[] distance = new int[ids.size()];
        Arrays.fill(distance, -1);
        int[] queue = new int[ids.size()];
        int tail = 0;
        Integer source = ids.get("Isenbaev");
        if (source != null) {
            distance[source] = 0;
            queue[tail++] = source;
        }
        for (int head = 0; head < tail; head++) {
            int current = queue[head];
            for (int edge = first[current]; edge != -1; edge = nextEdge[edge]) {
                int next = neighbor[edge];
                if (distance[next] == -1) {
                    distance[next] = distance[current] + 1;
                    queue[tail++] = next;
                }
            }
        }
        StringBuilder out = new StringBuilder();
        for (Map.Entry<String, Integer> entry : ids.entrySet()) {
            out.append(entry.getKey()).append(' ');
            int value = distance[entry.getValue()];
            if (value == -1)
                out.append("undefined");
            else
                out.append(value);
            out.append('\n');
        }
        System.out.print(out);
    }
}
