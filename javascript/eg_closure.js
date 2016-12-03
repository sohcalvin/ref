
var obj1 = function(){
  var i=1;
  return {
    "print" : function(){ console.log(i); },
    "increment" : function(){ i=i+ 1;}
  }
}();
obj1.increment();
obj1.print();
