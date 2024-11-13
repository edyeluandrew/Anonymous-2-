<?php
// login.php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get the submitted username and password
    $username = $_POST['username'];
    $password = $_POST['password'];

    // You can add validation here (e.g., check if username and password match)
    
    // Redirect to homepage after successful login
    header("Location: v1.html");
    exit();
}
?>
