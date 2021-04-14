# Socket
My Socket Class in C++

## Introduction
This headers is a socket implementation in C++, this headers is multiplatform it can run on Windows as well as on Linux, and the syntax remains the same with some exceptions

## Documentations

  ## Windows Usage
    
   ### Constructor
   ```cpp
   WinSocket(short Family,int Type,int Protocol);
   ```
   
   ### Structures
  ```cpp
    typedef struct{
        char *address;
        int port;
    } peer_t;
   ```
   ### Methods
   ```cpp
    int Connect(string host,int port);
   ```
   - Description : this method allows to connect to a remote host.
   - Return value : the function returns 0 if it worked, otherwise in case of error it returns a SOCKET_ERROR (-1).
   ```cpp
    int Bind(int port);
   ```
   - Description : This method allows you to bind on a port.
   - Return value : same as Connect functions.
   ```cpp
    int Listen(int maxcon);
   ```
   - Description : this function allows you to listen on a port.
   - Return value : same as Connect functions.
   ```cpp
    SOCKET Accept();
   ```
   - Description : this function allows you to accepted client.
   - Return value : return Client file descriptor.
   ```cpp
    int Send(string data,int flags);
   ```
   - Description : this function allows you to send data.
   - Return value : in case of error the send function returns a SOCKET_ERROR, otherwise it returns the number of bytes send.
   
   ```cpp
    int SendTimeout(string data,unsigned long ms,int flags);
   ```
   - Description : same as the Send function but it takes a third parameter which is the timeout in milliseconds.
   - Return value : in case of error the send function returns a SOCKET_ERROR, otherwise it returns the number of bytes send.
   - Help : 1000 miliseconds = 1 seconds
   
   ```cpp
    int CSend(SOCKET fd,string data,int flags);
   ```
   - Description : this method is the same as the Send method except that if it allows to choose the file descriptor, this method is usually used after the Accept() methods
   - Return value : same as Send, SendTimeout
   
   ```cpp
    int CSendTimeout(SOCKET fd,string data,unsigned long ms,int flags);
   ```
   - Description : this method is the same as the SendTimeout but take file descriptor in parameter.
   - Return value : same as Send, SendTimeout and CSend.
   
   ```cpp
    std::string RecvData(int bytes,int flags);
   ```
   - Description : this method allows you to receive data.
   - Return value : it returns the content sent by the remote host or it returns an error message if there is an error.
   ```cpp
    std::string RecvDataTimeout(int bytes,int flags,unsigned long ms);
   ```
   - Description : this method works the same as SendTimeout except that this time if it's for data reception.
   - Return value : same as RecvData.
   ```cpp 
    std::string CRecvData(SOCKET fd,int bytes,int flags);
    std::string CRecvDataTimeout(SOCKET fd,int bytes,int flags,unsigned long ms);
   ```
   - Description : its methods work the same as CSend and CSendTimeout has a difference that CSendTimeout allows you to receive data.
   - Return value : same as RecvData, RecvDataTimeout.
   ```cpp
    void ExecuteAndStreamProcess(string process);
    void CExecuteAndStreamProcess(SOCKET fd,string process);
   ```
   - Description : its methods allow to execute and stream a process via a socket.
   - Return value : his methods don't have a return value they are of the void type.
   ```cpp
    peer_t GetPeerName(SOCKET fd);
   ```
   - Description : this method allows to retrieve the address and port of the remote host from a descriptor file
   - Return value : this method returns a peer_t type which is a typedef on a structure.
   ```cpp
    int Close();
    int CClose(SOCKET fd);
   ```
   - Description : its methods allow to close a descriptor file.
   - Return value : return value of close functions.
 
## Work on Linux ?
  to use this headers on linux just change WinSocket by LinSocket, nothing changes in terms of methods, but miliseconds turn into seconds
  see examples for more information.
  
    
   
   
   
