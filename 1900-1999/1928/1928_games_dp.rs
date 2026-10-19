use std::io::{self, Read};

fn optimal_totals(budget: usize, gift: i32, limit: usize) -> (i32, i32) {
    let mut current = vec![0; budget + 1];
    let mut opponent = vec![0; budget + 1];
    for remaining in 1..=budget {
        let mut best = if remaining < limit { gift } else { -1 };
        let mut other = 0;
        for request in 1..=remaining.min(limit) {
            let rest = remaining - request;
            let own_total = request as i32 + opponent[rest];
            let other_total = current[rest];
            if own_total > best || (own_total == best && other_total < other) {
                best = own_total;
                other = other_total;
            }
        }
        current[remaining] = best;
        opponent[remaining] = other;
    }
    (current[budget], opponent[budget])
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut tokens = text.split_whitespace();
    let budget = tokens.next().unwrap().parse().unwrap();
    let gift = tokens.next().unwrap().parse().unwrap();
    let limit = tokens.next().unwrap().parse().unwrap();
    let (first, second) = optimal_totals(budget, gift, limit);
    println!("{} {}", first, second);
}
