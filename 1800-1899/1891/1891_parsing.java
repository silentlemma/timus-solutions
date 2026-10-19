import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class Main {
    private static final int CALL_PREFIX = 3;

    private static String signature(String name, String[] types, int from, int until) {
        StringBuilder result = new StringBuilder(name).append(':');
        for (int i = from; i < until; ++i) {
            result.append(types[i]).append(',');
        }
        return result.toString();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int functionCount = Integer.parseInt(input.readLine());
        Map<String, String> functions = new HashMap<>();
        for (int i = 0; i < functionCount; ++i) {
            String[] tokens = input.readLine().split("[^A-Za-z]+");
            String key = signature(tokens[0], tokens, 1, tokens.length - 1);
            functions.put(key, tokens[tokens.length - 1]);
        }
        int lineCount = Integer.parseInt(input.readLine());
        Map<String, String> variables = new HashMap<>();
        StringBuilder inferred = new StringBuilder();
        for (int number = 1; number <= lineCount; ++number) {
            String[] tokens = input.readLine().split("[^A-Za-z]+");
            String declared = tokens[0];
            String name = tokens[1];
            String error = null;
            String[] argumentTypes = new String[tokens.length - CALL_PREFIX];
            if (variables.containsKey(name)) {
                error = "Double declaration";
            } else {
                for (int i = CALL_PREFIX; i < tokens.length; ++i) {
                    String type = variables.get(tokens[i]);
                    if (type == null) {
                        error = "Unknown variable";
                        break;
                    }
                    argumentTypes[i - CALL_PREFIX] = type;
                }
            }
            if (error == null) {
                String key = signature(tokens[2], argumentTypes, 0, argumentTypes.length);
                String result = functions.get(key);
                if (result == null) {
                    error = "No such function";
                } else if (!declared.equals("auto") && !declared.equals(result)) {
                    error = "Invalid initialization";
                } else {
                    variables.put(name, result);
                    if (declared.equals("auto")) {
                        inferred.append(name).append(" : ").append(result).append('\n');
                    }
                }
            }
            if (error != null) {
                System.out.println("Error on line " + number + ": " + error);
                return;
            }
        }
        System.out.print(inferred);
    }
}
