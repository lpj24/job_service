# job_service
bi定时任务管理(vue+drf)重写https://github.com/lpj24/jobManage

## 代码描述
    job_vue是webpack打包编译之后的vue前端代码, 完整代码存放于/home/huolibi/local/job_vue
    其它代码就是drf后端代码, 使用nginx转发前端和后端, 详见nginx.conf
    另外, 如果拥有root权限可以使用docker部署

## 该页面主要功能主要包含以下几个方面
##### 1. 对所有定时任务详情进行描述, 代替文档描述方式, 使其得到更清晰的展现
##### 2. 逐条或者批量定制化(日期, 天数)重复更新任务
##### 3. 批量更新由于各种原因引起数据更新失败的昨日任务
##### 4. 增加任务检索功能, 在做大类更新时有作用


## 下面图片展示功能
