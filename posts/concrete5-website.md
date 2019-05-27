#Apache2 Concrete5 Website Setup With phpMyAdmin
## 05/26/2019

1. SSH into server that will hold the website.
2. Go to directory that will hold the website folder.
3. Create folder and name it. (I name it after the domain name)
4. Add etc, www, and possibly log folder within the new folder
5. Add a httpd.conf file to the etc folder
    1. Add a successful apache configuration to the httpd.conf file
    2. Symbolically link conf file to apache2 sites-enabled folder
        ```sh
        ln /pathToFolder/etc/httpd.conf -s /etc/apache2/sites-enabled/domainName.conf
        ```
6. Update apache2 to get to the server address
    1. Make sure apachectl configtest returns Syntax OK
    2. If it returns successfully, run apachectl restart
    3. If it does not return successfully, troubleshoot httpd.conf file
7. Add User to phpMyAdmin User Base
    1. Go to User Accounts in phpMyAdmin
    2. Add new user account
    3. Username: domainName dropping TLD
    4. Password: Randomly generated password
    5. Check the box to create database with the same name
8. Download concrete5 and install
    1. Go to the www folder
    2. Download and unzip through browser or use these commands:
        ```sh
        wget https://www.concrete5.org/download_file/-/view/109615/concrete5-8.5.1.zip
        unzip concrete5-8.5.1.zip
        ```
    3. Make sure to unzip concrete5, then move the contents into the www folder such that index.php is now located in the www folder
    4. Move the contents of the concrete5 folder into the www folder
        ```sh
        mv concrete5-8.5.1.zip/* ../www/
        ```
    5. Feel free to delete the zip and empty unzipped folder
9. Allow Concrete5 to access all needed web files
    ```sh
    chmod -R 777 ../www/
    ```
10. Go to domain name url (if set up) or IP address, and follow Concrete5 Install Instructions
    1. Make sure everything is correctly installed, and then proceed to the next page
        1. Name: Something that relates to the domain name or what it will be for
        2. Administrator Email: Probably Your Email :P
        3. Password: Another randomly generated password
        4. Database Location: localhost
        5. Database domain, password, and database come from phpMyAdmin
        6. Install
    2. Wait for Concrete5 to download everything that it needs
11. Done! :)