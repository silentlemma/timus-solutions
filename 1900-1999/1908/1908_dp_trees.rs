use std::io::{self, Read};

#[derive(Default)]
struct Node {
    first: usize,
    next: usize,
    leaves: usize,
    normal: usize,
    supplied: usize,
    label: u8,
}

fn minimum_clicks(words: &[Vec<u8>]) -> usize {
    let capacity = 1 + words.iter().map(Vec::len).sum::<usize>();
    let mut nodes = Vec::with_capacity(capacity);
    nodes.push(Node::default());
    for word in words {
        let mut node = 0;
        for &letter in word {
            let mut child = nodes[node].first;
            while child != 0 && nodes[child].label != letter {
                child = nodes[child].next;
            }
            if child == 0 {
                child = nodes.len();
                nodes.push(Node {
                    next: nodes[node].first,
                    label: letter,
                    ..Node::default()
                });
                nodes[node].first = child;
            }
            node = child;
        }
    }
    for node in (0..nodes.len()).rev() {
        let mut child = nodes[node].first;
        if child == 0 {
            nodes[node].leaves = 1;
            continue;
        }
        let mut total = 0;
        let mut best_normal = 0;
        let mut best_supplied = 0;
        while child != 0 {
            let count = nodes[child].leaves;
            nodes[node].leaves += count;
            total += nodes[child].normal + count;
            let saving = nodes[child].normal - nodes[child].supplied;
            best_normal = best_normal.max(saving);
            best_supplied = best_supplied.max(count + saving);
            child = nodes[child].next;
        }
        nodes[node].normal = total - best_normal;
        nodes[node].supplied = total - best_supplied;
    }
    nodes[0].normal
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let count = tokens.next().unwrap().parse::<usize>().unwrap();
    let words: Vec<Vec<u8>> = tokens
        .take(count)
        .map(|word| word.as_bytes().to_vec())
        .collect();
    println!("{}", minimum_clicks(&words));
}
