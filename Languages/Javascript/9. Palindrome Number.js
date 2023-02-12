/**
 * @param {number} x
 * @return {boolean}
 */
function reverseInt(x) {
  var digits = ("" + x).split("");
  return digits.reverse().join("");
}

var isPalindrome = function (x) {
  var stringReverse = reverseInt(x);
  if (x.toString() == stringReverse) {
    return true;
  }
  return false;
};
