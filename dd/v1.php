<!-- v1.php -->
<?php
    // Check if user is logged in (for now we assume they are always redirected)
    session_start();
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Homepage</title>
</head>
<body>
    <h1>Welcome to the Homepage</h1>
    <p>You have successfully logged in or signed up!</p>
</body>
</html>