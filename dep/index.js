//id= rent, rentTime, salery, bank, savings, gig

function submit() {
    rent = document.getElementById("rent").value;
    rentTime = document.getElementById("rentTime").value;
    salery = document.getElementById("salery").value;
    bank = document.getElementById("bank").value;
    savings = document.getElementById("savings").value;
    gig = document.getElementById("gig").checked;
    document.getElementById("output").innerHTML = "Rent: " + rent + "<br> Rent Time: " + rentTime + "<br> Salery: " + salery + "<br> Bank: " + bank + "<br> Savings: " + savings + "<br> Gig: " + gig;
}
