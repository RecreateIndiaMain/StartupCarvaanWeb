console.log('Connected!');
const desc = document.querySelectorAll('.desc');
const commentsBtn = document.querySelector('.btn-comments');
const arrowBtn = document.querySelector('#arrow-btn');
const cmmts = document.querySelectorAll('.cmmts');
const blogs = document.querySelectorAll('.blog-data');

//To Descrease the len of the desc on SideBar
for(let i = 0; i<desc.length; i++){
    if(desc[i].textContent.length>80){
        desc[i].textContent = desc[i].textContent.substring(0, 80) + '...';
    }
}

//To make the Comments btn rotate Icon and to add active tag to sideBar
for(let i = 0; i<blogs.length; i++){
    blogs[i].addEventListener('click', ()=> {
        for(let i = 0; i<blogs.length; i++){
            blogs[i].classList.remove('active');
        }
        blogs[i].classList.add('active');
        console.log(blogs[i].id);
    });
}

commentsBtn.addEventListener('click', ()=>{
    if(commentsBtn.classList[1] !== 'active'){
        arrowBtn.classList.add('rotate');
        commentsBtn.classList.add('active');
    }else{
        arrowBtn.classList.remove('rotate');
        commentsBtn.classList.remove('active');
    }
})

//To make the Comments Show on click;
commentsBtn.addEventListener('click', ()=>{
    for(let i = 0; i<cmmts.length; i++){
        if(cmmts[i].classList[1] === 'show'){
            cmmts[i].classList.remove('show')
        }else{
            cmmts[i].classList.add('show');
        }
    }
})
