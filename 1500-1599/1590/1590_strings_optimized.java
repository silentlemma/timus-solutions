import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    static final int EDGE_FACTOR = 3; // a suffix automaton has fewer than 3N edges
    static class Automaton {
        final int[] length, link, head, target, following;
        final byte[] letter;
        int size = 1, edgeCount;

        int find(int state, byte ch) {
            // A sparse outgoing list contains at most the 26 alphabet letters.
            int edge = head[state];
            while (edge >= 0 && letter[edge] != ch)
                edge = following[edge];
            return edge;
        }

        void add(int state, byte ch, int to) {
            target[edgeCount] = to;
            following[edgeCount] = head[state];
            letter[edgeCount] = ch;
            head[state] = edgeCount++;
        }

        Automaton(byte[] text) {
            length = new int[2 * text.length + 1];
            link = new int[length.length];
            head = new int[length.length];
            target = new int[EDGE_FACTOR * text.length];
            following = new int[target.length];
            letter = new byte[target.length];
            link[0] = head[0] = -1;
            int last = 0;
            for (byte ch : text) {
                int current = size++;
                length[current] = length[last] + 1;
                head[current] = -1;
                int state = last;
                while (state >= 0 && find(state, ch) < 0) {
                    add(state, ch, current);
                    state = link[state];
                }
                if (state >= 0) {
                    int to = target[find(state, ch)];
                    if (length[state] + 1 == length[to])
                        link[current] = to;
                    else {
                        int clone = size++;
                        length[clone] = length[state] + 1;
                        link[clone] = link[to];
                        head[clone] = -1;
                        // Copy actual edges independently so subsequent
                        // redirects cannot change the original and clone alike.
                        for (int edge = head[to]; edge >= 0; edge = following[edge])
                            add(clone, letter[edge], target[edge]);
                        while (state >= 0) {
                            int edge = find(state, ch);
                            if (edge < 0 || target[edge] != to)
                                break;
                            target[edge] = clone;
                            state = link[state];
                        }
                        link[to] = link[current] = clone;
                    }
                }
                last = current;
            }
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        byte[] text = input.readLine().trim().getBytes("US-ASCII");
        Automaton a = new Automaton(text);
        long answer = 0;
        for (int v = 1; v < a.size; v++)
            answer += a.length[v] - a.length[a.link[v]];
        System.out.println(answer);
    }
}
