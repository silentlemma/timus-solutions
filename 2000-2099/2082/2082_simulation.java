import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
    private static final String[] STREETS = {"preflop", "flop", "turn", "river"};

    private static class Input {
        private final BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        private StringTokenizer tokens;

        String next() throws IOException {
            while (tokens == null || !tokens.hasMoreTokens()) {
                String line = reader.readLine();
                if (line == null) {
                    return null;
                }
                tokens = new StringTokenizer(line);
            }
            return tokens.nextToken();
        }

        int nextInt() throws IOException {
            return Integer.parseInt(next());
        }
    }

    private static class Game {
        final int[] stack;
        final int[] bet;
        final boolean[] folded;
        final boolean[] pending;
        final int dealer;
        int cursor;
        int street;
        int currentBet;

        Game(int count, int dealer) {
            stack = new int[count];
            bet = new int[count];
            folded = new boolean[count];
            pending = new boolean[count];
            this.dealer = dealer;
        }

        void resetPending() {
            for (int i = 0; i < stack.length; i++) {
                pending[i] = !folded[i] && stack[i] > 0;
            }
        }

        void act(int player, int paid, boolean fold) {
            stack[player] -= paid;
            bet[player] += paid;
            if (fold) {
                folded[player] = true;
            }
            if (bet[player] > currentBet) {
                currentBet = bet[player];
                resetPending();
            }
            pending[player] = false;
            cursor = (player + 1) % stack.length;
        }

        void deal() {
            street++;
            currentBet = 0;
            Arrays.fill(bet, 0);
            resetPending();
            cursor = (dealer + 1) % stack.length;
        }

        int nextPlayer() {
            for (int offset = 0; offset < stack.length; offset++) {
                int player = (cursor + offset) % stack.length;
                if (pending[player] && !folded[player] && stack[player] > 0) {
                    return player;
                }
            }
            return -1;
        }
    }

    public static void main(String[] args) throws IOException {
        Input input = new Input();
        String first = input.next();
        if (first == null) {
            return;
        }
        int smallBlind = Integer.parseInt(first);
        int bigBlind = input.nextInt();
        int ante = input.nextInt();
        int count = input.nextInt();
        int dealer = input.nextInt() - 1;
        int bot = input.nextInt() - 1;
        String targetName = input.next();
        int target = 0;
        for (int i = 0; i < STREETS.length; i++) {
            if (STREETS[i].equals(targetName)) {
                target = i;
            }
        }
        String[] names = new String[count];
        Map<String, Integer> indices = new HashMap<>();
        Game game = new Game(count, dealer);
        for (int i = 0; i < count; i++) {
            names[i] = input.next();
            indices.put(names[i], i);
            game.stack[i] = input.nextInt();
            game.stack[i] -= Math.min(game.stack[i], ante);
        }
        int small = count == 2 ? dealer : (dealer + 1) % count;
        int big = (small + 1) % count;
        game.bet[small] = Math.min(game.stack[small], smallBlind);
        game.stack[small] -= game.bet[small];
        game.bet[big] = Math.min(game.stack[big], bigBlind);
        game.stack[big] -= game.bet[big];
        game.currentBet = bigBlind;
        game.cursor = (big + 1) % count;
        game.resetPending();

        int known = input.nextInt();
        for (int action = 0; action < known; action++) {
            String name = input.next();
            String kind = input.next();
            if (name.equals("dealing")) {
                game.deal();
                continue;
            }
            int player = indices.get(name);
            int paid = 0;
            if (kind.equals("calls") || kind.equals("bets")) {
                paid = input.nextInt();
            } else if (kind.equals("raises")) {
                input.nextInt();
                input.next();
                paid = input.nextInt() - game.bet[player];
            }
            game.act(player, paid, kind.equals("folds"));
        }
        int[] finalStack = new int[count];
        for (int i = 0; i < count; i++) {
            finalStack[i] = input.nextInt();
        }

        List<String> answer = new ArrayList<>();
        while (true) {
            int player = game.nextPlayer();
            if (player < 0) {
                game.deal();
                answer.add("dealing " + STREETS[game.street]);
                continue;
            }
            if (player == bot && game.street == target
                    && Arrays.equals(game.stack, finalStack)) {
                break;
            }
            int paid = game.stack[player] - finalStack[player];
            // Before the next street, only the bot can spend beyond the current bet.
            if (game.street != target && player != bot) {
                paid = Math.min(paid, game.currentBet - game.bet[player]);
            }
            boolean fold = false;
            String action;
            if (paid == 0) {
                fold = game.bet[player] < game.currentBet;
                action = names[player] + (fold ? " folds" : " checks");
            } else if (game.currentBet == 0) {
                action = names[player] + " bets " + paid;
            } else if (game.bet[player] + paid > game.currentBet) {
                int total = game.bet[player] + paid;
                action = names[player] + " raises " + (total - game.currentBet) + " to " + total;
            } else {
                action = names[player] + " calls " + paid;
            }
            answer.add(action);
            game.act(player, paid, fold);
        }
        StringBuilder output = new StringBuilder();
        output.append(answer.size()).append('\n');
        for (String action : answer) {
            output.append(action).append('\n');
        }
        System.out.print(output);
    }
}
