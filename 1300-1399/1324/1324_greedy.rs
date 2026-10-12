use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let limit: i64 = input.trim().parse().unwrap();
    // going back from the last replacement: reach is the longest run that
    // the replacements chosen so far turn into a single space
    let mut plan = Vec::new();
    let mut reach: i64 = 1;
    while reach < limit {
        let step = (reach + 1) / 2 + 1; // the best length to replace here
        let groups = reach + 2 - step; // most groups in a run that still fits
        reach = groups * step + step - 2;
        plan.push(step);
    }
    println!("{}", plan.len());
    for step in plan.iter().rev() {
        println!("{}", step);
    }
}
