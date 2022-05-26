object HelloWorld{
    def main(args:Array[String]){
        println("Hello world")
    }
}

def nano() ={
    println("Getting nano")
    System.nanoTime
}



for {i <- 1 to 10
     j <- 1 to 10}
    println(i*j)