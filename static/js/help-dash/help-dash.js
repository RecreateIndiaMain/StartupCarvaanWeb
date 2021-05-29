<<<<<<< HEAD
const showModal = document.querySelectorAll('#btn-view');
const dataRow = document.querySelectorAll('.data-row');
const modalBtn = document.querySelector('.modal-content');
const closeModal = document.querySelector('.modal-close');
closeModal.addEventListener('click', () => {
    modalBtn.classList.add('hide-modal');
});


for(let i = 0; i<dataRow.length; i++)
{
    showModal[i].addEventListener('click', () => {
        var title = document.querySelectorAll("#title")[i];
        var date = document.querySelectorAll("#date")[i];
        var comment = document.querySelectorAll("#comment")[i];
        var status = document.querySelectorAll("#status")[i];
        modalBtn.classList.remove('hide-modal');
        document.getElementById("1").innerHTML = title.textContent;
        document.getElementById("2").innerHTML = comment.textContent;
        document.getElementById("3").innerHTML = date.textContent;
        document.getElementById("4").innerHTML = status.textContent;
    })
=======
function myfunct(){
    var title = document.getElementById("title").textContent;
    var date = document.getElementById("date").textContent;
    var comment = document.getElementById("comment").textContent;
    var status = document.getElementById("status").textContent;
    var author = document.getElementById("author").textContent;
    document.getElementById("1").innerHTML = title;
    document.getElementById("2").innerHTML = comment;
    document.getElementById("3").innerHTML = date;
    document.getElementById("4").innerHTML = status;
    document.getElementById("5").innerHTML = author;
>>>>>>> f04145b318d6bc2816596527fe7815da61029446
}