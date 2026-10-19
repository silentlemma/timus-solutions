use std::fmt::Write as FmtWrite;
use std::io::{self, Read};

fn complete(n: usize, k: usize, next: &mut [usize]) -> bool {
    let mut indegree = vec![0; n + 1];
    for vertex in 1..=n {
        if next[vertex] != 0 {
            indegree[next[vertex]] += 1;
            if indegree[next[vertex]] > 1 {
                return false;
            }
        }
    }

    let mut visited = vec![false; n + 1];
    let mut buckets = vec![Vec::<Vec<usize>>::new(); n + 1];
    for start in 1..=n {
        if indegree[start] != 0 {
            continue;
        }
        let mut path = Vec::new();
        let mut vertex = start;
        while vertex != 0 {
            visited[vertex] = true;
            path.push(vertex);
            vertex = next[vertex];
        }
        buckets[path.len()].push(path);
    }
    for start in 1..=n {
        if visited[start] {
            continue;
        }
        let mut length = 0;
        let mut vertex = start;
        while !visited[vertex] {
            visited[vertex] = true;
            length += 1;
            vertex = next[vertex];
        }
        if k % length != 0 {
            return false;
        }
    }

    let mut lengths = Vec::new();
    let mut radices = Vec::new();
    let mut states = 1;
    for (length, bucket) in buckets.iter().enumerate().skip(1) {
        if !bucket.is_empty() {
            lengths.push(length);
            radices.push(bucket.len() + 1);
            states *= bucket.len() + 1;
        }
    }

    // A mixed-radix state records how many paths of every length are used.
    let mut digits = vec![vec![0; lengths.len()]; states];
    let mut groups = Vec::new();
    for (state, state_digits) in digits.iter_mut().enumerate() {
        let mut value = state;
        let mut weight = 0;
        for (kind, &length) in lengths.iter().enumerate() {
            state_digits[kind] = value % radices[kind];
            value /= radices[kind];
            weight += state_digits[kind] * length;
        }
        if weight != 0 && k % weight == 0 {
            groups.push(state);
        }
    }

    let mut possible = vec![false; states];
    let mut choice = vec![0; states];
    possible[0] = true;
    for state in 1..states {
        let anchor = digits[state].iter().rposition(|&count| count != 0).unwrap();
        for &group in &groups {
            if group > state {
                break;
            }
            if digits[group][anchor] == 0 || !possible[state - group] {
                continue;
            }
            let fits = digits[group]
                .iter()
                .zip(&digits[state])
                .all(|(used, available)| used <= available);
            if fits {
                possible[state] = true;
                choice[state] = group;
                break;
            }
        }
    }
    if !possible[states - 1] {
        return false;
    }

    let mut state = states - 1;
    while state != 0 {
        let group = choice[state];
        let mut paths = Vec::new();
        for (kind, &length) in lengths.iter().enumerate() {
            for _ in 0..digits[group][kind] {
                paths.push(buckets[length].pop().unwrap());
            }
        }
        for (index, path) in paths.iter().enumerate() {
            next[*path.last().unwrap()] = paths[(index + 1) % paths.len()][0];
        }
        state -= group;
    }
    true
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let k: usize = tokens.next().unwrap().parse().unwrap();
    let mut next = vec![0; n + 1];
    for value in next.iter_mut().skip(1) {
        *value = tokens.next().unwrap().parse().unwrap();
    }
    if !complete(n, k, &mut next) {
        println!("No");
        return;
    }
    let mut output = String::from("Yes\n");
    for (index, value) in next.iter().enumerate().skip(1) {
        if index != 1 {
            output.push(' ');
        }
        write!(output, "{}", value).unwrap();
    }
    output.push('\n');
    print!("{}", output);
}
