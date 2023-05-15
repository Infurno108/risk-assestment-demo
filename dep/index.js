//id= rent, rentTime, salery, bank, savings, gig
function submit() {
    rent = document.getElementById("rent").value;
    rentTime = document.getElementById("rentTime").value;
    salery = document.getElementById("salery").value;
    bank = document.getElementById("bank").value;
    savings = document.getElementById("savings").value;
    gig = document.getElementById("gig").checked;

    //dog = tf.loadLayersModel('javascriptAI');
    //output = dog.predict(tf.tensor2d([rent, rentTime, salery, bank, savings, gig]));
    document.getElementById("output").innerHTML = "waggy!";
}