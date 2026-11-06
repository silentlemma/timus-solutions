use std::io::{self, Read};

#[derive(Clone, Copy)]
struct Offer {
    mask: usize,
    price: u16,
}

fn main() -> io::Result<()> {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input)?;
    let mut tokens = input
        .split_ascii_whitespace()
        .map(|s| s.parse::<usize>().unwrap());
    let caps = tokens.next().unwrap();
    let mut offers: Vec<_> = (0..caps)
        .map(|cap| Offer {
            mask: 1 << cap,
            price: tokens.next().unwrap() as u16,
        })
        .collect();
    let bundles = tokens.next().unwrap();
    for _ in 0..bundles {
        let price = tokens.next().unwrap() as u16;
        let size = tokens.next().unwrap();
        let mask = (&mut tokens)
            .take(size)
            .fold(0, |mask, cap| mask | 1 << (cap - 1));
        offers.push(Offer { mask, price });
    }
    let count = tokens.next().unwrap_or(0);
    let wanted = tokens
        .take(count)
        .fold(0, |mask, cap| mask | 1 << (cap - 1));
    for offer in &mut offers {
        offer.mask &= wanted;
    }
    let useful: Vec<_> = offers
        .iter()
        .enumerate()
        .filter_map(|(i, &offer)| {
            let dominated = offers.iter().enumerate().any(|(j, better)| {
                better.mask & offer.mask == offer.mask
                    && (better.price < offer.price
                        || better.price == offer.price && (better.mask != offer.mask || j < i))
            });
            (offer.mask != 0 && !dominated).then_some(offer)
        })
        .collect();

    let mut order: Vec<_> = (0..caps).filter(|&cap| wanted & (1 << cap) != 0).collect();
    order.sort_unstable_by_key(|&cap| useful.iter().filter(|o| o.mask & (1 << cap) != 0).count());
    let full = (1usize << order.len()) - 1;
    let mut choices = vec![Vec::new(); order.len()];
    for offer in useful {
        let mut mask = 0;
        for (bit, &cap) in order.iter().enumerate() {
            if offer.mask & (1 << cap) != 0 {
                mask |= 1 << bit;
            }
        }
        for (bit, list) in choices.iter_mut().enumerate() {
            if mask & (1 << bit) != 0 {
                list.push((full ^ mask, offer.price));
            }
        }
    }
    // Buying each cap separately costs at most 20,000.
    let mut cheapest = vec![0u16; full + 1];
    for missing in 1..=full {
        cheapest[missing] = choices[missing.trailing_zeros() as usize]
            .iter()
            .map(|&(keep, price)| price + cheapest[missing & keep])
            .min()
            .unwrap();
    }
    println!("{}", cheapest[full]);
    Ok(())
}
