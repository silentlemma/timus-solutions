import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    private static final int TRANSITIONS_PER_CHARACTER = 3;

    private static int[] palindromeRadii(String text, boolean odd) {
        int count = text.length();
        int[] radius = new int[count];
        int left = 0;
        int right = -1;
        if (odd) {
            for (int center = 0; center < count; center++) {
                int current = center > right ? 0
                    : Math.min(radius[left + right - center], right - center);
                while (center - current - 1 >= 0 && center + current + 1 < count
                    && text.charAt(center - current - 1) == text.charAt(center + current + 1)) {
                    current++;
                }
                radius[center] = current;
                if (center + current > right) {
                    left = center - current;
                    right = center + current;
                }
            }
        } else {
            for (int center = 0; center < count; center++) {
                int current = center > right ? 0
                    : Math.min(radius[left + right - center + 1], right - center + 1);
                while (center - current - 1 >= 0 && center + current < count
                    && text.charAt(center - current - 1) == text.charAt(center + current)) {
                    current++;
                }
                radius[center] = current;
                if (center + current - 1 > right) {
                    left = center - current;
                    right = center + current - 1;
                }
            }
        }
        return radius;
    }

    private static final class SuffixAutomaton {
        final int[] head;
        final int[] length;
        final int[] link;
        final int[] firstEnd;
        final int[] edgeTo;
        final int[] edgeNext;
        final byte[] edgeLetter;
        private int edges;

        int findEdge(int state, int symbol) {
            for (int edge = head[state]; edge >= 0; edge = edgeNext[edge]) {
                if (edgeLetter[edge] == symbol) {
                    return edge;
                }
            }
            return -1;
        }

        void addEdge(int state, int symbol, int destination) {
            edgeTo[edges] = destination;
            edgeLetter[edges] = (byte) symbol;
            edgeNext[edges] = head[state];
            head[state] = edges++;
        }

        SuffixAutomaton(String pattern) {
            int capacity = 2 * pattern.length();
            head = new int[capacity];
            length = new int[capacity];
            link = new int[capacity];
            firstEnd = new int[capacity];
            Arrays.fill(head, -1);
            Arrays.fill(link, -1);
            Arrays.fill(firstEnd, -1);
            int edgeCapacity = TRANSITIONS_PER_CHARACTER * pattern.length() + 1;
            edgeTo = new int[edgeCapacity];
            edgeNext = new int[edgeCapacity];
            edgeLetter = new byte[edgeCapacity];
            int states = 1;
            int last = 0;
            for (int position = 0; position < pattern.length(); position++) {
                int symbol = pattern.charAt(position) - 'a';
                int current = states++;
                length[current] = length[last] + 1;
                firstEnd[current] = position;
                int previous = last;
                int edge = -1;
                while (previous >= 0) {
                    edge = findEdge(previous, symbol);
                    if (edge >= 0) {
                        break;
                    }
                    addEdge(previous, symbol, current);
                    previous = link[previous];
                }
                if (previous < 0) {
                    link[current] = 0;
                } else {
                    int following = edgeTo[edge];
                    if (length[previous] + 1 == length[following]) {
                        link[current] = following;
                    } else {
                        int clone = states++;
                        length[clone] = length[previous] + 1;
                        link[clone] = link[following];
                        firstEnd[clone] = firstEnd[following];
                        for (int copy = head[following]; copy >= 0; copy = edgeNext[copy]) {
                            addEdge(clone, edgeLetter[copy], edgeTo[copy]);
                        }
                        while (previous >= 0) {
                            edge = findEdge(previous, symbol);
                            if (edge < 0 || edgeTo[edge] != following) {
                                break;
                            }
                            edgeTo[edge] = clone;
                            previous = link[previous];
                        }
                        link[following] = clone;
                        link[current] = clone;
                    }
                }
                last = current;
            }
        }
    }

    private static int[] findRotations(String first, String second) {
        int firstSize = first.length();
        int secondSize = second.length();
        int middleSize = firstSize - secondSize;
        String doubled = first + first;
        int[] radius = palindromeRadii(doubled, middleSize % 2 != 0);
        int half = middleSize / 2;
        int centerOffset = secondSize + half;
        boolean candidateExists = false;
        for (int start = 0; start < firstSize; start++) {
            if (radius[start + centerOffset] >= half) {
                candidateExists = true;
                break;
            }
        }
        if (!candidateExists) {
            return null;
        }
        String reversedSecond = new StringBuilder(second).reverse().toString();
        String pattern = reversedSecond + reversedSecond.substring(0, secondSize - 1);
        SuffixAutomaton automaton = new SuffixAutomaton(pattern);
        int state = 0;
        int matched = 0;
        for (int position = 0; position < firstSize + secondSize - 1; position++) {
            int symbol = doubled.charAt(position) - 'a';
            int edge = automaton.findEdge(state, symbol);
            while (state != 0 && edge < 0) {
                state = automaton.link[state];
                matched = automaton.length[state];
                edge = automaton.findEdge(state, symbol);
            }
            if (edge >= 0) {
                state = automaton.edgeTo[edge];
                matched++;
            } else {
                state = 0;
                matched = 0;
            }
            int start = position - secondSize + 1;
            if (start >= 0 && matched >= secondSize && radius[start + centerOffset] >= half) {
                int reversedStart = automaton.firstEnd[state] - secondSize + 1;
                return new int[] {start, (secondSize - reversedStart) % secondSize};
            }
        }
        return null;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        String first = input.readLine().trim();
        String second = input.readLine().trim();
        int[] answer = findRotations(first, second);
        if (answer == null) {
            System.out.println("No");
        } else {
            System.out.println("Yes");
            System.out.println((answer[0] + 1) + " " + (answer[1] + 1));
        }
    }
}
