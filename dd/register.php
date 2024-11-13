<?php
// signup.php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Retrieve form data
    $username = $_POST['username'];
    $email = $_POST['email'];
    $password = $_POST['password'];

    // Validation can go here (if any)
    
    // Redirect to homepage after successful signup
    header("Location: v1.html");
    exit();
}
?>