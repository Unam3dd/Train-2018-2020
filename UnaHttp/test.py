import unahttp

if __name__ == "__main__":
    client = unahttp.HttpClient()
    r = client.get("http://ifconfig.me/ip"); # by defaults gzip_compress is enable you can change it with this
    # get method is keyword  variadic function
    # r = client.get("http://ifconfig.me/ip",gzip_response=False)
    # r = client.get("http://ifconfig.me/ip",gzip_response=False,user_agent="Unam3ddHttpey/1.0",accept="application/json")
    print(r.text) # print content 
    print(r.text_headers) # print content headers
    print(r.status_code) # get status code
    print(r.status_line) # get status line
    print(r.status_reason) # get status reason
    print(r.target_ip) # get target_ip
    print(r.target_port) # get target port
    print(r.local_ip) # get local ip
    print(r.local_port) # get local_port
    print(r.http_version) # get http version
    print(r.is_redirect) # check if redirect
    print(r.content) # get compressed content

    # is same for the post method
