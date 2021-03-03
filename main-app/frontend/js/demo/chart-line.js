Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

// Pie Chart Example
function loadVideoAnalysis() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      data = JSON.parse(this.responseText)["result"]
      populate_data = []
      labels = []
      for (info in data) {
        temp_array = data[info]
        if (temp_array[0] != 0) {
          populate_data.push(temp_array[0])
          labels.push(temp_array[1])
        }
      }
      labels = [3, 3.2, 3.4, 4, 4.2, 4.4, 5, 5.2, 5.4, 6, 6.2]
      var ctx = document.getElementById("videoline");
      var myLineChart = new Chart(ctx, {
        type: 'line',
        data: {
          labels: labels,
          datasets: [{
            data: populate_data,
            fill: false,
            backgroundColor: "#739aff",
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
  xhttp.open("GET", "http://127.0.0.1:5004/insta/videoduration", true);
  xhttp.send();
}


function instaDayPost() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      data = JSON.parse(this.responseText)["result"]
      populate_data = []
      for (info in data) {
        temp_array = data[info]
        populate_data.push(temp_array)
      }
      final_data = []
      final_data.push(populate_data[1])
      final_data.push(populate_data[5])
      final_data.push(populate_data[6])
      final_data.push(populate_data[4])
      final_data.push(populate_data[0])
      final_data.push(populate_data[2])
      final_data.push(populate_data[3])
      console.log(populate_data)
      var ctx = document.getElementById("daypostinsta");
      var myLineChart = new Chart(ctx, {
        type: 'line',
        data: {
          labels: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],

          datasets: [{
            data: final_data,
            fill: false,
            pointRadius: 5,
            backgroundColor: "#c9cdd1",
            borderColor: "#c60be3"
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
  xhttp.open("GET", "http://127.0.0.1:5004/insta/dayofpost", true);
  xhttp.send();
}

function facebookDayPost() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      data = JSON.parse(this.responseText)["result"]
      populate_data = []
      for (info in data) {
        temp_array = data[info]
        populate_data.push(temp_array)
      }
      final_data = []
      final_data.push(populate_data[1])
      final_data.push(populate_data[5])
      final_data.push(populate_data[6])
      final_data.push(populate_data[4])
      final_data.push(populate_data[0])
      final_data.push(populate_data[2])
      final_data.push(populate_data[3])
      console.log(populate_data)
      var ctx = document.getElementById("daypostfb");
      var myLineChart = new Chart(ctx, {
        type: 'line',
        data: {
          labels: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],

          datasets: [{
            data: final_data,
            fill: false,
            backgroundColor: "#c9cdd1",
            pointRadius: 5,
            borderColor: "#0b77e3"
          }],
        },
        options: {
          maintainAspectRatio: false,
          tooltips: {
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
  xhttp.open("GET", "http://127.0.0.1:5005/fb/dayofpost", true);
  xhttp.send();
}

function instaTimePost() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      data = JSON.parse(this.responseText)["result"]
      populate_data = []
      labels = []
      for (info in data) {
        temp_array = data[info]
        populate_data.push(temp_array)
        labels.push(info + ":00")
      }
      console.log(populate_data)
      var ctx = document.getElementById("timepostinsta");
      var myLineChart = new Chart(ctx, {
        type: 'line',
        data: {
          labels: labels,

          datasets: [{
            data: populate_data,
            fill: false,
            pointRadius: 5,
            backgroundColor: "#c9cdd1",
            borderColor: "#c60be3"
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
  xhttp.open("GET", "http://127.0.0.1:5004/insta/timeofpost", true);
  xhttp.send();
}


function facebookTimePost() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      data = JSON.parse(this.responseText)["result"]
      populate_data = []
      labels = []
      for (info in data) {
        temp_array = data[info]
        populate_data.push(temp_array)
        labels.push(info + ":00")
      }
      console.log(populate_data)
      var ctx = document.getElementById("timepostfb");
      var myLineChart = new Chart(ctx, {
        type: 'line',
        data: {
          labels: labels,

          datasets: [{
            data: populate_data,
            fill: false,
            pointRadius: 5,
            backgroundColor: "#c9cdd1",
            borderColor: "#c60be3"
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
  xhttp.open("GET", "http://127.0.0.1:5005/fb/timeofpost", true);
  xhttp.send();
}

function competitorPost() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      data = JSON.parse(this.responseText)["result"]
      enchanted_cafe = data["enchantedcafe"]
      handlebar = data["handlebaroriginal"]
      hatterstreet = data["hatterstreet"]
      thewhiterabbitsg = data["thewhiterabbitsg"]
      windowsillpies = data["windowsillpies"]
      listinfo = []
      labels = []
      interaction_types = []

      interaction_types_data = {}
      // competition	featured	product	promotion	infographics	others
      labeling = ["competition", "featured", "product", "promotion", "infographics", "others"]




      for (info of enchanted_cafe) {
        if (info[2] < 2000) {
          if (!(info[3] in interaction_types_data))
            interaction_types_data[info[3]] = []

          interaction_types_data[info[3]].push([info[1], info[2], info[0], "Enchanted Cafe"])
        }
      }
      for (info of handlebar) {
        if (info[2] < 2000) {
          if (!(info[3] in interaction_types_data))
            interaction_types_data[info[3]] = []
          interaction_types_data[info[3]].push([info[1], info[2], info[0], "Handle Bar Cafe"])
          console.log(interaction_types_data)
        }
      }
      for (info of hatterstreet) {
        if (info[2] < 2000) {
          if (!(info[3] in interaction_types_data))
            interaction_types_data[info[3]] = []

          interaction_types_data[info[3]].push([info[1], info[2], info[0], "Hatterstreet"])
        }
      }
      for (info of thewhiterabbitsg) {
        if (info[2] < 2000) {
          if (!(info[3] in interaction_types_data))
            interaction_types_data[info[3]] = []

          interaction_types_data[info[3]].push([info[1], info[2], info[0], "White Rabbit SG"])
        }
      }
      for (info of windowsillpies) {
        if (info[2] < 2000) {
          if (!(info[3] in interaction_types_data))
            interaction_types_data[info[3]] = []

          interaction_types_data[info[3]].push([info[1], info[2], info[0], "Windowsill Pies"])
        }
      }
      // console.log(interaction_types_data)

      competition_data = []
      featured_data = []
      product_data = []
      promotion_data = []
      infographics_data = []
      other_data = []

      competition_label = []
      featured_label = []
      product_label = []
      promotion_label = []
      infographics_label = []
      other_label = []

      for (key in interaction_types_data) {
        data = interaction_types_data[key]

        for (obj in data) {

          if (key == "competition") {
            competition_data.push({ x: data[obj][0], y: data[obj][1] })
            competition_label.push(["Instagram User: " + data[obj][3], "Caption: " + data[obj][2], "Interaction Type: " + key])
          }
          else if (key == "featured") {
            featured_data.push({ x: data[obj][0], y: data[obj][1] })
            featured_label.push(["Instagram User: " + data[obj][3], "Caption: " + data[obj][2], "Interaction Type: " + key])

          } else if (key == "product") {
            product_data.push({ x: data[obj][0], y: data[obj][1] })
            product_label.push(["Instagram User: " + data[obj][3], "Caption: " + data[obj][2], "Interaction Type: " + key])

          } else if (key == "promotion") {
            promotion_data.push({ x: data[obj][0], y: data[obj][1] })
            promotion_label.push(["Instagram User: " + data[obj][3], "Caption: " + data[obj][2], "Interaction Type: " + key])

          } else if (key == "infographics") {
            infographics_data.push({ x: data[obj][0], y: data[obj][1] })
            infographics_label.push(["Instagram User: " + data[obj][3], "Caption: " + data[obj][2], "Interaction Type: " + key])

          } else if (key == "others") {
            other_data.push({ x: data[obj][0], y: data[obj][1] })
            other_label.push(["Instagram User: " + data[obj][3], "Caption: " + data[obj][2], "Interaction Type: " + key])

          }
        }

      }
      console.log(infographics_data)
      var ctx = document.getElementById("competitor_post");
      var myCompetitorPostScatterPlot = new Chart(ctx, {
        type: 'scatter',
        data: {
          datasets: [{
            label: "competition",
            fill: true,
            pointRadius: 5,
            backgroundColor: "red",
            // borderColor: "#c60be3",
            pointBackgroundColor: "red",
            data: competition_data,
          },
          {
            label: "featured",
            fill: true,
            pointRadius: 5,
            backgroundColor: "blue",
            // borderColor: "#c60be3",
            pointBackgroundColor: "blue",
            data: featured_data,
          },
          {
            label: "product",
            fill: true,
            pointRadius: 5,
            backgroundColor: "green",
            // borderColor: "#c60be3",
            pointBackgroundColor: "green",
            data: product_data,
          },
          {
            label: "promotion",
            fill: true,
            pointRadius: 5,
            backgroundColor: "yellow",
            // borderColor: "#c60be3",
            pointBackgroundColor: "yellow",
            data: promotion_data,
          },
          {
            label: "infographics",
            fill: true,
            pointRadius: 5,
            backgroundColor: "cyan",
            // borderColor: "#c60be3",
            pointBackgroundColor: "cyan",
            data: infographics_data,
          },
          {
            label: "others",
            fill: true,
            pointRadius: 5,
            backgroundColor: "purple",
            // borderColor: "#c60be3",
            pointBackgroundColor: "purple",
            data: other_data,
          },
          ],
        },
        options: {
          maintainAspectRatio: false,
          tooltips: {
            callbacks: {
              label: function (tooltipItem, data) {
                console.log(data)
                console.log(tooltipItem)
                console.log(labeling[tooltipItem['datasetIndex']])
                interaction_type = labeling[tooltipItem['datasetIndex']]
                if (interaction_type == 'competition') {
                  return competition_label[tooltipItem['index']];
                }
                else if (interaction_type == 'featured') {
                  return featured_label[tooltipItem['index']];
                }
                else if (interaction_type == 'product') {
                  return product_label[tooltipItem['index']];
                }
                else if (interaction_type == 'promotion') {
                  return promotion_label[tooltipItem['index']];
                }
                else if (interaction_type == 'infographics') {
                  return infographics_label[tooltipItem['index']];
                }
                else if (interaction_type == 'others') {
                  return other_label[tooltipItem['index']];
                }
                // return interaction_types_data[tooltipItem['datasetIndex']][labels[tooltipItem['index']]]
              }
            },
            // label: infographics_label,
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
            display: true,
          },
        },
      });
    }
  }
  xhttp.open("GET", "http://127.0.0.1:5008/competitor/intermlikes", true);
  xhttp.send();
}

function influencerStrength() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      user_data = JSON.parse(this.responseText)["result"]

      no_of_likes_and_comments = []
      profile_name = []
      followers = []
      engagement_rate = []
      user_count = 0

      listinfo = []
      labels = []

      for (user in user_data) {
        user_count += 1
        no_of_likes_and_comments.push(user_data[user]["no_of_likes_and_comments"])
        profile_name.push(user)
        followers.push(user_data[user]["followers"])
        engagement_rate.push(user_data[user]["engagement_rate"])
      }

      for (var i = 0; i < user_count; i++) {

        listinfo.push({ x: no_of_likes_and_comments[i], y: followers[i] })
        // labels.push([Math.round(engagement_rate[i] * 100) / 100 + "%", profile_name[i]])
        labels.push([
          "User: " + profile_name[i],
          "Total likes and comments on FFL related post: " + no_of_likes_and_comments[i],
          "Followers: " + followers[i],
          "Engagement Rate: " + (no_of_likes_and_comments[i] / followers[i]) * 100])
      }

      var ctx = document.getElementById("influencer_engagement_chart");
      var myLineChart = new Chart(ctx, {
        type: 'scatter',
        data: {
          datasets: [{
            data: listinfo,
            fill: false,
            pointRadius: 5,
            backgroundColor: "#c9cdd1",
            borderColor: "#c60be3"
          }],
        },
        options: {
          maintainAspectRatio: false,
          tooltips: {
            callbacks: {
              label: function (tooltipItem, data) {
                return labels[tooltipItem['index']]
              }
            },
            label: labels,
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
  xhttp.open("GET", "http://127.0.0.1:5011/influencer_engagement/influencers_strength", true);
  xhttp.send();
}


function postFrequency() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      data = JSON.parse(this.responseText)["result"]

      populate_data = []
      labels = []
      for (info in data) {
        console.log(info)
        populate_data.push(data[info])
        labels.push(info)
        // labels.push(info + ":00")
      }
      console.log(populate_data)
      var ctx = document.getElementById("postfrequency");
      var myLineChart = new Chart(ctx, {
        type: 'line',
        data: {
          labels: labels,

          datasets: [{
            data: populate_data,
            fill: false,
            pointRadius: 5,
            backgroundColor: "#c9cdd1",
            borderColor: "#c60be3"
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
  xhttp.open("GET", "http://127.0.0.1:5009/insta/postdateinformation", true);
  xhttp.send();
}

function postFrequencyFB() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      data = JSON.parse(this.responseText)["result"]

      populate_data = []
      labels = []
      for (info in data) {
        populate_data.push(data[info])
        labels.push(info)
        // labels.push(info + ":00")
      }
      console.log(populate_data)
      var ctx = document.getElementById("postfrequencyFB");
      var myLineChart = new Chart(ctx, {
        type: 'line',
        data: {
          labels: labels,

          datasets: [{
            data: populate_data,
            fill: false,
            pointRadius: 5,
            backgroundColor: "#c9cdd1",
            borderColor: "#0b77e3"
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
  xhttp.open("GET", "http://127.0.0.1:5009/fb/postdateinformation", true);
  xhttp.send();
}


function enchantedFreqInsta() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      data = JSON.parse(this.responseText)["result"]

      populate_data = []
      labels = []
      for (info in data) {
        populate_data.push(data[info])
        labels.push(info)
        // labels.push(info + ":00")
      }
      console.log(populate_data)
      var ctx = document.getElementById("enchanted_freq");
      var myLineChart = new Chart(ctx, {
        type: 'line',
        data: {
          labels: labels,

          datasets: [{
            data: populate_data,
            fill: false,
            pointRadius: 5,
            backgroundColor: "#c9cdd1",
            borderColor: "#0b77e3"
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
  xhttp.open("GET", "http://127.0.0.1:5009/insta/enchanted_freq", true);
  xhttp.send();
}

function handlerbarFreqInsta() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      data = JSON.parse(this.responseText)["result"]

      populate_data = []
      labels = []
      for (info in data) {
        populate_data.push(data[info])
        labels.push(info)
        // labels.push(info + ":00")
      }
      console.log(populate_data)
      var ctx = document.getElementById("handlebar_freq");
      var myLineChart = new Chart(ctx, {
        type: 'line',
        data: {
          labels: labels,

          datasets: [{
            data: populate_data,
            fill: false,
            pointRadius: 5,
            backgroundColor: "#c9cdd1",
            borderColor: "#0b77e3"
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
  xhttp.open("GET", "http://127.0.0.1:5009/insta/handlerbar_freq", true);
  xhttp.send();
}


function hatterstreetFreqInsta() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      data = JSON.parse(this.responseText)["result"]

      populate_data = []
      labels = []
      for (info in data) {
        populate_data.push(data[info])
        labels.push(info)
        // labels.push(info + ":00")
      }
      console.log(populate_data)
      var ctx = document.getElementById("hatterstreet_freq");
      var myLineChart = new Chart(ctx, {
        type: 'line',
        data: {
          labels: labels,

          datasets: [{
            data: populate_data,
            fill: false,
            pointRadius: 5,
            backgroundColor: "#c9cdd1",
            borderColor: "#0b77e3"
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
  xhttp.open("GET", "http://127.0.0.1:5009/insta/hatterstreet_freq", true);
  xhttp.send();
}

function whiterabbitFreqInsta() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      data = JSON.parse(this.responseText)["result"]

      populate_data = []
      labels = []
      for (info in data) {
        populate_data.push(data[info])
        labels.push(info)
        // labels.push(info + ":00")
      }
      console.log(populate_data)
      var ctx = document.getElementById("whiterabbite_freq");
      var myLineChart = new Chart(ctx, {
        type: 'line',
        data: {
          labels: labels,

          datasets: [{
            data: populate_data,
            fill: false,
            pointRadius: 5,
            backgroundColor: "#c9cdd1",
            borderColor: "#0b77e3"
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
  xhttp.open("GET", "http://127.0.0.1:5009/insta/whiterabbit_freq", true);
  xhttp.send();
}