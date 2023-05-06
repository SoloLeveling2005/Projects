<?php

$uri = getenv("php_path");
$urls = ['/' => ['name' => 'index'], '/home' => ['name' => 'home']];
// print_r($urls);
// echo $uri;

foreach ($urls as $url) {
    echo key($url);
}
// print_r($uri_parts);
// switch($uri_parts[0]) {
//     case 'home':
//         // Handle requests for the homepage
//         echo 'Welcome to the homepage';
//         break;
//     case 'about':
//         // Handle requests for the about page
//         echo 'This is the about page';
//         break;
//     default:
//         // No route was matched
// //         header($_SERVER['SERVER_PROTOCOL'] . ' 404 Not Found');
// //         echo "no";
//         break;
// }

// $path = $_SERVER['SCRIPT_NAME'];
// print_r($_SERVER);
// switch ($path) {
//     case '/':
//         echo 'Welcome to my website!';
//         break;
//     case '/about':
//         echo 'This is an example of simple routing in PHP.';
//         break;
//     case '/contact':
//         echo 'Contact us at info@example.com';
//         break;
//     default:
// //         echo '404 Page Not Found';
//         break;
// }
//
//
?>