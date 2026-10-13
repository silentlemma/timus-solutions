use std::io::{self, Read};

fn gcd(mut a: i32, mut b: i32) -> i32 {
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
        .map(|x| x.parse::<i32>().unwrap());
    let n = it.next().unwrap() as usize;
    let p: Vec<(i32, i32, i32)> = (0..n)
        .map(|_| (it.next().unwrap(), it.next().unwrap(), it.next().unwrap()))
        .collect();
    let mut best = 1;
    let mut dirs: Vec<(i32, i32, i32)> = Vec::with_capacity(n);
    for i in 0..n {
        if n - i <= best {
            break;
        }
        let mut same = 0;
        dirs.clear();
        for j in i + 1..n {
            let (dx, dy, dz) = (p[j].0 - p[i].0, p[j].1 - p[i].1, p[j].2 - p[i].2);
            let mut g = gcd(dx.abs(), gcd(dy.abs(), dz.abs()));
            if g == 0 {
                same += 1; // several flies may hang at one point
                continue;
            }
            // one key per direction: reduced, with the first non-zero part positive
            if dx < 0 || (dx == 0 && (dy < 0 || (dy == 0 && dz < 0))) {
                g = -g;
            }
            dirs.push((dx / g, dy / g, dz / g));
        }
        dirs.sort_unstable();
        let mut most = 0;
        let mut a = 0;
        while a < dirs.len() {
            let mut b = a;
            while b < dirs.len() && dirs[b] == dirs[a] {
                b += 1;
            }
            most = most.max(b - a);
            a = b;
        }
        best = best.max(1 + same + most);
    }
    println!("{}", best);
}
