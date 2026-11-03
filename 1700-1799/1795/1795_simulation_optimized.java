import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int m = Integer.parseInt(in.readLine().trim());
        Map<String, Integer> ids = new HashMap<>();
        int[] stock = new int[m + 1];
        for (int id = 1; id <= m; id++) {
            StringTokenizer words = new StringTokenizer(in.readLine());
            int amount = Integer.parseInt(words.nextToken());
            words.nextToken();
            ids.put(words.nextToken(), id);
            stock[id] = amount;
        }
        int n = Integer.parseInt(in.readLine().trim());
        int[] product = new int[n], wanted = new int[n], seen = new int[n], order = new int[n];
        Arrays.fill(seen, -1);
        for (int i = 0; i < n; i++) {
            StringTokenizer words = new StringTokenizer(in.readLine());
            wanted[i] = Integer.parseInt(words.nextToken());
            words.nextToken();
            product[i] = ids.getOrDefault(words.nextToken(), 0);
            order[i] = i;
        }
        int front = 0, minutes = 0;
        while (front < n) {
            int customer = order[front], id = product[customer], left = stock[id];
            minutes++;
            if (left >= wanted[customer])
                stock[id] = left - wanted[customer];
            else if (left == seen[customer])
                stock[id] = 0;
            else if (left > 0) {
                seen[customer] = left;
                if (front + 1 == n)
                    break;
                order[front] = order[front + 1];
                order[front + 1] = customer;
                continue;
            }
            front++;
        }
        System.out.println(minutes);
    }
}
