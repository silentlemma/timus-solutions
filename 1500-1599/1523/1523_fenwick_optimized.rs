use std::io::{self, Read};

const MOD: u32 = 1_000_000_000;

fn main() {
    let (n, k, flipped) = {
        let mut input = String::new();
        io::stdin().read_to_string(&mut input).unwrap();
        let mut words = input.split_ascii_whitespace();
        let n: usize = words.next().unwrap().parse().unwrap();
        let k: usize = words.next().unwrap().parse().unwrap();
        if k > n {
            println!("0");
            return;
        }
        let flipped: Vec<u16> = (0..n)
            .map(|_| (n + 1 - words.next().unwrap().parse::<usize>().unwrap()) as u16)
            .collect();
        (n, k, flipped)
    };
    let mut ways = vec![1u32; n];
    let mut tree = vec![0u32; n + 1];
    let mut total = 0;
    for _ in 1..k {
        tree.fill(0);
        total = 0;
        let mut nonzero = false;
        for (i, &coordinate) in flipped.iter().enumerate() {
            let old = ways[i];
            let (mut result, mut j) = (0, usize::from(coordinate) - 1);
            while j > 0 {
                result += tree[j];
                if result >= MOD {
                    result -= MOD;
                }
                j &= j - 1;
            }
            ways[i] = result;
            if result != 0 {
                nonzero = true;
                total += result;
                if total >= MOD {
                    total -= MOD;
                }
            }
            // Capture before overwrite: this insertion belongs to the previous layer.
            if old != 0 {
                let mut j = usize::from(coordinate);
                while j <= n {
                    tree[j] += old;
                    if tree[j] >= MOD {
                        tree[j] -= MOD;
                    }
                    j += j & j.wrapping_neg();
                }
            }
        }
        if !nonzero {
            println!("0");
            return;
        }
    }
    println!("{}", total);
}
