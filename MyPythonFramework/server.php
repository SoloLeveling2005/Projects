<?php
// create a server on port 8000
$server = stream_socket_server("http://0.0.0.0:8000");
echo "hi";
while (true) {
    // accept incoming connections
    $client = stream_socket_accept($server);

    // read data from the client
    $request = stream_get_contents($client);

    // process the request and get the response
    $response = handle_request($request);

    // send the response to the client
    fwrite($client, $response);

    // close the client connection
    fclose($client);
}

// this function handles the request and generates a response
function handle_request($request) {
    // parse the request to get the path
    $path = parse_request($request);

    // handle different paths
    if ($path == '/') {
        return "Welcome to my OpenServer!\n";
    } else if ($path == '/about') {
        return "This is a simple OpenServer created with PHP.\n";
    } else {
        return "404 Not Found\n";
    }
}

// this function parses the request and returns the path
function parse_request($request) {
    // extract the path from the request
    // assuming the request is in the format "GET /path HTTP/1.1"
    return explode(' ', $request)[1];
}
