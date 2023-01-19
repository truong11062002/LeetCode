/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function (nums) {
  let i = 1;
  let k = 1;

  let n = nums.length;

  while (i < n) {
    while (i < n && nums[k - 1] == nums[i]) {
      i++;
    }
    if (i < n) {
      nums[k] = nums[i];
      k++;
    }
  }

  return k;
};
