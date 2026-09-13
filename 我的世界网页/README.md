# 我的世界网页版

浏览器里直接玩的 Minecraft 1.5.2，不用安装，打开网页就能进游戏。

原作是 Eaglercraft（lax1dude 做的），这里是一份整理过的副本，只保留了网页运行需要的文件。

## 怎么打开

这个游戏不能直接双击 index.html 打开，浏览器会拦（本地文件协议下 worker 跑不起来）。

必须放在 HTTP 服务器上访问。三种办法：

1. 已经部署好的话，直接访问那个网址就行。
2. 本地测试：在文件夹里开一个服务，比如 `python -m http.server 8000`，然后浏览器打开 `http://localhost:8000`。
3. 传到 GitHub Pages 上也行，仓库设置里开 Pages，指向 main 分支根目录。

如果只是想一个人玩，不想弄服务器，那就直接开 `Eaglercraft_1.5_Offline_Download.html`，这个是离线单文件版，双击就能用。

## 文件说明

- `index.html` —— 网页入口，在线版的加载页面
- `classes.js` —— 客户端主程序
- `classes_server.js` —— 内置服务器，单机模式靠它
- `worker_bootstrap.js` —— worker 启动脚本
- `assets.epk` —— 游戏资源包（贴图、音效那些）
- `eagswebrtc.js` —— 局域网联机用的
- `Eaglercraft_1.5_Offline_Download.html` —— 离线单文件版

以上这些是一个都不能少的，删了就跑不起来。

## 关于联机

单机肯定能用。多人联机（就是游戏里那个 Open to LAN）需要 relay 服务器中转，默认配的是国外的，国内不一定连得上。要是只玩单机就不用管这个。

想自己架服务器的话，原作那边有 Java 版的 bukkit 和 bungee 服务端，这里没放进来，因为跟网页版没关系。

## 来源

https://github.com/catfoolyou/Eagler-Online
