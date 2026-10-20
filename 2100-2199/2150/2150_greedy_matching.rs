use std::fmt::Write as FmtWrite;
use std::io::{self, Read, Write};

const TRIANGLE_SIZE: usize = 3;

struct Scanner {
    data: Vec<u8>,
    pos: usize,
}

impl Scanner {
    fn next_int(&mut self) -> usize {
        while self.pos < self.data.len() && self.data[self.pos].is_ascii_whitespace() {
            self.pos += 1;
        }
        let mut value = 0;
        while self.pos < self.data.len() && self.data[self.pos].is_ascii_digit() {
            value = value * 10 + usize::from(self.data[self.pos] - b'0');
            self.pos += 1;
        }
        value
    }
}

fn main() {
    let mut data = Vec::new();
    io::stdin().read_to_end(&mut data).unwrap();
    let mut input = Scanner { data, pos: 0 };
    let n = input.next_int();
    let mut adj = vec![vec![false; n]; n];
    for row in &mut adj {
        for edge in row {
            *edge = input.next_int() == 1;
        }
    }

    let mut used = vec![false; n];
    let mut pairs = Vec::with_capacity(n / 2);
    for u in 0..n {
        if used[u] {
            continue;
        }
        for v in 0..n {
            if !used[v] && adj[u][v] {
                used[u] = true;
                used[v] = true;
                pairs.push([u, v]);
                break;
            }
        }
    }

    let unmatched: Vec<usize> = (0..n).filter(|&u| !used[u]).collect();
    for vertices in unmatched.chunks_exact(2) {
        let u = vertices[0];
        let v = vertices[1];
        // Two unmatched vertices always admit an augmentation through one pair.
        for j in 0..pairs.len() {
            let [a, b] = pairs[j];
            if adj[u][a] && adj[v][b] {
                pairs[j] = [u, a];
                pairs.push([v, b]);
                break;
            }
            if adj[u][b] && adj[v][a] {
                pairs[j] = [u, b];
                pairs.push([v, a]);
                break;
            }
        }
    }

    let mut triangle = None;
    let mut extra = 0;
    if unmatched.len() % 2 == 1 {
        extra = *unmatched.last().unwrap();
        triangle = pairs
            .iter()
            .position(|&[a, b]| adj[extra][a] && adj[extra][b]);
    }

    let mut output = String::new();
    writeln!(output, "YES\n{}", pairs.len()).unwrap();
    for (i, &[a, b]) in pairs.iter().enumerate() {
        if triangle == Some(i) {
            writeln!(
                output,
                "{} {} {} {}",
                TRIANGLE_SIZE,
                a + 1,
                b + 1,
                extra + 1
            )
            .unwrap();
        } else {
            writeln!(output, "2 {} {}", a + 1, b + 1).unwrap();
        }
    }
    io::stdout().write_all(output.as_bytes()).unwrap();
}
