$("#poempic").hide();
$("#submit").hide();

var file = null;

$("#poemimg").change(element => {
  element = element.target;
  if ((!element.files || !element.files[0]) && !file) {
    $("#submit").hide();
    return;
  }
  file = element.files[0] || file;
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
  if ((!element.files || !element.files[0]) && !file) {
    alert("Whoops! Something went wrong; no file is selected.");
    $("#submit").hide();
    return;
  }
  var reader = new FileReader();
  reader.readAsDataURL(element.files[0] || file);
  reader.onloadend = async () => {
    const response = await fetch("/clarifai", {
      method: "POST",
      headers: {
        "Accept": "application/json",
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        image: reader.result.split(",")[1]
      })
    });
    const data = await response.text();
    document.getElementById("result").innerHTML = data.replace(/\n/g, "<br />");
    // window.open("#third", "_self");
    $("#result").show();
  }
}
