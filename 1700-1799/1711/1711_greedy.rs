use std::io::{self, Read};

const CHOICES: usize = 3; // names offered for every problem

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut words = text.split_ascii_whitespace();
    let n: usize = words.next().unwrap().parse().unwrap();
    let names: Vec<Vec<&str>> = (0..n)
        .map(|_| {
            let mut options: Vec<&str> = (0..CHOICES).map(|_| words.next().unwrap()).collect();
            options.sort();
            options
        })
        .collect();
    // in the given order, the least name above the previous one leaves the
    // most room for the problems still to come
    let mut chosen: Vec<&str> = Vec::new();
    let mut last = "";
    for _ in 0..n {
        let p: usize = words.next().unwrap().parse().unwrap();
        match names[p - 1].iter().find(|&&name| name > last) {
            Some(&name) => {
                last = name;
                chosen.push(name);
            }
            None => {
                println!("IMPOSSIBLE");
                return;
            }
        }
    }
    println!("{}", chosen.join("\n"));
}
