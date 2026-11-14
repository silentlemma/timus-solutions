import java.io.IOException;

public class Main {
    private static final int MAX_LINE = 100000;

    private static void erase(byte[] input, int first, int end) {
        for (int i = first; i < end; i++) {
            if (input[i] != ' ') {
                input[i] = '_';
            }
        }
    }

    private static boolean fill(byte[] input, int sourceEnd, int start, int end) {
        int[] prefix = new int[1];
        int search = 0;
        int keptUntil = 0;
        while (start < end) {
            int wordEnd = start;
            while (wordEnd < end && input[wordEnd] != ' ') {
                wordEnd++;
            }
            int length = wordEnd - start;
            // Reuse the prefix table for successive words.
            if (prefix.length < length) {
                prefix = new int[Math.max(length, 2 * prefix.length)];
            }
            int matched = 0;
            for (int i = 1; i < length; i++) {
                byte letter = input[start + i];
                while (matched > 0 && letter != input[start + matched]) {
                    matched = prefix[matched - 1];
                }
                if (letter == input[start + matched]) {
                    matched++;
                }
                prefix[i] = matched;
            }

            matched = 0;
            while (search < sourceEnd) {
                byte letter = input[search++];
                while (matched > 0 && letter != input[start + matched]) {
                    matched = prefix[matched - 1];
                }
                if (letter == input[start + matched] && ++matched == length) {
                    break;
                }
            }
            if (matched != length) {
                return false;
            }

            // Leave a separator before the next kept word and mask the gap in place.
            erase(input, keptUntil, search - length);
            keptUntil = search++;
            start = wordEnd + 1;
        }
        erase(input, keptUntil, sourceEnd);
        return true;
    }

    public static void main(String[] args) throws IOException {
        byte[] input = new byte[2 * (MAX_LINE + 2)];
        int length = 0;
        while (length < input.length) {
            int read = System.in.read(input, length, input.length - length);
            if (read < 0) {
                break;
            }
            length += read;
        }
        int firstBreak = 0;
        while (firstBreak < length && input[firstBreak] != '\n') {
            firstBreak++;
        }
        int sourceEnd = firstBreak;
        if (sourceEnd > 0 && input[sourceEnd - 1] == '\r') {
            sourceEnd--;
        }
        int targetEnd = length;
        while (targetEnd > firstBreak &&
               (input[targetEnd - 1] == '\r' || input[targetEnd - 1] == '\n')) {
            targetEnd--;
        }
        if (fill(input, sourceEnd, firstBreak + 1, targetEnd)) {
            System.out.write(input, 0, sourceEnd);
            System.out.write('\n');
            System.out.flush();
        } else {
            System.out.println("I HAVE FAILED!!!");
        }
    }
}
