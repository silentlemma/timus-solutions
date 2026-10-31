use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let mut names = Vec::<String>::new();
    // at most thirty names are retained, not the potentially long partition list.
    for line in stdin.lock().lines() {
        let line = line.unwrap();
        if line.trim().is_empty() {
            continue;
        }
        if line.trim() == "#" {
            break;
        }
        for name in line.trim().split('-') {
            if !names.iter().any(|known| known == name) {
                names.push(name.to_owned());
            }
        }
    }
    // every other compartment must be emptied through one opened partition,
    // and the partitions of a tree towards the airlock are enough
    println!("{}", names.len() - 1);
}
