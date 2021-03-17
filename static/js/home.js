window.addEventListener('scroll', ()=>{
    const scroll = document.querySelector('.gotobtn');
    scroll.classList.toggle('active', window.scrollY>500);
})