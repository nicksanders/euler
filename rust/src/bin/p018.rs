
use std::io::Read;
use std::fs::File;

fn calc_sum_at_row(mut nums: Vec<Vec<usize>>, row_num: usize) -> usize {

    for i in (0..nums[row_num].len()) {
        nums[row_num][i] += *[nums[row_num + 1][i], nums[row_num + 1][i + 1]].iter().max().unwrap();
    }

    if nums[row_num].len() == 1 {
        return nums[row_num][0];
    } else {
        return calc_sum_at_row(nums.clone(), row_num - 1);
    }
}

fn main() {

    let mut s = String::new();
    let mut f = File::open("../data/p018.txt").unwrap();
    let _ = f.read_to_string(&mut s);

    let mut nums: Vec<Vec<usize>> = vec![];

    for l in s.trim_matches('\n').split("\n") {
        nums.push(l.split(" ").map(|x| x.parse::<usize>().unwrap()).collect());
    }

    let row_num = nums.len() - 2;
    println!("{}", calc_sum_at_row(nums, row_num));

}
