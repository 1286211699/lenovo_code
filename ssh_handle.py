# @Time : 2021/4/20 18:14 
# @Author : Smile_Mr
# @File : ssh_handle.py 
# @Software: PyCharm
import paramiko

class ssh_paramiko:

    def __init__(self,host,username,password):

        self.host = host
        self.username = username
        self.password = password
        self.ssh = self.clinet_ssh()

    def clinet_ssh(self):

        ssh = None
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect( self.host, 22, self.username, self.password, timeout=5)
        except:
            print('%s Error\n' % (self.host))
            # raise  Exception('%s Error\n' % (self.host))
        return ssh

    def ssh_send_cmd(self,cmd):

        try:
            stdin,stdout,stderr = self.ssh.exec_command(cmd)

        except Exception as e:
            print(e)

        # print(stdout.read().decode("utf-8"))

    def handle_ssh(self,local_ssh_file):

        stdin,stdout,stderr = self.ssh.exec_command('cat /root/mmc2/1.txt')
        host_data = stdout.read().decode('utf-8')
        # print(host_data)
        if host_data:
            with open(local_ssh_file,encoding='utf-8') as f:
                ssh_local_data = f.read()

                if ssh_local_data not in host_data:
                    cmd = 'echo ' + ssh_local_data.strip() +  ' >>' + ' /root/mmc2/1.txt'
                    # print(cmd)
                    self.ssh.exec_command(cmd)
                else:
                    pass

    def __del__(self):

        self.ssh.close()




if __name__ == '__main__':
    test_ssh  = ssh_paramiko('10.110.149.133','root','root')
    # test_ssh.ssh_send_cmd("echo 313123213131131131131232131231312  >> /root/mmc2/1.txt")
    test_ssh.handle_ssh(r'C:\Users\12862\.ssh\id_rsa.pub')
    # test_ssh.ssh_send_cmd('ls')
