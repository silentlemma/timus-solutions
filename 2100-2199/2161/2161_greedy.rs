use std::io::{self, Read};

// The two largest values and the position of the first one; -1 stands for a
// missing value, so a lone knight needs nothing.
fn top_two(values: &[i64]) -> (i64, i64, usize) {
    let (mut first, mut second, mut place) = (-1i64, -1i64, usize::MAX);
    for (index, &value) in values.iter().enumerate() {
        if value > first {
            second = first;
            first = value;
            place = index;
        } else if value > second {
            second = value;
        }
    }
    (first, second, place)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|t| t.parse::<i64>().unwrap());
    let n = it.next().unwrap() as usize;
    let mut knights = Vec::with_capacity(n);
    for _ in 0..n {
        let (a, d, g) = (it.next().unwrap(), it.next().unwrap(), it.next().unwrap());
        knights.push((a, d, g));
    }
    // the strongest attack and shield each rival can afford
    let attack = top_two(&knights.iter().map(|k| k.0 + k.2).collect::<Vec<_>>());
    let shield = top_two(&knights.iter().map(|k| k.1 + k.2).collect::<Vec<_>>());
    for (i, &(a, d, g)) in knights.iter().enumerate() {
        // The shield must exceed every rival's best attack and the attack must
        // reach every rival's best shield, whatever the rivals do.
        let rival_attack = if attack.2 == i { attack.1 } else { attack.0 };
        let rival_shield = if shield.2 == i { shield.1 } else { shield.0 };
        let cost = (rival_attack + 1 - d).max(0) + (rival_shield - a).max(0);
        if cost <= g {
            println!("{}", i + 1);
            return;
        }
    }
    println!("-1");
}
