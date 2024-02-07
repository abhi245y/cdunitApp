document.addEventListener("DOMContentLoaded", function () {
  axios
    .post("/api/load-table")
    .then((response) => {
      const tableBody = $("#myTable tbody");
      console.log(response.data);
      response.data.forEach((row) => {
        const newRow = $("<tr>");
        // Iterate over object properties instead of array indices
        Object.keys(row).forEach((key) => {
          if (key === "receivedDate") {
            var dateObject = new Date(row[key]);
            var datePart = dateObject.toISOString().split("T")[0];
            const newCell = $("<td>");
            newCell.text(datePart);
            newRow.append(newCell);
          } else {
            const newCell = $("<td>");
            newCell.text(row[key]);
            newRow.append(newCell);
          }
        });
        tableBody.append(newRow);
      });
      $("#myTable").DataTable({
        dom: "Pfrtip",
        searchPanes: {
          show: true,
          selectStyle: "dropdown",
          cascadePanes: true,
          initCollapsed: true,
        },
      });
    })
    .catch((error) => {
      console.error("Error fetching data:", error);
    });
});
