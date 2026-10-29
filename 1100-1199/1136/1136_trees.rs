use std::fmt::Write as _;
use std::io::{self, Read};

// a binary search tree: the number of every node and its children
struct Tree {
    number: Vec<u32>,
    left: Vec<Option<usize>>,
    right: Vec<Option<usize>>,
}

impl Tree {
    fn insert(&mut self, value: u32) {
        let node = self.number.len();
        self.number.push(value);
        self.left.push(None);
        self.right.push(None);
        if node == 0 {
            return;
        }
        let mut v = 0;
        loop {
            let child = if value < self.number[v] {
                &mut self.left[v]
            } else {
                &mut self.right[v]
            };
            match *child {
                Some(next) => v = next,
                None => {
                    *child = Some(node);
                    return;
                }
            }
        }
    }

    // the even-session order: right wing, left wing, then the chairman
    fn speak(&self, v: Option<usize>, out: &mut String) {
        if let Some(v) = v {
            self.speak(self.right[v], out);
            self.speak(self.left[v], out);
            writeln!(out, "{}", self.number[v]).unwrap();
        }
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tok = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<u32>().unwrap());
    let n = tok.next().unwrap() as usize;
    let post: Vec<u32> = tok.take(n).collect();
    let mut tree = Tree {
        number: Vec::new(),
        left: Vec::new(),
        right: Vec::new(),
    };
    // read backwards, the odd-session order names every chairman before the
    // members of the wings, so inserting in that order rebuilds the tree
    for &value in post.iter().rev() {
        tree.insert(value);
    }
    let mut out = String::new();
    if n > 0 {
        tree.speak(Some(0), &mut out);
    }
    print!("{}", out);
}
