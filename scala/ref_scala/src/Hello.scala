class Hello {
  var myField : String = "";
  def this(value : String) = {
    this();
    this.myField = value;
  }

  def divideByZero() : Double={
    return 1/0;
  }

  override def toString: String = s"Hello back ${myField}"
}


object Hello{
  def main(args : Array[String] )={
    // 1) toString()
    val helo = new Hello("csoh");
    println(helo)

    //2) match
    var a = "theValue";
    var myResult =
      a match {
        case "someValue"   => a + " A";
        case "thisValue"   => a + " B";
        case "theValue"    => a + " C";
        case "doubleValue" => a + " D";
      }
    println(myResult)


    // 3) try catch finally
    try {
      val x = helo.divideByZero()
    }catch{
      case e : Exception => {
        println(e)
      }
    }finally{
      print("Finally it's over")
    }


  }
}
