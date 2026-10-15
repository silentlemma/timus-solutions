use std::collections::HashSet;
use std::io::{self, Read};

// test 6 was removed and new tests were added after test 7, which became
// test 6: a failure on old test 7 must now read 6, while an accepted run or
// a failure on old test 6 may change or stay as it was
const REMOVED: u32 = 6;
const RENUMBERED: u32 = 7;

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut words = text.split_ascii_whitespace();
    let n: usize = words.next().unwrap().parse().unwrap();
    let mut must: HashSet<&str> = HashSet::new();
    let mut any: HashSet<&str> = HashSet::new();
    for _ in 0..n {
        let name = words.next().unwrap();
        match words.next().unwrap() {
            "ML" | "TL" | "WA" => {
                let test: u32 = words.next().unwrap().parse().unwrap();
                if test == RENUMBERED {
                    must.insert(name);
                    any.insert(name);
                } else if test == REMOVED {
                    any.insert(name);
                }
            }
            "AC" => {
                any.insert(name);
            }
            _ => {}
        }
    }
    println!("{} {}", must.len(), any.len());
}
