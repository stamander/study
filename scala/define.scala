class Foo 

public class Foo {

}

new Foo

class Bar(name: String)

new Bar("Working...")


class Baz(name: String){
    if(name == null) throw new Exception("Name is null")
}

trait Dog

class Fizz2(name: String) extends Bar(name) with Dog


//トレイト....クラスの継承を使わずにコードの再利用を行うための仕組み
trait Cat{
    def meow() : String
}

aa