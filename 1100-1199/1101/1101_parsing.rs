use std::collections::{HashMap, HashSet};
use std::io::{self, Read};

/// OR, AND, NOT, a constant or a register.
enum Node {
    Or(Box<Node>, Box<Node>),
    And(Box<Node>, Box<Node>),
    Not(Box<Node>),
    Const(bool),
    Reg(u8),
}

struct Parser {
    tokens: Vec<String>,
    pos: usize,
}

impl Parser {
    fn peek(&self) -> &str {
        self.tokens.get(self.pos).map_or("", |s| s.as_str())
    }

    /// Recursive descent: NOT binds tightest, OR loosest.
    fn disjunction(&mut self) -> Node {
        let mut node = self.conjunction();
        while self.peek() == "OR" {
            self.pos += 1;
            node = Node::Or(Box::new(node), Box::new(self.conjunction()));
        }
        node
    }

    fn conjunction(&mut self) -> Node {
        let mut node = self.negation();
        while self.peek() == "AND" {
            self.pos += 1;
            node = Node::And(Box::new(node), Box::new(self.negation()));
        }
        node
    }

    fn negation(&mut self) -> Node {
        let word = self.tokens[self.pos].clone();
        self.pos += 1;
        match word.as_str() {
            "NOT" => Node::Not(Box::new(self.negation())),
            "(" => {
                let node = self.disjunction();
                self.pos += 1;
                node
            }
            "TRUE" => Node::Const(true),
            "FALSE" => Node::Const(false),
            _ => Node::Reg(word.as_bytes()[0]),
        }
    }
}

fn value(node: &Node, reg: &[bool]) -> bool {
    match node {
        Node::Or(a, b) => value(a, reg) || value(b, reg),
        Node::And(a, b) => value(a, reg) && value(b, reg),
        Node::Not(a) => !value(a, reg),
        Node::Const(v) => *v,
        Node::Reg(c) => reg[(c - b'A') as usize],
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let (expr, rest) = input.split_once('\n').unwrap_or((&input, ""));
    let bytes = expr.as_bytes();
    let mut tokens = Vec::new();
    let mut i = 0;
    while i < bytes.len() {
        if bytes[i].is_ascii_alphabetic() {
            let start = i;
            while i < bytes.len() && bytes[i].is_ascii_alphabetic() {
                i += 1;
            }
            tokens.push(expr[start..i].to_string());
            continue;
        }
        if bytes[i] == b'(' || bytes[i] == b')' {
            tokens.push(expr[i..i + 1].to_string());
        }
        i += 1;
    }
    let root = Parser { tokens, pos: 0 }.disjunction();
    let mut it = rest.split_ascii_whitespace();
    let mut num = || it.next().unwrap().parse::<i32>().unwrap();
    let (n, m, k) = (num(), num(), num());
    let forks: HashSet<(i32, i32)> = (0..m).map(|_| (num(), num())).collect();
    drop(num);
    let mut switches: HashMap<(i32, i32), u8> = HashMap::new();
    for _ in 0..k {
        let x: i32 = it.next().unwrap().parse().unwrap();
        let y: i32 = it.next().unwrap().parse().unwrap();
        switches.insert((x, y), it.next().unwrap().as_bytes()[0]);
    }
    let mut reg = vec![false; (b'Z' - b'A' + 1) as usize];
    let (mut x, mut y, mut dx, mut dy) = (0i32, 0i32, 1i32, 0i32);
    let mut out = String::new();
    while (-n..=n).contains(&x) && (-n..=n).contains(&y) {
        out.push_str(&format!("{} {}\n", x, y));
        if let Some(&c) = switches.get(&(x, y)) {
            let r = (c - b'A') as usize;
            reg[r] = !reg[r];
        }
        if forks.contains(&(x, y)) {
            // TRUE turns right, FALSE turns left
            (dx, dy) = if value(&root, &reg) {
                (dy, -dx)
            } else {
                (-dy, dx)
            };
        }
        x += dx;
        y += dy;
    }
    print!("{}", out);
}
