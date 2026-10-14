use std::io::{self, Read};

const SCALE: usize = 1000; // satiety has at most three digits after the point
const MOST_DISHES: i64 = 128; // more than the number of different dishes
const NONE: i64 = 1 << 62;
const DIGITS: usize = 3;

fn thousandths(text: &str) -> usize {
    let (whole, part) = text.split_once('.').unwrap_or((text, ""));
    let part = format!("{}000", part);
    whole.parse::<usize>().unwrap() * SCALE + part[..DIGITS].parse::<usize>().unwrap()
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut words = text.split_ascii_whitespace();
    let n: usize = words.next().unwrap().parse().unwrap();
    let m: usize = words.next().unwrap().parse().unwrap();
    let mut menu = Vec::with_capacity(n);
    for _ in 0..n {
        let name = words.next().unwrap();
        let price: i64 = words.next().unwrap().parse().unwrap();
        menu.push((name, price, thousandths(words.next().unwrap())));
    }
    let top = m * SCALE;
    // best[s]: the least cost, then the most different dishes, of an order with
    // satiety s, where s = top stands for top or more; one number holds both,
    // cost * MOST_DISHES - dishes, so that smaller is better
    let mut best = vec![NONE; top + 1];
    best[0] = 0;
    // per dish: whether the best order at s takes it, and in the orders
    // that take it, the satiety before the last plate and if that plate was the
    // first one, which leaves the orders without the dish
    let mut took = vec![vec![false; top + 1]; n];
    let mut first = vec![vec![false; top + 1]; n];
    let mut back = vec![vec![0u32; top + 1]; n];
    let mut mine = vec![NONE; top + 1];
    for (i, &(_, price, fill)) in menu.iter().enumerate() {
        let step = price * MOST_DISHES;
        mine.iter_mut().for_each(|v| *v = NONE);
        for s in 0..=top {
            let t = top.min(s + fill);
            if best[s] < NONE && best[s] + step - 1 < mine[t] {
                mine[t] = best[s] + step - 1;
                back[i][t] = s as u32;
                first[i][t] = true;
            }
        }
        // more plates of the same dish, from lower satiety up
        for s in 0..top {
            let t = top.min(s + fill);
            if mine[s] < NONE && mine[s] + step < mine[t] {
                mine[t] = mine[s] + step;
                back[i][t] = s as u32;
                first[i][t] = false;
            }
        }
        for s in 0..=top {
            if mine[s] < best[s] {
                best[s] = mine[s];
                took[i][s] = true;
            }
        }
    }
    // walk back from the full order, dish by dish from the last one
    let mut plates = vec![0i64; n];
    let mut s = top;
    for i in (0..n).rev() {
        if took[i][s] {
            loop {
                plates[i] += 1;
                let done = first[i][s];
                s = back[i][s] as usize;
                if done {
                    break;
                }
            }
        }
    }
    let cost: i64 = menu.iter().zip(&plates).map(|(d, &k)| d.1 * k).sum();
    let mut out = vec![cost.to_string()];
    for (d, &k) in menu.iter().zip(&plates) {
        if k > 0 {
            out.push(format!("{} {}", d.0, k));
        }
    }
    println!("{}", out.join("\n"));
}
