const uploadBtn = document.getElementById("file-upload");
const fileChosen = document.getElementById("file-chosen");

uploadBtn.addEventListener("change", function(){
  fileChosen.textContent = this.files[0].name
})