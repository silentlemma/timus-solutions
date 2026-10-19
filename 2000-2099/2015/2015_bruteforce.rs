use std::io::{self, Read};

const APARTMENT_FIELDS: usize = 3;

fn solve(
    budget: i32,
    alone: &[i32; 2],
    friends: &[[i32; 2]],
    apartments: &[[i32; APARTMENT_FIELDS]],
) -> [usize; 2] {
    let mut best = -1;
    let mut choice = [0, 0];
    for (i, &[rooms, price, benefit]) in apartments.iter().enumerate() {
        if price <= budget {
            let score = benefit + alone[(rooms - 1) as usize];
            if score > best {
                best = score;
                choice = [i + 1, 0];
            }
        }
        if rooms == 2 && price <= 2 * budget {
            for (j, &[money, value]) in friends.iter().enumerate() {
                if price <= 2 * money {
                    let score = benefit + value;
                    if score > best {
                        best = score;
                        choice = [i + 1, j + 1];
                    }
                }
            }
        }
    }
    choice
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut t = input.split_whitespace().map(|s| s.parse::<i32>().unwrap());
    let budget = t.next().unwrap();
    let alone = [t.next().unwrap(), t.next().unwrap()];
    let n = t.next().unwrap() as usize;
    let friends: Vec<[i32; 2]> = (0..n)
        .map(|_| [t.next().unwrap(), t.next().unwrap()])
        .collect();
    let m = t.next().unwrap() as usize;
    let apartments: Vec<[i32; APARTMENT_FIELDS]> = (0..m)
        .map(|_| [t.next().unwrap(), t.next().unwrap(), t.next().unwrap()])
        .collect();
    let choice = solve(budget, &alone, &friends, &apartments);
    if choice[0] == 0 {
        println!("Forget about apartments. Live in the dormitory.");
    } else if choice[1] == 0 {
        println!("You should rent the apartment #{} alone.", choice[0]);
    } else {
        println!(
            "You should rent the apartment #{} with the friend #{}.",
            choice[0], choice[1]
        );
    }
}
