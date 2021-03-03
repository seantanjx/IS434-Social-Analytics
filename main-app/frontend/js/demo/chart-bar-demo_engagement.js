// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

function number_format(number, decimals, dec_point, thousands_sep) {
  // *     example: number_format(1234.56, 2, ',', ' ');
  // *     return: '1 234,56'
  number = (number + '').replace(',', '').replace(' ', '');
  var n = !isFinite(+number) ? 0 : +number,
    prec = !isFinite(+decimals) ? 0 : Math.abs(decimals),
    sep = (typeof thousands_sep === 'undefined') ? ',' : thousands_sep,
    dec = (typeof dec_point === 'undefined') ? '.' : dec_point,
    s = '',
    toFixedFix = function (n, prec) {
      var k = Math.pow(10, prec);
      return '' + Math.round(n * k) / k;
    };
  // Fix for IE parseFloat(0.55).toFixed(0) = 0;
  s = (prec ? toFixedFix(n, prec) : '' + Math.round(n)).split('.');
  if (s[0].length > 3) {
    s[0] = s[0].replace(/\B(?=(?:\d{3})+(?!\d))/g, sep);
  }
  if ((s[1] || '').length < prec) {
    s[1] = s[1] || '';
    s[1] += new Array(prec - s[1].length + 1).join('0');
  }
  return s.join(dec);
}
function loadInstaEngagementLikes() {
  // Bar Chart Example
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      data = JSON.parse(this.responseText)
      platform1094 = data["platform1094"]
      freshfruitlab = data["freshfruitslab"]
      herit8ge = data["herit8ge"]
      console.log(data)
      var ctx = document.getElementById("insta_engage_likes");
      var myBarChart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: ["Platform1094", "Fresh Fruit Lab", "Herit8ge"],
          datasets: [{
            label: "Engagement Rate",
            backgroundColor: "#4e73df",
            hoverBackgroundColor: "#2e59d9",
            borderColor: "#4e73df",
            data: [platform1094, freshfruitlab, herit8ge],
          }],
        },
        options: {
          maintainAspectRatio: false,
          layout: {
            padding: {
              left: 10,
              right: 10,
              top: 10,
              bottom: 0
            }
          },
          scales: {
            xAxes: [{
              time: {
                unit: 'month'
              },
              gridLines: {
                display: false,
                drawBorder: false
              },
              ticks: {
                maxTicksLimit: 6
              },
              maxBarThickness: 50,
            }],
            yAxes: [{
              ticks: {
              },
              gridLines: {
                color: "rgb(234, 236, 244)",
                zeroLineColor: "rgb(234, 236, 244)",
                drawBorder: false,
                borderDash: [2],
                zeroLineBorderDash: [2]
              }
            }],
          },
          legend: {
            display: false
          },
          tooltips: {
            titleMarginBottom: 10,
            titleFontColor: '#6e707e',
            titleFontSize: 14,
            backgroundColor: "rgb(255,255,255)",
            bodyFontColor: "#858796",
            borderColor: '#dddfeb',
            borderWidth: 1,
            xPadding: 15,
            yPadding: 15,
            displayColors: false,
            caretPadding: 10,
            callbacks: {
              label: function (tooltipItem, chart) {
                var datasetLabel = chart.datasets[tooltipItem.datasetIndex].label || '';
                return datasetLabel + ": " + tooltipItem.yLabel;
              }
            }
          },
        }
      })
    }
  }
  xhttp.open("GET", "http://localhost:5000/insta/engagement_likes", true);
  xhttp.send();
}

function loadFbEngagementLikes() {
  // Bar Chart Example
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      data = JSON.parse(this.responseText)
      platform1094 = data["platform1094"]
      freshfruitlab = data["freshfruitslab"]
      herit8ge = data["herit8ge"]
      console.log(data)
      var ctx = document.getElementById("fb_engage_likes");
      var myBarChart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: ["Platform1094", "Fresh Fruit Lab", "Herit8ge"],
          datasets: [{
            label: "Engagement Rate",
            barThickness: 80,
            backgroundColor: "#4e73df",
            hoverBackgroundColor: "#2e59d9",
            borderColor: "#4e73df",
            data: [platform1094, freshfruitlab, herit8ge],
          }],
        },
        options: {
          maintainAspectRatio: false,
          layout: {
            padding: {
              left: 10,
              right: 10,
              top: 5,
              bottom: 0
            }
          },
          scales: {
            xAxes: [{
              time: {
                unit: 'month'
              },
              gridLines: {
                display: false,
                drawBorder: false
              },
              ticks: {
                maxTicksLimit: 6
              },
              maxBarThickness: 50,
            }],
            yAxes: [{
              ticks: {

              },
              gridLines: {
                color: "rgb(234, 236, 244)",
                zeroLineColor: "rgb(234, 236, 244)",
                drawBorder: false,
                borderDash: [2],
                zeroLineBorderDash: [2]
              }
            }],
          },
          legend: {
            display: false
          },
          tooltips: {
            titleMarginBottom: 10,
            titleFontColor: '#6e707e',
            titleFontSize: 14,
            backgroundColor: "rgb(255,255,255)",
            bodyFontColor: "#858796",
            borderColor: '#dddfeb',
            borderWidth: 1,
            xPadding: 15,
            yPadding: 15,
            displayColors: false,
            caretPadding: 10,
            callbacks: {
              label: function (tooltipItem, chart) {
                var datasetLabel = chart.datasets[tooltipItem.datasetIndex].label || '';
                return datasetLabel + ": " + tooltipItem.yLabel;
              }
            }
          },
        }
      })
    }
  }
  xhttp.open("GET", "http://localhost:5002/fb/engagement_likes", true);
  xhttp.send();
}


function posttypelikes() {
  // Bar Chart Example
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      data = JSON.parse(this.responseText)
      image = data["GraphImage"]
      sidecar = data["GraphSidecar"]
      video = data["GraphVideo"]
      comments = [image["comments"], sidecar["comments"], video["comments"]]
      likes = [image["likes"], sidecar["likes"], video["likes"]]
      var ctx = document.getElementById("insta_posttype");
      var myBarChart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: ["Image", "Side Car", "Video"],
          datasets: [
            {
              label: "Likes",
              barThickness: 80,
              backgroundColor: "blue",
              borderColor: "#4e73df",
              data: likes,
            },
            {
              label: "Comments",
              barThickness: 80,
              borderColor: "#4e73df",
              backgroundColor: "red",
              data: comments,
            },
          ],
        },
        options: {
          maintainAspectRatio: false,
          layout: {
            padding: {
              left: 10,
              right: 10,
              top: 5,
              bottom: 0
            }
          },
          scales: {
            xAxes: [{
              time: {
                unit: 'month'
              },
              gridLines: {
                display: false,
                drawBorder: false
              },
              ticks: {
                maxTicksLimit: 6
              },
              maxBarThickness: 50,
            }],
            yAxes: [{
              ticks: {

              },
              gridLines: {
                color: "rgb(234, 236, 244)",
                zeroLineColor: "rgb(234, 236, 244)",
                drawBorder: false,
                borderDash: [2],
                zeroLineBorderDash: [2]
              }
            }],
          },
          legend: {
            display: false
          },
          tooltips: {
            titleMarginBottom: 10,
            titleFontColor: '#6e707e',
            titleFontSize: 14,
            backgroundColor: "rgb(255,255,255)",
            bodyFontColor: "#858796",
            borderColor: '#dddfeb',
            borderWidth: 1,
            xPadding: 15,
            yPadding: 15,
            displayColors: true,
            caretPadding: 10,
            callbacks: {
              label: function (tooltipItem, chart) {
                var datasetLabel = chart.datasets[tooltipItem.datasetIndex].label || '';
                return datasetLabel + ": " + tooltipItem.yLabel;
              }
            }
          },
        }
      })
    }
  }
  xhttp.open("GET", "http://localhost:5004/insta/posttype", true);
  xhttp.send();
}



function competitorsLikesComments() {
  // Bar Chart Example
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      data = JSON.parse(this.responseText)["result"]
      enchanted_cafe = data["enchantedcafe"]
      ffl_cafe = data["freshfruitslab"]
      handlebar = data["handlebaroriginal"]
      hatterstreet = data["hatterstreet"]
      rabbit = data["thewhiterabbitsg"]
      sillpies = data["windowsillpies"]
      comments = [ffl_cafe[1], enchanted_cafe[1], handlebar[1], hatterstreet[1], rabbit[1], sillpies[1]]
      likes = [ffl_cafe[0], enchanted_cafe[0], handlebar[0], hatterstreet[0], rabbit[0], sillpies[0]]
      var ctx = document.getElementById("competitors_likes_comments");
      var myBarChart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: ["Fresh Fruits Lab", "Enchanted Cafe", "Handle Bar Original", "Hatterstreet", "The White Rabbit Sg", "Windowsill Pies"],
          datasets: [
            {
              label: "Likes",
              barThickness: 30,
              backgroundColor: "blue",
              borderColor: "#4e73df",
              data: likes,
            },
            {
              label: "Comments",
              barThickness: 30,
              borderColor: "#4e73df",
              backgroundColor: "red",
              data: comments,
            },
          ],
        },
        options: {
          maintainAspectRatio: false,
          layout: {
            padding: {
              left: 10,
              right: 10,
              top: 5,
              bottom: 0
            }
          },
          scales: {
            xAxes: [{
              time: {
              },
              gridLines: {
                display: false,
                drawBorder: false
              },
              ticks: {
                maxTicksLimit: 6
              },
              maxBarThickness: 50,
            }],
            yAxes: [{
              ticks: {

              },
              gridLines: {
                color: "rgb(234, 236, 244)",
                zeroLineColor: "rgb(234, 236, 244)",
                drawBorder: false,
                borderDash: [2],
                zeroLineBorderDash: [2]
              }
            }],
          },
          legend: {
            display: false
          },
          tooltips: {
            titleMarginBottom: 10,
            titleFontColor: '#6e707e',
            titleFontSize: 14,
            backgroundColor: "rgb(255,255,255)",
            bodyFontColor: "#858796",
            borderColor: '#dddfeb',
            borderWidth: 1,
            xPadding: 15,
            yPadding: 15,
            displayColors: true,
            caretPadding: 10,
            callbacks: {
              label: function (tooltipItem, chart) {
                var datasetLabel = chart.datasets[tooltipItem.datasetIndex].label || '';
                return datasetLabel + ": " + tooltipItem.yLabel;
              }
            }
          },
        }
      })
    }
  }
  xhttp.open("GET", "http://127.0.0.1:5008/competitor/likes_comments", true);
  xhttp.send();
}

function competitorsEngagement() {
  // Bar Chart Example
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      data = JSON.parse(this.responseText)["result"]
      enchanted_cafe = data["enchantedcafe"]
      ffl_cafe = data["freshfruitslab"]
      handlebar = data["handlebaroriginal"]
      hatterstreet = data["hatterstreet"]
      rabbit = data["thewhiterabbitsg"]
      sillpies = data["windowsillpies"]
      comments = [ffl_cafe[1], enchanted_cafe[1], handlebar[1], hatterstreet[1], rabbit[1], sillpies[1]]
      likes = [ffl_cafe[0], enchanted_cafe[0], handlebar[0], hatterstreet[0], rabbit[0], sillpies[0]]
      var ctx = document.getElementById("competitors_engagement");
      var myBarChart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: ["Fresh Fruits Lab", "Enchanted Cafe", "Handle Bar Original", "Hatterstreet", "The White Rabbit Sg", "Windowsill Pies"],
          datasets: [
            {
              label: "Likes",
              barThickness: 30,
              backgroundColor: "blue",
              borderColor: "#4e73df",
              data: likes,
            },
            {
              label: "Comments",
              barThickness: 30,
              borderColor: "#4e73df",
              backgroundColor: "red",
              data: comments,
            },
          ],
        },
        options: {
          maintainAspectRatio: false,
          layout: {
            padding: {
              left: 10,
              right: 10,
              top: 5,
              bottom: 0
            }
          },
          scales: {
            xAxes: [{
              time: {
              },
              gridLines: {
                display: false,
                drawBorder: false
              },
              ticks: {
                maxTicksLimit: 6
              },
              maxBarThickness: 50,
            }],
            yAxes: [{
              ticks: {

              },
              gridLines: {
                color: "rgb(234, 236, 244)",
                zeroLineColor: "rgb(234, 236, 244)",
                drawBorder: false,
                borderDash: [2],
                zeroLineBorderDash: [2]
              }
            }],
          },
          legend: {
            display: false
          },
          tooltips: {
            titleMarginBottom: 10,
            titleFontColor: '#6e707e',
            titleFontSize: 14,
            backgroundColor: "rgb(255,255,255)",
            bodyFontColor: "#858796",
            borderColor: '#dddfeb',
            borderWidth: 1,
            xPadding: 15,
            yPadding: 15,
            displayColors: true,
            caretPadding: 10,
            callbacks: {
              label: function (tooltipItem, chart) {
                var datasetLabel = chart.datasets[tooltipItem.datasetIndex].label || '';
                return datasetLabel + ": " + tooltipItem.yLabel;
              }
            }
          },
        }
      })
    }
  }
  xhttp.open("GET", "http://127.0.0.1:5008/competitor/engagement_rate", true);
  xhttp.send();
}

function competitorPostType() {
  // Bar Chart Example
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      data = JSON.parse(this.responseText)["result"]
      enchanted_cafe = data["enchanted"]["GraphImage"]
      handlebar = data["handlebar"]["GraphImage"]
      hatterstreet = data["hatterstreet"]["GraphImage"]
      sillipies = data["illipies"]["GraphImage"]
      rabbit = data["whiterabbit"]["GraphImage"]
      comments = [enchanted_cafe["comments"], handlebar["comments"], hatterstreet["comments"], rabbit["comments"], sillipies["comments"]]
      likes = [enchanted_cafe["likes"], handlebar["likes"], hatterstreet["likes"], rabbit["likes"], sillipies["likes"]]
      console.log(comments)
      var ctx = document.getElementById("competitor_post_type");
      var myBarChart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: ["Enchanted Cafe", "Handle Bar Original", "Hatterstreet", "The White Rabbit Sg", "Windowsill Pies"],
          datasets: [
            {
              label: "Likes",
              barThickness: 25,
              backgroundColor: "blue",
              borderColor: "#4e73df",
              data: likes
            },
            {
              label: "Comments",
              barThickness: 25,
              borderColor: "#4e73df",
              backgroundColor: "red",
              data: comments,
            },
          ],
        },
        options: {
          maintainAspectRatio: false,
          layout: {
            padding: {
              left: 10,
              right: 10,
              top: 5,
              bottom: 0
            }
          },
          scales: {
            xAxes: [{
              time: {
              },
              gridLines: {
                display: false,
                drawBorder: false
              },
              ticks: {
                maxTicksLimit: 6
              },
              maxBarThickness: 50,
            }],
            yAxes: [{
              ticks: {

              },
              gridLines: {
                color: "rgb(234, 236, 244)",
                zeroLineColor: "rgb(234, 236, 244)",
                drawBorder: false,
                borderDash: [2],
                zeroLineBorderDash: [2]
              }
            }],
          },
          legend: {
            display: false
          },
          tooltips: {
            titleMarginBottom: 10,
            titleFontColor: '#6e707e',
            titleFontSize: 14,
            backgroundColor: "rgb(255,255,255)",
            bodyFontColor: "#858796",
            borderColor: '#dddfeb',
            borderWidth: 1,
            xPadding: 15,
            yPadding: 15,
            displayColors: true,
            caretPadding: 10,
            callbacks: {
              label: function (tooltipItem, chart) {
                var datasetLabel = chart.datasets[tooltipItem.datasetIndex].label || '';
                return datasetLabel + ": " + tooltipItem.yLabel;
              }
            }
          },
        }
      })
    }
  }
  xhttp.open("GET", "http://127.0.0.1:5008/competitor/posttype", true);
  xhttp.send();
}

function competitorPostTypeSideCar() {
  // Bar Chart Example
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      data = JSON.parse(this.responseText)["result"]
      enchanted_cafe = data["enchanted"]["GraphSidecar"]
      handlebar = data["handlebar"]["GraphSidecar"]
      hatterstreet = data["hatterstreet"]["GraphSidecar"]
      sillipies = data["illipies"]["GraphSidecar"]
      rabbit = data["whiterabbit"]["GraphSidecar"]
      comments = [enchanted_cafe["comments"], handlebar["comments"], hatterstreet["comments"], rabbit["comments"], sillipies["comments"]]
      likes = [enchanted_cafe["likes"], handlebar["likes"], hatterstreet["likes"], rabbit["likes"], sillipies["likes"]]
      console.log(comments)
      var ctx = document.getElementById("competitor_post_sidecar");
      var myBarChart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: ["Enchanted Cafe", "Handle Bar Original", "Hatterstreet", "The White Rabbit Sg", "Windowsill Pies"],
          datasets: [
            {
              label: "Likes",
              barThickness: 25,
              backgroundColor: "blue",
              borderColor: "#4e73df",
              data: likes
            },
            {
              label: "Comments",
              barThickness: 25,
              borderColor: "#4e73df",
              backgroundColor: "red",
              data: comments,
            },
          ],
        },
        options: {
          maintainAspectRatio: false,
          layout: {
            padding: {
              left: 10,
              right: 10,
              top: 5,
              bottom: 0
            }
          },
          scales: {
            xAxes: [{
              time: {
              },
              gridLines: {
                display: false,
                drawBorder: false
              },
              ticks: {
                maxTicksLimit: 6
              },
              maxBarThickness: 50,
            }],
            yAxes: [{
              ticks: {

              },
              gridLines: {
                color: "rgb(234, 236, 244)",
                zeroLineColor: "rgb(234, 236, 244)",
                drawBorder: false,
                borderDash: [2],
                zeroLineBorderDash: [2]
              }
            }],
          },
          legend: {
            display: false
          },
          tooltips: {
            titleMarginBottom: 10,
            titleFontColor: '#6e707e',
            titleFontSize: 14,
            backgroundColor: "rgb(255,255,255)",
            bodyFontColor: "#858796",
            borderColor: '#dddfeb',
            borderWidth: 1,
            xPadding: 15,
            yPadding: 15,
            displayColors: true,
            caretPadding: 10,
            callbacks: {
              label: function (tooltipItem, chart) {
                var datasetLabel = chart.datasets[tooltipItem.datasetIndex].label || '';
                return datasetLabel + ": " + tooltipItem.yLabel;
              }
            }
          },
        }
      })
    }
  }
  xhttp.open("GET", "http://127.0.0.1:5008/competitor/posttype", true);
  xhttp.send();
}

function competitorPostTypeVideo() {
  // Bar Chart Example
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      data = JSON.parse(this.responseText)["result"]
      enchanted_cafe = data["enchanted"]["GraphVideo"]
      handlebar = data["handlebar"]["GraphVideo"]
      hatterstreet = data["hatterstreet"]["GraphVideo"]
      sillipies = data["illipies"]["GraphVideo"]
      rabbit = data["whiterabbit"]["GraphVideo"]
      comments = [enchanted_cafe["comments"], handlebar["comments"], hatterstreet["comments"], rabbit["comments"], sillipies["comments"]]
      likes = [enchanted_cafe["likes"], handlebar["likes"], hatterstreet["likes"], rabbit["likes"], sillipies["likes"]]
      console.log(comments)
      var ctx = document.getElementById("competitor_post_video");
      var myBarChart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: ["Enchanted Cafe", "Handle Bar Original", "Hatterstreet", "The White Rabbit Sg", "Windowsill Pies"],
          datasets: [
            {
              label: "Likes",
              barThickness: 25,
              backgroundColor: "blue",
              borderColor: "#4e73df",
              data: likes
            },
            {
              label: "Comments",
              barThickness: 25,
              borderColor: "#4e73df",
              backgroundColor: "red",
              data: comments,
            },
          ],
        },
        options: {
          maintainAspectRatio: false,
          layout: {
            padding: {
              left: 10,
              right: 10,
              top: 5,
              bottom: 0
            }
          },
          scales: {
            xAxes: [{
              time: {
              },
              gridLines: {
                display: false,
                drawBorder: false
              },
              ticks: {
                maxTicksLimit: 6
              },
              maxBarThickness: 50,
            }],
            yAxes: [{
              ticks: {

              },
              gridLines: {
                color: "rgb(234, 236, 244)",
                zeroLineColor: "rgb(234, 236, 244)",
                drawBorder: false,
                borderDash: [2],
                zeroLineBorderDash: [2]
              }
            }],
          },
          legend: {
            display: false
          },
          tooltips: {
            titleMarginBottom: 10,
            titleFontColor: '#6e707e',
            titleFontSize: 14,
            backgroundColor: "rgb(255,255,255)",
            bodyFontColor: "#858796",
            borderColor: '#dddfeb',
            borderWidth: 1,
            xPadding: 15,
            yPadding: 15,
            displayColors: true,
            caretPadding: 10,
            callbacks: {
              label: function (tooltipItem, chart) {
                var datasetLabel = chart.datasets[tooltipItem.datasetIndex].label || '';
                return datasetLabel + ": " + tooltipItem.yLabel;
              }
            }
          },
        }
      })
    }
  }
  xhttp.open("GET", "http://127.0.0.1:5008/competitor/posttype", true);
  xhttp.send();
}

function postInteractionType() {
  // Bar Chart Example
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      data = JSON.parse(this.responseText)["result"]
      competition = data["competition"]
      featured = data["featured"]
      infographics = data["infographics"]
      others = data["others"]
      product = data["product"]
      promotion = data["promotion"]
      comments = [competition[1], featured[1], infographics[1], product[1], promotion[1], others[1]]
      likes = [competition[0], featured[0], infographics[0], product[0], promotion[0], others[0]]
      var ctx = document.getElementById("interaction_insta");
      var myBarChart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: ["Competition", "Featured", "Infographics", "Product", "Promotion", "Others"],
          datasets: [
            {
              label: "Likes",
              barThickness: 25,
              backgroundColor: "blue",
              borderColor: "#4e73df",
              data: likes
            },
            {
              label: "Comments",
              barThickness: 25,
              borderColor: "#4e73df",
              backgroundColor: "red",
              data: comments,
            },
          ],
        },
        options: {
          maintainAspectRatio: false,
          layout: {
            padding: {
              left: 10,
              right: 10,
              top: 5,
              bottom: 0
            }
          },
          scales: {
            xAxes: [{
              time: {
              },
              gridLines: {
                display: false,
                drawBorder: false
              },
              ticks: {
                maxTicksLimit: 6
              },
              maxBarThickness: 50,
            }],
            yAxes: [{
              ticks: {

              },
              gridLines: {
                color: "rgb(234, 236, 244)",
                zeroLineColor: "rgb(234, 236, 244)",
                drawBorder: false,
                borderDash: [2],
                zeroLineBorderDash: [2]
              }
            }],
          },
          legend: {
            display: false
          },
          tooltips: {
            titleMarginBottom: 10,
            titleFontColor: '#6e707e',
            titleFontSize: 14,
            backgroundColor: "rgb(255,255,255)",
            bodyFontColor: "#858796",
            borderColor: '#dddfeb',
            borderWidth: 1,
            xPadding: 15,
            yPadding: 15,
            displayColors: true,
            caretPadding: 10,
            callbacks: {
              label: function (tooltipItem, chart) {
                var datasetLabel = chart.datasets[tooltipItem.datasetIndex].label || '';
                return datasetLabel + ": " + tooltipItem.yLabel;
              }
            }
          },
        }
      })
    }
  }
  xhttp.open("GET", "http://127.0.0.1:5004/insta/interaction_type", true);
  xhttp.send();
}

function postInteractionTypeFb() {
  // Bar Chart Example
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      data = JSON.parse(this.responseText)["result"]
      competition = data["competition"]
      featured = data["featured"]
      infographics = data["infographics"]
      others = data["others"]
      product = data["product"]
      promotion = data["promotion"]
      comments = [competition[1], featured[1], infographics[1], product[1], promotion[1], others[1]]
      likes = [competition[0], featured[0], infographics[0], product[0], promotion[0], others[0]]
      var ctx = document.getElementById("interaction_fb");
      var myBarChart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: ["Competition", "Featured", "Infographics", "Product", "Promotion", "Others"],
          datasets: [
            {
              label: "Likes",
              barThickness: 25,
              backgroundColor: "blue",
              borderColor: "#4e73df",
              data: likes
            },
            {
              label: "Comments",
              barThickness: 25,
              borderColor: "#4e73df",
              backgroundColor: "red",
              data: comments,
            },
          ],
        },
        options: {
          maintainAspectRatio: false,
          layout: {
            padding: {
              left: 10,
              right: 10,
              top: 5,
              bottom: 0
            }
          },
          scales: {
            xAxes: [{
              time: {
              },
              gridLines: {
                display: false,
                drawBorder: false
              },
              ticks: {
                maxTicksLimit: 6
              },
              maxBarThickness: 50,
            }],
            yAxes: [{
              ticks: {

              },
              gridLines: {
                color: "rgb(234, 236, 244)",
                zeroLineColor: "rgb(234, 236, 244)",
                drawBorder: false,
                borderDash: [2],
                zeroLineBorderDash: [2]
              }
            }],
          },
          legend: {
            display: false
          },
          tooltips: {
            titleMarginBottom: 10,
            titleFontColor: '#6e707e',
            titleFontSize: 14,
            backgroundColor: "rgb(255,255,255)",
            bodyFontColor: "#858796",
            borderColor: '#dddfeb',
            borderWidth: 1,
            xPadding: 15,
            yPadding: 15,
            displayColors: true,
            caretPadding: 10,
            callbacks: {
              label: function (tooltipItem, chart) {
                var datasetLabel = chart.datasets[tooltipItem.datasetIndex].label || '';
                return datasetLabel + ": " + tooltipItem.yLabel;
              }
            }
          },
        }
      })
    }
  }
  xhttp.open("GET", "http://127.0.0.1:5005/fb/interaction_type", true);
  xhttp.send();
}

function interactionType() {
  // Bar Chart Example
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      data = JSON.parse(this.responseText)["result"]
      competition = data["competition"]
      featured = data["featured"]
      infographics = data["infographics"]
      others = data["others"]
      product = data["product"]
      promotion = data["promotion"]
      comments = [competition[1], featured[1], infographics[1], product[1], promotion[1], others[1]]
      likes = [competition[0], featured[0], infographics[0], product[0], promotion[0], others[0]]
      var ctx = document.getElementById("interaction_type");
      var myBarChart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: ["Competition", "Featured", "Infographics", "Product", "Promotion", "Others"],
          datasets: [
            {
              label: "Likes",
              barThickness: 25,
              backgroundColor: "blue",
              borderColor: "#4e73df",
              data: likes
            },
            {
              label: "Comments",
              barThickness: 25,
              borderColor: "#4e73df",
              backgroundColor: "red",
              data: comments,
            },
          ],
        },
        options: {
          maintainAspectRatio: false,
          layout: {
            padding: {
              left: 10,
              right: 10,
              top: 5,
              bottom: 0
            }
          },
          scales: {
            xAxes: [{
              time: {
              },
              gridLines: {
                display: false,
                drawBorder: false
              },
              ticks: {
                maxTicksLimit: 6
              },
              maxBarThickness: 50,
            }],
            yAxes: [{
              ticks: {

              },
              gridLines: {
                color: "rgb(234, 236, 244)",
                zeroLineColor: "rgb(234, 236, 244)",
                drawBorder: false,
                borderDash: [2],
                zeroLineBorderDash: [2]
              }
            }],
          },
          legend: {
            display: false
          },
          tooltips: {
            titleMarginBottom: 10,
            titleFontColor: '#6e707e',
            titleFontSize: 14,
            backgroundColor: "rgb(255,255,255)",
            bodyFontColor: "#858796",
            borderColor: '#dddfeb',
            borderWidth: 1,
            xPadding: 15,
            yPadding: 15,
            displayColors: true,
            caretPadding: 10,
            callbacks: {
              label: function (tooltipItem, chart) {
                var datasetLabel = chart.datasets[tooltipItem.datasetIndex].label || '';
                return datasetLabel + ": " + tooltipItem.yLabel;
              }
            }
          },
        }
      })
    }
  }
  xhttp.open("GET", "http://127.0.0.1:5008/competitor/interaction_type", true);
  xhttp.send();
}