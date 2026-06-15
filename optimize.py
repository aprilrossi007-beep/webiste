import re

with open('/Users/rossiapril/Desktop/网页/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

old_str = """                        const videos = ['抖音/2.MP4', '抖音/3.MOV', '抖音/4.MOV', '抖音/5.MP4', '抖音/6.MP4', '抖音/7.MP4'];
                        
                        videos.forEach((videoSrc, index) => {
                            const video = document.createElement('video');
                            video.src = videoSrc;
                            video.controls = true;
                            video.preload = 'none'; // 修改为 none，不预加载，减轻本地服务器压力
                            video.style.flexShrink = '0'; // 防止在横向滚动时被挤压变形
                            // 为视频添加一个默认的海报背景，让它看起来不那么单调
                            video.poster = 'data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="300" height="200" viewBox="0 0 300 200"><rect width="300" height="200" fill="%23f4f1f8"/><text x="150" y="100" font-family="sans-serif" font-size="16" fill="%239b7bb3" text-anchor="middle" dominant-baseline="middle">视频 ' + (index + 1) + '</text></svg>';
                            
                            // 阻止点击视频区域时触发外层弹窗的关闭事件
                            video.addEventListener('click', function(e) {
                                e.stopPropagation();
                            });
                            
                            accountModalContent.appendChild(video);
                        });"""

new_str = """                        // 将原本的本地视频替换为跳转到抖音的链接块
                        const douyinLinks = [
                            { url: 'https://www.douyin.com/', title: '视频 1：点击前往抖音观看' },
                            { url: 'https://www.douyin.com/', title: '视频 2：点击前往抖音观看' },
                            { url: 'https://www.douyin.com/', title: '视频 3：点击前往抖音观看' },
                            { url: 'https://www.douyin.com/', title: '视频 4：点击前往抖音观看' },
                            { url: 'https://www.douyin.com/', title: '视频 5：点击前往抖音观看' },
                            { url: 'https://www.douyin.com/', title: '视频 6：点击前往抖音观看' }
                        ];
                        
                        douyinLinks.forEach((linkObj) => {
                            const linkContainer = document.createElement('a');
                            linkContainer.href = linkObj.url;
                            linkContainer.target = '_blank'; // 在新标签页打开
                            linkContainer.style.display = 'block';
                            linkContainer.style.width = '300px';
                            linkContainer.style.height = '200px';
                            linkContainer.style.flexShrink = '0';
                            linkContainer.style.borderRadius = '12px';
                            linkContainer.style.textDecoration = 'none';
                            linkContainer.style.overflow = 'hidden';
                            linkContainer.style.position = 'relative';
                            linkContainer.style.boxShadow = '0 4px 15px rgba(0,0,0,0.1)';
                            linkContainer.style.transition = 'transform 0.3s ease, box-shadow 0.3s ease';
                            
                            // 悬停动画
                            linkContainer.addEventListener('mouseenter', () => {
                                linkContainer.style.transform = 'translateY(-5px)';
                                linkContainer.style.boxShadow = '0 8px 25px rgba(155, 123, 179, 0.3)';
                            });
                            linkContainer.addEventListener('mouseleave', () => {
                                linkContainer.style.transform = 'translateY(0)';
                                linkContainer.style.boxShadow = '0 4px 15px rgba(0,0,0,0.1)';
                            });

                            // 使用 SVG 作为漂亮的封面背景
                            const svgBg = `data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="300" height="200" viewBox="0 0 300 200"><rect width="300" height="200" fill="%231e1e1e"/><circle cx="150" cy="90" r="30" fill="none" stroke="%239b7bb3" stroke-width="3"/><polygon points="140,75 140,105 165,90" fill="%239b7bb3"/><text x="150" y="150" font-family="sans-serif" font-size="14" fill="%23ffffff" text-anchor="middle">在抖音中打开</text></svg>`;
                            
                            linkContainer.style.backgroundImage = `url('${svgBg}')`;
                            linkContainer.style.backgroundSize = 'cover';
                            linkContainer.style.backgroundPosition = 'center';
                            
                            accountModalContent.appendChild(linkContainer);
                        });"""

c = c.replace(old_str, new_str)

with open('/Users/rossiapril/Desktop/网页/index.html', 'w', encoding='utf-8') as f:
    f.write(c)
