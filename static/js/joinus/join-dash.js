const viewModal = document.querySelectorAll('#btn-view');
const dataRows = document.querySelectorAll('.data-row');
const modalB = document.querySelector('.modal-content');
const closeModals = document.querySelector('.modal-close');
closeModals.addEventListener('click', () => {
    modalB.classList.add('hide-modal');
});


for(let i = 0; i<dataRows.length; i++)
{
    viewModal[i].addEventListener('click', () => {
        var teamname = document.querySelectorAll("#teamname")[i];
        var email = document.querySelectorAll("#email")[i];
        var number = document.querySelectorAll("#number")[i];
        var teamsize = document.querySelectorAll("#teamsize")[i];
        var filename = document.querySelectorAll("#filename")[i];
        var choice = document.querySelectorAll("#choice")[i];
        var status = document.querySelectorAll("#status")[i];
        modalB.classList.remove('hide-modal');
        document.getElementById("1").innerHTML = teamname.textContent;
        document.getElementById("2").innerHTML = email.textContent;
        document.getElementById("3").innerHTML = number.textContent;
        document.getElementById("4").innerHTML = teamsize.textContent;
        document.getElementById("5").innerHTML = filename.textContent;
        document.getElementById("6").innerHTML = choice.textContent;
        document.getElementById("7").innerHTML = status.textContent;
    })
}