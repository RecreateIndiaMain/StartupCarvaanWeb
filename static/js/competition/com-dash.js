const viewdata = document.querySelectorAll('#btn-view');
const data = document.querySelectorAll('.data-row');
const modalBold = document.querySelector('.modal-content');
const closeM = document.querySelector('.modal-close');
closeM.addEventListener('click', () => {
    modalBold.classList.add('hide-modal');
});


for(let i = 0; i<data.length; i++)
{
    viewdata[i].addEventListener('click', () => {
        var teamname = document.querySelectorAll("#title")[i];
        var email = document.querySelectorAll("#email")[i];
        var number = document.querySelectorAll("#phonenumber")[i];
        var link = document.querySelectorAll("#link")[i];
        var description = document.querySelectorAll("#desc")[i];
        var status = document.querySelectorAll("#status")[i];
        modalBold.classList.remove('hide-modal');
        document.getElementById("1").innerHTML = teamname.textContent;
        document.getElementById("2").innerHTML = email.textContent;
        document.getElementById("3").innerHTML = number.textContent;
        document.getElementById("4").innerHTML = link.textContent;
        document.getElementById("5").innerHTML = description.textContent;
        document.getElementById("6").innerHTML = status.textContent;
    })
}