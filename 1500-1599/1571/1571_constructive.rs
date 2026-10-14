use std::collections::HashSet;
use std::io::{self, Read};

const SMALL: usize = 2;

/// English, or else the first name of one or two letters that no team
/// speaks: at most 100 teams cannot take all 702 of them.
fn free_language(spoken: &HashSet<&str>) -> String {
    if !spoken.contains("english") {
        return "english".to_string();
    }
    let mut names: Vec<String> = (b'a'..=b'z').map(|a| (a as char).to_string()).collect();
    for a in b'a'..=b'z' {
        for b in b'a'..=b'z' {
            names.push(format!("{}{}", a as char, b as char));
        }
    }
    names.into_iter().find(|name| !spoken.contains(name.as_str())).unwrap()
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut words = text.split_ascii_whitespace();
    let n: usize = words.next().unwrap().parse().unwrap();
    let langs: Vec<&str> = words.take(n).collect();
    let distinct: HashSet<&str> = langs.iter().copied().collect();
    if distinct.len() < n {
        // a third team would overhear two teams of one language
        println!("{}", if n == SMALL { "0" } else { "Impossible" });
    } else if n == 1 {
        println!("0");
    } else if n == SMALL {
        println!("1\n{}-{}", langs[0], langs[1]);
    } else {
        // a talk through another team's language is overheard, so every talk
        // goes through a language no team speaks
        let hub = free_language(&distinct);
        let lines: Vec<String> = langs.iter().map(|l| format!("{}-{}", l, hub)).collect();
        println!("{}\n{}", n, lines.join("\n"));
    }
}
