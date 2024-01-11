// Get intitial details

// In your Javascript (external .js resource or <script> tag)
document.addEventListener("DOMContentLoaded", function () {
  let routesSelect = document.querySelector("#routes-select");
  let messengersSelect = document.querySelector("#messengers-select");
  let qpSeriesSelect = document.querySelector("#qp-series-select");
  let collegeSelect = document.querySelector("#college-select");

  axios
    .post("/api/initilize")
    .then((response) => {
      const data = response.data;

      // Access and utilize the retrieved data:
      const messengersNames = data.messengers;
      const qpSeries = data.qp_series; // Assuming a single value
      const routes = data.routes; // Assuming a single value

      routes.forEach((route) => {
        let option = document.createElement("option");
        option.value = route; // Set value to be the same as the string data
        option.text = route; // Set text content as well
        routesSelect.appendChild(option);
      });

      messengersNames.forEach((messengerName) => {
        let option = document.createElement("option");
        option.value = messengerName; // Set value to be the same as the string data
        option.text = messengerName; // Set text content as well
        messengersSelect.appendChild(option);
      });

      qpSeries.forEach((qpSerie) => {
        let option = document.createElement("option");
        option.value = qpSerie; // Set value to be the same as the string data
        option.text = qpSerie; // Set text content as well
        qpSeriesSelect.appendChild(option);
      });
    })
    .catch((error) => {
      console.error("Error fetching data:", error);
    });

  // get college details

  $("#routes-select").change(function () {
    let selectedValue = $(this).val();

    axios
      .post(
        "/api/get-colleges",
        {
          selectedRoute: selectedValue,
        },
        {
          headers: { "Content-Type": "application/x-www-form-urlencoded" },
        }
      )
      .then((response) => {
        var firstChildClist = collegeSelect.firstChild;
        $("#college-select").empty();
        collegeSelect.appendChild(firstChildClist);
        var collegeData = response.data;

        var collegeList = collegeData.collegeNames;

        collegeList.forEach((collegeName) => {
          let option = document.createElement("option");
          option.value = collegeName; // Set value to be the same as the string data
          option.text = collegeName; // Set text content as well
          collegeSelect.appendChild(option);
        });
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  });
  // $("#college-select").select2({
  //   theme: "classic",
  // });
});
