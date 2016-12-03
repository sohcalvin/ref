var i = 88;
var f = function() {
  var i = 0;
  return function() {
    i = i + 1;
    console.log(i);
  }
}();
i = 99;

f();
f();
