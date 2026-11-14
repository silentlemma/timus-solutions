use std::io::{self, Read, Write};

const MAX_CROSSINGS: usize = 30;
const GROUP_BITS: usize = 5;
const GROUPS: usize = 4;
const GROUP_SIZE: usize = 1 << GROUP_BITS;
const GROUP_MASK: usize = GROUP_SIZE - 1;
const HOME: u32 = 1;
const WORK: u32 = 2;

type Roads = [[[u32; GROUP_SIZE]; GROUPS]; MAX_CROSSINGS];

fn connects(roads: &Roads, permits: usize) -> bool {
    let a = permits & GROUP_MASK;
    let b = permits >> GROUP_BITS & GROUP_MASK;
    let c = permits >> (2 * GROUP_BITS) & GROUP_MASK;
    let d = permits >> ((GROUPS - 1) * GROUP_BITS);
    let (mut seen, mut pending) = (HOME, HOME);
    while pending != 0 {
        let row = &roads[pending.trailing_zeros() as usize];
        pending &= pending - 1;
        let fresh = (row[0][a] | row[1][b] | row[2][c] | row[GROUPS - 1][d]) & !seen;
        if fresh & WORK != 0 {
            return true;
        }
        seen |= fresh;
        pending |= fresh;
    }
    false
}

fn choose(roads: &Roads, required: usize, mut available: usize, count: u32) -> Option<usize> {
    if count == 0 {
        return connects(roads, required).then_some(required);
    }
    while available.count_ones() >= count {
        let bit = 1 << available.trailing_zeros();
        available ^= bit;
        if let Some(answer) = choose(roads, required | bit, available, count - 1) {
            return Some(answer);
        }
    }
    None
}

fn main() -> io::Result<()> {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input)?;
    let mut tokens = input
        .split_ascii_whitespace()
        .map(|token| token.parse::<usize>().unwrap());
    let categories = tokens.next().unwrap();
    let crossings = tokens.next().unwrap();
    let count = tokens.next().unwrap();
    let mut roads = [[[0; GROUP_SIZE]; GROUPS]; MAX_CROSSINGS];
    for _ in 0..count {
        let a = tokens.next().unwrap();
        let b = tokens.next().unwrap();
        let category = tokens.next().unwrap();
        let group = category / GROUP_BITS;
        let bit = 1 << (category % GROUP_BITS);
        roads[a][group][bit] |= 1 << b;
        roads[b][group][bit] |= 1 << a;
    }
    for row in &mut roads[..crossings] {
        for table in row {
            for mask in 1..GROUP_SIZE {
                let rest = mask & (mask - 1);
                table[mask] |= table[rest] | table[mask ^ rest];
            }
        }
    }

    let all = (1 << categories) - 1;
    let mut required = 0;
    // Every feasible set contains any category whose removal disconnects the route.
    for category in 0..categories {
        let bit = 1 << category;
        if !connects(&roads, all ^ bit) {
            required |= bit;
        }
    }
    let available = all ^ required;
    let answer = (0..=available.count_ones())
        .find_map(|count| choose(&roads, required, available, count))
        .unwrap();
    let mut output = io::stdout().lock();
    writeln!(output, "{}", answer.count_ones())?;
    let mut pending = answer;
    let mut separator = "";
    while pending != 0 {
        write!(output, "{separator}{}", pending.trailing_zeros())?;
        separator = " ";
        pending &= pending - 1;
    }
    writeln!(output)
}
