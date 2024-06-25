# MCommandes

## 关于此程序

1. 数据来源：[此处](https://docs.google.com/spreadsheets/d/1SJTOn0FNIzy76FH8OeSz1Ul55lJkL-ZkmWAUaa5tFGo/edit?usp=sharing)（共300个工作表）

2. 使用前，首先解压mcommandes_service.zip中的JSON文件（内含机密），因为GitHub代码仓库中禁止包含机密信息。

3. 启动celery消息中介：
    ```bash
    celery -A appli_celery worker --loglevel=INFO
    ```

4. 使用以下命令强制性删除所有未执行的任务：
    ```bash
    celery -A appli_celery purge
    ```
