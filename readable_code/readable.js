//見にくいコード
var remove_one = function(array,value_to_remove){
    var index_to_remove = null;
    for (var i = 0; i< array.length; i+=1){
        if(array[i] === value_to_remove){
            index_to_remove = i;
            break;
        }
    }

    if(index_to_remove !== null){
        array.splice(index_to_remove,1);
    }
};


//index_to_removeは中間結果を保持するために使っている

// index_removeを削除することによって簡潔になった。

var remove_one = function(array,value_to_remove){
    for(var i = 0; i < array.length ; i+=1){
        if(array[i] === value_to_remove){
            array.splice(i,1);
            return;
        }
    }
}