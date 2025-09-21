3.1 更新提要（爆破性能优化）

1.多线程并行处理

使用 ThreadPoolExecutor 实现多线程并行计算

自动检测 CPU 核心数，最多使用 8 个线程

所有参数组合同时处理，而不是串行执行

2.优化的 Arnold 变换算法

使用向量化计算替代双重循环

直接操作 numpy 数组，避免 PIL 转换开销

预分配内存，减少重复分配

3.批量文件保存
   
使用独立的保存线程处理文件 I/O

批量保存机制（每 10 个文件一批）

减少磁盘写入次数和系统调用开销

4.进度更新优化
   
减少进度更新频率（最多 100 次更新）

避免频繁的 UI 信号发送开销

5.内存优化
    
预先将图像转换为 numpy 数组

重用数组内存，减少垃圾回收

向量化坐标计算

总体性能提升：
多线程加速：4-8倍速度提升（取决于 CPU 核心数）
向量化计算：2-3倍算法效率提升
批量 I/O：减少 50-70% 的磁盘写入时间
总体提升：预计 8-20倍 的整体性能提升
<img width="2213" height="1143" alt="4ed6958a02772306281c8cc16603b727" src="https://github.com/user-attachments/assets/587bebbc-42c4-4606-81ca-c34477e903bf" />











3.0更新提要

1.pyside6重构优化，添加毛玻璃效果

2.支持界面浅色与深色

3.支持大部分图片格式

4.多线程优化，爆破速度对比2.0快2倍

5.支持十六进制与十进制输入的特殊加解密方式即不需要数字

6.不再与ico文件捆绑

注：如果3.0出现报错请使用2.0
<img width="1695" height="1358" alt="屏幕截图 2025-08-29 212741" src="https://github.com/user-attachments/assets/5625835c-89a3-4b9e-a31d-efc9601fc2e9" />

<img width="1184" height="1349" alt="屏幕截图 2025-08-29 212758" src="https://github.com/user-attachments/assets/77dd73d0-0262-4dd7-9abd-c5ee982bed10" />


2.0使用说明

ico文件需要和exe程序存在于同一目录下

![屏幕截图 2025-06-16 235721](https://github.com/user-attachments/assets/8ab9f3b7-1479-4358-b741-b2737cd0d9de)
![屏幕截图 2025-06-17 000015](https://github.com/user-attachments/assets/71b3be4a-698a-4aad-baf5-d2c3f5c6965f)

