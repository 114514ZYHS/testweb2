# 我的世界网页版

浏览器里直接玩的 Minecraft，不用装 Java，不用装客户端。三个版本可选，点进去就能玩。

原作是 Eaglercraft（lax1dude 做的），这里是一份整理过的副本。

## 目录结构

```
我的世界网页/
├── index.html              版本选择页（和 launcher.html 内容相同）
├── launcher.html           版本选择页
├── parts/                  1.8 和 1.12 的游戏文件分片
│   ├── manifest-mc18.json     1.8.8 的清单
│   ├── manifest-mc112.json    1.12.2 的清单
│   ├── mc18.part000..019      1.8.8 的分片，共 20 片（每片 8 MB）
│   └── mc112.part000..004     1.12.2 的分片，共 5 片
├── 1.5/
│   ├── index.html          1.5.2 入口
│   ├── classes.js          客户端主程序
│   ├── classes_server.js   内置服务端，单机靠它
│   ├── worker_bootstrap.js worker 启动脚本
│   ├── assets.epk          游戏资源包
│   ├── eagswebrtc.js       局域网联机
│   └── Eaglercraft_1.5_Offline_Download.html   离线单文件版（23 MB）
├── 1.8/
│   ├── index.html          1.8.8 入口（加载完自动进游戏）
│   └── offline.html        1.8.8 离线版（不自动跳，给下载按钮）
└── 1.12/
    ├── index.html          1.12.2 入口
    └── offline.html        1.12.2 离线版
```

## 三个版本

- **1.5.2** —— 最老，兼容性最好，启动最快
- **1.8.8** —— PvP 手感最经典的一代，用的人最多
- **1.12.2** —— 版本最新，方块物品种类最多，也最吃性能

## 为什么 1.8 和 1.12 要用分片

因为完整文件太大：**1.8.8 是 152 MB，1.12.2 是 32 MB**。
GitHub 单个文件上限 100 MB，152 MB 那个直接推不上去。

做法是：把完整文件切成 8 MB 的小片放进 `parts/`，
进游戏时浏览器按并发拉下来，在内存里用 `Blob` 拼回完整文件，再跳过去运行。

**每个分片和整包都有 SHA-256，浏览器逐个校验**，坏片自动重试，最多 4 次。

实测启动耗时（本地服务）：1.12 约 9 秒，1.8 约 29 秒。第一次慢一些，之后有浏览器缓存。

离线版下载页用的是同一套机制 —— 拼完之后**不自动跳转**，而是给一个下载按钮，
点了会把完整 HTML 存到本地（存下来的文件双击就能用，不需要联网）。

## 本地预览

不能直接双击 `index.html`，浏览器会拦（本地文件协议下 worker 跑不起来）。
必须放在 HTTP 服务器上：

```bash
cd 我的世界网页
python3 -m http.server 8000
```

然后浏览器打开 `http://localhost:8000/launcher.html`。

## 改东西要注意

- **`parts/` 里的分片不能单独改**。改一片，整包哈希就对不上。要更新游戏版本，
  得重新切分片并重生成对应的 `manifest-*.json`。
- **分片数量、文件名都写在 manifest 里**，`parts/` 下多出来的文件不会被加载。
- **`index.html` 和 `launcher.html` 内容相同**，改一个记得同步另一个。
- **加载器的路径是从 manifest 推出来的**（`BASE = MANIFEST` 的目录部分），
  别单独写死 `parts/`，两个对不上会 404。

## 关于 1.5 离线单文件版（2026-09-25 更正）

以前这里写过一句「离线单文件版因为浏览器安全策略必然崩溃、无法修复，已删除」。**这句话是错的。**

2026-09-25 实测：`Eaglercraft_1.5_Offline_Download.html` 在 Chromium 下
**HTTP 服务和 `file://` 直接打开都能正常进游戏**（canvas 正常建立，
日志能看到 `starting minecraft`、纹理加载、27 achievements）。
所以它已经放回 `1.5/` 目录，版本选择页上也有下载入口。

如果以后又有人说它崩，先实际跑一遍再下结论，别照抄这句。

## 关于联机

单机肯定能用。多人（游戏里的 Open to LAN）需要 relay 服务器中转，
默认配的是国外的，国内不一定连得上。只玩单机就不用管。

自己架服务器的话，原作那边有 Java 版的 bukkit 和 bungee 服务端，这里没放，
因为跟网页版没关系。

## 来源

- 1.5.2：https://github.com/catfoolyou/Eagler-Online
- 1.8.8 / 1.12.2：https://eaglercraft.q13x.com/（q13x 的 EaglercraftX 分发）

两个离线单文件版都按官方 `meta.json` 里的 SHA-256 校验通过：

- 1.8.8：`446e63cd...78c8ea8`（159,796,833 字节）
- 1.12.2：`5234c5a6...870383a`（33,746,160 字节）
