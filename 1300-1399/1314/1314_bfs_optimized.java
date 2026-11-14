import java.io.BufferedInputStream;
import java.io.IOException;

public class Main {
    private static final int STATION_IDS = 32768;
    private static final int MAX_SEGMENTS_PER_LINE = 49;

    private static int nextInt(BufferedInputStream input) throws IOException {
        int c = input.read();
        while (c >= 0 && c <= ' ') {
            c = input.read();
        }
        boolean negative = c == '-';
        if (negative) {
            c = input.read();
        }
        int value = 0;
        while (c >= '0' && c <= '9') {
            value = value * 10 + c - '0';
            c = input.read();
        }
        return negative ? -value : value;
    }

    private static int stationIndex(short[] index, int station) {
        return station >= 0 && station < index.length ? index[station] : 0;
    }

    public static void main(String[] args) throws IOException {
        BufferedInputStream input = new BufferedInputStream(System.in);
        int lines = nextInt(input);
        int maxSegments = lines * MAX_SEGMENTS_PER_LINE;
        short[] index = new short[STATION_IDS];
        short[] firstEdge = new short[maxSegments + lines + 1];
        short[] destination = new short[2 * maxSegments + 1];
        short[] nextEdge = new short[destination.length];
        short stations = 0;
        short edges = 0;
        // Reserve index zero for unknown stations and the end of each adjacency list.
        for (int i = 0; i < lines; i++) {
            int length = nextInt(input);
            int station = nextInt(input);
            if (index[station] == 0) {
                index[station] = ++stations;
            }
            short previous = index[station];
            for (int j = 1; j < length; j++) {
                station = nextInt(input);
                if (index[station] == 0) {
                    index[station] = ++stations;
                }
                short current = index[station];
                destination[++edges] = current;
                nextEdge[edges] = firstEdge[previous];
                firstEdge[previous] = edges;
                destination[++edges] = previous;
                nextEdge[edges] = firstEdge[current];
                firstEdge[current] = edges;
                previous = current;
            }
        }

        int length = nextInt(input);
        int start = stationIndex(index, nextInt(input));
        if (start == 0) {
            return;
        }
        int last = start;
        for (int i = 1; i < length; i++) {
            int current = stationIndex(index, nextInt(input));
            int edge = firstEdge[last];
            while (edge != 0 && destination[edge] != current) {
                edge = nextEdge[edge];
            }
            if (edge == 0) {
                return;
            }
            last = current;
        }

        short[] layer = new short[stations + 1];
        short[] queue = new short[stations];
        int tail = 1;
        layer[start] = 1;
        queue[0] = (short)start;
        for (int head = 0; head < tail; head++) {
            int station = queue[head];
            for (int edge = firstEdge[station]; edge != 0; edge = nextEdge[edge]) {
                short next = destination[edge];
                if (layer[next] == 0) {
                    layer[next] = (short)(layer[station] + 1);
                    queue[tail++] = next;
                }
            }
        }
        if (layer[last] != length) {
            return;
        }

        // BFS order visits every possible predecessor before its successors.
        boolean[] possible = new boolean[stations + 1];
        possible[last] = true;
        for (int i = 0; i < tail; i++) {
            int station = queue[i];
            if (possible[station]) {
                for (int edge = firstEdge[station]; edge != 0; edge = nextEdge[edge]) {
                    int next = destination[edge];
                    if (layer[next] == layer[station] + 1) {
                        possible[next] = true;
                    }
                }
            }
        }

        StringBuilder output = new StringBuilder();
        for (int station = 0; station < index.length; station++) {
            if (possible[index[station]]) {
                output.append(station).append('\n');
            }
        }
        System.out.print(output);
    }
}
