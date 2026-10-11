use std::io::{self, Read};

// marks everyone reachable from the victims along one kind of link
fn clear(start: &[usize], links: &[Vec<usize>], cleared: &mut [bool]) {
    let mut stack = start.to_vec();
    let mut seen = vec![false; links.len()];
    while let Some(v) = stack.pop() {
        for &u in &links[v] {
            if !seen[u] {
                seen[u] = true;
                cleared[u] = true;
                stack.push(u);
            }
        }
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let words: Vec<&str> = input.split_ascii_whitespace().collect();
    let n: usize = words[0].parse().unwrap();
    let blood = words.iter().position(|&w| w == "BLOOD").unwrap();
    let pairs: Vec<usize> = words[1..blood].iter().map(|w| w.parse().unwrap()).collect();
    let victims: Vec<usize> = words[blood + 1..]
        .iter()
        .map(|w| w.parse().unwrap())
        .collect();
    let (mut parents, mut children) = (vec![Vec::new(); n + 1], vec![Vec::new(); n + 1]);
    for p in pairs.chunks(2) {
        parents[p[0]].push(p[1]);
        children[p[1]].push(p[0]);
    }
    let mut cleared = vec![false; n + 1];
    for &v in &victims {
        cleared[v] = true;
    }
    // the werewolf spares its ancestors and descendants, so no ancestor and
    // no descendant of a victim can be the werewolf
    clear(&victims, &parents, &mut cleared);
    clear(&victims, &children, &mut cleared);
    let suspects: Vec<String> = (1..=n)
        .filter(|&u| !cleared[u])
        .map(|u| u.to_string())
        .collect();
    if suspects.is_empty() {
        println!("0");
    } else {
        println!("{}", suspects.join(" "));
    }
}
