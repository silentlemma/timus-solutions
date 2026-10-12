use std::collections::BTreeSet;
use std::io::{self, Read, Write};

const OPEN: &str = "<friend>";
const CLOSE: &str = "</friend>";
const END: &str = "</blog>";

// the name inside a friend tag, without other tags or spaces
fn clean(inside: &str) -> String {
    let mut name = String::new();
    let mut tag = false;
    for c in inside.chars() {
        match c {
            '<' => tag = true,
            '>' => tag = false,
            _ if !tag => name.push(c),
            _ => {}
        }
    }
    name.trim().to_string()
}

fn main() {
    let mut raw = Vec::new();
    io::stdin().read_to_end(&mut raw).unwrap();
    let all = String::from_utf8_lossy(&raw);
    let lines: Vec<&str> = all.split('\n').collect();
    let n: usize = lines[0].trim().parse().unwrap();
    let mut pos = 1;
    let mut blogs: Vec<(String, BTreeSet<String>)> = Vec::new();
    for _ in 0..n {
        while lines[pos].trim().is_empty() {
            pos += 1;
        }
        let name = lines[pos].trim().to_string();
        let mut text = String::new();
        pos += 1;
        loop {
            text.push_str(lines[pos]);
            text.push('\n');
            if lines[pos].contains(END) {
                break;
            }
            pos += 1;
        }
        pos += 1;
        let mut friends = BTreeSet::new();
        let mut body = text.as_str();
        while let Some(at) = body.find(OPEN) {
            body = &body[at + OPEN.len()..];
            let stop = body.find(CLOSE).unwrap();
            let friend = clean(&body[..stop]);
            if !friend.is_empty() && friend != name {
                friends.insert(friend);
            }
            body = &body[stop + CLOSE.len()..];
        }
        blogs.push((name, friends));
    }
    let mut out = String::new();
    for (b, (name, friends)) in blogs.iter().enumerate() {
        let readers: BTreeSet<String> = blogs
            .iter()
            .filter(|(other, theirs)| other != name && theirs.contains(name))
            .map(|(other, _)| other.clone())
            .collect();
        let both: BTreeSet<String> = friends.intersection(&readers).cloned().collect();
        if b > 0 {
            out.push('\n');
        }
        out.push_str(name);
        out.push('\n');
        for (g, group) in [friends, &readers, &both].iter().enumerate() {
            let list: Vec<&str> = group.iter().map(|s| s.as_str()).collect();
            out.push_str(&format!("{}: {}\n", g + 1, list.join(", ")));
        }
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
