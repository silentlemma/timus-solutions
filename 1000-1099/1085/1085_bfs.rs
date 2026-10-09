use std::collections::VecDeque;
use std::io::{self, Read};

const TICKET: i64 = 4;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<usize>().unwrap());
    let (n, m) = (it.next().unwrap(), it.next().unwrap());
    let mut routes: Vec<Vec<usize>> = Vec::with_capacity(m);
    let mut routes_at = vec![Vec::new(); n + 1];
    for r in 0..m {
        let size = it.next().unwrap();
        let stops: Vec<usize> = it.by_ref().take(size).collect();
        for &s in &stops {
            routes_at[s].push(r);
        }
        routes.push(stops);
    }
    let k = it.next().unwrap();
    let mut total = vec![0i64; n + 1];
    let mut ok = vec![true; n + 1];
    for _ in 0..k {
        let (money, start, card) = (
            it.next().unwrap() as i64,
            it.next().unwrap(),
            it.next().unwrap(),
        );
        // fewest rides from the start to every stop; a ride covers a whole route
        let mut rides = vec![-1i64; n + 1];
        let mut used = vec![false; m];
        rides[start] = 0;
        let mut queue = VecDeque::from([start]);
        while let Some(u) = queue.pop_front() {
            for &r in &routes_at[u] {
                if used[r] {
                    continue;
                }
                used[r] = true;
                for &v in &routes[r] {
                    if rides[v] < 0 {
                        rides[v] = rides[u] + 1;
                        queue.push_back(v);
                    }
                }
            }
        }
        for t in 1..=n {
            let cost = if card == 1 { 0 } else { TICKET * rides[t] };
            if rides[t] < 0 || cost > money {
                ok[t] = false;
            } else {
                total[t] += cost;
            }
        }
    }
    let best = (1..=n).filter(|&t| ok[t]).min_by_key(|&t| (total[t], t));
    match best {
        Some(t) => println!("{} {}", t, total[t]),
        None => println!("0"),
    }
}
