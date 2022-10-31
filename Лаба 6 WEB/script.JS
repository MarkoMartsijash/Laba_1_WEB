let btnPass = document.querySelector('.eye-img');
let inputPass = document.querySelector('.pass');


function seePass(){
    if(inputPass.type == 'password'){
        inputPass.type = 'text';
        btnPass.classList.add('active')
    } else{
        inputPass.type = 'password';
        btnPass.classList.remove('active')
    }
}

btnPass.onclick = seePass;