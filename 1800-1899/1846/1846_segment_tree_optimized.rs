use std::io::{self, Read, Write};

fn gcd(mut a: u32, mut b: u32) -> u32 {
    while b != 0 {
        let r = a % b;
        a = b;
        b = r;
    }
    a
}
fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_ascii_whitespace();
    let q: usize = words.next().unwrap().parse().unwrap();
    // x <= 10^9: signed 32-bit entries hold the operation and its value.
    let mut operations = Vec::with_capacity(q);
    let mut values = Vec::with_capacity(q);
    for _ in 0..q {
        let add = words.next().unwrap() == "+";
        let x: i32 = words.next().unwrap().parse().unwrap();
        operations.push(if add { x } else { -x });
        values.push(x);
    }
    drop(input);
    values.sort_unstable();
    values.dedup();
    let size = values.len();
    // one leaf per distinct value; counts are at most q <= 100000.
    let mut counts = vec![0u32; size];
    let mut tree = vec![0u32; 2 * size];
    let mut out = io::BufWriter::new(io::stdout().lock());
    for operation in operations {
        let x = operation.abs();
        let id = values.binary_search(&x).unwrap();
        if operation > 0 {
            counts[id] += 1;
        } else {
            counts[id] -= 1;
        }
        let mut v = size + id;
        let value = if counts[id] == 0 { 0 } else { x as u32 };
        if tree[v] != value {
            tree[v] = value;
            v /= 2;
            while v > 0 {
                let g = gcd(tree[2 * v], tree[2 * v + 1]);
                if g == tree[v] {
                    break;
                }
                tree[v] = g;
                v /= 2;
            }
        }
        writeln!(out, "{}", tree[1].max(1)).unwrap();
    }
}
