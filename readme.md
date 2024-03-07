
## reference

- https://ithelp.ithome.com.tw/m/articles/10290517

- https://learnku.com/articles/71840

確認k8s cluster是否有啟動
kubectl cluster-info

使用minikube

## 在本機搭建k8s方法有哪些?
https://yourdevopsmentor.com/blog/5-ways-to-install-a-kubernetes-cluster/
https://opensource.com/article/20/11/run-kubernetes-locally
- Docker Desktop
- Minikube
- Kubeadm
- Kind(Kubernetes in Docker)

## 練習用Docker Desktop, minikube搭建k8s
使用到的工具有哪些?
- Docker Desktop: 圖形介面的管理工具，可以進行 Docker 的設定、管理等操作
- VirtualBox: 跨平台虛擬化軟體，能讓開發人員在單一裝置上執行多個作業系統
- Minikube: 輕量級的工具，用於在本地運行 Kubernetes 環境，用來開發和測試
- Kubectl: 是 Kubernetes 的命令列工具，用來管理 Kubernetes 叢集、部署應用程式、檢視與管理各種叢集中的各項資源與紀錄

## docker 指令

>> docker run --name mynginx -d -p 8081:80 nginx:latest
>> docker ps --format="ID\t{{.ID}}\nNAME\t{{.Names}}\nIMAGE\t{{.Image}}\nPORTS\t{{.Ports}}\nCOMMAND\t{{.Command}}\nCREATED\t{{.CreatedAt}}\nSTATUS\t{{.Status}}\n"
>> 查container ip: docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' container_name

## 把多個container連接的練習(架設WordPress並搭配MySQL)

docker network create wordpress000net1

docker run --name mysql000ex11 -dit --net=wordpress000net1 -e MYSQL_ROOT_PASSWORD=myrootpass -e MYSQL_DATABASE=wordpress000db -e MYSQL_USER=wordpress000kun -e MYSQL_PASSWORD=wkunpass mysql --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci --default-authentication-plugin=mysql_native_password

docker run --name wordpress000ex12 -dit --net=wordpress000net1 -p 8085:80 -e WORDPRESS_DB_HOST=mysql000ex11 -e WORDPRESS_DB_NAME=wordpress000db -e WORDPRESS_DB_USER=wordpress000kun -e WORDPRESS_DB_PASSWORD=wkunpass wordpress