
extern crate num;
use std::collections::HashSet;
use num::bigint::{BigUint, ToBigUint};

fn main() {

    let mut nums: HashSet<BigUint> = HashSet::new();

    for a in (2..101) {
        for b in (2..101) {
            nums.insert(num::pow(a.to_biguint().unwrap(), b));
        }
    }

    println!("{:?}", nums.len());

}
