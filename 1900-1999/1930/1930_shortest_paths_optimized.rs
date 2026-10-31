use std::collections::VecDeque;
use std::io::{self, Read};

fn minimum_changes(adjacency: &[Vec<u16>], start: usize, target: usize) -> i32 {
    let state_count = 2 * adjacency.len();
    let mut distance = vec![state_count as i32; state_count];
    let mut settled = vec![false; state_count];
    let first = 2 * start;
    distance[first] = 0;
    distance[first + 1] = 0;
    let mut queue = VecDeque::from(vec![first, first + 1]);
    while let Some(state) = queue.pop_front() {
        if settled[state] {
            continue;
        }
        settled[state] = true;
        let (city, gear) = (state / 2, state & 1);
        if city == target {
            return distance[state];
        }
        for &encoded in &adjacency[city] {
            let next_state = usize::from(encoded);
            let cost = i32::from((next_state & 1) != gear);
            let candidate = distance[state] + cost;
            if candidate < distance[next_state] {
                distance[next_state] = candidate;
                if cost == 0 {
                    queue.push_front(next_state);
                } else {
                    queue.push_back(next_state);
                }
            }
        }
    }
    -1
}

const INPUT_BUFFER: usize = 4096;
// the refillable buffer holds only a chunk, never the complete input.
struct Reader<R> {
    input: R,
    buffer: [u8; INPUT_BUFFER],
    at: usize,
    size: usize,
}
impl<R: Read> Reader<R> {
    fn new(input: R) -> Self {
        Self {
            input,
            buffer: [0; INPUT_BUFFER],
            at: 0,
            size: 0,
        }
    }
    fn byte(&mut self) -> u8 {
        if self.at == self.size {
            self.size = self.input.read(&mut self.buffer).unwrap();
            self.at = 0;
            if self.size == 0 {
                return 0;
            }
        }
        let c = self.buffer[self.at];
        self.at += 1;
        c
    }
    fn next(&mut self) -> i32 {
        let mut c = self.byte();
        while c != 0 && c != b'-' && !c.is_ascii_digit() {
            c = self.byte();
        }
        let mut sign = 1;
        if c == b'-' {
            sign = -1;
            c = self.byte();
        }
        let mut value = 0;
        while c.is_ascii_digit() {
            value = value * 10 + i32::from(c - b'0');
            c = self.byte();
        }
        value * sign
    }
}

fn main() {
    let stdin = io::stdin();
    let mut input = Reader::new(stdin.lock());
    let mut values = std::iter::from_fn(|| Some(input.next() as usize));
    let count = values.next().unwrap();
    let roads = values.next().unwrap();
    // 2 * city + gear is at most 19999 since n <= 10000, so u16 suffices.
    let mut adjacency = vec![Vec::new(); count];
    for _ in 0..roads {
        let lower = values.next().unwrap() - 1;
        let upper = values.next().unwrap() - 1;
        adjacency[lower].push((2 * upper) as u16);
        adjacency[upper].push((2 * lower + 1) as u16);
    }
    let start = values.next().unwrap() - 1;
    let target = values.next().unwrap() - 1;
    println!("{}", minimum_changes(&adjacency, start, target));
}
