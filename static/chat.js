
document.getElementById("submit").addEventListener('click',submitChat, false);


function submitChat(){
  var msg = document.getElementById("msg").value;
  console.log(msg);
  document.getElementById("text").innerHTML = msg;
}