import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

public class Main {
    static final long LIMIT = 10000000;
    static final int SET = 0, NOT = 1, CALC = 2, END = 3, PRINT = 4, GOTO = 5, IF = 6;
    // the operations and comparisons in the order of their codes
    static final int ADD = 0, SUB = 1, MUL = 2, DIV = 3, MOD = 4, OR = 5, AND = 6;
    static final int EQ = 0, NE = 1, GE = 2, GT = 3, LE = 4;
    static final List<String> CALCS = Arrays.asList("+", "-", "*", "/", "%", "or", "and", "xor");
    static final List<String> TESTS = Arrays.asList("==", "!=", ">=", ">", "<=", "<");
    static final int START = 16;

    static Map<String, Integer> names = new TreeMap<>();
    static long[] values = new long[START];
    static int count = 0;

    // operands are slots in one value table: variables and constants
    static int operand(String tok) {
        if (tok.matches("-?\\d+")) {
            return slot(Long.parseLong(tok));
        }
        Integer k = names.get(tok);
        if (k != null)
            return k;
        names.put(tok, count);
        return slot(0);
    }

    static int slot(long v) {
        if (count == values.length)
            values = Arrays.copyOf(values, 2 * count);
        values[count] = v;
        return count++;
    }

    static long calc(int code, long x, long y) {
        switch (code) {
        case ADD:
            return x + y;
        case SUB:
            return x - y;
        case MUL:
            return x * y;
        case DIV:
            return x / y; // rounds towards zero
        case MOD:
            return (x % y + Math.abs(y)) % Math.abs(y); // never negative
        case OR:
            return x | y;
        case AND:
            return x & y;
        default:
            return x ^ y;
        }
    }

    static boolean test(int code, long x, long y) {
        switch (code) {
        case EQ:
            return x == y;
        case NE:
            return x != y;
        case GE:
            return x >= y;
        case GT:
            return x > y;
        case LE:
            return x <= y;
        default:
            return x < y;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        // a line is "label:", "label: command" or "command",
        // lines with only a label are no commands
        Map<String, Integer> labels = new HashMap<>();
        List<String[]> commands = new ArrayList<>();
        for (String line; (line = in.readLine()) != null;) {
            String trimmed = line.trim();
            String[] t = trimmed.isEmpty() ? new String[0] : trimmed.split("\\s+");
            if (t.length > 0 && t[0].endsWith(":")) {
                labels.put(t[0].substring(0, t[0].length() - 1).toLowerCase(), commands.size());
                t = Arrays.copyOfRange(t, 1, t.length);
            }
            if (t.length > 0)
                commands.add(t);
        }
        int size = commands.size();
        int[] kind = new int[size], dst = new int[size], a = new int[size], b = new int[size];
        int[] target = new int[size], code = new int[size];
        for (int pc = 0; pc < size; pc++) {
            String[] t = commands.get(pc);
            String head = t[0].toLowerCase();
            if (t.length > 1 && t[1].equals("=")) {
                dst[pc] = operand(t[0]);
                // a value, "not" and a value, or a value, an operation and a value
                String[] rest = Arrays.copyOfRange(t, 2, t.length);
                if (rest.length == 1) {
                    kind[pc] = SET;
                    a[pc] = operand(rest[0]);
                } else if (rest.length == 2) {
                    kind[pc] = NOT;
                    a[pc] = operand(rest[1]);
                } else {
                    kind[pc] = CALC;
                    a[pc] = operand(rest[0]);
                    b[pc] = operand(rest[2]);
                    code[pc] = CALCS.indexOf(rest[1].toLowerCase());
                }
            } else if (head.equals("end")) {
                kind[pc] = END;
            } else if (head.equals("print")) {
                kind[pc] = PRINT;
                a[pc] = operand(t[1]);
            } else if (head.equals("goto")) {
                kind[pc] = GOTO;
                target[pc] = labels.get(t[1].toLowerCase());
            } else { // a conditional jump: two values around a comparison, then a label
                String[] rest = Arrays.copyOfRange(t, 1, t.length);
                kind[pc] = IF;
                a[pc] = operand(rest[0]);
                b[pc] = operand(rest[2]);
                code[pc] = TESTS.indexOf(rest[1]);
                target[pc] = labels.get(rest[rest.length - 1].toLowerCase());
            }
        }
        long[] v = values;
        boolean[] assigned = new boolean[count];
        StringBuilder out = new StringBuilder();
        int pc = 0;
        long executed = 0;
        boolean ended = false;
        while (pc < size && executed < LIMIT) {
            int i = pc++;
            executed++;
            switch (kind[i]) {
            case SET:
                v[dst[i]] = v[a[i]];
                assigned[dst[i]] = true;
                break;
            case NOT:
                v[dst[i]] = ~v[a[i]];
                assigned[dst[i]] = true;
                break;
            case CALC:
                v[dst[i]] = calc(code[i], v[a[i]], v[b[i]]);
                assigned[dst[i]] = true;
                break;
            case END:
                ended = true;
                pc = size;
                break;
            case PRINT:
                out.append(v[a[i]]).append('\n');
                break;
            case GOTO:
                pc = target[i];
                break;
            default:
                if (test(code[i], v[a[i]], v[b[i]]))
                    pc = target[i];
            }
        }
        if (!ended && executed == LIMIT) {
            // ten million commands done and the program still runs
            out.append("Program terminated. Variables state:\n");
            for (Map.Entry<String, Integer> e : names.entrySet())
                if (assigned[e.getValue()])
                    out.append(e.getKey()).append(": ").append(v[e.getValue()]).append('\n');
        }
        System.out.print(out);
    }
}
