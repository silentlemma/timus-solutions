use std::io::{self, Read};

const BOUND: u64 = 1_000_000; // the cube root of the largest C

fn isqrt(x: u64) -> u64 {
    let mut r = (x as f64).sqrt() as u64;
    while r * r > x {
        r -= 1;
    }
    while (r + 1) * (r + 1) <= x {
        r += 1;
    }
    r
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut c: u64 = input.trim().parse().unwrap();
    if c == 0 {
        println!("1"); // only 0 + 0
        return;
    }
    // sqrt A + sqrt B = sqrt C exactly when C = s^2 q with q square-free and
    // A = a^2 q, B = b^2 q, a + b = s; so the answer counts the pairs a <= b
    let mut root = 1u64;
    let mut d = 2u64;
    while d <= BOUND && d * d <= c {
        while c % (d * d) == 0 {
            c /= d * d;
            root *= d;
        }
        if c % d == 0 {
            c /= d;
        }
        d += 1;
    }
    // what is left has only prime factors above the bound, at most two of them,
    // so it holds a square factor only when it is a square itself
    let r = isqrt(c);
    if c > 1 && r * r == c {
        root *= r;
    }
    println!("{}", root / 2 + 1);
}
