use std::collections::HashMap;
use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|v| v.parse::<i64>().unwrap());
    let n = it.next().unwrap() as usize;
    let xs: Vec<i64> = (0..=n).map(|_| it.next().unwrap()).collect();
    let mut speed = vec![0i64; n];
    // (segment owning the start, x, time)
    let mut cables: Vec<(usize, i64, i64)> = Vec::new();
    for i in 0..n {
        speed[i] = it.next().unwrap();
        let m = it.next().unwrap();
        for _ in 0..m {
            let x = it.next().unwrap();
            let t = it.next().unwrap();
            // a start at the first vertex of a segment is the last point of
            // the segment before it
            let owner = if i > 0 && x == xs[i] { i - 1 } else { i };
            cables.push((owner, x, t));
        }
    }
    let mut walk = vec![0i64; n + 1];
    for i in 0..n {
        walk[i + 1] = walk[i] + speed[i] * (xs[i + 1] - xs[i]).abs();
    }
    let cost = |seg: usize, x: i64| walk[seg] + speed[seg] * (x - xs[seg]).abs();
    // every point but the foot belongs to one segment, which owns its x
    // range without its first vertex; a cable lands on the first later
    // segment owning its x, found by painting the segments from the top down
    let mut keys: Vec<i64> = cables.iter().map(|c| c.1).collect();
    keys.sort_unstable();
    keys.dedup();
    let mut size = 1;
    while size < keys.len() {
        size *= 2;
    }
    let mut paint = vec![n; 2 * size];
    let mut by_owner: Vec<Vec<usize>> = vec![Vec::new(); n];
    for (k, c) in cables.iter().enumerate() {
        by_owner[c.0].push(k);
    }
    // (walking cost, kind, start, time): kind 0 a landing, 1 a start, so
    // landings come first at one point
    let mut events: Vec<(i64, u8, i64, i64)> = Vec::with_capacity(2 * cables.len());
    for seg in (0..n).rev() {
        for &k in &by_owner[seg] {
            let (owner, x, t) = cables[k];
            // paints only go down, so the lowest segment is the latest one
            let mut land = n;
            let mut i = keys.partition_point(|&v| v < x) + size;
            while i > 0 {
                land = land.min(paint[i]);
                i /= 2;
            }
            let from = cost(owner, x);
            events.push((from, 1, 0, 0));
            events.push((cost(land, x), 0, from, t));
        }
        let (a, b) = (xs[seg], xs[seg + 1]);
        let (lo, hi) = if a < b { (a + 1, b) } else { (b, a - 1) };
        let mut l = keys.partition_point(|&v| v < lo) + size;
        let mut h = keys.partition_point(|&v| v <= hi) + size;
        while l < h {
            if l & 1 == 1 {
                paint[l] = seg;
                l += 1;
            }
            if h & 1 == 1 {
                h -= 1;
                paint[h] = seg;
            }
            l /= 2;
            h /= 2;
        }
    }
    events.sort_unstable_by_key(|e| (e.0, e.1));
    // going up, the best time at a point is its walking cost plus the least
    // (time - walking cost) over the landings so far
    let mut best: HashMap<i64, i64> = HashMap::with_capacity(cables.len());
    let mut gain = 0i64;
    for &(at, kind, start, t) in &events {
        if kind == 0 {
            gain = gain.min(best[&start] + t - at);
        } else {
            best.insert(at, at + gain);
        }
    }
    println!("{}", walk[n] + gain);
}
