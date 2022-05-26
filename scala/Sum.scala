import scala.io._ //scala.ipのパッケージをすべてインポート"_"はワイルドカード
def toInt(in: String): Option[Int] = //toIntメソッドの定義Stringのパラメータを持つ 戻り値はOptionのint
try{
    Some(Integer.parseInt(in.trim))//数値変換
}catch{
    case e: NumberFormatException => None //数値変換できないときNoneを返す
}

def sum(in: Seq[String]) = {
    var ints = in.flatMap(s => toInt(s))
    ints.foldLeft(0)((a,b)=> a + b)
}

println("Enter some numbers and press")
val input = Source.fromInputStream(System.in)
val lines = input.getLines.collect
println("Sum " +sum(lines))