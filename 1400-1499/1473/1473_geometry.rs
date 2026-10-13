use std::io::{self, Read, Write};

const CAMEL: i64 = 1;

fn gcd(mut x: i64, mut y: i64) -> i64 {
    while y != 0 {
        let t = x % y;
        x = y;
        y = t;
    }
    x
}

/// (a, b, kind): a ray from the origin, reduced by the gcd, and the kind.
type Animal = (i64, i64, i64);

fn cross(p: &Animal, q: &Animal) -> i64 {
    p.0 * q.1 - p.1 * q.0
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|x| x.parse::<i64>().unwrap());
    let n = it.next().unwrap() as usize;
    let mut animals: Vec<Animal> = Vec::with_capacity(n);
    let mut origin = false;
    for _ in 0..n {
        let (a, b, c) = (it.next().unwrap(), it.next().unwrap(), it.next().unwrap());
        let g = gcd(a, b);
        if g == 0 {
            origin = true; // nobody can judge an animal at the origin
            animals.push((a, b, c));
        } else {
            animals.push((a / g, b / g, c));
        }
    }
    if origin {
        println!("-1");
        return;
    }
    // rays by angle, counterclockwise from the A axis
    animals.sort_by(|p, q| 0.cmp(&cross(p, q)));
    let mut experts: Vec<(i64, i64)> = Vec::new();
    for w in animals.windows(2) {
        let (p, q) = (&w[0], &w[1]);
        if cross(p, q) == 0 {
            if p.2 != q.2 {
                println!("-1"); // every expert judges a whole ray alike
                return;
            }
            continue;
        }
        if p.2 == q.2 {
            continue;
        }
        // a line along p + q passes strictly between the two rays
        let (x, y) = (p.0 + q.0, p.1 + q.1);
        let g = gcd(x, y);
        let (x, y) = (x / g, y / g);
        experts.push(if p.2 == CAMEL { (y, -x) } else { (-y, x) });
    }
    if experts.len() % 2 == 0 {
        // an odd count avoids ties; one more expert votes for the first kind
        let s = if animals[0].2 == CAMEL { 1 } else { -1 };
        experts.push((s, s));
    }
    let mut out = format!("{}\n", experts.len());
    for (x, y) in experts {
        out.push_str(&format!("{} {}\n", x, y));
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
