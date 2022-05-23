
const promise = new Promise(function(resolve,reject){
    // resolve(variable1);
    reject(variable2);
})
.then((variable1)=>{
    console.log("成功")
})

.catch((variable2) =>{
    console.log("reject")
})