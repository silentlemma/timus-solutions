use std::cmp::Reverse;
use std::collections::{BinaryHeap, HashMap};
use std::io::{self, Read, Write};

const NO_EDGE: usize = usize::MAX;

fn intern<'a>(word: &'a str, ids: &mut HashMap<&'a str, usize>, words: &mut Vec<&'a str>) -> usize {
    if let Some(&id) = ids.get(word) {
        return id;
    }
    let id = words.len();
    ids.insert(word, id);
    words.push(word);
    id
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_ascii_whitespace();
    let keyword_count: usize = tokens.next().unwrap().parse().unwrap();
    let rule_count: usize = tokens.next().unwrap().parse().unwrap();
    let capacity = keyword_count + 2 * rule_count;
    let mut ids = HashMap::with_capacity(capacity);
    let mut words = Vec::with_capacity(capacity);
    for _ in 0..keyword_count {
        intern(tokens.next().unwrap(), &mut ids, &mut words);
    }

    let mut head = vec![NO_EDGE; capacity];
    let mut target = Vec::with_capacity(rule_count);
    let mut next = Vec::with_capacity(rule_count);
    for edge in 0..rule_count {
        let from = intern(tokens.next().unwrap(), &mut ids, &mut words);
        let to = intern(tokens.next().unwrap(), &mut ids, &mut words);
        target.push(to);
        next.push(head[from]);
        head[from] = edge;
    }

    let mut required = vec![false; words.len()];
    let mut indegree = vec![0; words.len()];
    let mut queue = Vec::with_capacity(words.len());
    for (word, needed) in required.iter_mut().enumerate().take(keyword_count) {
        *needed = true;
        queue.push(word);
    }
    // Only edges leaving required words constrain the answer.
    let mut position = 0;
    while position < queue.len() {
        let word = queue[position];
        let mut edge = head[word];
        while edge != NO_EDGE {
            let to = target[edge];
            indegree[to] += 1;
            if !required[to] {
                required[to] = true;
                queue.push(to);
            }
            edge = next[edge];
        }
        position += 1;
    }

    let mut ready = BinaryHeap::new();
    for &word in &queue {
        if indegree[word] == 0 {
            ready.push(Reverse((words[word], word)));
        }
    }

    let mut answer = String::with_capacity(input.len());
    let mut emitted = 0;
    while let Some(Reverse((text, word))) = ready.pop() {
        if emitted > 0 {
            answer.push(' ');
        }
        answer.push_str(text);
        emitted += 1;
        let mut edge = head[word];
        while edge != NO_EDGE {
            let to = target[edge];
            indegree[to] -= 1;
            if indegree[to] == 0 {
                ready.push(Reverse((words[to], to)));
            }
            edge = next[edge];
        }
    }

    let mut output = io::BufWriter::new(io::stdout().lock());
    if emitted != queue.len() {
        output.write_all(b"-1\n").unwrap();
    } else {
        answer.push('\n');
        output.write_all(answer.as_bytes()).unwrap();
    }
}
