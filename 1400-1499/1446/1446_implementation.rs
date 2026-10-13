use std::collections::HashMap;
use std::io::{self, Read};

const HOUSES: [&str; 4] = ["Slytherin", "Hufflepuff", "Gryffindor", "Ravenclaw"];

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut lines = input.split('\n').map(|l| l.trim_end_matches('\r'));
    let n: usize = lines.next().unwrap().trim().parse().unwrap();
    let mut lists: HashMap<&str, Vec<&str>> = HashMap::new();
    for _ in 0..n {
        // names keep their inner spaces, so only the line break is dropped
        let name = lines.next().unwrap();
        let house = lines.next().unwrap().trim();
        lists.entry(house).or_default().push(name);
    }
    let blocks: Vec<String> = HOUSES
        .iter()
        .map(|house| {
            let mut block = format!("{}:\n", house);
            for name in lists.get(house).map(|v| v.as_slice()).unwrap_or(&[]) {
                block.push_str(name);
                block.push('\n');
            }
            block
        })
        .collect();
    print!("{}", blocks.join("\n"));
}
