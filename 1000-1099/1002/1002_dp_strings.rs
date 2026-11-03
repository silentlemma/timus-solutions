use std::io::{self, BufRead, Write};

const MAX_WORD_LENGTH: usize = 50;
const KEYPAD: &[u8] = b"22233344115566070778889990";

fn main() {
    let stdin = io::stdin();
    let mut input = stdin.lock();
    let stdout = io::stdout();
    let mut output = io::BufWriter::new(stdout.lock());
    let mut line = String::new();
    loop {
        line.clear();
        if input.read_line(&mut line).unwrap() == 0 || line.trim() == "-1" {
            break;
        }
        let phone = line.trim().as_bytes().to_vec();
        let n = phone.len();
        line.clear();
        input.read_line(&mut line).unwrap();
        let count: usize = line.trim().parse().unwrap();
        let mut edges = vec![[0usize; 10]; n * MAX_WORD_LENGTH + 1];
        let mut words = vec![String::new(); edges.len()];
        let mut nodes = 1;
        // Only phone substrings get nodes. Stream unrelated dictionary words
        // through the same buffer instead of retaining the whole dictionary.
        for start in 0..n {
            let mut node = 0;
            for &digit in phone
                .iter()
                .take(n.min(start + MAX_WORD_LENGTH))
                .skip(start)
            {
                let d = (digit - b'0') as usize;
                if edges[node][d] == 0 {
                    edges[node][d] = nodes;
                    nodes += 1;
                }
                node = edges[node][d];
            }
        }
        for _ in 0..count {
            line.clear();
            input.read_line(&mut line).unwrap();
            let word = line.trim();
            let mut node = 0;
            for &letter in word.as_bytes() {
                node = edges[node][(KEYPAD[(letter - b'a') as usize] - b'0') as usize];
                if node == 0 {
                    break;
                }
            }
            if node != 0 && words[node].is_empty() {
                words[node] = word.to_string();
            }
        }
        let mut best = vec![n + 1; n + 1];
        let mut how = vec![0; n + 1];
        best[0] = 0;
        for start in 0..n {
            if best[start] > n {
                continue;
            }
            let mut node = 0;
            for end in start..n.min(start + MAX_WORD_LENGTH) {
                node = edges[node][(phone[end] - b'0') as usize];
                if !words[node].is_empty() && best[start] + 1 < best[end + 1] {
                    best[end + 1] = best[start] + 1;
                    how[end + 1] = node;
                }
            }
        }
        if best[n] > n {
            writeln!(output, "No solution.").unwrap();
            continue;
        }
        let mut used = Vec::new();
        let mut end = n;
        while end > 0 {
            let word = &words[how[end]];
            used.push(word.as_str());
            end -= word.len();
        }
        used.reverse();
        writeln!(output, "{}", used.join(" ")).unwrap();
    }
}
