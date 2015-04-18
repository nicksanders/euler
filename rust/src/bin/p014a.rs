
use std::collections::HashMap;

fn main() {

    let limit = 1000000;
    let mut cache: HashMap<usize, usize> = HashMap::new();
    cache.insert(1, 1);
    let mut result = [1, 1];

    for i in (1..limit) {
        let mut cnt = 0;
        let mut n = i;

        while !cache.contains_key(&n) {
            if n % 2 == 0 {
                n /= 2;
            } else {
                n = (n * 3) + 1;
            }
            cnt += 1;
        }

        let tmp = *cache.get(&n).unwrap() + cnt;
        cache.insert(i, tmp);
        if tmp > result[1] {
            result = [i, tmp];
        }

    }

    println!("{} {}", result[0], result[1]);
}
