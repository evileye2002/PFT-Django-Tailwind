// CONSTAIN //
const MAX_ROW_SELECTED = 50;
const MIN_ROW_TO_BULK_DELETE = 2;

// Func //
function togglePassword(e) {
  const self = e.target;
  const input = self.closest(".input").querySelector(".password-input");
  const new_type = self.checked ? "text" : "password";
  input.setAttribute("type", new_type);
}

function amountValueChange(e) {
  const value = e.target.value;
  var str = value.replace(/[^-()\d/*+.]/g, "");
  try {
    var number = eval(str);
    var result = new Intl.NumberFormat("en-US", {
      maximumFractionDigits: 20,
    }).format(number);

    e.target.value = result != "NaN" ? result : str;
    // console.log(str);
    // console.log(number);
    // console.log(result);
  } catch (error) {}
}

function onRowSelected(e) {
  // const checked = e.target.checked;
  const rows = document.querySelectorAll("input[row-selection]:checked");

  toggleBulkDeleteBtn(rows.length);
  toggleAllRowsSelection(rows.length);
}

function toggleAllRowsSelection(rowLength = 0) {
  const rowEls = document.querySelectorAll("input[row-selection]");
  const allRowSelectEl = document.querySelector("input[all-row-selection]");

  const breakPoint =
    rowEls.length < MAX_ROW_SELECTED ? rowEls.length : MAX_ROW_SELECTED;

  if (rowLength == breakPoint) allRowSelectEl.checked = true;
  else allRowSelectEl.checked = false;
}

function toggleBulkDeleteBtn(rowLength = 0) {
  const rowEls = document.querySelectorAll("input[row-selection]");
  const bulk_delete_btn = document.querySelector("[bulk-delete-btn]");

  const break_point =
    rowEls.length < MIN_ROW_TO_BULK_DELETE
      ? rowEls.length
      : MIN_ROW_TO_BULK_DELETE;

  if (rowLength >= break_point) bulk_delete_btn.classList.remove("hidden");
  else if (!bulk_delete_btn.classList.contains("hidden")) {
    bulk_delete_btn.classList.add("hidden");
  }
}

function selectAllRow(e) {
  const checked = e.target.checked;
  const rowEls = document.querySelectorAll("input[row-selection]");

  if (rowEls.length == 0) return;

  const breakPoint =
    rowEls.length < MAX_ROW_SELECTED ? rowEls.length : MAX_ROW_SELECTED;

  for (let i = 0; i < breakPoint; i++) {
    if (rowEls[i.checked]) continue;
    rowEls[i].checked = checked;
  }

  toggleBulkDeleteBtn(checked ? rowEls.length : 0);
}

function initDatepicker(id, options = null) {
  const $datepickerEl = document.getElementById(id);

  if (!options) {
    options = {
      autohide: true,
      format: "dd-mm-yyyy",
      orientation: "top",
      clearBtn: true,
      todayBtn: true,
      todayBtnMode: 1,
      weekStart: 1,
    };
  }
  new Datepicker($datepickerEl, options);
}

function addTransactionValidation(formID, modalID) {
  const $form = document.getElementById(formID);
  const $toggleBtn = document.querySelector(`label[for='${modalID}']`);
  const isValid = $form.checkValidity();

  if (isValid) $toggleBtn.click();
}

function resetForm(formID) {
  const $form = document.getElementById(formID);

  Array.from($form.elements).forEach((element) => {
    if (element.name !== "is-income") {
      if (element.type === "checkbox" || element.type === "radio") {
        element.checked = false;
      } else {
        element.value = "";
      }
    }
  });
}

function onDetailModalClose(e, modalBoxID = "") {
  const checked = e.target.checked;

  if (!checked && modalBoxID) addLoadingToModalBox(modalBoxID);
}

function addLoadingToModalBox(modalBoxID) {
  const $modalBox = document.getElementById(modalBoxID);

  if ($modalBox.querySelector(".loading")) return;

  $modalBox.addEventListener(
    "transitionend",
    function onTransitionEnd(event) {
      $modalBox.removeEventListener("transitionend", onTransitionEnd);
      $modalBox.innerHTML = `
        <div class="flex justify-center items-center h-full">
          <span class="loading loading-spinner loading-lg"></span>
        </div>
      `;
      $modalBox.classList.add("h-80");
    },
    { once: true }
  );
}

function toggleModal(modalID) {
  const $modalInput = document.getElementById(modalID);
  if ($modalInput) $modalInput.click();
}

function isNumber($this) {
  var value = Number($this.value.replace(/,/g, ""));
  var isValid = !isNaN(value) && value > 0;
  if (!isValid) $this.setCustomValidity("Vui lòng nhập 1 số lớn hơn 0.");
}

function showConfirmModal(title, question) {
  const $title = document.querySelector(".modal-confirm-title");
  const $question = document.querySelector(".modal-confirm-question");

  if ($title) $title.textContent = title;
  if ($question) $question.textContent = question;
  toggleModal("confirm-modal");
}

function removeAlert($alert) {
  $alert.classList.add("alert-hide");
  $alert.addEventListener("animationend", () => {
    $alert.remove();
  });
}

function onDetailFormChanged($form, $saveBtn, initialData) {
  const currentData = new FormData($form);

  const currentMap = new Map(currentData.entries());
  const initialMap = new Map(initialData.entries());

  if (currentMap.size != initialMap.size) {
    $saveBtn.removeAttribute("disabled");
    return;
  }

  let isChange = false;
  for (const [key, value] of currentMap.entries()) {
    if (key.includes("csrf")) continue;
    if (value !== initialMap.get(key)) {
      isChange = true;
      break;
    }
  }

  if (isChange) $saveBtn.removeAttribute("disabled");
  else $saveBtn.setAttribute("disabled", true);
}

function previewAvatar(e, imgID) {
  const file = e.target.files[0];
  if (file) {
    const reader = new FileReader();
    reader.onload = function (event) {
      const imgElement = document.getElementById(imgID);
      imgElement.src = event.target.result;
      imgElement.style.display = "block";
    };
    reader.readAsDataURL(file);
  }
}

document.addEventListener("htmx:confirm", function (e) {
  e.preventDefault();
  if (e.detail.question) {
    const $btnConfirm = document.getElementById("btn-confirm");

    showConfirmModal("Thông báo", e.detail.question);
    $btnConfirm.onclick = function (event) {
      e.detail.issueRequest(true);
      toggleModal("confirm-modal");
    };
  } else e.detail.issueRequest(true);
});

document.addEventListener("keydown", function (e) {
  if (e.ctrlKey && e.key === "k") {
    e.preventDefault();
    document.querySelector("input[name='s']").focus();
  }
});
