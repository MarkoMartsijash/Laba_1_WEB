function Timer(){
    let second = prompt("Enter your time (second)");
    let minute = 0;
    let hour = 0;

    


    
    let counterS = setInterval(
        function S(){
            while(second > 60){
                minute ++;
                second -= 60;
            }
            while(minute >= 60){
                hour ++;
                minute -= 60;
            }
            document.getElementById('second').innerHTML=`${second}`;
            document.getElementById('minute').innerHTML=`${minute}`;
            document.getElementById('hour').innerHTML=`${hour}`;
                     

            if(minute == 0 && hour > 0){
                hour--;
                minute += 59;
                second += 60;
            }

            if(second == 0 && minute > 0){
                minute--;
                second += 60;
            }

            if(second <= 0 || second == 0){
                clearInterval(counterS);
                }

            
            if(hour == 0 && minute == 0 && second == 0){
                alert("Time out!");
            }

            second --;

        },1000
    )

    
}
Timer();