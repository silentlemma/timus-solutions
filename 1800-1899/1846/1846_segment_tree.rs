use std::collections::HashMap;
use std::fmt::Write;
use std::io::{self, Read};

fn gcd(mut a: u32, mut b: u32) -> u32 {
    while b != 0 {
        let t = a % b;
        a = b;
        b = t;
    }
    a
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let q: usize = it.next().unwrap().parse().unwrap();
    let mut size = 1;
    while size < q {
        size *= 2;
    }
    // every addition gets its own leaf; an empty leaf holds 0, which does
    // not change a gcd
    let mut tree = vec![0u32; 2 * size];
    let mut leaves: HashMap<u32, Vec<usize>> = HashMap::new(); // value -> leaves
    let mut out = String::new();
    for k in 0..q {
        let add = it.next().unwrap() == "+";
        let x: u32 = it.next().unwrap().parse().unwrap();
        let (mut v, value) = if add {
            leaves.entry(x).or_default().push(k);
            (k + size, x)
        } else {
            (leaves.get_mut(&x).unwrap().pop().unwrap() + size, 0)
        };
        tree[v] = value;
        v /= 2;
        // once a node keeps its value, so do all above it
        while v > 0 {
            let g = gcd(tree[2 * v], tree[2 * v + 1]);
            if tree[v] == g {
                break;
            }
            tree[v] = g;
            v /= 2;
        }
        writeln!(out, "{}", if tree[1] == 0 { 1 } else { tree[1] }).unwrap();
    }
    print!("{}", out);
}
