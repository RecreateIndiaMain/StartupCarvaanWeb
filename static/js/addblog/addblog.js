console.log("I am here from add blog");

const videoBtn = document.querySelectorAll('.video-btn');
const imageBtn = document.querySelectorAll('.image-btn');

const imageInput = document.querySelectorAll('.image-input');
const videoInput = document.querySelectorAll('.video-input');


console.log(imageBtn[0].classList[1]);
imageBtn[0].addEventListener('click', ()=>{
    console.log('clicked');
    if( imageBtn[0].classList[1] ){
        imageBtn[0].classList.remove('active-btn');
        imageInput[0].classList.remove('input-active');
    }
    else {
        videoBtn[0].classList.remove('active-btn');
        videoInput[0].classList.remove('input-active');
        imageBtn[0].classList.add('active-btn');
        imageInput[0].classList.add('input-active');
    }
    console.log(imageBtn[0].classList);
});

videoBtn[0].addEventListener('click', ()=>{
    console.log('clicked');
    if( videoBtn[0].classList[1] ){
        videoBtn[0].classList.remove('active-btn');
        videoInput[0].classList.remove('input-active');
    }
    else {
        imageBtn[0].classList.remove('active-btn');
        imageInput[0].classList.remove('input-active');
        videoBtn[0].classList.add('active-btn');
        videoInput[0].classList.add('input-active');
    }
    console.log(videoBtn[0].classList);
});

