use std::collections::HashMap;
use std::io::{self, Read};

const HALF: f64 = 0.5; // rounds to the nearest mile

fn gcd(mut a: i32, mut b: i32) -> i32 {
    while b != 0 {
        let t = a % b;
        a = b;
        b = t;
    }
    a.abs()
}

fn main() {
    let mut s = String::new();
    io::stdin().read_to_string(&mut s).unwrap();
    let v: Vec<i32> = s
        .split_ascii_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    if v.is_empty() {
        return;
    }
    let n = v[0] as usize;
    let xs: Vec<i32> = (0..n).map(|i| v[1 + 2 * i]).collect();
    let ys: Vec<i32> = (0..n).map(|i| v[2 + 2 * i]).collect();
    let mut total = 0.0f64;
    for i in 0..n {
        // the farthest city in each reduced direction from city i, in steps
        let mut far: HashMap<(i32, i32), i32> = HashMap::new();
        for j in 0..n {
            if j == i {
                continue;
            }
            let (dx, dy) = (xs[j] - xs[i], ys[j] - ys[i]);
            let g = gcd(dx, dy);
            let steps = far.entry((dx / g, dy / g)).or_insert(0);
            *steps = (*steps).max(g);
        }
        for (&(dx, dy), &steps) in &far {
            // city i ends the road in this direction when nothing lies behind it
            if !far.contains_key(&(-dx, -dy)) {
                total += steps as f64 * (dx as f64).hypot(dy as f64);
            }
        }
    }
    // every road is found from both of its ends
    println!("{}", (total / 2.0 + HALF).floor() as i64);
}
