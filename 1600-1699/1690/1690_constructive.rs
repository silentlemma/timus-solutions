use std::io::{self, Read};

const CLASSES: usize = 4; // houses by the parities of x and y
const CANDIDATES_PER_PLACE: usize = 5; // 5n names for n places

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut it = text.split_ascii_whitespace().map(|w| w.parse::<i64>().unwrap());
    let n = it.next().unwrap() as usize;
    let mut groups: Vec<Vec<String>> = vec![Vec::new(); CLASSES];
    for i in 1..=CANDIDATES_PER_PLACE * n {
        let (x, y) = (it.next().unwrap(), it.next().unwrap());
        groups[(2 * (x & 1) + (y & 1)) as usize].push(i.to_string());
    }
    // two houses with the same parities differ by even dx and dy, so the
    // middle of their segment is a lattice point; 5n houses in 4 classes
    // leave one class with at least n of them, so the army always exists
    let best = groups.iter().max_by_key(|g| g.len()).unwrap();
    println!("OK");
    println!("{}", best[..n].join(" "));
}
