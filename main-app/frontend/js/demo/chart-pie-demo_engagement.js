// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

// Pie Chart Example
function loadInstaEngagementComments() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      data = JSON.parse(this.responseText)
      platform1094 = data["platform1094"] * 100
      freshfruitlab = data["freshfruitslab"] * 100
      herit8ge = data["herit8ge"] * 100
      var ctx = document.getElementById("myPieChart_insta");
      var myPieChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
          labels: ["Platform 1094", "Fresh Fruits Lab", "Herit8ge"],
          datasets: [{
            data: [platform1094, freshfruitlab, herit8ge],
            backgroundColor: ['#4e73df', '#1cc88a', '#36b9cc'],
            hoverBackgroundColor: ['#2e59d9', '#17a673', '#2c9faf'],
            hoverBorderColor: "rgba(234, 236, 244, 1)",
          }],
        },
        options: {
          maintainAspectRatio: false,
          tooltips: {
            backgroundColor: "rgb(255,255,255)",
            bodyFontColor: "#858796",
            borderColor: '#dddfeb',
            borderWidth: 1,
            xPadding: 15,
            yPadding: 15,
            displayColors: false,
            caretPadding: 10,
          },
          legend: {
            display: false
          },
          cutoutPercentage: 80,
        },
      });
    }
  }
  xhttp.open("GET", "http://localhost:5000/insta/engagement_comments", true);
  xhttp.send();
}


// Pie Chart Example
function loadFbEngagementComments() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      data = JSON.parse(this.responseText)
      platform1094 = data["platform1094"] * 100
      freshfruitlab = data["freshfruitslab"] * 100
      herit8ge = data["herit8ge"] * 100
      var ctx = document.getElementById("myPieChart_fb");
      var myPieChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
          labels: ["Platform 1094", "Fresh Fruits Lab", "Herit8ge"],
          datasets: [{
            data: [platform1094, freshfruitlab, herit8ge],
            backgroundColor: ['#4e73df', '#1cc88a', '#36b9cc'],
            hoverBackgroundColor: ['#2e59d9', '#17a673', '#2c9faf'],
            hoverBorderColor: "rgba(234, 236, 244, 1)",
          }],
        },
        options: {
          maintainAspectRatio: false,
          tooltips: {
            backgroundColor: "rgb(255,255,255)",
            bodyFontColor: "#858796",
            borderColor: '#dddfeb',
            borderWidth: 1,
            xPadding: 15,
            yPadding: 15,
            displayColors: false,
            caretPadding: 10,
          },
          legend: {
            display: false
          },
          cutoutPercentage: 80,
        },
      });
    }
  }
  xhttp.open("GET", "http://localhost:5002/fb/engagement_comments", true);
  xhttp.send();
}


function reviewsGoogle(){
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      data = JSON.parse(this.responseText)["result"]
      result = []
      for (info in data){
        result.push(data[info])
      }
      console.log(result)
      var ctx = document.getElementById("pieGReviews");
      var myPieChart = new Chart(ctx, {
        type: 'pie',
        data: {
          labels: ["0", "1", "2", "3", "4" , "5"],
          datasets: [{
            data: result,
            backgroundColor: ['#4e73df', '#1cc88a', '#36b9cc', '#d4db4f', '#220ced', '#6c07a3'],
            borderWidth: 1
          }],
        },
        options: {
          maintainAspectRatio: false,
          tooltips: {
            backgroundColor: "rgb(255,255,255)",
            bodyFontColor: "#858796",
            borderColor: '#dddfeb',
            borderWidth: 1,
            xPadding: 15,
            yPadding: 15,
            displayColors: false,
            caretPadding: 10,
          },
          legend: {
            display: false
          },
          cutoutPercentage: 80,
        },
      });
    }
  }
  xhttp.open("GET", "http://localhost:5007/reviews/grating", true);
  xhttp.send();
}

function reviewsTrip(){
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      data = JSON.parse(this.responseText)["result"]
      result = []
      for (info in data){
        result.push(data[info])
      }
      console.log(result)
      var ctx = document.getElementById("pieTReviews");
      var myPieChart = new Chart(ctx, {
        type: 'pie',
        data: {
          labels: ["0", "1", "2", "3", "4" , "5"],
          datasets: [{
            data: result,
            backgroundColor: ['#4e73df', '#1cc88a', '#36b9cc', '#d4db4f', '#220ced', '#6c07a3'],
            borderWidth: 1
          }],
        },
        options: {
          maintainAspectRatio: false,
          tooltips: {
            backgroundColor: "rgb(255,255,255)",
            bodyFontColor: "#858796",
            borderColor: '#dddfeb',
            borderWidth: 1,
            xPadding: 15,
            yPadding: 15,
            displayColors: false,
            caretPadding: 10,
          },
          legend: {
            display: false
          },
          cutoutPercentage: 80,
        },
      });
    }
  }
  xhttp.open("GET", "http://localhost:5007/reviews/trating", true);
  xhttp.send();
}
