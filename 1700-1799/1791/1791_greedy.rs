use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|x| x.parse::<i64>().unwrap());
    // ready and last: the first and the last minute a bus may enter
    let mut ready: Vec<Vec<i64>> = Vec::new();
    let mut last: Vec<Vec<i64>> = Vec::new();
    for _ in 0..2 {
        let count = it.next().unwrap() as usize;
        let mut r = Vec::with_capacity(count);
        let mut d = Vec::with_capacity(count);
        for _ in 0..count {
            let t = it.next().unwrap();
            let p = it.next().unwrap();
            r.push(t);
            d.push(t + p - 1);
        }
        // a bus must enter before the next one on its side
        for i in (0..count.saturating_sub(1)).rev() {
            d[i] = d[i].min(d[i + 1] - 1);
        }
        ready.push(r);
        last.push(d);
    }
    let mut head = [0usize; 2];
    let mut now = 0i64;
    while head[0] < ready[0].len() || head[1] < ready[1].len() {
        // among the waiting front buses, the one with the earlier last minute
        let mut pick: Option<usize> = None;
        let mut soonest = i64::MAX;
        for s in 0..2 {
            let h = head[s];
            if h == ready[s].len() {
                continue;
            }
            soonest = soonest.min(ready[s][h]);
            let better = match pick {
                None => true,
                Some(q) => last[s][h] < last[q][head[q]],
            };
            if ready[s][h] <= now && better {
                pick = Some(s);
            }
        }
        match pick {
            None => now = soonest,
            Some(s) => {
                if now > last[s][head[s]] {
                    println!("NO");
                    return;
                }
                head[s] += 1;
                now += 1;
            }
        }
    }
    println!("YES");
}
