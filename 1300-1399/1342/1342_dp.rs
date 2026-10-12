use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<usize>().unwrap());
    let (n, m) = (it.next().unwrap(), it.next().unwrap());
    let factories: Vec<(usize, f64, f64)> = (0..n)
        .map(|_| {
            let k = it.next().unwrap();
            (k, it.next().unwrap() as f64, it.next().unwrap() as f64)
        })
        .collect();
    let target = m.min(factories.iter().map(|f| f.0).sum());
    // best[j]: the cheapest way to make exactly j brooms at the factories so far
    let mut best = vec![f64::INFINITY; target + 1];
    best[0] = 0.0;
    let mut reach = 0;
    for &(k, first, last) in &factories {
        let step = if k > 1 {
            (last - first) / (k - 1) as f64
        } else {
            0.0
        };
        // cost[x]: x brooms at this factory, the j-th one costing first + step (j - 1)
        let cost: Vec<f64> = (0..=k)
            .map(|x| {
                let fx = x as f64;
                fx * first + step * fx * (fx - 1.0) / 2.0
            })
            .collect();
        reach = target.min(reach + k);
        let mut fresh = best.clone();
        for j in 1..=reach {
            let mut here = fresh[j];
            for x in 1..=j.min(k) {
                here = here.min(best[j - x] + cost[x]);
            }
            fresh[j] = here;
        }
        best = fresh;
    }
    if target < m {
        println!("Maximum possible amount: {}", target);
    }
    println!("Minimum possible cost: {:.2}", best[target]);
}
