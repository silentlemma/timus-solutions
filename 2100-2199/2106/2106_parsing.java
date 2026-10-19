import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
    private static final int INTEGER_TYPE = -1;
    private static final int STRING_TYPE = -2;
    private static final int INTEGER_SIZE = 4;
    private static final int BYTE_BASE = 256;
    private static final int BYTE_MASK = BYTE_BASE - 1;
    private static final int HEX_BASE = 16;
    private static final int HEX_DIGITS_PER_BYTE = 2;

    private static final class Structure {
        private final String name;
        private final ArrayList<Integer> fields = new ArrayList<Integer>();

        private Structure(String name) {
            this.name = name;
        }
    }

    private static final class BinaryReader {
        private final byte[] data;
        private int offset;

        private BinaryReader(String encoded) {
            data = new byte[encoded.length() / HEX_DIGITS_PER_BYTE];
            for (int i = 0; i < data.length; i++) {
                int start = i * HEX_DIGITS_PER_BYTE;
                int high = Character.digit(encoded.charAt(start), HEX_BASE);
                int low = Character.digit(encoded.charAt(start + 1), HEX_BASE);
                data[i] = (byte) (high * HEX_BASE + low);
            }
        }

        private long integer() {
            long value = 0;
            for (int i = 0; i < INTEGER_SIZE; i++) {
                value = value * BYTE_BASE + (data[offset++] & BYTE_MASK);
            }
            return value;
        }

        private String text() {
            int length = (int) integer();
            StringBuilder result = new StringBuilder(length);
            for (int i = 0; i < length; i++) {
                result.append((char) (data[offset++] & BYTE_MASK));
            }
            return result.toString();
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer header = new StringTokenizer(input.readLine());
        int typeCount = Integer.parseInt(header.nextToken());
        int lineCount = Integer.parseInt(header.nextToken());
        Structure[] types = new Structure[typeCount];
        Map<String, Integer> typeIDs = new HashMap<String, Integer>();
        int current = -1;
        for (int line = 0; line < lineCount; line++) {
            StringTokenizer parts = new StringTokenizer(input.readLine());
            String first = parts.nextToken();
            if (first.equals("struct")) {
                String name = parts.nextToken();
                current++;
                types[current] = new Structure(name);
                typeIDs.put(name, current);
            } else if (first.equals("int")) {
                types[current].fields.add(INTEGER_TYPE);
            } else if (first.equals("string")) {
                types[current].fields.add(STRING_TYPE);
            } else {
                types[current].fields.add(typeIDs.get(first));
            }
        }

        BinaryReader reader = new BinaryReader(input.readLine().trim());
        StringBuilder output = new StringBuilder();
        int[] stackTypes = new int[typeCount];
        int[] stackNext = new int[typeCount];
        while (reader.offset < reader.data.length) {
            int root = (int) reader.integer() - 1;
            output.append(types[root].name).append('\n');
            stackTypes[0] = root;
            stackNext[0] = 0;
            int depth = 1;
            while (depth > 0) {
                int top = depth - 1;
                Structure type = types[stackTypes[top]];
                if (stackNext[top] == type.fields.size()) {
                    depth--;
                    continue;
                }
                int fieldType = type.fields.get(stackNext[top]++);
                for (int i = 0; i < depth; i++) {
                    output.append(' ');
                }
                if (fieldType == INTEGER_TYPE) {
                    output.append("int ").append(reader.integer());
                } else if (fieldType == STRING_TYPE) {
                    output.append("string ").append(reader.text());
                } else {
                    output.append(types[fieldType].name);
                    stackTypes[depth] = fieldType;
                    stackNext[depth] = 0;
                    depth++;
                }
                output.append('\n');
            }
        }
        System.out.print(output.toString());
    }
}
