function populateTableRow(rowData) {
  var newRow = $("<tr>");

  $.each(rowData, function (columnName, value) {
    var cell = $("<td>");
    if (columnName === "Nil") {
      cell.append(
        $("<input>", {
          type: "checkbox",
          checked: value,
        })
      );
    } else {
      cell.text(value);
    }
    if (columnName === "collegeName") {
      cell.class = "shrink";
    }
    if (columnName === "Action") {
      cell.append(
        $("<button>", {
          class: "secondary",
          dataTarget: "modal-edit-row-entry",
          onClick: "toggleModal(event)",
        }).append($("<i>", { class: "fa-regular fa-pen-to-square" }))
      );
    }
    newRow.append(cell);
  });

  $("#DataTables_Table_0").DataTable().rows.add(newRow).draw();
  document.querySelector(".table-container").style.display = "";
}

$(function () {
  $("#add-bundles-form").on("submit", function (e) {
    e.preventDefault();

    var selectedRoute = $("#routes-select :selected").val();
    var selectedMessengers = $("#messengers-select :selected").val();
    var selectedCollege = $("#college-select :selected").val();
    var selectedQPseries = $("#qp-series-select :selected").val();

    var inputReceivedDateVal = $("#received-date-input").val();
    var inputQPCodeVal = $("#qp-code-input").val();
    var inputBundleQuantityVal = $("#bundle-quantity-input").val();
    var textareaRemarksVal = $("#remarks-textarea").val();

    var isNilCheck = $("#nil-check").is(":checked");
    var isMalpractice = $("#malpractice-check").is(":checked");

    var formData = {
      series: selectedQPseries,
      qpCode: inputQPCodeVal,
      Nil: isNilCheck,
      receivedDate: inputReceivedDateVal,
      messenger: selectedMessengers,
      collegeName: selectedCollege,
      remark: textareaRemarksVal,
      Action: "",
    };
    for (let i = 0; i < inputBundleQuantityVal; i++) {
      populateTableRow(formData);
    }

    document.querySelector("#add-bundles-form").reset();
  });
});
