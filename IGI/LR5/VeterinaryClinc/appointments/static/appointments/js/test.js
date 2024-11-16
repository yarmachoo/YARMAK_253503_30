var a = [];
var b = [1, 2+3];
var c = [1, "Alex", []];

var car = {manyCars: {a: "Saab", "b": "Jeep"}, 7: 'Mazda'};
alert(car.manyCars.b);
alert(car[7]);

var unusualPropertyNames = {"": "An empty string",
                            "!": "Bang!"};

//alert(unusualPropertyNames."");
alert(unusualPropertyNames[""]);
//alert(unusualPropertyNames.!);
alert(unusualPropertyNames["!"])


var answer =42;
answer = "thanks for all the fish..";

x = "the answer is "+ 42;
y = 42 + "is the answer ";
alert("37" - 7); // 30
alert("37" + 7); // 377


// строковое преобразование:
var a = true;
alert(a);

alert(String(null)==="null");
alert(true+"test")
alert("123"+undefined)


alert(+" \n 123 \n \n");
alert(+true);
alert(+false);
alert("\n0" == 0); //true

alert("\n" == false);
alert(Boolean("3")==true)

alert(null==undefined)