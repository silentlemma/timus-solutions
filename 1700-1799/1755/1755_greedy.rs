use std::io::{self, Read};

struct Good {
    worth: i64,
    cost: i64,
    amount: i64,
    slot: usize,
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_ascii_whitespace().map(|w| w.parse::<i64>().unwrap());
    let mut next = || words.next().unwrap();
    let (a1, b1, a2, b2, n, m) = (next(), next(), next(), next(), next(), next());
    // Karlsson leaves the piece he likes no more than half, so the best is
    // the piece of greatest worth to Little Boy within half of Karlsson's total:
    // a fractional knapsack where each ingredient is taken by worth per cost
    let mut goods = vec![
        Good { worth: a1, cost: a2, amount: n, slot: 0 },
        Good { worth: b1, cost: b2, amount: m, slot: 1 },
    ];
    // zero-cost goods first, then by worth over cost, highest first
    if goods[1].worth * goods[0].cost > goods[0].worth * goods[1].cost {
        goods.swap(0, 1);
    }
    let mut room = (a2 * n + b2 * m) as f64 / 2.0;
    let mut piece = vec![0.0; goods.len()];
    for g in &goods {
        let take = if (g.cost * g.amount) as f64 <= room {
            g.amount as f64
        } else {
            room / g.cost as f64
        };
        piece[g.slot] = take;
        room -= take * g.cost as f64;
    }
    println!("{:.8} {:.8}", piece[0], piece[1]);
}
