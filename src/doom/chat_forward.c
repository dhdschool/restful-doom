// src/chat_forward.c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

void send_chat_to_host(const char *msg)
{
    if (!msg || msg[0] == '\0') return;

    int sock = socket(AF_INET, SOCK_DGRAM, 0);
    if (sock < 0) {
        return; // silence on failure
    }

    struct sockaddr_in addr;
    memset(&addr, 0, sizeof(addr));
    addr.sin_family = AF_INET;
    addr.sin_port = htons(5005);               // listening port
    addr.sin_addr.s_addr = inet_addr("127.0.0.1");

    // Limit message size to avoid fragmentation (adjust as needed)
    size_t len = strlen(msg);
    if (len > 1024) len = 1024;

    // send (ignore result)
    sendto(sock, msg, len, 0, (struct sockaddr*)&addr, sizeof(addr));

    close(sock);
}
