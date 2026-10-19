use std::collections::{BTreeMap, HashMap, VecDeque};
use std::io::{self, Read};

const CHAMPION: &str = "Isenbaev";
const TEAM: usize = 3;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let teams: usize = match it.next() {
        Some(t) => t.parse().unwrap(),
        None => return,
    };
    let mut mates: BTreeMap<&str, Vec<&str>> = BTreeMap::new();
    for _ in 0..teams {
        let names: Vec<&str> = (0..TEAM).map(|_| it.next().unwrap()).collect();
        for &name in &names {
            mates.entry(name).or_default().extend(&names);
        }
    }
    // breadth-first search from the champion over shared teams
    let mut number: HashMap<&str, usize> = HashMap::new();
    if mates.contains_key(CHAMPION) {
        number.insert(CHAMPION, 0);
        let mut queue = VecDeque::from(vec![CHAMPION]);
        while let Some(name) = queue.pop_front() {
            let next = number[name] + 1;
            for &mate in &mates[name] {
                if !number.contains_key(mate) {
                    number.insert(mate, next);
                    queue.push_back(mate);
                }
            }
        }
    }
    for name in mates.keys() {
        match number.get(name) {
            Some(v) => println!("{} {}", name, v),
            None => println!("{} undefined", name),
        }
    }
}
