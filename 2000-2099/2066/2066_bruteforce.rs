use std::io::{self, Read};

const ORDERS: [[usize; 3]; 6] = [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]];
const OPS: [u8; 3] = [b'+', b'-', b'*'];

fn apply(x: i32, op: u8, y: i32) -> i32 {
    match op {
        b'*' => x * y,
        b'+' => x + y,
        _ => x - y,
    }
}

// x op1 y op2 z, multiplication first
fn evaluate(x: i32, op1: u8, y: i32, op2: u8, z: i32) -> i32 {
    if op2 == b'*' && op1 != b'*' {
        apply(x, op1, y * z)
    } else {
        apply(apply(x, op1, y), op2, z)
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i32> = input.split_ascii_whitespace().map(|t| t.parse().unwrap()).collect();
    let mut best = v[0] + v[1] + v[2];
    for o in &ORDERS {
        for &a in &OPS {
            for &b in &OPS {
                best = best.min(evaluate(v[o[0]], a, v[o[1]], b, v[o[2]]));
            }
        }
    }
    println!("{}", best);
}
