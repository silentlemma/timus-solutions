import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    private static final int STEP = 10;
    private static final int UNREACHABLE = 10001;

    private static String plan(String good, int limit) {
        int n = good.length();
        int stride = limit + 1;
        byte[] history = new byte[((n + limit) / STEP) * stride];
        int[] costs = new int[stride];
        int[] next = new int[stride];
        int[] window = new int[stride];
        Arrays.fill(costs, 1, stride, UNREACHABLE);
        int best = n < STEP ? 0 : UNREACHABLE;
        int lastPlace = 0;
        int lastFriends = 0;
        for (int place = STEP; place <= n + limit; place += STEP) {
            int head = 0;
            int tail = 0;
            int offset = (place / STEP - 1) * stride;
            Arrays.fill(next, UNREACHABLE);
            for (int friends = 0; friends <= Math.min(limit, place); friends++) {
                // A block ending in a friend adds one to ten friends.
                int friendParent = 0;
                int friendCost = UNREACHABLE;
                if (head < tail) {
                    friendParent = window[head];
                    friendCost = costs[friendParent] + 1;
                    if (friendParent == friends - STEP) {
                        head++;
                    }
                }
                // A block ending in a conductor adds zero to nine friends.
                while (head < tail && costs[window[tail - 1]] >= costs[friends]) {
                    tail--;
                }
                window[tail++] = friends;
                int conductors = place - friends;
                if (conductors > n) {
                    continue;
                }
                int conductorParent = window[head];
                int conductorCost = UNREACHABLE;
                if (conductors != 0) {
                    conductorCost =
                        costs[conductorParent] + (good.charAt(conductors - 1) == '1' ? 1 : 0);
                }
                if (conductorCost <= friendCost) {
                    next[friends] = conductorCost;
                    history[offset + friends] = (byte)(2 * conductorParent);
                } else {
                    next[friends] = friendCost;
                    history[offset + friends] = (byte)(2 * friendParent + 1);
                }
                if (n - conductors < STEP && next[friends] < best) {
                    best = next[friends];
                    lastPlace = place;
                    lastFriends = friends;
                }
            }
            int[] previous = costs;
            costs = next;
            next = previous;
        }
        int[] inserted = new int[lastFriends];
        int write = lastFriends;
        while (lastPlace != 0) {
            int code = history[(lastPlace / STEP - 1) * stride + lastFriends];
            int parent = code / 2;
            int finedFriend = code % 2;
            if (finedFriend != 0) {
                inserted[--write] = lastPlace;
            }
            int first = lastPlace - STEP + 1;
            for (int position = first + lastFriends - parent - finedFriend - 1; position >= first;
                 position--) {
                inserted[--write] = position;
            }
            lastFriends = parent;
            lastPlace -= STEP;
        }
        StringBuilder answer = new StringBuilder();
        answer.append(best).append('\n').append(inserted.length);
        for (int position : inserted) {
            answer.append(' ').append(position);
        }
        return answer.append('\n').toString();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer header = new StringTokenizer(input.readLine());
        int n = Integer.parseInt(header.nextToken());
        int limit = Integer.parseInt(header.nextToken());
        String good = n == 0 ? "" : input.readLine().trim();
        System.out.print(plan(good, limit));
    }
}
