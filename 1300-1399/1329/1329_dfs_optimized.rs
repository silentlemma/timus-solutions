use std::io::{self, Read, Write};

const IDS: usize = 40001;
const NONE: u16 = u16::MAX;

#[derive(Clone, Copy)]
struct Node {
    parent: u16,
    child: u16,
    sibling: u16,
    enter: u16,
    leave: u16,
}

fn ancestor(nodes: &[Node], a: usize, b: usize) -> bool {
    nodes[a].enter != NONE && nodes[a].enter <= nodes[b].enter && nodes[b].enter < nodes[a].leave
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut values = text
        .split_ascii_whitespace()
        .map(|word| word.parse::<i32>().unwrap());
    let n = values.next().unwrap() as usize;
    let mut nodes = vec![
        Node {
            parent: NONE,
            child: NONE,
            sibling: NONE,
            enter: NONE,
            leave: 0
        };
        IDS
    ];
    let mut root = NONE;
    for _ in 0..n {
        let vertex = values.next().unwrap() as usize;
        let parent = values.next().unwrap();
        if parent < 0 {
            root = vertex as u16;
        } else {
            let parent = parent as usize;
            nodes[vertex].parent = parent as u16;
            nodes[vertex].sibling = nodes[parent].child;
            nodes[parent].child = vertex as u16;
        }
    }
    let mut vertex = root;
    let mut clock = 0_u16;
    while vertex != NONE {
        let v = vertex as usize;
        nodes[v].enter = clock;
        clock += 1;
        if nodes[v].child != NONE {
            vertex = nodes[v].child;
            continue;
        }
        while vertex != NONE {
            let v = vertex as usize;
            nodes[v].leave = clock;
            if nodes[v].sibling != NONE {
                vertex = nodes[v].sibling;
                break;
            }
            vertex = nodes[v].parent;
        }
    }
    let queries = values.next().unwrap();
    let mut output = io::BufWriter::new(io::stdout().lock());
    for _ in 0..queries {
        let a = values.next().unwrap() as usize;
        let b = values.next().unwrap() as usize;
        let answer = if ancestor(&nodes, a, b) {
            b'1'
        } else if ancestor(&nodes, b, a) {
            b'2'
        } else {
            b'0'
        };
        output.write_all(&[answer, b'\n']).unwrap();
    }
}
