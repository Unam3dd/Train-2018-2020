#!/usr/bin/python3
#-*- coding:utf-8 -*-
#Author : Unam3dd

try:
    import socket
    import zlib
    import sys
except ImportError as ierror:
    print("[-] Error import module : %s\n",ierror)

class HttpParseResponse:

    raw_headers = None
    text_headers = None
    content = None
    text = None
    status_line = None
    status_code = None
    status_reason = None
    http_version = None
    is_redirect = None
    request = None
    target_ip = None
    target_port = None
    local_ip = None
    local_port = None

    def __init__(self,response,gzip_response,request,t_session,l_session):
        self.raw_headers = self.parse_headers(response)
        self.text_headers = self.parse_headers(response).decode("utf-8")
        self.content = self.parse_content(response)
        self.status_line = self.parse_status_line(self.raw_headers).decode("utf-8")
        self.http_version = self.format_status_line(self.status_line)[0]
        self.status_code = int(self.format_status_line(self.status_line)[1])
        self.status_reason = self.format_status_line(self.status_line)[2]
        self.request = request
        self.target_ip = t_session[0]
        self.target_port = int(t_session[1])
        self.local_ip = l_session[0]
        self.local_port = l_session[1]
        
        if gzip_response == True:
            if "Content-Encoding".encode("utf-8") in self.raw_headers:
                self.text = self.uncompress_content(self.content).decode("utf-8")
            else:
                self.text = self.content.decode("utf-8")
        
        if "Location" in self.text_headers:
            self.is_redirect = True
        else:
            self.is_redirect = False

    def parse_headers(self,response):
        return response.split("\r\n\r\n".encode("utf-8"))[0]
    
    def parse_content(self,response):
        return response.split("\r\n\r\n".encode("utf-8"))[1]
    
    def uncompress_content(self,content):
        return zlib.decompress(content,zlib.MAX_WBITS|32)
    
    def parse_status_line(self,raw_headers):
        return raw_headers.split("\r\n".encode("utf-8"))[0]
    
    def format_status_line(self,status_line):
        return status_line.split(" ")
    
    def get_value_from_headers(self,value):
        split_headers = self.text_headers.split("\r\n")
        
        for content in split_headers:
            if value in content:
                return content.split(value+": ")[1]

    


class HttpClient:
    python_version = None

    def __init__(self):
        if self.get_python_version() != 3:
            print("[-] Error Initialize HttpClient()")

    def http_parse_url(self,url):
        protocol = url.split("://")[0]
        host = url.split("://")[1].split("/")[0]
        
        if ":" in host:
            port = int(url.split("://")[1].split("/")[0].split(":")[1])
        else:
            port = 80
        
        path_ = url.split("://")[1].split("/")[1:]
        path = "/"
        path += "/".join(path_)

        if protocol == "https":
            print("[-] Error your url use https protocol is not supported !\n")
            sys.exit(-1);

        return (protocol,host,port,path)
    

    def get_python_version(self):
        self.python_version = int(sys.version[0])
        return self.python_version
    
    def send_requests(self,requests,host,port):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM,socket.IPPROTO_TCP)
            s.connect((socket.gethostbyname(host),port))
            s.send(requests.encode("utf-8"))
            data = s.recv(8192)
            t_session = s.getpeername()
            l_session = s.getsockname()
            s.close()
            return data, t_session, l_session
        except socket.error as error_send_request:
            return error_send_request

    def get(self,url,**kwargs):
        url_parsed = self.http_parse_url(url)
        gzip_response = True
        user_agent = "unahttp/1.0"
        accept_encoding = "gzip, deflate"
        accept = "*/*"
        connection = "keep-alive"

        
        for key, value in kwargs.items():
            
            if key == "user_agent":
                user_agent = value
            
            if key == "accept_encoding":
                accept_encoding = value
            
            if key == "accept":
                accept = value
            
            if key == "connection":
                connection = value
            
            if key == "gzip_response":
                gzip_response = value
        

        payload = "GET %s HTTP/1.1\r\nHost: %s\r\nUser-Agent: %s\r\n" % (url_parsed[3],url_parsed[1],user_agent)

        if gzip_response != False:
            payload += "Accept-Encoding: %s\r\n" % (accept_encoding)
        
        payload += "Accept: %s\r\n" % (accept)
        payload += "Connection: %s\r\n" % (connection)

        payload += "\r\n"

        recv_data = self.send_requests(payload,url_parsed[1],int(url_parsed[2]))
        parse = HttpParseResponse(recv_data[0],gzip_response,payload,recv_data[1],recv_data[2])

        return (parse)
    
    def post(self,url,**kwargs):
        url_parsed = self.http_parse_url(url)
        gzip_response = True
        user_agent = "unahttp/1.0"
        accept_encoding = "gzip, deflate"
        accept = "*/*"
        connection = "keep-alive"
        content_type = "application/x-www-form-urlencoded"
        content_len = None
        data = None
        
        for key, value in kwargs.items():
            
            if key == "user_agent":
                user_agent = value
            
            if key == "accept_encoding":
                accept_encoding = value
            
            if key == "accept":
                accept = value
            
            if key == "connection":
                connection = value
            
            if key == "gzip_response":
                gzip_response = value
            
            if key == "content_type":
                content_type = value
            
            if data == None:
                s = value.split(" ")
                data = "%s=%s" % (key,"+".join(s))
            else:
                s = value.split(" ")
                data += "&%s=%s" % (key,"+".join(s))
        
        if data == None:
            print("[-] Error data not set !\n")
            return None
        
        content_len = len(data)
        payload = "POST %s HTTP/1.1\r\nHost: %s\r\nUser-Agent: %s\r\n" % (url_parsed[3],url_parsed[1],user_agent)
        
        if gzip_response != False:
            payload += "Accept-Encoding: %s\r\n" % (accept_encoding)
        
        payload += "Accept: %s\r\n" % (accept)
        payload += "Connection: %s\r\n" % (connection)
        payload += "Content-Type: %s\r\nContent-Length: %d\r\n" % (content_type,content_len)
        payload += "\r\n%s" % (data)
        
        recv_data = self.send_requests(payload,url_parsed[1],int(url_parsed[2]))
        parse = HttpParseResponse(recv_data[0],gzip_response,payload,recv_data[1],recv_data[2])

        return (parse)