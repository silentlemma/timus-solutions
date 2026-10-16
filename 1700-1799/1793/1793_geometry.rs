use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i64> = input.split_ascii_whitespace().map(|x| x.parse().unwrap()).collect();
    let [a, b, d, r1, top1, r2, top2, h] = v[..] else {
        return;
    };
    // the widest part of a plate inside the borders, at height min(d, h),
    // scaled by h to stay in integers
    let low = d.min(h);
    let w1 = r1 * h + (top1 - r1) * low;
    let w2 = r2 * h + (top2 - r2) * low;
    let fits = 2 * w1.max(w2) <= a.min(b) * h;
    // the centres can be this far apart along each side, and the plates
    // must be at least top1 + top2 apart, where they are widest
    let (dx, dy, need) = (a * h - w1 - w2, b * h - w1 - w2, (top1 + top2) * h);
    let apart = dx * dx + dy * dy >= need * need;
    println!("{}", if fits && apart { "YES" } else { "NO" });
}
