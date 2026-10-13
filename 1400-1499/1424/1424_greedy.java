import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.StreamTokenizer;
import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) throws IOException {
        StreamTokenizer in =
            new StreamTokenizer(new BufferedReader(new InputStreamReader(System.in)));
        in.nextToken();
        int n = (int)in.nval;
        in.nextToken();
        int m = (int)in.nval;
        in.nextToken();
        int k = (int)in.nval;
        in.nextToken();
        int price = (int)in.nval;
        List<List<Integer>> starts = new ArrayList<>();
        for (int i = 0; i <= n; i++)
            starts.add(new ArrayList<>());
        int[] finish = new int[k + 1], ends = new int[n + 1];
        for (int i = 1; i <= k; i++) {
            in.nextToken();
            int s = (int)in.nval;
            in.nextToken();
            finish[i] = (int)in.nval;
            starts.get(s).add(i);
        }
        boolean[] taken = new boolean[k + 1];
        // riders by the farthest stop first
        PriorityQueue<Integer> onBoard =
            new PriorityQueue<>((a, b) -> Integer.compare(finish[b], finish[a]));
        int riding = 0;
        for (int stop = 1; stop <= n; stop++) {
            riding -= ends[stop];
            for (int i : starts.get(stop)) {
                taken[i] = true;
                onBoard.add(i);
                ends[finish[i]]++;
                riding++;
            }
            // too many: drop whoever would ride the longest
            while (riding > m) {
                int i = onBoard.poll();
                taken[i] = false;
                ends[finish[i]]--;
                riding--;
            }
        }
        StringBuilder list = new StringBuilder();
        long count = 0;
        for (int i = 1; i <= k; i++)
            if (taken[i]) {
                if (count++ > 0)
                    list.append(' ');
                list.append(i);
            }
        System.out.println(count * price);
        System.out.println(list);
    }
}
