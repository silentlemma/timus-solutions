use std::io::{self, Read};

const FACES: usize = 4;

fn search(a: &[u8], b: &[u8], p: &mut Vec<usize>) -> bool {
    if p.len() == FACES {
        let inversions = (0..FACES)
            .flat_map(|i| (i + 1..FACES).map(move |j| (i, j)))
            .filter(|&(i, j)| p[i] > p[j])
            .count();
        // the rotations of a tetrahedron move its faces by exactly the even permutations
        return inversions % 2 == 0 && (0..FACES).all(|i| b[i] == a[p[i]]);
    }
    for k in 0..FACES {
        if !p.contains(&k) {
            p.push(k);
            let found = search(a, b, p);
            p.pop();
            if found {
                return true;
            }
        }
    }
    false
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let words: Vec<&[u8]> = input.split_whitespace().map(|w| w.as_bytes()).collect();
    let same = search(words[0], words[1], &mut Vec::new());
    println!("{}", if same { "equal" } else { "different" });
}
