use std::fmt::Write;
use std::io::{self, Read};

const ALPHABET_SIZE: usize = 26;
const EMPTY_ROOT: usize = 1;
const ROOT_COUNT: usize = 2;

#[derive(Clone)]
struct Node {
    length: i32,
    link: usize,
    next: [usize; ALPHABET_SIZE],
}

fn distinct_counts(text: &[u8]) -> Vec<usize> {
    let mut nodes = vec![
        Node {
            length: 0,
            link: 0,
            next: [0; ALPHABET_SIZE]
        };
        text.len() + ROOT_COUNT
    ];
    nodes[0].length = -1;
    let mut count = ROOT_COUNT;
    let mut last = EMPTY_ROOT;
    let mut answer = Vec::with_capacity(text.len());
    for (position, &letter) in text.iter().enumerate() {
        let code = (letter - b'a') as usize;
        let mut parent = last;
        loop {
            let left = position as i32 - nodes[parent].length - 1;
            if left >= 0 && text[left as usize] == letter {
                break;
            }
            parent = nodes[parent].link;
        }
        let mut node = nodes[parent].next[code];
        if node == 0 {
            node = count;
            count += 1;
            nodes[node].length = nodes[parent].length + 2;
            nodes[parent].next[code] = node;
            if nodes[node].length == 1 {
                nodes[node].link = EMPTY_ROOT;
            } else {
                let mut candidate = nodes[parent].link;
                loop {
                    let left = position as i32 - nodes[candidate].length - 1;
                    if left >= 0 && text[left as usize] == letter {
                        break;
                    }
                    candidate = nodes[candidate].link;
                }
                nodes[node].link = nodes[candidate].next[code];
            }
        }
        last = node;
        answer.push(count - ROOT_COUNT);
    }
    answer
}

fn print_counts(output: &mut String, values: &[usize]) {
    for (i, value) in values.iter().enumerate() {
        if i > 0 {
            output.push(' ');
        }
        write!(output, "{}", value).unwrap();
    }
    output.push('\n');
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let answer = distinct_counts(input.trim().as_bytes());
    let mut output = String::new();
    print_counts(&mut output, &answer);
    print!("{output}");
}
