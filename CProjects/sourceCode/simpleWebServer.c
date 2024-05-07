// This will be my first introduction to Web Servers, hoping to build a web page, then a Minecraft server

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <winsock2.h>

#define PORT 8080

int main() {
	WSADATA wsa;
	SOCKET server_fd, new_socket;
	struct sockaddr_in server, client;
	int addrlen = sizeof(client);
	char *response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<html><body><h1>Suprise motha fucka</h1></body></html>\r\n";
	
	// Initialize Winsock
	if (WSAStartup(MAKEWORD(2,2), &wsa) !=0) {
		printf("WSAStartup failed\n");
		return 1;
	}
	
	// Create socket
	if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == INVALID_SOCKET) {
		printf("Socket creation failed\n");
		return 1;
	}	
	
	// Set up address struct
	server.sin_family = AF_INET;
	server.sin_addr.s_addr = INADDR_ANY;
	server.sin_port = htons(PORT);

	// Bind socket
	if (bind(server_fd, (struct sockaddr *)&server, sizeof(server)) == SOCKET_ERROR) {
		printf("Bind failed\n");
		closesocket(server_fd);
		WSACleanup();
		return 1;
	}

	// Listen
	if (listen(server_fd, 3) == SOCKET_ERROR) {
		printf("listen failed\n");
		closesocket(server_fd);
		WSACleanup();
		return 1;

	}

	// Accept Connections
	while (1) {
		if ((new_socket = accept(server_fd, (struct sockaddr *)&client, (int *)&addrlen)) == INVALID_SOCKET) {
			printf("Accept failed\n");
			closesocket(server_fd);
			WSACleanup();
			return 1;
		}
		// Send response
		send(new_socket, response, strlen(response), 0);
		closesocket(new_socket);
	}
	closesocket(server_fd);
	WSACleanup();
	return 0;
}
