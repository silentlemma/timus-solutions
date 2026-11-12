use std::io::{self, Read, Write};

const MAX_ALPHABET: usize = 50;
const MAX_STATES: usize = 101;
const BYTE_VALUES: usize = 256;
const INPUT_SIZE: usize = 512;
const OUTPUT_SIZE: usize = 128;
const LIMB_COUNT: usize = 10;
const LIMB_BASE: u64 = 1_000_000_000;
type Big = [u32; LIMB_COUNT];

struct Input<R: Read> {
    stream: R,
    bytes: [u8; INPUT_SIZE],
    position: usize,
    length: usize,
}

impl<R: Read> Input<R> {
    fn next(&mut self) -> u8 {
        if self.position == self.length {
            self.length = self.stream.read(&mut self.bytes).unwrap();
            self.position = 0;
            if self.length == 0 {
                return 0;
            }
        }
        let c = self.bytes[self.position];
        self.position += 1;
        c
    }

    fn start(&mut self) -> u8 {
        let mut c = self.next();
        while c != 0 && c <= b' ' {
            c = self.next();
        }
        c
    }

    fn number(&mut self) -> usize {
        let mut c = self.start();
        let mut value = 0;
        while c.is_ascii_digit() {
            value = value * 10 + (c - b'0') as usize;
            c = self.next();
        }
        value
    }
}

#[derive(Clone, Copy)]
struct Node {
    next: [u8; MAX_ALPHABET],
    fail: u8,
    degree: u8,
    bad: bool,
}

impl Node {
    const fn new() -> Self {
        Self {
            next: [0; MAX_ALPHABET],
            fail: 0,
            degree: 0,
            bad: false,
        }
    }
}

fn add(destination: &mut Big, source: &Big, weight: u8) {
    let mut carry = 0;
    for (digit, &other) in destination.iter_mut().zip(source.iter()) {
        let value = u64::from(*digit) + u64::from(other) * u64::from(weight) + carry;
        *digit = (value % LIMB_BASE) as u32;
        carry = value / LIMB_BASE;
    }
    // Each count is <=50^50<10^85, well within ten base10^9 limbs.
    assert_eq!(carry, 0);
}

fn main() {
    let stdin = io::stdin();
    let mut input = Input {
        stream: stdin.lock(),
        bytes: [0; INPUT_SIZE],
        position: 0,
        length: 0,
    };
    let (n, m, p) = (input.number(), input.number(), input.number());
    let mut index = [0_u8; BYTE_VALUES];
    let mut c = input.start();
    for letter in 0..n {
        index[c as usize] = letter as u8;
        c = input.next();
    }
    let mut nodes = [Node::new(); MAX_STATES];
    let mut states = 1;
    for _ in 0..p {
        let mut state = 0;
        c = input.start();
        while c > b' ' {
            let letter = index[c as usize] as usize;
            if nodes[state].next[letter] == 0 {
                nodes[state].next[letter] = states as u8;
                states += 1;
            }
            state = nodes[state].next[letter] as usize;
            c = input.next();
        }
        nodes[state].bad = true;
    }
    let mut queue = [0_u8; MAX_STATES];
    let mut tail = 0;
    for letter in 0..n {
        let child = nodes[0].next[letter];
        if child != 0 {
            queue[tail] = child;
            tail += 1;
        }
    }
    let mut head = 0;
    while head < tail {
        let state = queue[head] as usize;
        head += 1;
        let failure = nodes[state].fail as usize;
        nodes[state].bad |= nodes[failure].bad;
        for letter in 0..n {
            let child = nodes[state].next[letter] as usize;
            if child != 0 {
                nodes[child].fail = nodes[failure].next[letter];
                queue[tail] = child as u8;
                tail += 1;
            } else {
                nodes[state].next[letter] = nodes[failure].next[letter];
            }
        }
    }
    let mut weights = [[0_u8; MAX_ALPHABET]; MAX_STATES];
    for state in 0..states {
        if nodes[state].bad {
            continue;
        }
        let mut counts = [0_u8; MAX_STATES];
        for letter in 0..n {
            let target = nodes[state].next[letter] as usize;
            if !nodes[target].bad {
                counts[target] += 1;
            }
        }
        // Failure completion is finished before transition rows are compacted.
        for (target, &weight) in counts[..states].iter().enumerate() {
            if weight != 0 {
                let edge = nodes[state].degree as usize;
                nodes[state].next[edge] = target as u8;
                weights[state][edge] = weight;
                nodes[state].degree += 1;
            }
        }
    }
    let mut current = [[0_u32; LIMB_COUNT]; MAX_STATES];
    let mut next = current;
    current[0][0] = 1;
    for _ in 0..m {
        next[..states].fill([0; LIMB_COUNT]);
        for state in 0..states {
            if current[state].iter().all(|&digit| digit == 0) {
                continue;
            }
            for edge in 0..nodes[state].degree as usize {
                let target = nodes[state].next[edge] as usize;
                add(&mut next[target], &current[state], weights[state][edge]);
            }
        }
        std::mem::swap(&mut current, &mut next);
    }
    let mut total = [0_u32; LIMB_COUNT];
    for value in &current[..states] {
        add(&mut total, value, 1);
    }
    let mut last = LIMB_COUNT - 1;
    while last > 0 && total[last] == 0 {
        last -= 1;
    }
    let mut output = [0_u8; OUTPUT_SIZE];
    let mut used = 0;
    for limb in (0..=last).rev() {
        let mut divisor = LIMB_BASE / 10;
        if limb == last {
            while divisor > 1 && divisor > u64::from(total[limb]) {
                divisor /= 10;
            }
        }
        while divisor > 0 {
            output[used] = b'0' + (u64::from(total[limb]) / divisor % 10) as u8;
            used += 1;
            divisor /= 10;
        }
    }
    output[used] = b'\n';
    io::stdout().write_all(&output[..used + 1]).unwrap();
}
