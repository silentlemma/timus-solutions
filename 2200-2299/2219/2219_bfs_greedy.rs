use std::fmt::Write as FmtWrite;
use std::io::{self, Read, Write};

struct Scanner {
    data: Vec<u8>,
    position: usize,
}

impl Scanner {
    fn next(&mut self) -> usize {
        while self.position < self.data.len() && self.data[self.position].is_ascii_whitespace() {
            self.position += 1;
        }
        let mut value = 0;
        while self.position < self.data.len() && self.data[self.position].is_ascii_digit() {
            value = value * 10 + (self.data[self.position] - b'0') as usize;
            self.position += 1;
        }
        value
    }
}

fn fill(required: &mut [i32], next: &mut [usize; 2], parity: usize, limit: i64, count: i32) {
    while next[parity] < required.len() && next[parity] as i64 <= limit {
        required[next[parity]] = count;
        next[parity] += 2;
    }
}

fn main() {
    let mut data = Vec::new();
    io::stdin().read_to_end(&mut data).unwrap();
    let mut input = Scanner { data, position: 0 };
    let n = input.next();
    let m = input.next();
    let k = input.next();
    let mut head = vec![-1_i32; n];
    let mut to = vec![0; 2 * m];
    let mut link = vec![-1_i32; 2 * m];
    for edge in (0..2 * m).step_by(2) {
        let u = input.next() - 1;
        let v = input.next() - 1;
        to[edge] = v;
        link[edge] = head[u];
        head[u] = edge as i32;
        to[edge + 1] = u;
        link[edge + 1] = head[v];
        head[v] = (edge + 1) as i32;
    }

    let mut distance = vec![-1_i32; 2 * n];
    distance[0] = 0;
    let mut queue = Vec::with_capacity(2 * n);
    queue.push(0);
    let mut front = 0;
    while front < queue.len() {
        let state = queue[front];
        front += 1;
        let vertex = state / 2;
        let parity = (state % 2) ^ 1;
        let mut edge = head[vertex];
        while edge != -1 {
            let edge_index = edge as usize;
            let next_state = 2 * to[edge_index] + parity;
            if distance[next_state] == -1 {
                distance[next_state] = distance[state] + 1;
                queue.push(next_state);
            }
            edge = link[edge_index];
        }
    }

    let mut cups: Vec<usize> = (0..k).map(|_| input.next()).collect();
    cups.sort_unstable();
    let mut prefix = vec![[-1_i64; 2]; k + 1];
    for (i, &cup) in cups.iter().enumerate() {
        prefix[i + 1] = prefix[i];
        prefix[i + 1][cup % 2] = cup as i64;
    }
    let mut required = vec![-1_i32; 2 * n];
    required[0] = 0;
    let mut next = [2, 1];
    let mut smallest = [-1_i64; 2];
    let mut sum = 0_i64;
    for count in 1..=k {
        let index = k - count;
        let cup = cups[index];
        sum += cup as i64;
        smallest[cup % 2] = cup as i64;
        let parity = (sum % 2) as usize;
        fill(&mut required, &mut next, parity, sum, count as i32);
        // An optimal sum of the other parity replaces one selected cup.
        let mut best = -1_i64;
        for removed in 0..2 {
            let added = removed ^ 1;
            if smallest[removed] != -1 && prefix[index][added] != -1 {
                best = best.max(sum - smallest[removed] + prefix[index][added]);
            }
        }
        fill(&mut required, &mut next, parity ^ 1, best, count as i32);
    }

    let mut output = String::new();
    for vertex in 0..n {
        let mut answer = -1;
        for parity in 0..2 {
            let d = distance[2 * vertex + parity];
            if d != -1 {
                let count = required[d as usize];
                if count != -1 && (answer == -1 || count < answer) {
                    answer = count;
                }
            }
        }
        if vertex != 0 {
            output.push(' ');
        }
        write!(output, "{}", answer).unwrap();
    }
    output.push('\n');
    io::stdout().write_all(output.as_bytes()).unwrap();
}
