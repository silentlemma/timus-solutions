use std::collections::BTreeMap;
use std::io::{self, Read, Write};

#[derive(Default)]
struct Folder {
    // the ordered map keeps the subfolders sorted by name
    sub: BTreeMap<String, Folder>,
}

fn print(f: &Folder, depth: usize, out: &mut String) {
    for (name, child) in &f.sub {
        out.push_str(&" ".repeat(depth));
        out.push_str(name);
        out.push('\n');
        print(child, depth + 1, out);
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let n: usize = it.next().unwrap().parse().unwrap();
    let mut root = Folder::default();
    for _ in 0..n {
        let mut cur = &mut root;
        for name in it.next().unwrap().split('\\') {
            cur = cur.sub.entry(name.to_string()).or_default();
        }
    }
    let mut out = String::new();
    print(&root, 0, &mut out);
    io::stdout().write_all(out.as_bytes()).unwrap();
}
