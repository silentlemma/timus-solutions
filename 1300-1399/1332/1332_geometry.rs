use std::io::{self, Read};

const EPS: f64 = 1e-7;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<i64>().unwrap());
    let n = it.next().unwrap() as usize;
    let cities: Vec<(f64, f64)> = (0..n)
        .map(|_| (it.next().unwrap() as f64, it.next().unwrap() as f64))
        .collect();
    let (big, small) = (it.next().unwrap(), it.next().unwrap());
    let reach = (big - small) as f64; // how far a center may be
    if reach < 0.0 {
        println!("0");
        return;
    }
    // a best circle can be moved until it passes through two centers or
    // stands on one, so only such places need to be tried
    let mut places = cities.clone();
    for i in 0..n {
        for j in 0..i {
            let (ax, ay) = cities[i];
            let (dx, dy) = (cities[j].0 - ax, cities[j].1 - ay);
            let half = dx.hypot(dy) / 2.0;
            if half > 0.0 && half <= reach {
                let rise = (reach * reach - half * half).max(0.0).sqrt() / (2.0 * half);
                let (mx, my) = (ax + dx / 2.0, ay + dy / 2.0);
                places.push((mx - dy * rise, my + dx * rise));
                places.push((mx + dy * rise, my - dx * rise));
            }
        }
    }
    let limit = (reach + EPS) * (reach + EPS);
    let best = places
        .iter()
        .map(|&(px, py)| {
            cities
                .iter()
                .filter(|&&(x, y)| (x - px) * (x - px) + (y - py) * (y - py) <= limit)
                .count()
        })
        .max()
        .unwrap();
    println!("{}", best);
}
