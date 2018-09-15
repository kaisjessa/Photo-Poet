

$("#submit").hide();
$("#result").hide();

$("#poemimg").change(element => {
  element = element.target;
  if (!element.files || !element.files[0]) {
    $("#submit").hide();
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
    alert("Whoops! Something went wrong; no file is selected.");
    $("#submit").hide();
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
    document.getElementById("result").innerHTML = data.join(", ");
    $("#result").show();
  }
}
