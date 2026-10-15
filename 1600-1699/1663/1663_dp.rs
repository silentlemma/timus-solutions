use std::io::{self, Read};

const TOLL: i64 = 1000;

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let v: Vec<i64> = text.split_ascii_whitespace().map(|w| w.parse().unwrap()).collect();
    let n = v[0] as usize;
    let people = &v[1..=n];
    if n == 2 {
        println!("1 2");
        return;
    }
    let mut order: Vec<usize> = (0..n).collect();
    order.sort_by_key(|&i| people[i]);
    let p: Vec<i64> = order.iter().map(|&i| people[i]).collect();
    let q: Vec<i64> = p.iter().map(|&x| TOLL / x).collect();
    // towns sorted by size: the best tour climbs to the last town on one path
    // and comes back on the other; up[j] costs a climb ending at the newest
    // town and a return ending at town j, down[j] the other way round
    let mut up = vec![q[0] * p[1]];
    let mut down = vec![q[1] * p[0]];
    let (mut shift_up, mut shift_down) = (0i64, 0i64);
    let (mut from_down, mut from_up) = (vec![0usize, 0], vec![0usize, 0]);
    for m in 1..n - 2 {
        let nxt = m + 1;
        let best_up = (0..m).min_by_key(|&j| down[j] + q[j] * p[nxt]).unwrap();
        let best_down = (0..m).min_by_key(|&j| up[j] + q[nxt] * p[j]).unwrap();
        let new_up = down[best_up] + shift_down + q[best_up] * p[nxt];
        let new_down = up[best_down] + shift_up + q[nxt] * p[best_down];
        shift_up += q[m] * p[nxt];
        shift_down += q[nxt] * p[m];
        up.push(new_up - shift_up);
        down.push(new_down - shift_down);
        from_down.push(best_up);
        from_up.push(best_down);
    }
    let (last, mut m) = (n - 1, n - 2);
    let (mut climbing, mut j, mut best) = (true, 0, i64::MAX);
    for k in 0..m {
        let close_up = up[k] + shift_up + q[m] * p[last] + q[last] * p[k];
        let close_down = down[k] + shift_down + q[k] * p[last] + q[last] * p[m];
        if close_up < best {
            best = close_up;
            climbing = true;
            j = k;
        }
        if close_down < best {
            best = close_down;
            climbing = false;
            j = k;
        }
    }
    // walk back: town m is on the climbing path or not, the other path ends at j
    let mut on_up = vec![false; n];
    while m >= 1 {
        on_up[m] = climbing;
        if j == m - 1 {
            j = if climbing { from_down[m] } else { from_up[m] };
            climbing = !climbing;
        }
        m -= 1;
    }
    let mut tour = vec![0];
    tour.extend((1..n - 1).filter(|&k| on_up[k]));
    tour.push(n - 1);
    tour.extend((1..n - 1).rev().filter(|&k| !on_up[k]));
    let tour: Vec<usize> = tour.iter().map(|&k| order[k]).collect();
    let start = tour.iter().position(|&t| t == 0).unwrap();
    let words: Vec<String> = (0..n).map(|i| (tour[(start + i) % n] + 1).to_string()).collect();
    println!("{}", words.join(" "));
}
