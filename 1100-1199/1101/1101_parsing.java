import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {
    // a node is OR, AND, NOT, a constant or a register, with up to two children
    static final class Node {
        final String kind;
        final Node left, right;
        final boolean value;
        final char name;

        Node(String kind, Node left, Node right, boolean value, char name) {
            this.kind = kind;
            this.left = left;
            this.right = right;
            this.value = value;
            this.name = name;
        }
    }

    static List<String> tokens = new ArrayList<>();
    static int pos = 0;

    static String peek() { return pos < tokens.size() ? tokens.get(pos) : ""; }

    // recursive descent: NOT binds tightest, OR loosest
    static Node disjunction() {
        Node node = conjunction();
        while (peek().equals("OR")) {
            pos++;
            node = new Node("OR", node, conjunction(), false, ' ');
        }
        return node;
    }

    static Node conjunction() {
        Node node = negation();
        while (peek().equals("AND")) {
            pos++;
            node = new Node("AND", node, negation(), false, ' ');
        }
        return node;
    }

    static Node negation() {
        String word = tokens.get(pos++);
        if (word.equals("NOT")) {
            return new Node("NOT", negation(), null, false, ' ');
        }
        if (word.equals("(")) {
            Node node = disjunction();
            pos++;
            return node;
        }
        if (word.equals("TRUE") || word.equals("FALSE")) {
            return new Node("CONST", null, null, word.equals("TRUE"), ' ');
        }
        return new Node("REG", null, null, false, word.charAt(0));
    }

    static boolean value(Node node, boolean[] reg) {
        switch (node.kind) {
        case "OR":
            return value(node.left, reg) || value(node.right, reg);
        case "AND":
            return value(node.left, reg) && value(node.right, reg);
        case "NOT":
            return !value(node.left, reg);
        case "CONST":
            return node.value;
        default:
            return reg[node.name - 'A'];
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String expr = in.readLine();
        for (int i = 0; i < expr.length();) {
            char c = expr.charAt(i);
            if (Character.isLetter(c)) {
                int j = i;
                while (j < expr.length() && Character.isLetter(expr.charAt(j))) {
                    j++;
                }
                tokens.add(expr.substring(i, j));
                i = j;
            } else {
                if (c == '(' || c == ')') {
                    tokens.add(String.valueOf(c));
                }
                i++;
            }
        }
        Node root = disjunction();
        StringBuilder text = new StringBuilder();
        for (String line; (line = in.readLine()) != null;) {
            text.append(line).append(' ');
        }
        StringTokenizer tok = new StringTokenizer(text.toString());
        int n = Integer.parseInt(tok.nextToken());
        int m = Integer.parseInt(tok.nextToken());
        int k = Integer.parseInt(tok.nextToken());
        Set<String> forks = new HashSet<>();
        for (int i = 0; i < m; i++) {
            forks.add(tok.nextToken() + " " + tok.nextToken());
        }
        Map<String, Character> switches = new HashMap<>();
        for (int i = 0; i < k; i++) {
            String at = tok.nextToken() + " " + tok.nextToken();
            switches.put(at, tok.nextToken().charAt(0));
        }
        boolean[] reg = new boolean['Z' - 'A' + 1];
        int x = 0, y = 0, dx = 1, dy = 0;
        StringBuilder out = new StringBuilder();
        while (-n <= x && x <= n && -n <= y && y <= n) {
            String at = x + " " + y;
            out.append(at).append('\n');
            Character name = switches.get(at);
            if (name != null) {
                reg[name - 'A'] = !reg[name - 'A'];
            }
            if (forks.contains(at)) {
                // TRUE turns right, FALSE turns left
                boolean right = value(root, reg);
                int ndx = right ? dy : -dy, ndy = right ? -dx : dx;
                dx = ndx;
                dy = ndy;
            }
            x += dx;
            y += dy;
        }
        System.out.print(out);
    }
}
