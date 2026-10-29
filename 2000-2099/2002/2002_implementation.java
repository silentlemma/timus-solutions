import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
    static class Account {
        String password;
        boolean online;
        Account(String value) {
            password = value;
            online = false;
        }
    }
    static List<String> process(List<String[]> commands) {
        Map<String, Account> accounts = new HashMap<>();
        List<String> replies = new ArrayList<>();
        for (String[] command : commands) {
            String action = command[0], name = command[1], reply;
            Account account = accounts.get(name);
            if (action.equals("register")) {
                if (account != null)
                    reply = "fail: user already exists";
                else {
                    accounts.put(name, new Account(command[2]));
                    reply = "success: new user added";
                }
            } else if (action.equals("login")) {
                if (account == null)
                    reply = "fail: no such user";
                else if (!account.password.equals(command[2]))
                    reply = "fail: incorrect password";
                else if (account.online)
                    reply = "fail: already logged in";
                else {
                    account.online = true;
                    reply = "success: user logged in";
                }
            } else {
                if (account == null)
                    reply = "fail: no such user";
                else if (!account.online)
                    reply = "fail: already logged out";
                else {
                    account.online = false;
                    reply = "success: user logged out";
                }
            }
            replies.add(reply);
        }
        return replies;
    }
    static List<String[]> readCommands(BufferedReader input, int count) throws IOException {
        List<String[]> commands = new ArrayList<>();
        for (int i = 0; i < count; i++) {
            StringTokenizer tokens = new StringTokenizer(input.readLine());
            String action = tokens.nextToken(), name = tokens.nextToken();
            commands.add(action.equals("logout") ? new String[] {action, name}
                                                 : new String[] {action, name, tokens.nextToken()});
        }
        return commands;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int count = Integer.parseInt(input.readLine().trim());
        StringBuilder out = new StringBuilder();
        for (String reply : process(readCommands(input, count)))
            out.append(reply).append('\n');
        System.out.print(out);
    }
}
