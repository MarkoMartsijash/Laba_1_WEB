let a = 1;

console.log("Task №1");
console.log();

function task1(a){
    console.log(a == 0);
}
task1(1);
task1(0);
task1(-3);

console.log();
console.log();


console.log("Task №2");
console.log();

function task2(a){
    console.log(a > 0);
}
task2(1);
task2(0);
task2(-3);

console.log();
console.log();


console.log("Task №3");
console.log();

function task3(a){
    console.log(a < 0);
}
task3(1);
task3(0);
task3(-3);

console.log();
console.log();



console.log("Task №4");
console.log();

function task4(a){
    console.log(a >= 0);
}
task4(1);
task4(0);
task4(-3);

console.log();
console.log();



console.log("Task №5");
console.log();

function task5(a){
    console.log(a <= 0);
}
task5(1);
task5(0);
task5(-3);

console.log();
console.log();




console.log("Task №6");
console.log();

function task6(a){
    console.log(a != 0);
}
task6(1);
task6(0);
task6(-3);

console.log();
console.log();


console.log("Task №7");
console.log();

function task7(a){
    console.log(a == "test");
}
task7("test");
task7("тест");
task7("3");

console.log();
console.log();



console.log("Task №8");
console.log();

function task8(a){
    if(a == "1" & typeof "1" == typeof "1"){
        console.log("True");
    }
    else{
        console.log("False");
    }
}
task8("1");
task8(1);
task8(3);

console.log();
console.log();



console.log("Task №9");
console.log("Option 1");

function task9(a){
    if(a == true){
        console.log("True");
    }
    else{
        console.log("False");
    }
}
task9(true);
task9(false);

console.log();
console.log("Option 2");
console.log();

function task9_2(a){
    console.log(a == true);
}
task9_2(true);
task9_2(false);

console.log();
console.log();



console.log("Task №10");
console.log("Option 1");

function task10(a){
    if(a != true){
        console.log("True");
    }
    else{
        console.log("False");
    }
}
task10(true);
task10(false);

console.log();
console.log("Option 2");
console.log();

function task10_2(a){
    console.log(a != true);
}
task10_2(true);
task10_2(false);

console.log();
console.log();


console.log("Task №11");
console.log();

function task11(a){
    if(a > 0 & a < 5){
        console.log("True");
    }
    else{
        console.log("False");
    }
}
task11(5);
task11(0);
task11(-3);
task11(2);

console.log();
console.log();



console.log("Task №12");
console.log();

function task12(a){
    if(a == 0 || a == 2){
        console.log(a + 7);
    }
    else{
        console.log(a / 10);
    }
}
task12(5);
task12(0);
task12(-3);
task12(2);

console.log();
console.log();



console.log("Task №13");
console.log();

function task13(a, b){
    if(a <= 1 & b >= 3){
        console.log(a + b);
    }
    else{
        console.log(a - b);
    }
}
task13(1, 3);
task13(0, 6);
task13(3, 5);

console.log();
console.log();


console.log("Task №14");
console.log();

function task14(a, b){
    if(a > 2 & a < 11 || b >= 6 & b < 14){
        console.log("True");
    }
    else{
        console.log("False");
    }
}
task14(3, 5);
task14(1, 15);
task14(-3, 3);

console.log();
console.log();


console.log("Task №15");
console.log();

let result;

for(let num = 1; num <= 5; num++){
    switch(num){
        case 1:
            result = "Winter";
            break;
                            
        case 2:
            result = "Spring";
            break;
        
        case 3:
            result = "Summer";
            break;

        case 4:
            result = "Autumn";
            break;
        
        default:
            result = "Some time of the year";
    }
    console.log(result);
    console.log();
}

