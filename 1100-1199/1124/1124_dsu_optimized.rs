use std::io::{self, Read};

const BOXES: usize = 501;

fn number(input: &mut impl Iterator<Item = u8>) -> usize {
    let first = input.find(|byte| byte.is_ascii_digit()).unwrap();
    let mut value = usize::from(first - b'0');
    for byte in input.take_while(u8::is_ascii_digit) {
        value = value * 10 + usize::from(byte - b'0');
    }
    value
}

fn root(parent: &mut [i16; BOXES], mut node: usize) -> usize {
    while parent[node] > 0 {
        let next = parent[node] as usize;
        if parent[next] > 0 {
            parent[node] = parent[next];
        }
        node = parent[node] as usize;
    }
    node
}

fn main() {
    let stdin = io::stdin();
    let mut input = stdin.lock().bytes().map(Result::unwrap);
    let (m, n) = (number(&mut input), number(&mut input));
    // Zero means untouched. A root stores the negative size of its group.
    let mut parent = [0i16; BOXES];
    let (mut moves, mut groups) = (0, 0);
    for box_id in 1..=m {
        for _ in 0..n {
            let colour = number(&mut input);
            if colour == box_id {
                continue;
            }
            moves += 1;
            for node in [box_id, colour] {
                if parent[node] == 0 {
                    parent[node] = -1;
                    groups += 1;
                }
            }
            let (mut a, mut b) = (root(&mut parent, box_id), root(&mut parent, colour));
            if a == b {
                continue;
            }
            if parent[a] > parent[b] {
                std::mem::swap(&mut a, &mut b);
            }
            parent[a] += parent[b];
            parent[b] = a as i16;
            groups -= 1;
        }
    }
    if moves > 0 {
        moves += groups - 1;
    }
    println!("{}", moves);
}
