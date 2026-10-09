use std::io::{self, Read};

// a member is appended after all its descendants: the reversed list puts
// everyone before their descendants
fn visit(v: usize, children: &[Vec<usize>], done: &mut [bool], order: &mut Vec<usize>) {
    done[v] = true;
    for &c in &children[v] {
        if !done[c] {
            visit(c, children, done, order);
        }
    }
    order.push(v);
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<usize>().unwrap());
    let n = it.next().unwrap();
    let mut children = vec![Vec::new(); n + 1];
    for kids in children.iter_mut().skip(1) {
        for c in it.by_ref() {
            if c == 0 {
                break;
            }
            kids.push(c);
        }
    }
    let mut done = vec![false; n + 1];
    let mut order = Vec::new();
    for v in 1..=n {
        if !done[v] {
            visit(v, &children, &mut done, &mut order);
        }
    }
    let words: Vec<String> = order.iter().rev().map(|v| v.to_string()).collect();
    println!("{}", words.join(" "));
}
