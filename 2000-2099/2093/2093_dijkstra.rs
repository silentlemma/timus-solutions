use std::cmp::Reverse;
use std::collections::BinaryHeap;
use std::io::{self, Read};

const PERCENT_SCALE: i64 = 100;
const MAX_SLOWDOWN: i64 = 100_500;
const SNOW_LIMIT: i64 = (MAX_SLOWDOWN - 1) * PERCENT_SCALE;
const INFINITY: i64 = 1 << 62;

struct Input {
    data: Vec<u8>,
    pos: usize,
}

impl Input {
    fn next(&mut self) -> i64 {
        while self.pos < self.data.len() && self.data[self.pos].is_ascii_whitespace() {
            self.pos += 1;
        }
        let mut value = 0;
        while self.pos < self.data.len() && self.data[self.pos].is_ascii_digit() {
            value = value * 10 + i64::from(self.data[self.pos] - b'0');
            self.pos += 1;
        }
        value
    }
}

struct Arc {
    to: u32,
    road: u32,
    next: i32,
}

struct Cleaning {
    start: i64,
    finish: i64,
    road: u32,
}

fn arrival(at: i64, cleared: i64, base: i64) -> i64 {
    let departure = at.max(cleared);
    let elapsed = (departure - cleared).min(SNOW_LIMIT);
    let duration = base + (elapsed * base + PERCENT_SCALE - 1) / PERCENT_SCALE;
    departure + duration
}

fn earliest(at: i64, base: i64, events: &[Cleaning]) -> i64 {
    let mut cleared = 0;
    // Later gaps start after any feasible arrival in the current gap.
    for event in events {
        let candidate = arrival(at, cleared, base);
        if candidate <= event.start {
            return candidate;
        }
        cleared = event.finish;
    }
    arrival(at, cleared, base)
}

fn main() {
    let mut data = Vec::new();
    io::stdin().read_to_end(&mut data).unwrap();
    let mut input = Input { data, pos: 0 };
    let n = input.next() as usize;
    let m = input.next() as usize;
    let mut heads = vec![-1; n];
    let mut arcs = Vec::with_capacity(2 * m);
    let mut bases = Vec::with_capacity(m);
    for road in 0..m {
        let a = (input.next() - 1) as usize;
        let b = (input.next() - 1) as usize;
        bases.push(input.next());
        arcs.push(Arc {
            to: b as u32,
            road: road as u32,
            next: heads[a],
        });
        heads[a] = (arcs.len() - 1) as i32;
        arcs.push(Arc {
            to: a as u32,
            road: road as u32,
            next: heads[b],
        });
        heads[b] = (arcs.len() - 1) as i32;
    }
    let k = input.next() as usize;
    let mut events = Vec::with_capacity(k);
    let mut offsets = vec![0; m + 1];
    for _ in 0..k {
        let road = (input.next() - 1) as u32;
        events.push(Cleaning {
            start: input.next(),
            finish: input.next(),
            road,
        });
        offsets[road as usize + 1] += 1;
    }
    events.sort_unstable_by_key(|event| (event.road, event.start));
    for road in 0..m {
        offsets[road + 1] += offsets[road];
    }
    drop(input);
    let mut distances = vec![INFINITY; n];
    distances[0] = 0;
    let mut queue = BinaryHeap::new();
    queue.push(Reverse((0, 0)));
    while let Some(Reverse((time, vertex))) = queue.pop() {
        if time != distances[vertex] {
            continue;
        }
        if vertex == n - 1 {
            break;
        }
        let mut index = heads[vertex];
        while index >= 0 {
            let edge = &arcs[index as usize];
            let road = edge.road as usize;
            let next = earliest(time, bases[road], &events[offsets[road]..offsets[road + 1]]);
            let to = edge.to as usize;
            if next < distances[to] {
                distances[to] = next;
                queue.push(Reverse((next, to)));
            }
            index = edge.next;
        }
    }
    println!("{}", distances[n - 1]);
}
