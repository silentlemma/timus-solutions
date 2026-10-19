use std::io::{self, Read, Write};

const MAX_WORD_LENGTH: usize = 200000;
const MAX_NODES: usize = 2 * MAX_WORD_LENGTH + 2;
const OUTPUT_BATCH: usize = 65536;

struct Tree {
    length: Vec<i32>,
    link: Vec<usize>,
    first: Vec<usize>,
    next: Vec<usize>,
    label: Vec<u8>,
    a: Vec<i32>,
    b: Vec<i32>,
    x: usize,
    y: usize,
    z: usize,
}

impl Tree {
    fn new() -> Self {
        let mut tree = Self {
            length: vec![0; MAX_NODES],
            link: vec![0; MAX_NODES],
            first: vec![0; MAX_NODES],
            next: vec![0; MAX_NODES],
            label: vec![0; MAX_NODES],
            a: vec![0; MAX_NODES],
            b: vec![0; MAX_NODES],
            x: 0,
            y: 0,
            z: 0,
        };
        tree.length[0] = -1;
        tree
    }
    fn solve(&mut self, a: &[u8], b: &[u8]) {
        self.x = 0;
        self.y = 0;
        self.z = 0;
        if a.len() == 1 && b.len() == 1 {
            if a == b {
                self.y = 1;
            } else {
                self.x = 1;
                self.z = 1;
            }
            return;
        }
        self.first[0] = 0;
        self.first[1] = 0;
        self.a[0] = 0;
        self.a[1] = 0;
        self.b[0] = 0;
        self.b[1] = 0;
        let mut nodes = 2;
        for pass in 0..2 {
            let word = if pass == 0 { a } else { b };
            let mut last = 1;
            for end in 0..word.len() {
                let letter = word[end];
                let mut node = last;
                while end as i32 - self.length[node] - 1 < 0
                    || word[(end as i32 - self.length[node] - 1) as usize] != letter
                {
                    node = self.link[node];
                }
                let mut found = self.first[node];
                while found != 0 && self.label[found] != letter {
                    found = self.next[found];
                }
                if found == 0 {
                    found = nodes;
                    nodes += 1;
                    let size = self.length[node] + 2;
                    let mut suffix = 1;
                    if size != 1 {
                        let mut candidate = self.link[node];
                        while end as i32 - self.length[candidate] - 1 < 0
                            || word[(end as i32 - self.length[candidate] - 1) as usize] != letter
                        {
                            candidate = self.link[candidate];
                        }
                        suffix = self.first[candidate];
                        while self.label[suffix] != letter {
                            suffix = self.next[suffix];
                        }
                    }
                    self.length[found] = size;
                    self.link[found] = suffix;
                    self.first[found] = 0;
                    self.next[found] = self.first[node];
                    self.label[found] = letter;
                    self.first[node] = found;
                    self.a[found] = 0;
                    self.b[found] = 0;
                }
                last = found;
                if pass == 0 {
                    self.a[found] += 1;
                } else {
                    self.b[found] += 1;
                }
            }
        }
        for node in (2..nodes).rev() {
            let ca = self.a[node];
            let cb = self.b[node];
            let suffix = self.link[node];
            self.a[suffix] += ca;
            self.b[suffix] += cb;
            if ca > cb {
                self.x += 1;
            } else if ca == cb {
                self.y += 1;
            } else {
                self.z += 1;
            }
        }
    }
}

fn next_line<'a>(raw: &'a [u8], at: &mut usize) -> &'a [u8] {
    let begin = *at;
    while *at < raw.len() && raw[*at] != b'\n' {
        *at += 1;
    }
    let mut end = *at;
    if *at < raw.len() {
        *at += 1;
    }
    if end > begin && raw[end - 1] == b'\r' {
        end -= 1;
    }
    &raw[begin..end]
}

fn main() {
    let mut raw = Vec::new();
    io::stdin().read_to_end(&mut raw).unwrap();
    let mut at = 0;
    let tests: usize = std::str::from_utf8(next_line(&raw, &mut at))
        .unwrap()
        .trim()
        .parse()
        .unwrap();
    let mut tree = Tree::new();
    let stdout = io::stdout();
    let mut output = io::BufWriter::with_capacity(OUTPUT_BATCH, stdout.lock());
    for index in 1..=tests {
        let a = next_line(&raw, &mut at);
        let b = next_line(&raw, &mut at);
        tree.solve(a, b);
        writeln!(output, "Case #{}: {} {} {}", index, tree.x, tree.y, tree.z).unwrap();
    }
}
