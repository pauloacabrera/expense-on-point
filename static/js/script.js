
const expenseChart =
document.getElementById("expenseChart");


if(expenseChart){


new Chart(expenseChart,{

type:"line",

data:{


labels:[
"Jan",
"Feb",
"Mar",
"Apr",
"May"
],


datasets:[{


label:"Expenses",

data:[
5000,
7000,
4500,
9000,
6000
],


borderWidth:3


}]

}

});

}



const categoryChart =
document.getElementById("categoryChart");


if(categoryChart){


new Chart(categoryChart,{

type:"doughnut",

data:{


labels:[
"Food",
"Bills",
"Shopping",
"Travel"
],


datasets:[{


data:[
5000,
3000,
2000,
1500
]


}]


}


});


}