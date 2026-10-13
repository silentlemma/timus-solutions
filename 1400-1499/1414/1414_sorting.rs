use std::collections::BTreeSet;
use std::fmt::Write as _;
use std::io::{self, Read};

const LIMIT: usize = 20;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    // the base starts with this one name
    let mut names: BTreeSet<String> = BTreeSet::new();
    names.insert("sun".to_string());
    let mut out = String::new();
    for line in input.split_whitespace() {
        let arg = &line[1..];
        if line.starts_with('+') {
            names.insert(arg.to_string());
            continue;
        }
        writeln!(out, "{}", arg).unwrap();
        // names with this prefix form a run starting where the prefix would go
        for name in names
            .range(arg.to_string()..)
            .take(LIMIT)
            .take_while(|name| name.starts_with(arg))
        {
            writeln!(out, "  {}", name).unwrap();
        }
    }
    print!("{}", out);
}
