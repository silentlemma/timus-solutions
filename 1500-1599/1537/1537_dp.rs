use std::io::{self, Read};

fn main() {
    let mut s = String::new();
    io::stdin().read_to_string(&mut s).unwrap();
    let v: Vec<u64> = s
        .split_ascii_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    let (k, p) = (v[0] as usize, v[1]);
    // an ent with w words teaches an old ent who ends with w + 1 words and a
    // young one who ends with 2w, so with g(m) ents knowing 2m (or 2m + 1)
    // words: g(1) = 1 and g(m) = g(m - 1) + g(m / 2)
    if k < 2 {
        println!("0");
        return;
    }
    let (top, half) = (k / 2, k / 2 / 2); // only g up to half is looked up again
    let mut g = vec![0u32; half + 1];
    let mut cur = 1 % p;
    if half >= 1 {
        g[1] = cur as u32;
    }
    for m in 2..=top {
        cur = (cur + g[m / 2] as u64) % p;
        if m <= half {
            g[m] = cur as u32;
        }
    }
    println!("{}", cur);
}
