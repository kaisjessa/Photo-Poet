var poempic = document.getElementById("poemimg");

$("#poemimg").change(element => {
  if (!element.files || !element.files[0]) {
    document.getElementById("submit").hidden = true;
    return;
  }
  var file = element.files[0];
  var reader = new FileReader();
  reader.readAsDataURL(file);
  reader.onloadend = () => {
    document.getElementById("poempic").setAttribute("src", reader.result);
  };
  $("#poempic").show();
  $("#submit").show();
});

function send() {
  var element = document.getElementById("poemimg");
  if (!element.files || !element.files[0]) {
    document.getElementById("submit").hidden = true;
    alert("Whoops! Something went wrong; no file is selected. "
        + "The submission button is now hidden.");
    return;
  }
  var reader = new FileReader();
  reader.readAsDataURL(element.files[0]);
  reader.onloadend = async () => {
    const response = await fetch("/clarifai", {
      method: "POST",
      headers: {
        "Accept": "application/json",
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        image: reader.result.slice(22)
      })
    });
    const data = await response.json();
    console.log(data);
  }
}
