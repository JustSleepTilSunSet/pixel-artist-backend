import paramiko
from dotenv import dotenv_values
import os
username = os.getenv("SFTP_USER")
password = os.getenv("SFTP_PWD")
hostname = os.getenv("SFTP_HOST")
port = os.getenv("SFTP_PORT")
remote_directory = '.'
sftp = None
ssh = None

def sftpConnect():
    global sftp
    global ssh
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print(f"Connecting to {hostname}:{port} with username {username}")
        ssh.connect(hostname, port, username, password)
        sftp = ssh.open_sftp()
        print("Connected successfully")
        return sftp
    except Exception as e :
        print(f"An error occurred: {e}")
        raise

def getDir():
    global sftp
    global ssh
    try:
        print(f"Listing files in directory: {remote_directory}")
        file_list = sftp.listdir(remote_directory)
        print(f"Files in {remote_directory}:")
        for file in file_list:
            print(file)
    except Exception as e :
        print(f"An error occurred: {e}")
        raise

def toCloseAllConnect():
    global sftp
    global ssh
    try:
        sftp.close()
        ssh.close()
    except Exception as e :
        print(f"An error occurred: {e}")
        raise

def uploadFile(fileBin, remotePath):
    global sftp
    global ssh
    with sftp.file(remotePath, 'wb') as remote_file:
        remote_file.write(fileBin)
    print("Upload done.")