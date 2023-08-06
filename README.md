# Efficient-data-communication-and-storage-using-synchronized-servers
Sure! Here's a detailed README file for your "Synchronized Servers For Reliable Data Storage" project:

# Synchronized Servers For Reliable Data Storage

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [How it Works](#how-it-works)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project, "Synchronized Servers For Reliable Data Storage," is a distributed system that facilitates synchronized data storage across multiple servers. It provides a reliable and efficient solution for data storage and synchronization, ensuring data consistency and integrity while optimizing update operations.

The main goals of this project are:
1. **Synchronization**: All connected servers are synchronized with each other, meaning any data uploaded by a client on one server is automatically replicated to all other servers in the network.

2. **Optimal Updating**: The system ensures efficient updates by employing a smart hashing mechanism based on SHA-256. When a file is updated, only the portions that have changed are transferred, reducing bandwidth consumption and optimizing the update process.

## Features

- Synchronized data storage across multiple servers.
- Efficient updates with partial file transfers using SHA-256 hashing.
- Client-server architecture with support for multiple concurrent clients.
- Secure data transmission with encryption.
- Fault tolerance and error handling.
- Scalable for large-scale deployment.
- Cross-platform compatibility.

## How it Works

The system operates using a client-server architecture, where multiple clients can connect to one or more servers in the network. Here's an overview of how the system works:

1. **Client Upload**:
   - Clients can upload files to any server in the network.
   - When a file is uploaded, the system generates its SHA-256 hash.
   - The file is divided into smaller logical units based on the SHA-256 hash.
   - The server stores the file and its hash, dividing it into manageable chunks.

2. **Server Synchronization**:
   - All servers in the network are synchronized with each other continuously.
   - When a file is uploaded on one server, it automatically propagates to all other servers.
   - Servers communicate with each other to ensure data consistency.

3. **Client Update**:
   - If a client wants to update a file, the system follows an optimal updating approach.
   - The client sends the updated file to the server.
   - The server calculates the SHA-256 hash of the updated file.
   - It then compares the new hash with the existing hash to identify the changed portions.
   - Only the modified portions are transmitted to the other servers for updates.

4. **Fault Tolerance**:
   - The system is designed to handle server failures and network interruptions.
   - Data is replicated across multiple servers, reducing the risk of data loss.
   - Servers communicate with each other to identify and recover from failures.

## Installation

To install and run the system, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/amitraj360e/Efficient-data-communication-and-storage-using-synchronized-servers

   cd synchronized-servers
   ```

2. Install dependencies:
   ```
   sudo apt update
   sudo apt upgrade
   ### Prerequisites
1. G++ compiler
   * ```sudo apt-get install g++```
2. openssl for SHA hashing
   * ```sudo apt-get install openssl```
### How to compile project
1. go to client directory
   * ```make```
2. go to tracker directory
   * ```make```
3. To clean solution 
   * ```make clean```
   ```
4. Run the system:
   ```
   # Instructions to start the servers and clients.
   ```
   #### To run the Tracker

```
./tracker <my_tracker_ip>:<my_tracker_port> <other_tracker_ip>:<other_tracker_port>  <seederlist_file>  < tracker_log_file>

eg : ./tracker 127.0.0.1:5000 127.0.0.1:6000 seederlist serverlog1
```

#### To run the Client

```
./client <CLIENT_IP>:<UPLOAD_PORT> <TRACKER_IP_1>:<TRACKER_PORT_1> <TRACKER_IP_2>:<TRACKER_PORT_2> <client_log_file>
```
* creating client1 on new terminal with socket : 127.0.0.1:8800 <br/>
eg : ```./client 127.0.0.1:8800 127.0.0.1:5000 127.0.0.1:6000 clientlog1```

* creating client2 on another terminal with socket : 127.0.0.1:7600 <br/>
eg : ```./client 127.0.0.1:7600 127.0.0.1:5000 127.0.0.1:6000 clientlog2```

#### Command/Functionality on Clinent side 
 
 1. **To Share the file over network :** <br/>
 ```
  share <local_file_path> <filename>.<file_extension>.mtorrent
  Eg : share /home/darshan/movie.mp4 movie.mp4.mtorrent.
  ```
 * It will generate .mtorrent file and send data to tracker that I(clinet/seeder) have this file. Now other client/leecher can download this file using .mtorrent file.
  
 2. **To Download the file :** <br/>
 ```
  get <path_to_.mtorrent_file> <destination_path>
  Eg : get movie.mp4.mtorrent newmovie.mp4
  ```
 * It will send request to tracker to know about available seeders and then randomly choose one seeder and make connection with it to get chunk of data. 
  
 3. **Show Downloading status** <br/>
 ```
 show_downloads
 ```
 * It will list out files which are downloading(D), successfully downloaded(S). 
 
4. **To Stop sharing of file over network :** <br/>
 ```
 remove <filename.mtorrent>
 Eg : remove movie.mp4.mtorrent
 ```
 * It will stop sharing of that file over network by removing .mtorrent file and metadata of that file from tracker.

5. **close client :** <br/>
 ```
 close
 ```
 * It will shutdown client and  remove all metadata of files which have been shared by this client from tracker. 
  
 #### Assumptions

* seederlist file must be present on tracker folder for tracker to run. If not then create empty seederlist file.
* Use ```\``` as delimeter for filename.
* absolute & relative path, both are supported.
* whenever client starts, it scans current working directory for .mtorrent file and update/inform tracker about it.
* Client(seeder/leecher) and tracker implemented by multithreading thus also support multithreading environment.
 
   



## Contributing

We welcome contributions to this project! If you want to contribute, please follow the guidelines in [CONTRIBUTING.md](CONTRIBUTING.md) for the code of conduct, pull request process, etc.

## License

Feel free to use, modify, and distribute the code as per the terms of the license.
