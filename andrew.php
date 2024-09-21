<?php
function name(){
    $my_name="edyelu andrew";
    return $my_name;
}
function my_age($c_year,$birth_year){
    $dob=25/8/2002;
    $age=$c_year-$birth_year;
    return $age;
}
function my_address(){
    $address="okile town,kaberamaido district";
    return $address;
}

print("wagwan,welcome ".name()." to ".my_address());
print("<br> You are ".my_age(2024,2002)." years old");



?>