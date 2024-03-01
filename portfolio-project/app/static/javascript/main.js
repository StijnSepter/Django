function myFunction() {
let  x = document.getElementsByClassName("show");
  if (x.style.display === "block") {
    x.style.display = "none";
  } else {
    x.style.display = "block";
  }
}

// .collapse:not(.show) {
//     display: block;
// }