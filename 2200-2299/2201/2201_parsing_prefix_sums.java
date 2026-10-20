import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.nio.charset.StandardCharsets;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
    private static final String ADMIN = "admin";
    private static final int MAX_EXPONENT = 30;

    // A^g = B^f exactly when both are powers of one root with matching
    // exponents; a base of 1 contributes nothing.
    private static boolean related = true;
    private static long scaleGood;
    private static long scaleFun;

    /** Writes value as root^exponent with the largest possible exponent. */
    private static long[] perfectPower(long value) {
        for (int exponent = MAX_EXPONENT; exponent > 1; exponent--) {
            long guess = Math.round(Math.pow(value, 1.0 / exponent));
            for (long root = Math.max(2, guess - 1); root <= guess + 1; root++) {
                long power = 1;
                for (int i = 0; i < exponent && power <= value; i++) {
                    power *= root;
                }
                if (power == value) {
                    return new long[] {root, exponent};
                }
            }
        }
        return new long[] {value, 1};
    }

    private static final class Player {
        int good;
        int fun;
        boolean online;
    }

    private static void missing(StringBuilder output, String name) {
        output.append("Failed: ").append(name).append(" is not on the server\n");
    }

    private static void compare(StringBuilder output, String firstName, Player first,
            String secondName, Player second, boolean explicitPair, double logGood,
            double logFun) {
        if (first == null || !first.online) {
            missing(output, firstName);
            return;
        }
        if (second == null || !second.online) {
            missing(output, secondName);
            return;
        }
        // The common broadcast totals cancel for two players who are online.
        long good = first.good - second.good;
        long fun = first.fun - second.fun;
        boolean equal = related ? good * scaleGood == fun * scaleFun : good == 0 && fun == 0;
        if (equal && explicitPair) {
            output.append("Their luck is equal\n");
        } else if (equal) {
            output.append(secondName).append(" is good\n");
        } else if (good * logGood - fun * logFun > 0) {
            output.append(secondName).append(" is a loser\n");
        } else {
            output.append(secondName).append(" is a lucky guy\n");
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(
                new InputStreamReader(System.in, StandardCharsets.US_ASCII));
        BufferedWriter answer = new BufferedWriter(
                new OutputStreamWriter(System.out, StandardCharsets.US_ASCII));
        StringTokenizer header = new StringTokenizer(input.readLine());
        int commands = Integer.parseInt(header.nextToken());
        header.nextToken();
        int multiplier = Integer.parseInt(header.nextToken());
        int divisor = Integer.parseInt(header.nextToken());
        double logGood = Math.log(multiplier);
        double logFun = Math.log(divisor);
        scaleGood = multiplier > 1 ? 1 : 0;
        scaleFun = divisor > 1 ? 1 : 0;
        if (multiplier > 1 && divisor > 1) {
            long[] goodRoot = perfectPower(multiplier);
            long[] funRoot = perfectPower(divisor);
            related = goodRoot[0] == funRoot[0];
            scaleGood = goodRoot[1];
            scaleFun = funRoot[1];
        }
        Map<String, Player> players = new HashMap<>();
        Player admin = new Player();
        admin.online = true;
        players.put(ADMIN, admin);
        int online = 1;
        int globalGood = 0;
        int globalFun = 0;
        StringBuilder output = new StringBuilder();

        for (int index = 0; index < commands; index++) {
            String line = input.readLine();
            int nameStart = line.indexOf(' ') + 1;
            int nameEnd = line.indexOf(':', nameStart);
            String authorName = line.substring(nameStart, nameEnd);
            Player author = players.get(authorName);
            int commandStart = line.indexOf('/', nameEnd) + 1;
            char command = line.charAt(commandStart);

            if (command == 'j') {
                if (author == null) {
                    author = new Player();
                    players.put(authorName, author);
                }
                if (author.online) {
                    output.append("Failed: ").append(authorName)
                            .append(" is already on the server\n");
                } else {
                    author.good -= globalGood;
                    author.fun -= globalFun;
                    author.online = true;
                    online++;
                    output.append("Successful\n");
                }
            } else if (command == 'q') {
                author.good += globalGood;
                author.fun += globalFun;
                author.online = false;
                online--;
                output.append("Successful\n");
            } else if (command == 'o') {
                output.append("There are ").append(online)
                        .append(" players on the server\n");
            } else if (command == 'c') {
                if (!authorName.equals(ADMIN)) {
                    output.append("Failed: you have no such rights\n");
                    answer.write(output.toString());
                    output.setLength(0);
                    continue;
                }
                int firstStart = line.indexOf('<', commandStart) + 1;
                int firstEnd = line.indexOf('>', firstStart);
                String firstName = line.substring(firstStart, firstEnd);
                int secondStart = line.indexOf('<', firstEnd);
                if (secondStart < 0) {
                    compare(output, ADMIN, admin, firstName, players.get(firstName), false,
                            logGood, logFun);
                } else {
                    secondStart++;
                    int secondEnd = line.indexOf('>', secondStart);
                    String secondName = line.substring(secondStart, secondEnd);
                    compare(output, firstName, players.get(firstName), secondName,
                            players.get(secondName), true, logGood, logFun);
                }
            } else {
                int messageStart = line.indexOf(' ', commandStart);
                String message = messageStart < 0 ? "" : line.substring(messageStart + 1);
                int good = 0;
                int fun = 0;
                for (int position = 0; position < message.length(); position += 2) {
                    if (message.charAt(position) == 'g') {
                        good++;
                    } else {
                        fun++;
                    }
                }
                output.append(authorName);
                if (command == 's') {
                    globalGood += good;
                    globalFun += fun;
                    author.good -= good;
                    author.fun -= fun;
                } else {
                    int recipientStart = line.indexOf('<', commandStart) + 1;
                    int recipientEnd = line.indexOf('>', recipientStart);
                    String recipientName = line.substring(recipientStart, recipientEnd);
                    Player recipient = players.get(recipientName);
                    if (recipient != null && recipient.online) {
                        recipient.good += good;
                        recipient.fun += fun;
                    }
                    output.append(" (to ").append(recipientName).append(')');
                }
                output.append(": ").append(message).append('\n');
            }
            answer.write(output.toString());
            output.setLength(0);
        }
        answer.flush();
    }
}
