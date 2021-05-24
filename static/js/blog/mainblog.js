function myfunct(){
    var title = document.getElementById("title").textContent;
    var date = document.getElementById("date").textContent;
    var author = document.getElementById("author").textContent;
    var likes = document.getElementById("likes").textContent;
    var description = document.getElementById("description").textContent;
    document.getElementById("1").innerHTML = title;
    document.getElementById("2").innerHTML = date;
    document.getElementById("3").innerHTML = author;
    document.getElementById("4").innerHTML = likes;
    document.getElementById("5").innerHTML = description;
}