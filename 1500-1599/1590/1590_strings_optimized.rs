use std::io::{self, Read};

const EDGE_FACTOR: usize = 3; // a suffix automaton has fewer than 3N edges

#[derive(Clone, Copy)]
struct State {
    length: i32,
    link: i32,
    head: i32,
}

#[derive(Clone, Copy)]
struct Edge {
    target: i32,
    following: i32,
    letter: u8,
}

struct Automaton {
    states: Vec<State>,
    edges: Vec<Edge>,
}

impl Automaton {
    fn find(&self, state: usize, ch: u8) -> i32 {
        // Sparse outgoing lists have at most the 26 alphabet letters.
        let mut edge = self.states[state].head;
        while edge >= 0 && self.edges[edge as usize].letter != ch {
            edge = self.edges[edge as usize].following;
        }
        edge
    }

    fn add(&mut self, state: usize, ch: u8, target: usize) {
        self.edges.push(Edge {
            target: target as i32,
            following: self.states[state].head,
            letter: ch,
        });
        self.states[state].head = self.edges.len() as i32 - 1;
    }

    fn new(text: &[u8]) -> Self {
        let mut a = Self {
            states: Vec::with_capacity(2 * text.len() + 1),
            edges: Vec::with_capacity(EDGE_FACTOR * text.len()),
        };
        a.states.push(State {
            length: 0,
            link: -1,
            head: -1,
        });
        let mut last = 0;
        for &ch in text {
            let current = a.states.len();
            a.states.push(State {
                length: a.states[last].length + 1,
                link: 0,
                head: -1,
            });
            let mut state = last as i32;
            while state >= 0 && a.find(state as usize, ch) < 0 {
                a.add(state as usize, ch, current);
                state = a.states[state as usize].link;
            }
            if state >= 0 {
                let target = a.edges[a.find(state as usize, ch) as usize].target as usize;
                if a.states[state as usize].length + 1 == a.states[target].length {
                    a.states[current].link = target as i32;
                } else {
                    let clone = a.states.len();
                    a.states.push(State {
                        length: a.states[state as usize].length + 1,
                        link: a.states[target].link,
                        head: -1,
                    });
                    // Copy actual edges independently, so later redirects
                    // cannot modify the original state and its clone together.
                    let mut edge = a.states[target].head;
                    while edge >= 0 {
                        let old = a.edges[edge as usize];
                        a.add(clone, old.letter, old.target as usize);
                        edge = old.following;
                    }
                    while state >= 0 {
                        let edge = a.find(state as usize, ch);
                        if edge < 0 || a.edges[edge as usize].target as usize != target {
                            break;
                        }
                        a.edges[edge as usize].target = clone as i32;
                        state = a.states[state as usize].link;
                    }
                    a.states[target].link = clone as i32;
                    a.states[current].link = clone as i32;
                }
            }
            last = current;
        }
        a
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_ascii_whitespace();
    let text = tokens.next().unwrap().as_bytes();
    let a = Automaton::new(text);
    let answer: i64 = (1..a.states.len())
        .map(|v| (a.states[v].length - a.states[a.states[v].link as usize].length) as i64)
        .sum();
    println!("{}", answer);
}
