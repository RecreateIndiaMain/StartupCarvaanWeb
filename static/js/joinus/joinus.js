const statusBtn = document.querySelector(".status");
const msgBar = document.querySelector(".msg");
const loading = document.querySelector('.status>img');
statusBtn.addEventListener("click", ()=>{
    loading.classList.add("statuslogo")
    setTimeout(
        ()=>{
            msgBar.style.display = "inline-block";
            loading.classList.remove("statuslogo")
        }
    ,5000);
});
