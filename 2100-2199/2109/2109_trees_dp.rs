use std::io::{self, Read, Write};

const BUFFER_SIZE: usize = 65536;
const DIGIT_CAPACITY: usize = 10;

struct Scanner {
    data: Vec<u8>,
    position: usize,
}

impl Scanner {
    fn next_int(&mut self) -> usize {
        while self.position < self.data.len() && self.data[self.position] <= b' ' {
            self.position += 1;
        }
        let mut value = 0;
        while self.position < self.data.len() && self.data[self.position] > b' ' {
            value = value * 10 + usize::from(self.data[self.position] - b'0');
            self.position += 1;
        }
        value
    }
}

fn find(representative: &mut [usize], mut vertex: usize) -> usize {
    while representative[vertex] != vertex {
        representative[vertex] = representative[representative[vertex]];
        vertex = representative[vertex];
    }
    vertex
}

fn main() {
    let mut data = Vec::new();
    io::stdin().read_to_end(&mut data).unwrap();
    let mut input = Scanner { data, position: 0 };
    let n = input.next_int();
    let absent = usize::MAX;
    let mut head = vec![absent; n + 1];
    let mut to = vec![0; 2 * (n - 1)];
    let mut next = vec![absent; to.len()];
    for edge in (0..to.len()).step_by(2) {
        let u = input.next_int();
        let v = input.next_int();
        to[edge] = v;
        next[edge] = head[u];
        head[u] = edge;
        to[edge + 1] = u;
        next[edge + 1] = head[v];
        head[v] = edge + 1;
    }

    let mut parent = vec![0; n + 1];
    let mut representative: Vec<usize> = (0..=n).collect();
    let mut tin = vec![absent; n + 1];
    parent[1] = 1;
    let mut order = Vec::with_capacity(n);
    let mut adjacent = vec![0; n - 1];
    let mut stack = Vec::with_capacity(2 * n);
    stack.push(1_isize);
    while let Some(event) = stack.pop() {
        if event < 0 {
            let u = (-event) as usize;
            representative[u] = parent[u];
            continue;
        }
        let u = event as usize;
        tin[u] = order.len();
        order.push(u);
        // Finished subtrees point to their nearest active ancestor.
        if u > 1 && tin[u - 1] != absent {
            adjacent[u - 2] = tin[find(&mut representative, u - 1)];
        }
        if u < n && tin[u + 1] != absent {
            adjacent[u - 1] = tin[find(&mut representative, u + 1)];
        }
        stack.push(-event);
        let mut edge = head[u];
        while edge != absent {
            let v = to[edge];
            if v != parent[u] {
                parent[v] = u;
                stack.push(v as isize);
            }
            edge = next[edge];
        }
    }

    let mut logarithm = vec![0; n + 1];
    for length in 2..=n {
        logarithm[length] = logarithm[length / 2] + 1;
    }
    let mut table = vec![adjacent];
    let mut span = 1;
    while 2 * span <= n - 1 {
        let previous = table.last().unwrap();
        let mut row = Vec::with_capacity(n - 2 * span);
        for index in 0..n - 2 * span {
            row.push(previous[index].min(previous[index + span]));
        }
        table.push(row);
        span *= 2;
    }

    let queries = input.next_int();
    let stdout = io::stdout();
    let mut output = io::BufWriter::with_capacity(BUFFER_SIZE, stdout.lock());
    let mut digits = [0_u8; DIGIT_CAPACITY];
    for _ in 0..queries {
        let left = input.next_int();
        let right = input.next_int();
        let mut answer = left;
        if left < right {
            let level = logarithm[right - left];
            let row = &table[level];
            let value = row[left - 1].min(row[right - 1 - (1 << level)]);
            answer = order[value];
        }
        let mut start = digits.len();
        loop {
            start -= 1;
            digits[start] = b'0' + (answer % 10) as u8;
            answer /= 10;
            if answer == 0 {
                break;
            }
        }
        output.write_all(&digits[start..]).unwrap();
        output.write_all(b"\n").unwrap();
    }
    output.flush().unwrap();
}
