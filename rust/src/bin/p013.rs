
extern crate num;

use std::io::Read;
use std::fs::File;
use num::bigint::{BigUint, ToBigUint};

fn main() {

    let mut s = String::new();
    let mut f = File::open("../data/p013.txt").unwrap();
    let _ = f.read_to_string(&mut s);

    let mut nums: Vec<BigUint> = vec![];

    for l in s.trim_matches('\n').split("\n") {
        nums.push(BigUint::parse_bytes(l.as_bytes(), 10).unwrap());
    }

    let res: BigUint = nums.iter().fold(0.to_biguint().unwrap(), |acc, ref x| acc + *x);
    let res_str = res.to_string()[0 .. 10].to_string();

    println!("{}", res_str);

}
