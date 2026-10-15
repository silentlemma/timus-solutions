use std::io::{self, Read};

// the stack after each prefix is a tree node: a push makes a new node, a
// matching close returns to the parent, a wrong close starts a lone node,
// and a piece is human exactly when it ends on the node it started on
fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let dna = it.next().unwrap().as_bytes();
    let mut parent: Vec<usize> = vec![usize::MAX];
    let mut letter: Vec<u8> = vec![0];
    let mut state = vec![0usize; dna.len() + 1];
    let mut cur = 0;
    for (i, &c) in dna.iter().enumerate() {
        if c.is_ascii_uppercase() {
            parent.push(cur);
            letter.push(c);
            cur = parent.len() - 1;
        } else if letter[cur] == c.to_ascii_uppercase() {
            cur = parent[cur];
        } else {
            parent.push(usize::MAX);
            letter.push(0);
            cur = parent.len() - 1;
        }
        state[i + 1] = cur;
    }
    let q: usize = it.next().unwrap().parse().unwrap();
    let mut out = String::with_capacity(q + 1);
    for _ in 0..q {
        let left: usize = it.next().unwrap().parse().unwrap();
        let right: usize = it.next().unwrap().parse().unwrap();
        out.push(if state[left - 1] == state[right] { '1' } else { '0' });
    }
    println!("{}", out);
}
