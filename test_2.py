import pytest
import warnings
warnings.filterwarnings("ignore")


class TestServer:

    def test_nginx_is_installed(self,host):
        nginx = host.package("nginx")
        nginx_version = nginx.version
        assert nginx.is_installed
        assert nginx_version == "1.16.1"

    def test_nginx_service(self,host):
        nginx_service = host.run("ps -aux | grep nginx")
        nginx_stdout = nginx_service.stdout
        result = False
        if nginx_stdout:

            try:
                assert "0:00 nginx: worker process" in nginx_stdout
                result = True
            except:
                raise Exception("nginx is not runing")
            finally:
                pass

    def test_mysql_is_installed(self,host):
        mysql = host.run('mysql -V')
        mysql_stdout = mysql.stdout
        # print(mysql_stdout)
        result = False
        if mysql_stdout:
            try:
                assert "mysql  Ver 14.14" in mysql_stdout
                result = True
            except:
                raise Exception("mysql is not runing")
            finally:
                pass
        else:
            raise Exception('获取不到对应的版本')


    # class Test(unittest.TestCase):
#
#     def setUp(self):
#         ##1.创建一个ssh对象
#         self.host = testinfra.get_host("paramiko://root@10.110.149.133")
#
#     def test_nginx_is_installed(self):
#         nginx = self.host.package("nginx")
#         assert nginx.is_installed
#         print(nginx.version)
#         # assert nginx.version.startswith("1.6")
#
#
#     def test_nginx_service(self):
#         service = self.host.service("nginx")
#         print(dir(service))
#         print(service.is_valid)
#         print(service.is_running)
#         print(service.name)
        # self.assertTrue(service.is_running)
        # self.assertTrue(service.is_enabled)

#
# if __name__ == "__main__":
#     unittest.main()

# def test_passwd_file(host):
#     passwd = host.file("/etc/passwd")
#     assert passwd.contains("root")
#     assert passwd.user == "root"
#     assert passwd.group == "root"
#     assert passwd.mode == 0o644


# def test_nginx_is_installed(host):
#     nginx = host.package("nginx")
#     assert nginx.is_installed
#     print(nginx.version)
#
#
#
# def test_nginx_running_and_enabled(host):
#     nginx = host.service("nginx")
#     print(dir(nginx))
#     print(nginx.is_running)


# def test_redis_is_installed(host):
#
#     redis = host.run('ps -aux | grep nginx')
#     print(redis)
#     print(dir(redis))
#     print(redis.stdout)
#
#     # print(redis.is_running)

if __name__ == '__main__':
    pytest.main(['-s','test_2.py'])

