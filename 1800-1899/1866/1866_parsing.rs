use std::io::{self, Read};

// (name, syllables in a foot, place of the stressed syllable from 1)
const METERS: [(&str, usize, usize); 5] = [
    ("trochee", 2, 1),
    ("iamb", 2, 2),
    ("dactyl", 3, 1),
    ("amphibrach", 3, 2),
    ("anapaest", 3, 3),
];

fn stresses(line: &str) -> Vec<bool> {
    line.split_whitespace()
        .flat_map(|word| word.split('-'))
        .filter(|s| !s.is_empty())
        .map(|s| s.contains('['))
        .collect()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut lines = input.lines();
    let n: usize = lines.next().unwrap().trim().parse().unwrap();
    let poem: Vec<Vec<bool>> = lines.take(n).map(stresses).collect();
    for &(name, foot, place) in METERS.iter() {
        // the last foot may be cut short, so only the place within a foot
        // matters, and every syllable must agree with it
        let fits = poem
            .iter()
            .all(|verse| verse.iter().enumerate().all(|(i, &s)| s == (i % foot == place - 1)));
        if fits {
            println!("{}", name);
            return;
        }
    }
    println!("not a poem");
}
