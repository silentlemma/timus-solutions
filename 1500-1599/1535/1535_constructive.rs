use std::io::{self, Read};

fn join(order: &[usize]) -> String {
    order
        .iter()
        .map(|v| v.to_string())
        .collect::<Vec<_>>()
        .join(" ")
}

fn main() {
    let mut s = String::new();
    io::stdin().read_to_string(&mut s).unwrap();
    let n: usize = s.trim().parse().unwrap();
    // the cheapest round trip, as a cycle through n: one side of n goes
    // 2, n - 2, 4, n - 4, ..., the other 1, n - 1, 3, n - 3, ...; step k
    // takes the pair k, k + 1 for odd k and n - k, n - k + 1 for even k
    let mut used = vec![false; n + 1];
    used[n] = true;
    let (mut one_side, mut other_side) = (Vec::new(), Vec::new());
    for k in 1.. {
        if k % 2 == 0 && k >= n {
            break;
        }
        let (a, b) = if k % 2 == 1 {
            (k + 1, k)
        } else {
            (n - k, n - k + 1)
        };
        if a > n || used[a] || used[b] {
            break;
        }
        one_side.push(a);
        other_side.push(b);
        used[a] = true;
        used[b] = true;
    }
    // the cycle: n, one side, the city left where the two sides meet if
    // any, and the other side back to n; it ends with city 1
    let mut cycle = vec![n];
    cycle.extend(&one_side);
    cycle.extend((1..n).filter(|&v| !used[v]));
    cycle.extend(other_side.iter().rev());
    let mut cheap = vec![*cycle.last().unwrap()];
    cheap.extend(&cycle[..cycle.len() - 1]);
    // the dearest: odd numbers up, then even numbers down, so that every
    // city is next to the two closest in size
    let dear: Vec<usize> = (1..=n)
        .step_by(2)
        .chain((2..=n - n % 2).rev().step_by(2))
        .collect();
    println!("{}\n{}", join(&cheap), join(&dear));
}
