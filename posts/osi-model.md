#OSI Seven Layer Model
##06/01/2019

OSI (Open Source Interconnection) 7 Layer Model

Layer Seven: Application
- Serves as the window for users and application processes to access the network services.
- Application: End User layer- Program that opens what was sent or creates what is to be sent
- Examples:
    - Resource sharing
    - Remote file access
    - Remote printer access
    - Directory services
    - Network management
- Central Device / Protocols
    - User Applications
    - SMTP
    - Gateway
- DOD4 Model
    - Process
Layer Six: Presentation
- Formats the data to be presented to the Application layer. It can be viewed as the "translator" for the network.
- Application: Syntax layer- encrypt and decrypt (if needed)
- Examples:
    - Character code translation
    - Data conversion
    - Data compression
    - Data encryption
    - Character Set Translation
- Central Device / Protocols
    - JPEG
    - ASCII
    - EBDIC
    - TIFF
    - GIF
    - PICT
    - Gateway
- DOD4 Model
    - Process
Layer Five: Session
- Allows session establishment between processes running on different stations. 
- Application: Sync and send to ports (logical ports)
- Examples:
    - Session establishment
    - Maintenance and termination
    - Session support
    - Perform security
    - Name recognition
    - Logging
- Central Device / Protocols
    - Logical Ports
    - RPC
    - SQL
    - NFS
    - NetBIOS names
    - Gateway
- DOD4 Model
    - Process
Layer Four: Transport
- Ensures that messages are delivered error-free, in sequence, and with no losses or duplications.
- Application: TCP- Host to Host, Flow Control
- Examples:
    - Message segmentation
    - Message acknowledgement
    - Message traffic control
    - Session multiplexing
    - Packet filtering
- Central Device / Protocols
    - TCP
    - SPX
    - UDP
    - Gateway
- DOD4 Model
    - Host to Host
Layer Three: Network
- Controls the operations of the subnet, deciding which physical path the data takes.
- Application: Packets ("letter", contains IP address)
- Examples:
    - Routing
    - Subnet traffic control
    - Frame fragmentation
    - Logical-physical address mapping
    - Subnet usage accounting
    - Packet Filtering
- Central Device / Protocols
    - Routers
    - IP
    - IPX
    - ICMP
    - Gateway
- DOD4 Model
    - Internet
Layer Two: Data Link
- Provides error-free transfer of data frames from one node to another over the Physical layer.
- Application: Frames ("envelopes", contains MAC address) [NIC card--Switch--NIC card] (end to end)
- Examples:
    - Establishes and terminates the logical link between nodes
    - Frame traffic control
    - Frame sequencing
    - Frame acknowledgement
    - Frame delimiting
    - Frame error checking
    - Media access control
- Central Device / Protocols
    - Switch Bridge WAP
    - PPP
    - SLIP
    - Land Based Layer
    - Gateway
- DOD4 Model
    - Network
Layer One: Physical
- Concerned with the transmission and reception of the unstructured raw bit stream over the physical medium.
- Application: Physical structure- Cables, hubs, etc.
- Examples:
    - Data Encoding
    - Physical medium attachment
    - Transmission technique
    - Baseband or Broadband
    - Phyiscal medium transmission
    - Bits and Volts
- Central Device / Protocols
    - Hub
    - Land Based Layer
    - Gateway
- DOD4 Model
    - Network

:)

#####Sources:
######None