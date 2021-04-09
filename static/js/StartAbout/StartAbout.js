console.log("I am here");

// const blogVideo = document.querySelectorAll('.blog-page');
// const blogContent = document.querySelectorAll('.blog-content');

// for(let i = 0; i<blogVideo.length; i++){
//     if(i%2 == 0){
//         blogVideo[i].classList.add('reverse');
//         blogContent[i].classList.add('spacing');
//     }
// }

google.charts.load("current", { packages: ["corechart"] });
google.charts.setOnLoadCallback(drawChart);

function drawChart() {
  var data = google.visualization.arrayToDataTable([
    ["Year", "Sales", "Expenses"],
    ["2004", 1000, 400],
    ["2005", 1170, 460],
    ["2006", 660, 1120],
    ["2007", 1030, 540],
  ]);

  var options = {
    title: "Company Performance",
    curveType: "function",
    legend: { position: "bottom" },
  };
  const charts = document.querySelectorAll('#curve_chart');
  for(let i = 0; i<charts.length; i++){
      var chart = new google.visualization.LineChart(charts[i]);
      chart.draw(data, options)
  }
}
