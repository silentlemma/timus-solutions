use std::io::{self, Read};

const UPPER_COUNT: usize = 26;

#[derive(Default)]
struct Node {
    next: [usize; 2],
    fail: usize,
    terminal: bool,
}

fn symbol_index(letter: u8) -> usize {
    if letter <= b'Z' {
        (letter - b'A') as usize
    } else {
        (letter - b'a') as usize + UPPER_COUNT
    }
}

fn solve(input: &str) -> i32 {
    let mut tokens = input.split_ascii_whitespace();
    let k: usize = tokens.next().unwrap().parse().unwrap();
    let message = tokens.next().unwrap().as_bytes();
    let codes: Vec<&[u8]> = tokens.take(k).map(str::as_bytes).collect();
    let mut singletons = 0;
    let mut good = b'0';
    let mut capacity = 1;
    for code in &codes {
        capacity += code.len();
        if code.len() == 1 {
            singletons += 1;
            good = code[0];
        }
    }
    if singletons == 0 {
        return message
            .iter()
            .map(|&letter| codes[symbol_index(letter)].len() as i32)
            .sum();
    }
    if singletons == 2 {
        return -1;
    }

    let bad = b'0' + b'1' - good;
    let mut weights = vec![0; k];
    let mut reversed = vec![Vec::new(); k];
    let mut nodes = Vec::with_capacity(capacity);
    nodes.push(Node::default());
    for (symbol, code) in codes.iter().enumerate() {
        let mut state = 0;
        for &bit in code.iter().rev() {
            reversed[symbol].push(bit);
            if bit == bad {
                weights[symbol] += 1;
            }
            let edge = (bit - b'0') as usize;
            if nodes[state].next[edge] == 0 {
                nodes[state].next[edge] = nodes.len();
                nodes.push(Node::default());
            }
            state = nodes[state].next[edge];
        }
        nodes[state].terminal = true;
    }
    let total_bad: i32 = message
        .iter()
        .map(|&letter| weights[symbol_index(letter)])
        .sum();
    if total_bad == 0 {
        return -1;
    }

    let mut queue = Vec::with_capacity(nodes.len());
    for bit in 0..2 {
        if nodes[0].next[bit] != 0 {
            queue.push(nodes[0].next[bit]);
        }
    }
    let mut head = 0;
    while head < queue.len() {
        let state = queue[head];
        head += 1;
        let fallback = nodes[state].fail;
        nodes[state].terminal |= nodes[fallback].terminal;
        for bit in 0..2 {
            let child = nodes[state].next[bit];
            if child == 0 {
                nodes[state].next[bit] = nodes[fallback].next[bit];
            } else {
                nodes[child].fail = nodes[fallback].next[bit];
                queue.push(child);
            }
        }
    }

    // Cache complete codeword transitions instead of expanding the message.
    let mut cache = vec![0; nodes.len() * k];
    let mut state = 0;
    let mut tail_bad = 0;
    for &letter in message.iter().rev() {
        let symbol = symbol_index(letter);
        let key = state * k + symbol;
        let mut edge = cache[key];
        if edge == 0 {
            let mut target = state;
            let mut consumed = 0;
            for &bit in &reversed[symbol] {
                if bit == bad {
                    consumed += 1;
                }
                target = nodes[target].next[(bit - b'0') as usize];
                if !nodes[target].terminal {
                    edge = -consumed;
                    break;
                }
            }
            if edge == 0 {
                edge = target as i32 + 1;
            }
            cache[key] = edge;
        }
        if edge < 0 {
            return total_bad - tail_bad + edge + 1;
        }
        state = (edge - 1) as usize;
        tail_bad += weights[symbol];
    }
    -1
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    println!("{}", solve(&input));
}
