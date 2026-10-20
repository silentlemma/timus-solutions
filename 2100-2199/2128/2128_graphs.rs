use std::io::{self, Read, Write};

struct Scanner {
    data: Vec<u8>,
    position: usize,
}

impl Scanner {
    fn next_usize(&mut self) -> usize {
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

fn main() {
    let mut data = Vec::new();
    io::stdin().read_to_end(&mut data).unwrap();
    if data.is_empty() {
        return;
    }
    let mut input = Scanner { data, position: 0 };
    let suits = input.next_usize();
    let ranks = input.next_usize();
    let rows = input.next_usize();
    let total = suits * ranks;
    let mut indegree = vec![0; total];
    let mut left = vec![-1_isize; total];
    for (card, degree) in indegree.iter_mut().enumerate() {
        if card % ranks != 0 {
            *degree = 1;
        }
    }
    for _ in 0..rows {
        let length = input.next_usize();
        let mut previous = -1_isize;
        for _ in 0..length {
            let suit = input.next_usize();
            let rank = input.next_usize();
            let card = (suit - 1) * ranks + rank - 1;
            left[card] = previous;
            if previous != -1 {
                indegree[previous as usize] += 1;
            }
            previous = card as isize;
        }
    }

    let mut queue = Vec::with_capacity(total);
    for (card, &degree) in indegree.iter().enumerate() {
        if degree == 0 {
            queue.push(card);
        }
    }
    let mut head = 0;
    while head < queue.len() {
        let card = queue[head];
        head += 1;
        // Removing a card may unlock its suit successor and its left neighbor.
        if card % ranks + 1 < ranks {
            let next = card + 1;
            indegree[next] -= 1;
            if indegree[next] == 0 {
                queue.push(next);
            }
        }
        if left[card] != -1 {
            let next = left[card] as usize;
            indegree[next] -= 1;
            if indegree[next] == 0 {
                queue.push(next);
            }
        }
    }
    let mut output = io::BufWriter::new(io::stdout().lock());
    if queue.len() != total {
        writeln!(output, "NO").unwrap();
        return;
    }
    writeln!(output, "YES").unwrap();
    for card in queue {
        writeln!(output, "{} {}", card / ranks + 1, card % ranks + 1).unwrap();
    }
}
