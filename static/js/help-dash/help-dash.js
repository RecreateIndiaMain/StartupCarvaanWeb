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
}