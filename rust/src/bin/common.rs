
pub fn split_num(mut n: usize) -> Vec<usize> {
    let mut nums = vec![];
    while n > 0 {
        let x = n % 10;
        n = (n - x) / 10;
        nums.push(x);
    }
    nums
}

pub fn gcd(mut a: usize, mut b: usize) -> usize {
    while b {
        let tmp = a;
        a = b;
        b = tmp % b;
    }
    a
}
