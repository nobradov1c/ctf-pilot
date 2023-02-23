# HTTP request smuggling

https://portswigger.net/web-security/request-smuggling

Most HTTP request smuggling vulnerabilities arise because the HTTP specification provides two different ways to specify where a request ends: the Content-Length header and the Transfer-Encoding header.

- The Content-Length header is straightforward: it specifies the length of the message body in bytes. For example:

  ```
  POST /search HTTP/1.1
  Host: normal-website.com
  Content-Type: application/x-www-form-urlencoded
  Content-Length: 11

  q=smuggling

  ```

- The Transfer-Encoding header can be used to specify that the message body uses chunked encoding. This means that the message body contains one or more chunks of data. Each chunk consists of the chunk size in bytes (expressed in hexadecimal), followed by a newline, followed by the chunk contents. The message is terminated with a chunk of size zero. For example:

  ```
  POST /search HTTP/1.1
  Host: normal-website.com
  Content-Type: application/x-www-form-urlencoded
  Transfer-Encoding: chunked

  b
  q=smuggling
  0
  ```

## tools

- burp suite
  - [http request-smuggler extension](https://github.com/portswigger/http-request-smuggler)
