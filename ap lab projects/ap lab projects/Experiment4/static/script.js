async function getPrediction() {
  let days = document.getElementById("daysInput").value;
  if (!days) return alert("Enter a valid number of days!");

  let response = await fetch("http://127.0.0.1:5000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ days: days })
  });

  let data = await response.json();
  document.getElementById("lrPrediction").innerText = data.lr_prediction[0];
  document.getElementById("lstmPrediction").innerText = data.lstm_prediction[0];

  updateChart(data.lr_prediction[0], data.lstm_prediction[0]);
}

function updateChart(lr, lstm) {
  let ctx = document.getElementById("predictionChart").getContext("2d");
  
  if (window.myChart) window.myChart.destroy(); // Destroy previous chart if exists

  window.myChart = new Chart(ctx, {
      type: "bar",
      data: {
          labels: ["Linear Regression", "LSTM"],
          datasets: [{
              label: "Stock Price Prediction",
              data: [lr, lstm],
              backgroundColor: ["#4CAF50", "#FF9800"]
          }]
      }
  });
}
