class Animal {
    name : String; // Note that the var keyword is not used here!!
    constructor(n :String){
        this.name = n;
    }

    sound(): String{
        return "Gibberish";
    }
}

export class Dog extends Animal{
    sound() :String {
        return "Woof woof!";
    }
}

