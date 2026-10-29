use std::collections::HashMap;
use std::io::{self, Read};

// the three cabinets from left to right, with the names from the statement
const CABINETS: [[&str; 9]; 3] = [
    [
        "Alice", "Ariel", "Aurora", "Phil", "Peter", "Olaf", "Phoebus", "Ralph", "Robin",
    ],
    [
        "Bambi", "Belle", "Bolt", "Mulan", "Mowgli", "Mickey", "Silver", "Simba", "Stitch",
    ],
    [
        "Dumbo", "Genie", "Jiminy", "Kuzko", "Kida", "Kenai", "Tarzan", "Tiana", "Winnie",
    ],
];

fn main() {
    let mut cabinet = HashMap::new();
    for (i, names) in CABINETS.iter().enumerate() {
        for &name in names {
            cabinet.insert(name, i as i32);
        }
    }
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_ascii_whitespace();
    let n: usize = words.next().unwrap().parse().unwrap();
    let (mut position, mut steps) = (0, 0);
    for name in words.take(n) {
        let target = cabinet[name];
        steps += (target - position).abs();
        position = target;
    }
    println!("{}", steps);
}
