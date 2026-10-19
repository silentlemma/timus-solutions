use std::io::{self, Read};

const MONKEYS: usize = 5;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i64> = input.split_ascii_whitespace().map(|t| t.parse().unwrap()).collect();
    let xs: Vec<i64> = v.iter().step_by(2).copied().collect();
    let ys: Vec<i64> = v.iter().skip(1).step_by(2).copied().collect();
    // y / x = b - c x along a shot, so the slopes y / x of points on one shot
    // lie on a line in x; compared with all fractions cleared
    let one_shot = |i: usize, j: usize, k: usize| {
        let left = (ys[k] * xs[i] - ys[i] * xs[k]) * xs[j] * (xs[j] - xs[i]);
        let right = (ys[j] * xs[i] - ys[i] * xs[j]) * xs[k] * (xs[k] - xs[i]);
        left == right
    };
    let full = (1usize << MONKEYS) - 1;
    let mut shots: Vec<usize> = (0..MONKEYS).map(|i| 1 << i).collect();
    for i in 0..MONKEYS {
        for j in 0..MONKEYS {
            // gravity bends the path down: the slope y / x must fall as x grows
            if xs[i] < xs[j] && ys[i] * xs[j] > ys[j] * xs[i] {
                shots.push((0..MONKEYS).filter(|&k| one_shot(i, j, k)).map(|k| 1 << k).sum());
            }
        }
    }
    let mut need = vec![MONKEYS; full + 1];
    need[0] = 0;
    for mask in 0..=full {
        for &shot in &shots {
            need[mask | shot] = need[mask | shot].min(need[mask] + 1);
        }
    }
    println!("{}", need[full]);
}
