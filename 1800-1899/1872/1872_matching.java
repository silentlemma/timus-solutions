import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.Arrays;
import java.util.PriorityQueue;

public class Main {
    // the first index whose size is at least value
    static int lowerBound(int[] sizes, int value) {
        int lo = 0;
        int hi = sizes.length;
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (sizes[mid] < value) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return lo;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StreamTokenizer in = new StreamTokenizer(reader);
        in.nextToken();
        int n = (int) in.nval;
        int[] area = new int[n];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            area[i] = (int) in.nval;
        }
        int[] low = new int[n];
        int[] high = new int[n];
        for (int i = 0; i < n; i++) {
            in.nextToken();
            low[i] = (int) in.nval;
            in.nextToken();
            high[i] = (int) in.nval;
        }
        Integer[] order = new Integer[n];
        Integer[] byLow = new Integer[n];
        for (int i = 0; i < n; i++) {
            order[i] = i;
            byLow[i] = i;
        }
        Arrays.sort(order, (a, b) -> Integer.compare(area[a], area[b]));
        Arrays.sort(byLow, (a, b) -> Integer.compare(low[a], low[b]));
        int[] sizes = new int[n];
        for (int i = 0; i < n; i++) {
            sizes[i] = area[order[i]];
        }
        // rooms from the smallest up, each to the waiting team whose largest
        // area is the smallest
        PriorityQueue<Integer> waiting =
            new PriorityQueue<>((a, b) -> Integer.compare(high[a], high[b]));
        int[] team = new int[n];
        int at = 0;
        for (int place = 0; place < n; place++) {
            while (at < n && low[byLow[at]] <= sizes[place]) {
                waiting.add(byLow[at]);
                at++;
            }
            if (waiting.isEmpty() || high[waiting.peek()] < sizes[place]) {
                System.out.println("Let's search for another office.");
                return;
            }
            team[place] = waiting.poll();
        }
        // the team in room place takes rooms first[place] .. last[place] in
        // sorted order; another seating exists exactly when two teams could swap
        int[] first = new int[n];
        int[] last = new int[n];
        for (int p = 0; p < n; p++) {
            first[p] = lowerBound(sizes, low[team[p]]);
            last[p] = lowerBound(sizes, high[team[p]] + 1) - 1;
        }
        for (int q = 1; q < n; q++) {
            for (int p = first[q]; p < q; p++) {
                if (last[p] >= q) {
                    System.out.println("Ask Shiftman for help.");
                    return;
                }
            }
        }
        int[] room = new int[n];
        for (int p = 0; p < n; p++) {
            room[team[p]] = order[p] + 1;
        }
        StringBuilder out = new StringBuilder("Perfect!\n");
        for (int i = 0; i < n; i++) {
            out.append(room[i]).append(i + 1 < n ? ' ' : '\n');
        }
        System.out.print(out);
    }
}
