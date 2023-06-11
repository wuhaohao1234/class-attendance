# 使用 MySQL 官方镜像作为基础镜像
FROM mysql:latest

# 设置环境变量
ENV MYSQL_ROOT_PASSWORD=abu0418
ENV MYSQL_DATABASE=mydatabase
ENV MYSQL_USER=myuser
ENV MYSQL_PASSWORD=abu0418

# 复制自定义配置文件到容器中
COPY my.cnf /etc/mysql/my.cnf
