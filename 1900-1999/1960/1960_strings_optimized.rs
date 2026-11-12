use std::io::{self, Read, Write};

const ROOT_COUNT: usize = 2;
const EMPTY_ROOT: u32 = 1;
const OUTPUT_SIZE: usize = 8192;

#[derive(Clone, Default)]
struct Node {
    length: i32,
    link: u32,
    child: u32,
    sibling: u32,
    letter: u8,
}

fn transition(nodes: &[Node], parent: u32, letter: u8) -> u32 {
    // Each real node supplies the edge from its unique inner palindrome.
    let mut edge = nodes[parent as usize].child;
    while edge != 0 {
        if nodes[edge as usize].letter == letter {
            return edge;
        }
        edge = nodes[edge as usize].sibling;
    }
    0
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let text = input.trim().as_bytes();
    let mut nodes = vec![Node::default(); text.len() + ROOT_COUNT];
    nodes[0].length = -1;
    let (mut count, mut last) = (ROOT_COUNT, EMPTY_ROOT);
    let stdout = io::stdout();
    let mut output = io::BufWriter::with_capacity(OUTPUT_SIZE, stdout.lock());
    for (position, &letter) in text.iter().enumerate() {
        let mut parent = last;
        loop {
            let left = position as i32 - nodes[parent as usize].length - 1;
            if left >= 0 && text[left as usize] == letter {
                break;
            }
            parent = nodes[parent as usize].link;
        }
        let mut node = transition(&nodes, parent, letter);
        if node == 0 {
            node = count as u32;
            count += 1;
            nodes[node as usize].length = nodes[parent as usize].length + 2;
            nodes[node as usize].letter = letter;
            nodes[node as usize].sibling = nodes[parent as usize].child;
            nodes[parent as usize].child = node;
            if nodes[node as usize].length == 1 {
                nodes[node as usize].link = EMPTY_ROOT;
            } else {
                let mut candidate = nodes[parent as usize].link;
                loop {
                    let left = position as i32 - nodes[candidate as usize].length - 1;
                    if left >= 0 && text[left as usize] == letter {
                        break;
                    }
                    candidate = nodes[candidate as usize].link;
                }
                nodes[node as usize].link = transition(&nodes, candidate, letter);
            }
        }
        last = node;
        if position != 0 {
            output.write_all(b" ").unwrap();
        }
        write!(output, "{}", count - ROOT_COUNT).unwrap();
    }
    output.write_all(b"\n").unwrap();
}
