
# LIU QIAO XIN - Personal Portfolio

一个优雅的个人作品集网站，展示个人信息、项目经历、社交媒体账号、照片画廊和文学作品。

## 项目结构

```
.
├── index.html          # 主页面
├── rossi/              # 个人照片
├── 抖音/               # 抖音相关内容
├── 小红书/             # 小红书相关内容
├── 照片/               # 照片画廊
└── optimize.py         # 图片优化脚本
```

## 功能特性

- 响应式设计，适配各种屏幕尺寸
- 平滑的页面滚动和动画效果
- 照片画廊支持懒加载和 Lightbox 查看
- 社交媒体账号展示
- 文学作品展示（支持展开/收起）
- 优雅的配色方案和视觉效果

## GitHub Pages 部署

### 方法一：直接部署 main 分支

1. 在 GitHub 上创建一个新仓库
2. 将代码推送到 GitHub
3. 进入仓库的 **Settings** → **Pages**
4. 在 **Build and deployment** 部分：
   - **Source**: 选择 `Deploy from a branch`
   - **Branch**: 选择 `main` 分支，文件夹选择 `/ (root)`
5. 点击 **Save**
6. 等待几分钟，网站将部署在 `https://&lt;your-username&gt;.github.io/&lt;repo-name&gt;/`

### 方法二：使用 gh-pages 分支

```bash
# 创建并切换到 gh-pages 分支
git checkout --orphan gh-pages

# 删除所有文件
git rm -rf .

# 创建一个简单的 index.html（或者从 main 分支复制）
git checkout main -- index.html
git checkout main -- rossi/
git checkout main -- 抖音/
git checkout main -- 小红书/
git checkout main -- 照片/

# 提交并推送
git add .
git commit -m "Initial gh-pages commit"
git push origin gh-pages
```

然后在 GitHub Pages 设置中选择 `gh-pages` 分支。

## 本地预览

直接在浏览器中打开 `index.html` 即可预览网站。

## 注意事项

- 确保 `index.html` 在仓库根目录
- 图片和视频路径使用相对路径
- GitHub Pages 对仓库大小有限制（建议单个仓库不超过 1GB）

