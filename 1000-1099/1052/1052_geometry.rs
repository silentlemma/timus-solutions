use std::collections::HashMap;
use std::io::{self, Read};

fn gcd(a: i32, b: i32) -> i32 {
    let (mut a, mut b) = (a.abs(), b.abs());
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
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<i32>().unwrap());
    let n = it.next().unwrap() as usize;
    let pts: Vec<(i32, i32)> = (0..n)
        .map(|_| (it.next().unwrap(), it.next().unwrap()))
        .collect();
    let mut best = n.min(2);
    for i in 0..n {
        // the points on one line through point i have the same reduced direction
        let mut count: HashMap<(i32, i32), usize> = HashMap::new();
        for j in i + 1..n {
            let (mut dx, mut dy) = (pts[j].0 - pts[i].0, pts[j].1 - pts[i].1);
            let g = gcd(dx, dy);
            dx /= g;
            dy /= g;
            // opposite directions are the same line
            if dx < 0 || (dx == 0 && dy < 0) {
                dx = -dx;
                dy = -dy;
            }
            let c = count.entry((dx, dy)).or_insert(0);
            *c += 1;
            best = best.max(*c + 1);
        }
    }
    println!("{}", best);
}
