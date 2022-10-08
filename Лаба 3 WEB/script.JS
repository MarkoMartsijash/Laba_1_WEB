console.log("Do you want play to chess?");

function chessBoard(a, b){

    console.log();
    console.log("Hey! It is your chess board!");
    console.log();
    
    let section1 = "@@";
    let section2 = "   ";
    let even = "";                            //парні
    let odd = "";                             //не парні

    for (i = 1; i <= a; i++){
        if(i % 2 == 0){
            even += section1;
            odd += section2;
        }
        else{
            even += section2;
            odd += section1;
        }
    }
    for(j = 1; j <= b; j++){
        if(j % 2 == 0){
            console.log(even);
        }
        else{
            console.log(odd);
        }
    }
}

chessBoard(8, 8);

console.log();
console.log();
console.log("Task №2");
console.log();

var a = 5;

for(let i = 1; i < 101; i++){
    if(i % 3 == 0){
        console.log("A multiple of three");
    }
    else{
        console.log(i);
    }
};

console.log();
console.log();
console.log("Task №3");
console.log();

"" + 1 + 0                                          //string10
console.log(typeof "" + 1 + 0);

"" - 1 + 0                                          //NaN
console.log(typeof "" - 1 + 0);

true + false                                        //boolean false
console.log(typeof true + false);

6 / "3"                                             //NaN
console.log(typeof 6 / "3");

"2" * "3"                                          //NaN
console.log(typeof "2" * "3");

4 + 5 + "px"                                       //number5px 
console.log(typeof 4 + 5 + "px");

"$" + 4 + 5                                        //string45
console.log(typeof "$" + 4 + 5);

"4" - 2                                            //NaN
console.log(typeof "4" - 2);

"4px" - 2                                          //NaN
console.log(typeof "4px" - 2);

7 / 0                                              //NaN
console.log(typeof 7 / 0);

"  -9\n" + 5                                       //string5   
console.log(typeof "  -9\n" + 5);

"  -9\n" - 5                                       //NaN
console.log(typeof "  -9\n" - 5);

5 && 2                                             //2
console.log(typeof 5 && 2);

2 && 5                                             //5
console.log(typeof 2 && 5);

5 || 0                                             //number
console.log(typeof 5 || 0);

0 || 5                                             //number
console.log(typeof 0 || 5);

null + 1                                           //object1
console.log(typeof null + 1);

undefined + 1                                      //undefined1   
console.log(typeof undefined + 1);

null == "\n0\n"                                    //false
console.log(typeof null == "\n0\n");

+null == +"\n0\n"                                  //false
console.log(typeof +null == +"\n0\n");