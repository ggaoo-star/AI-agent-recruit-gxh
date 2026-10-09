import matplotlib.pyplot as plt

# 修改全局字体，解决中文显示为方块的问题
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为黑体（Windows系统自带）
plt.rcParams['axes.unicode_minus'] = False    # 解决保存图像是负号'-'显示为方块的问题
# 导入工具包
import numpy as np #用来做数字计算
import matplotlib.pyplot as plt #画图工具
from sklearn.datasets import make_moons #导入函数,生成月牙型状数据
from sklearn.model_selection import train_test_split #划分数据集工具:训练验证和测试集
from sklearn.preprocessing import StandardScaler #导入标准化工具,缩放数据,便于训练

# 固定随机种子
SEED = 42
np.random.seed(SEED) #给np设置常用种子,只要种子固定生成的随机数相同

# 生成月牙数据
X, y = make_moons(n_samples=1500, noise=0.2, random_state=SEED)# ==========================================
# 补充：混淆矩阵与错误样本分析
# ==========================================
from sklearn.metrics import confusion_matrix
import seaborn as sns

# 总共生成1500个数据点;给点加一点噪声,模拟真实世界数据;固定随机种子,每次生成月牙点一样
# 返回两个结果:x每个点的坐标,是1500组(x,y);y每个点的标签(0/1)

# 划分数据集
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=SEED)
X_val, X_test,y_val,  y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=SEED)
# 全部数据的30%到临时变量X_temp, y_temp  剩下70%到训练集X_train,y_train;固定切分,每次切出来的数据不变
# 将刚才30%的临时数据对半,一般到验证集X_val,y_val,一半到测试机
# 标准化
scaler = StandardScaler() #创建标准化工具对象,准备缩放数据
X_train = scaler.fit_transform(X_train) #fit:只用训练集计算均值,方差 transform:用算出的均值方差缩放训练集坐标
X_val = scaler.transform(X_val)#验证集制作transform缩放,不重新fit,沿用训练集的
X_test = scaler.transform(X_test)#测试集同样

# 画原始月牙图
plt.figure(figsize=(5,4)) #新建画布,宽5,高4
plt.scatter(X[:,0], X[:,1], c=y, cmap="coolwarm", edgecolors="k")
#全部点的x,y坐标;根据标签y上色(0/1分别代表一种颜色);冷暖配色;k=black黑色
plt.title("月牙数据集 make_moons")
plt.xlabel("坐标x")
plt.ylabel("坐标y")
plt.show()

#导入PyTorch相关包 
import torch
# 导入pytorch深度学习框架，神经网络的基础。
import torch.nn as nn
#nn 里面存放网络层、激活函数、损失函数（Linear、ReLU、CrossEntropyLoss)
import torch.optim as optim
#optim 优化器，更新网络权重（Adam、SGD）
from torch.utils.data import TensorDataset, DataLoader
#TensorDataset：坐标X和标签y配对打包
#DataLoader：分批读取数据，一次拿32条
#将numpy数组转为torch张量
train_x = torch.tensor(X_train, dtype=torch.float32)
#torch.tensor()：把numpy格式的训练坐标，转成pytorch能识别的张量tensor
#dtype=torch.float32：坐标是小数，用浮点数类型
train_y = torch.tensor(y_train, dtype=torch.long)
#训练标签(0/1)转为张量；分类任务标签必须用long长整型
val_x = torch.tensor(X_val, dtype=torch.float32)
val_y = torch.tensor(y_val, dtype=torch.long)
#验证集坐标标签转为张量
test_x = torch.tensor(X_test, dtype=torch.float32)
test_y = torch.tensor(y_test, dtype=torch.long)
#测试集坐标、标签转张量

# 构造DataLoader，分批加载数据
train_loader = DataLoader(TensorDataset(train_x,train_y), batch_size=32, shuffle=True)
#TensorDataset(train_x,train_y)：把坐标和对应的标签一一绑定
#batch_size=32：每一批送入网络32个样本
#shuffle=True：每一轮训练前打乱样本顺序，防止模型背答案
val_loader = DataLoader(TensorDataset(val_x,val_y), batch_size=32, shuffle=False)
#验证集加载器，shuffle=False不打乱，只看模型好坏
test_loader = DataLoader(TensorDataset(test_x,test_y), batch_size=32, shuffle=False)
#测试集加载器

#搭建MLP多层感知机
class MLP(nn.Module):
#创建MLP网络类，nn.Module是pytorch网络的父类(面向对象编程中提供通用属性和方法的类，子类可以继承、扩展或重写这些功能)，固定写法
    def __init__(self, hidden_dim=64):
#初始化函数，hidden_dim=64隐藏层神经元数量
        super().__init__()
#固定必写，调用父类初始化(保证子类对象能够正确地继承和使用父类的属性和方法)
        self.net = nn.Sequential(
#Sequential：把网络层顺序串起来，数据一层一层往后走
            nn.Linear(2, hidden_dim),
#全连接层：输入是2个坐标(x,y)，输出64个隐藏层特征
            nn.ReLU(),
#ReLU激活函数，增加非线性，这样才能画出弯曲的决策边界，分开两个月牙
 nn.Linear(hidden_dim, 2)
#第二层全连接：隐藏层64个神经元-输出2个节点，对应类别0、类别1
       )
# CrossEntropyLoss内部包含LogSoftmax+NLLLoss,计算更稳定,如果输出维度是2,属于“多分类”如果要输出1个节点，用BCEWithLogitsLoss
#如果以后要改成三分类，模型只需把最后的2改为3，损失函数不用换
#结束Sequential
    def forward(self, x):
        return self.net(x)
#forward前向传播函数：输入x，网络自动计算输出 后面写model(x)就会自动调用这个函数

def train(model, train_loader, val_loader, lr=0.001, epoch_num=100):
#model：MLP网络
#train_loader：训练数据加载器,val_loader：验证数据加载器,lr=0.001：学习率，控制每次参数修改幅度,epoch_num=100：总共训练100轮
    loss_func = nn.CrossEntropyLoss()
#损失函数：交叉熵损失，分类任务专用，衡量预测结果和真实标签之间差距
    optimizer = optim.Adam(model.parameters(), lr=lr)
#优化器Adam，拿到网络里面全部参数；用学习率lr更新权重，让loss变小
    #保存每一轮的loss和准确率，后面画图
    train_loss_list, val_loss_list = [], []
    train_acc_list, val_acc_list = [], []
#4个空列表，记录训练,验证的损失和准确率,画曲线图依靠
    for epoch in range(epoch_num):
#循环,一轮epoch代表完整跑完一遍全部训练数据,循环100次
#训练
        model.train()
#model.train()：切换模型到训练模式，启用dropout、BN训练专属功能
        total_loss, correct, total = 0, 0, 0
#初始化变量：本轮总损失、猜对样本数量、样本总数，全部清零
        for xb, yb in train_loader:
#循环读取每一批数据：xb一批坐标，yb对应的标签，一批32个样本
            optimizer.zero_grad()
#梯度清零 PyTorch梯度会自动累加，不清零的话，上一轮的梯度会混进来，计算出错(重点)
            pred = model(xb)
#前向传播，这批坐标xb送入网络，得预测结果pred
            loss = loss_func(pred, yb)
#计算损失loss，对比网络预测pred和真实标签yb
            loss.backward()
#反向传播自动求导，算出每个权重要调整多少才能降低loss
            optimizer.step()
#更新权重,优化器根据上面求出的梯度，修改参数，完成一次学习
            total_loss += loss.item()
#累加这批损失,.item()把张量数字转普通Python数字
            pred_label = torch.argmax(pred, dim=1)
#argmax：找出pred里面最大值的下标，下标是预测类别（0/1）
            correct += (pred_label == yb).sum().item()
#对比预测标签和真实标签，相等就是猜对，累加猜对数量
            total += yb.size(0)
#累加本轮样本总数，yb.size(0)=这一批样本个数（32）
        train_loss = total_loss / len(train_loader)
#本轮训练平均loss = 总loss ÷ 一共有多少批次
        train_acc = correct / total
#训练集准确率 = 猜对数量 ÷ 全部样本数量
#验证
        model.eval()
#model.eval()：模型为评估模式，关闭训练专属功能，不计算梯度，省内存
        val_loss, val_correct, val_total = 0, 0, 0
        with torch.no_grad():
#with torch.no_grad()：不算梯度,验证阶段不用更新网络,关掉梯度计算,提速省内存
            for xb, yb in val_loader:
                pred = model(xb)
                loss = loss_func(pred, yb)
                val_loss += loss.item()
                pred_label = torch.argmax(pred, dim=1)
                val_correct += (pred_label == yb).sum().item()
                val_total += yb.size(0)

#循环读取验证集每一批数据，送入模型预测,计算损失、统计猜对数量
#with torch.no_grad()包裹这部分,不保存梯度信息
        val_loss = val_loss / len(val_loader)
        val_acc = val_correct / val_total
#计算验证集平均loss,验证集准确率
# 保存数据用于画图
        train_loss_list.append(train_loss)
        val_loss_list.append(val_loss)
        train_acc_list.append(train_acc)
        val_acc_list.append(val_acc)

# 打印每一轮结果
        print(f"Epoch:{epoch:3d}, train_loss:{train_loss:.4f}, train_acc:{train_acc:.4f}, val_loss:{val_loss:.4f}, val_acc:{val_acc:.4f}")
#把本轮loss,准确率存入列表；打印训练信息,看训练效果
    return train_loss_list, val_loss_list, train_acc_list, val_acc_list
#训练结束,返回4组数据,用来绘制loss,accuracy曲线
#训练
my_model = MLP(hidden_dim=64)
train_loss, val_loss, train_acc, val_acc = train(my_model, train_loader, val_loader, lr=0.001, epoch_num=100)
# 创建模型实例,隐藏层神经元64个
# 调用train函数,开始训练,接收返回的4组曲线数据
#保存
torch.save(my_model.state_dict(), "mlp_model.pth")
#torch.save():保存文件
#my_model.state_dict()只保存网络学到的权重参数
#"mlp_model.pth"文件名,pth模型文件后缀


import matplotlib.pyplot as plt
# 绘图库matplotlib,画曲线图
plt.figure(figsize=(12,4))
# 创建画布,大小宽12，高4
# 第一张loss损失曲线
plt.subplot(1,2,1)#画布分成1行2列，画第1个
plt.plot(train_loss, label="train loss")
# 画训练集损失曲线；loss小-模型预测错误少
plt.plot(val_loss, label="val loss")#画验证集损失曲线
plt.xlabel("epoch")#X轴名字：epoch，训练轮数
plt.ylabel("loss")#Y轴名字损失值
plt.title("Loss Curve")# 图片标题损失曲线
plt.legend()# 显示图例,区分两条线,第二张：accuracy准确率曲线
plt.subplot(1,2,2)# 换到第2张图
plt.plot(train_acc, label="train acc")# 训练集准确率，越接近1效果越好
plt.plot(val_acc, label="val acc")# 验证集准确率
plt.xlabel("epoch")#X轴：训练轮数
plt.ylabel("accuracy")#Y轴：准确率
plt.title("Accuracy Curve")#标题：准确率曲线
plt.legend()#显示图例
plt.tight_layout()#自动调整图的布局，防文字重叠
plt.savefig("loss_acc_curve.png")# 保存图片
plt.show()#展示图片


#二维决策边界是模型划分不同类别的分界线
#绘制二维决策边界
import numpy as np
#导入numpy，生成坐标网格点
def plot_decision_boundary(model, X, y,filename="decision_boundary.png"):
#定义函数plot_decision_boundary，专门画分割月牙的分界线
#参数model：训练完成的模型；X：原始样本坐标；y：原始样本标签
    x_min, x_max = X[:,0].min()-0.5, X[:,0].max()+0.5
#取出所有样本第1维坐标的最小、最大值，左右向外拓宽0.5，留出边距
    y_min, y_max = X[:,1].min()-0.5, X[:,1].max()+0.5
#取出所有样本第2维坐标的最小、最大值，上下向外拓宽0.5
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),
                         np.arange(y_min, y_max, 0.01))
#生成网格：在x、y范围内生成大量点，点间间隔0.01，铺满
    grid = np.c_[xx.ravel(), yy.ravel()]
#拉平网格，变成N行2列数组，一行代表平面上一个(x,y)坐标
    grid_tensor = torch.tensor(grid, dtype=torch.float32)
#numpy数组转为torch张量，只有张量才能送入PyTorch模型预测
    model.eval()
#模型切换评估模式，关闭dropout,bn这类训练专属功能
    with torch.no_grad():
#关闭梯度计算(画图只是预测，不需要求梯度；节省内存，跑得更快)
        pred = model(grid_tensor)
#把全部网格坐标送入模型，预测每一个网格点属于类别0/1
    pred_label = torch.argmax(pred, dim=1).reshape(xx.shape)
#argmax预测类别；reshape还原回二维网格形状，上色
    plt.contourf(xx, yy, pred_label, alpha=0.4, cmap="coolwarm")
#填充色块:不同类别填充不同颜色 两颜色交界线就是决策边界
#alpha=0.4  透明度，cmap="coolwarm"配色方案
    plt.scatter(X[:,0], X[:,1], c=y, s=20, cmap="coolwarm")
#绘制原始月牙样本散点，不同标签不同颜色，s=20是点的大小
    plt.title("Decision Boundary")
#设置标题决策边界
    plt.savefig(filename)
#保存图片到项目文件夹，文件名decision_boundary.png
    plt.show()
#展示这张图
#调用函数,画模型的决策边界import matplotlib.pyplot as plt

# 修改全局字体，解决中文显示为方块的问题
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为黑体（Windows系统自带）
plt.rcParams['axes.unicode_minus'] = False    # 解决保存图像是负号'-'显示为方块的问题
# 导入工具包
import numpy as np #用来做数字计算
import matplotlib.pyplot as plt #画图工具
from sklearn.datasets import make_moons #导入函数,生成月牙型状数据
from sklearn.model_selection import train_test_split #划分数据集工具:训练验证和测试集
from sklearn.preprocessing import StandardScaler #导入标准化工具,缩放数据,便于训练

# 固定随机种子
SEED = 42
np.random.seed(SEED) #给np设置常用种子,只要种子固定生成的随机数相同

# 生成月牙数据
X, y = make_moons(n_samples=1500, noise=0.2, random_state=SEED)
# 总共生成1500个数据点;给点加一点噪声,模拟真实世界数据;固定随机种子,每次生成月牙点一样
# 返回两个结果:x每个点的坐标,是1500组(x,y);y每个点的标签(0/1)

# 划分数据集
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=SEED)
X_val, X_test,y_val,  y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=SEED)
# 全部数据的30%到临时变量X_temp, y_temp  剩下70%到训练集X_train,y_train;固定切分,每次切出来的数据不变
# 将刚才30%的临时数据对半,一般到验证集X_val,y_val,一半到测试机
# 标准化
scaler = StandardScaler() #创建标准化工具对象,准备缩放数据
X_train = scaler.fit_transform(X_train) #fit:只用训练集计算均值,方差 transform:用算出的均值方差缩放训练集坐标
X_val = scaler.transform(X_val)#验证集制作transform缩放,不重新fit,沿用训练集的
X_test = scaler.transform(X_test)#测试集同样

# 画原始月牙图
plt.figure(figsize=(5,4)) #新建画布,宽5,高4
plt.scatter(X[:,0], X[:,1], c=y, cmap="coolwarm", edgecolors="k")
#全部点的x,y坐标;根据标签y上色(0/1分别代表一种颜色);冷暖配色;k=black黑色
plt.title("月牙数据集 make_moons")
plt.xlabel("坐标x")
plt.ylabel("坐标y")
plt.show()

#导入PyTorch相关包 
import torch
# 导入pytorch深度学习框架，神经网络的基础。
import torch.nn as nn
#nn 里面存放网络层、激活函数、损失函数（Linear、ReLU、CrossEntropyLoss)
import torch.optim as optim
#optim 优化器，更新网络权重（Adam、SGD）
from torch.utils.data import TensorDataset, DataLoader
#TensorDataset：坐标X和标签y配对打包
#DataLoader：分批读取数据，一次拿32条
#将numpy数组转为torch张量
train_x = torch.tensor(X_train, dtype=torch.float32)
#torch.tensor()：把numpy格式的训练坐标，转成pytorch能识别的张量tensor
#dtype=torch.float32：坐标是小数，用浮点数类型
train_y = torch.tensor(y_train, dtype=torch.long)
#训练标签(0/1)转为张量；分类任务标签必须用long长整型
val_x = torch.tensor(X_val, dtype=torch.float32)
val_y = torch.tensor(y_val, dtype=torch.long)
#验证集坐标标签转为张量
test_x = torch.tensor(X_test, dtype=torch.float32)
test_y = torch.tensor(y_test, dtype=torch.long)
#测试集坐标、标签转张量

# 构造DataLoader，分批加载数据
train_loader = DataLoader(TensorDataset(train_x,train_y), batch_size=32, shuffle=True)
#TensorDataset(train_x,train_y)：把坐标和对应的标签一一绑定
#batch_size=32：每一批送入网络32个样本
#shuffle=True：每一轮训练前打乱样本顺序，防止模型背答案
val_loader = DataLoader(TensorDataset(val_x,val_y), batch_size=32, shuffle=False)
#验证集加载器，shuffle=False不打乱，只看模型好坏
test_loader = DataLoader(TensorDataset(test_x,test_y), batch_size=32, shuffle=False)
#测试集加载器

#搭建MLP多层感知机
class MLP(nn.Module):
#创建MLP网络类，nn.Module是pytorch网络的父类(面向对象编程中提供通用属性和方法的类，子类可以继承、扩展或重写这些功能)，固定写法
    def __init__(self, hidden_dim=64):
#初始化函数，hidden_dim=64隐藏层神经元数量
        super().__init__()
#固定必写，调用父类初始化(保证子类对象能够正确地继承和使用父类的属性和方法)
        self.net = nn.Sequential(
#Sequential：把网络层顺序串起来，数据一层一层往后走
            nn.Linear(2, hidden_dim),
#全连接层：输入是2个坐标(x,y)，输出64个隐藏层特征
            nn.ReLU(),
#ReLU激活函数，增加非线性，这样才能画出弯曲的决策边界，分开两个月牙
 nn.Linear(hidden_dim, 2)
#第二层全连接：隐藏层64个神经元-输出2个节点，对应类别0、类别1
       )
# CrossEntropyLoss内部包含LogSoftmax+NLLLoss,计算更稳定,如果输出维度是2,属于“多分类”如果要输出1个节点，用BCEWithLogitsLoss
#如果以后要改成三分类，模型只需把最后的2改为3，损失函数不用换
#结束Sequential
    def forward(self, x):
        return self.net(x)
#forward前向传播函数：输入x，网络自动计算输出 后面写model(x)就会自动调用这个函数

def train(model, train_loader, val_loader, lr=0.001, epoch_num=100):
#model：MLP网络
#train_loader：训练数据加载器,val_loader：验证数据加载器,lr=0.001：学习率，控制每次参数修改幅度,epoch_num=100：总共训练100轮
    loss_func = nn.CrossEntropyLoss()
#损失函数：交叉熵损失，分类任务专用，衡量预测结果和真实标签之间差距
    optimizer = optim.Adam(model.parameters(), lr=lr)
#优化器Adam，拿到网络里面全部参数；用学习率lr更新权重，让loss变小
    #保存每一轮的loss和准确率，后面画图
    train_loss_list, val_loss_list = [], []
    train_acc_list, val_acc_list = [], []
#4个空列表，记录训练,验证的损失和准确率,画曲线图依靠
    for epoch in range(epoch_num):
#循环,一轮epoch代表完整跑完一遍全部训练数据,循环100次
#训练
        model.train()
#model.train()：切换模型到训练模式，启用dropout、BN训练专属功能
        total_loss, correct, total = 0, 0, 0
#初始化变量：本轮总损失、猜对样本数量、样本总数，全部清零
        for xb, yb in train_loader:
#循环读取每一批数据：xb一批坐标，yb对应的标签，一批32个样本
            optimizer.zero_grad()
#梯度清零 PyTorch梯度会自动累加，不清零的话，上一轮的梯度会混进来，计算出错(重点)
            pred = model(xb)
#前向传播，这批坐标xb送入网络，得预测结果pred
            loss = loss_func(pred, yb)
#计算损失loss，对比网络预测pred和真实标签yb
            loss.backward()
#反向传播自动求导，算出每个权重要调整多少才能降低loss
            optimizer.step()
#更新权重,优化器根据上面求出的梯度，修改参数，完成一次学习
            total_loss += loss.item()
#累加这批损失,.item()把张量数字转普通Python数字
            pred_label = torch.argmax(pred, dim=1)
#argmax：找出pred里面最大值的下标，下标是预测类别（0/1）
            correct += (pred_label == yb).sum().item()
#对比预测标签和真实标签，相等就是猜对，累加猜对数量
            total += yb.size(0)
#累加本轮样本总数，yb.size(0)=这一批样本个数（32）
        train_loss = total_loss / len(train_loader)
#本轮训练平均loss = 总loss ÷ 一共有多少批次
        train_acc = correct / total
#训练集准确率 = 猜对数量 ÷ 全部样本数量
#验证
        model.eval()
#model.eval()：模型为评估模式，关闭训练专属功能，不计算梯度，省内存
        val_loss, val_correct, val_total = 0, 0, 0
        with torch.no_grad():
#with torch.no_grad()：不算梯度,验证阶段不用更新网络,关掉梯度计算,提速省内存
            for xb, yb in val_loader:
                pred = model(xb)
                loss = loss_func(pred, yb)
                val_loss += loss.item()
                pred_label = torch.argmax(pred, dim=1)
                val_correct += (pred_label == yb).sum().item()
                val_total += yb.size(0)

#循环读取验证集每一批数据，送入模型预测,计算损失、统计猜对数量
#with torch.no_grad()包裹这部分,不保存梯度信息
        val_loss = val_loss / len(val_loader)
        val_acc = val_correct / val_total
#计算验证集平均loss,验证集准确率
# 保存数据用于画图
        train_loss_list.append(train_loss)
        val_loss_list.append(val_loss)
        train_acc_list.append(train_acc)
        val_acc_list.append(val_acc)

# 打印每一轮结果
        print(f"Epoch:{epoch:3d}, train_loss:{train_loss:.4f}, train_acc:{train_acc:.4f}, val_loss:{val_loss:.4f}, val_acc:{val_acc:.4f}")
#把本轮loss,准确率存入列表；打印训练信息,看训练效果
    return train_loss_list, val_loss_list, train_acc_list, val_acc_list
#训练结束,返回4组数据,用来绘制loss,accuracy曲线
#训练
my_model = MLP(hidden_dim=64)
train_loss, val_loss, train_acc, val_acc = train(my_model, train_loader, val_loader, lr=0.001, epoch_num=100)
# 创建模型实例,隐藏层神经元64个
# 调用train函数,开始训练,接收返回的4组曲线数据
#保存
torch.save(my_model.state_dict(), "mlp_model.pth")
#torch.save():保存文件
#my_model.state_dict()只保存网络学到的权重参数
#"mlp_model.pth"文件名,pth模型文件后缀


import matplotlib.pyplot as plt
# 绘图库matplotlib,画曲线图
plt.figure(figsize=(12,4))
# 创建画布,大小宽12，高4
# 第一张loss损失曲线
plt.subplot(1,2,1)#画布分成1行2列，画第1个
plt.plot(train_loss, label="train loss")
# 画训练集损失曲线；loss小-模型预测错误少
plt.plot(val_loss, label="val loss")#画验证集损失曲线
plt.xlabel("epoch")#X轴名字：epoch，训练轮数
plt.ylabel("loss")#Y轴名字损失值
plt.title("Loss Curve")# 图片标题损失曲线
plt.legend()# 显示图例,区分两条线,第二张：accuracy准确率曲线
plt.subplot(1,2,2)# 换到第2张图
plt.plot(train_acc, label="train acc")# 训练集准确率，越接近1效果越好
plt.plot(val_acc, label="val acc")# 验证集准确率
plt.xlabel("epoch")#X轴：训练轮数
plt.ylabel("accuracy")#Y轴：准确率
plt.title("Accuracy Curve")#标题：准确率曲线
plt.legend()#显示图例
plt.tight_layout()#自动调整图的布局，防文字重叠
plt.savefig("loss_acc_curve.png")# 保存图片
plt.show()#展示图片


#二维决策边界是模型划分不同类别的分界线
#绘制二维决策边界
import numpy as np
#导入numpy，生成坐标网格点
def plot_decision_boundary(model, X, y,filename="decision_boundary.png"):
#定义函数plot_decision_boundary，专门画分割月牙的分界线
#参数model：训练完成的模型；X：原始样本坐标；y：原始样本标签
    x_min, x_max = X[:,0].min()-0.5, X[:,0].max()+0.5
#取出所有样本第1维坐标的最小、最大值，左右向外拓宽0.5，留出边距
    y_min, y_max = X[:,1].min()-0.5, X[:,1].max()+0.5
#取出所有样本第2维坐标的最小、最大值，上下向外拓宽0.5
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),
                         np.arange(y_min, y_max, 0.01))
#生成网格：在x、y范围内生成大量点，点间间隔0.01，铺满
    grid = np.c_[xx.ravel(), yy.ravel()]
#拉平网格，变成N行2列数组，一行代表平面上一个(x,y)坐标
    grid_tensor = torch.tensor(grid, dtype=torch.float32)
#numpy数组转为torch张量，只有张量才能送入PyTorch模型预测
    model.eval()
#模型切换评估模式，关闭dropout,bn这类训练专属功能
    with torch.no_grad():
#关闭梯度计算(画图只是预测，不需要求梯度；节省内存，跑得更快)
        pred = model(grid_tensor)
#把全部网格坐标送入模型，预测每一个网格点属于类别0/1
    pred_label = torch.argmax(pred, dim=1).reshape(xx.shape)
#argmax预测类别；reshape还原回二维网格形状，上色
    plt.contourf(xx, yy, pred_label, alpha=0.4, cmap="coolwarm")
#填充色块:不同类别填充不同颜色 两颜色交界线就是决策边界
#alpha=0.4  透明度，cmap="coolwarm"配色方案
    plt.scatter(X[:,0], X[:,1], c=y, s=20, cmap="coolwarm")
#绘制原始月牙样本散点，不同标签不同颜色，s=20是点的大小
    plt.title("Decision Boundary")
#设置标题决策边界
    plt.savefig(filename)
#保存图片到项目文件夹，文件名decision_boundary.png
    plt.show()
#展示这张图
#调用函数,画模型的决策边界
plot_decision_boundary(my_model, X, y, filename="decision_boundary.png")
#给函数加一个参数，让保存的文件名可以自定义(修改)
#模型加载与测试集验证
print("\n开始加载模型并在测试集上验证...")
#实例化一个结构完全相同的空模型 创建一个新的神经网络对象
loaded_model = MLP(hidden_dim=64)
#PyTorch的state_dict保存了权重数值，不知道网络有多少层、每层多少个神经元所以把空骨架loaded_model搭出来，规格和保存的模型一致
#loaded_model：接收空模型的变量名
loaded_model.load_state_dict(torch.load("mlp_model.pth"))
#加载刚刚保存的权重参数
#从硬盘上把之前用torch.save()保存的文件读取,把读出来的权重数据，塞进刚刚创建的空骨架里变成了训练好的模型
loaded_model.eval() 
# 切换到评估模式(重要,确保 Dropout/BN(Dropout是训练时随机失活神经元以防过拟合，BN是归一化每层输入以加速训练和稳定梯度)等关闭）
# 测试前必须调用.eval(),否则Dropout会随机丢弃神经元,BatchNorm会用当前batch的统计量导致预测结果不稳定
#BatchNorm:对每层的输入mini‑batch计算均值方差,进行标准化,使其分布稳定,加速训练、缓解梯度消失/爆炸,提升泛化能力
test_correct, test_total = 0, 0 #初始化两个计数器,记录预测对和测试集的样本数
with torch.no_grad(): # 测试不需要计算梯度,不会记录任何梯度信息,节省大量显存，并加速运行
    for xb, yb in test_loader:#遍历32个样本的特征,真实标签
        pred = loaded_model(xb)
        #前向传播:32个样本进加载好的模型,模型输出形状是(32,2),两数值代表类别0和1的得分,数值越大,代表模型越确信属于该类别
        pred_label = torch.argmax(pred, dim=1)
        #取预测概率最大的类别索引0/1,沿着第1维度找出最大值所在的索引,返回的是最大值所在的下标/索引
        test_correct += (pred_label == yb).sum().item()
        #统计猜对的数量:逐个元素比较,预测对返到True(1),错到False(0),得一个布尔张量;把布尔张量里的True加起来,得到猜对数量;
        #item()把PyTorch的张量转成普通的Python整数(方便加减法);累加到总猜对数test_correct里
        test_total += yb.size(0)
        #当前批次的实际样本数累加到test_total里,算总数
test_acc = test_correct / test_total
print(f"加载模型后的测试集准确率: {test_acc:.4f}")
#最终准确率 = 猜对数/总数;格式化输出,保留小数点后4位
# 用刚刚加载并测试过的模型，在测试集上画决策边界
print("\n正在绘制测试集数据的决策边界...")
plt.figure(figsize=(6, 5)) # 新建一张画布
plot_decision_boundary(loaded_model, X_test, y_test, filename="decision_boundary_test.png")
#生成第二张图
# 4.对照试验(消融实验) 控制变量，观察不同超参数对训练结果的影响
print("\n开始实验")
# 建立实验清单
# 定义了一个列表，每个元素是一个字典，代表一个独立实验配置
experiments = [
    # 第一组：宽度对比实验（固定学习率0.001，改变宽度）
    {"name": "宽度=16 (小容量)",   "hidden_dim": 16,  "lr": 0.001},
    {"name": "宽度=64 (基线)",     "hidden_dim": 64,  "lr": 0.001},
    {"name": "宽度=256 (大容量)",  "hidden_dim": 256, "lr": 0.001},
    
    # 第二组：学习率对比实验（固定宽度64，改变学习率）
    {"name": "lr=0.1 (步子太大)",  "hidden_dim": 64,  "lr": 0.1},
    {"name": "lr=0.0001 (步子太小)","hidden_dim": 64,  "lr": 0.0001}
]
# 创建一个空的字典,保存实验结果，方便最后打印表格
results = {}
# 循环跑实验
for exp in experiments: #exp是临时变量
    print(f"\n----- 正在训练: {exp['name']} -----")
    print(f"参数设置: 隐藏层宽度={exp['hidden_dim']}, 学习率={exp['lr']}")
    
    # 每次实验要重新创建一个全新模型，防止上次训练结果残留
    exp_model = MLP(hidden_dim=exp['hidden_dim'])
    # 调用写的train函数训练
    # epoch_num=100固定，保证所有实验训练轮数一致
    t_loss, v_loss, t_acc, v_acc = train(
        exp_model, train_loader, val_loader, 
        lr=exp['lr'], epoch_num=100
    )
    
    # 训练结束，只记录最后一轮验证集Loss和准确率作为实验的最终成绩
    results[exp['name']] = {
        "val_loss": v_loss[-1],  # 取列表最后一个元素
        "val_acc": v_acc[-1]
    }
# 打印最终的对比表格
print("\n\n" + "="*50)
print("对照实验最终结果对比表")
print("="*50)
#使用格式化字符串对齐输出，看起来像表格(字符串乘法,会打印50个等号,起分隔作用,让控制台输出更美观)
print(f"{'实验设置 (配置名)':<25} | {'验证集Loss':<12} | {'验证集准确率':<12}")
print("-" * 55)
#:<25左对齐,并且强制占25个字符宽度(如 "宽度=16" 只有5个字符，自动在后面补20个空格,打印出来的各列能上下对齐)
for name, res in results.items():
    print(f"{name:<25} | {res['val_loss']:<12.4f} | {res['val_acc']:<12.4f}")
print("="*50)
#.items()：遍历字典，每次取出一个键name,如“宽度=16”)和一个值(res,就是{"val_loss":0.25,"val_acc": 0.89}

#1.激活函数
 #隐藏层用ReLU.因为计算快,缓解梯度消失,收敛快,让模型能画出弯曲的决策边界.输出层不加激活函数，配合 CrossEntropyLoss 内部自动处理，数值更稳定
#2.损失函数 三分类
 #选了CrossEntropyLoss;内部包含LogSoftmax和NLLLoss,数值稳定,二分类输出2个节点
#三分类:模型输出层改为3个节点,损失函数仍为CrossEntropyLoss
#3.zero_grad清空梯度,backward计算梯度,step更新参数
 #如果不清空,梯度累加,导致梯度爆炸,模型无法收敛
 #收敛:事物从分散,不确定或变化的状态,逐渐趋向某个确定,稳定或有限的值或状态;
#4.模型容量
 #更深、更宽的神经网络不一定能取得更好的效果;模型太简单会欠拟合(训练集和测试集表现差),太复杂会过拟合(训练集上表现好,但在测试集或新数据上表现差),需要平衡
#5.学习率
 #太大导致Loss震荡发散(震荡指变量在一定范围内来回波动不趋于固定值，发散指变量无限增大或无规律波动，不收敛于任何确定值；太小导致收敛缓慢
 #曲线表现:震荡锯齿形或平缓直线
#6.样本数量不均衡
 #模型偏向多数类,准确率虚高但少数类召回率低(少数类样本太少,模型为了降低Loss,选择“无脑全猜多数类”，导致整体准确率很高,而真正需要抓出来的少数类一个都没抓到(召回率为0))
 #eg.构造990个类别0,10个类别1 模型全猜0,准确率99%
 #解决办法:重采样,加权Loss(pos_weight),Focal Loss;给少数类Loss加更大的权重(让猜错少数类的代价变大)，或通过过采样把少数类数据复制多份
#7.想要过拟合这个数据集:
 #使用极复杂的模型,在极少的数据上训练长时间
 #表现:训练Loss持续下降接近0,验证Loss先降后升(U型);训练集准确率极高，验证集准确率明显低
plot_decision_boundary(my_model, X, y, filename="decision_boundary.png")
#给函数加一个参数，让保存的文件名可以自定义(修改)
#模型加载与测试集验证
print("\n开始加载模型并在测试集上验证...")
#实例化一个结构完全相同的空模型 创建一个新的神经网络对象
loaded_model = MLP(hidden_dim=64)
#PyTorch的state_dict保存了权重数值，不知道网络有多少层、每层多少个神经元所以把空骨架loaded_model搭出来，规格和保存的模型一致
#loaded_model：接收空模型的变量名
loaded_model.load_state_dict(torch.load("mlp_model.pth"))
#加载刚刚保存的权重参数
#从硬盘上把之前用torch.save()保存的文件读取,把读出来的权重数据，塞进刚刚创建的空骨架里变成了训练好的模型
loaded_model.eval() 
# 切换到评估模式(重要,确保 Dropout/BN(Dropout是训练时随机失活神经元以防过拟合，BN是归一化每层输入以加速训练和稳定梯度)等关闭）
# 测试前必须调用.eval(),否则Dropout会随机丢弃神经元,BatchNorm会用当前batch的统计量导致预测结果不稳定
#BatchNorm:对每层的输入mini‑batch计算均值方差,进行标准化,使其分布稳定,加速训练、缓解梯度消失/爆炸,提升泛化能力
test_correct, test_total = 0, 0 #初始化两个计数器,记录预测对和测试集的样本数
with torch.no_grad(): # 测试不需要计算梯度,不会记录任何梯度信息,节省大量显存，并加速运行
    for xb, yb in test_loader:#遍历32个样本的特征,真实标签
        pred = loaded_model(xb)
        #前向传播:32个样本进加载好的模型,模型输出形状是(32,2),两数值代表类别0和1的得分,数值越大,代表模型越确信属于该类别
        pred_label = torch.argmax(pred, dim=1)
        #取预测概率最大的类别索引0/1,沿着第1维度找出最大值所在的索引,返回的是最大值所在的下标/索引
        test_correct += (pred_label == yb).sum().item()
        #统计猜对的数量:逐个元素比较,预测对返到True(1),错到False(0),得一个布尔张量;把布尔张量里的True加起来,得到猜对数量;
        #item()把PyTorch的张量转成普通的Python整数(方便加减法);累加到总猜对数test_correct里
        test_total += yb.size(0)
        #当前批次的实际样本数累加到test_total里,算总数
test_acc = test_correct / test_total
print(f"加载模型后的测试集准确率: {test_acc:.4f}")
#最终准确率 = 猜对数/总数;格式化输出,保留小数点后4位
# 用刚刚加载并测试过的模型，在测试集上画决策边界
print("\n正在绘制测试集数据的决策边界...")
plt.figure(figsize=(6, 5)) # 新建一张画布
plot_decision_boundary(loaded_model, X_test, y_test, filename="decision_boundary_test.png")
#生成第二张图
# 4.对照试验(消融实验) 控制变量，观察不同超参数对训练结果的影响
print("\n开始实验")
# 建立实验清单
# 定义了一个列表，每个元素是一个字典，代表一个独立实验配置
experiments = [
    # 第一组：宽度对比实验（固定学习率0.001，改变宽度）
    {"name": "宽度=16 (小容量)",   "hidden_dim": 16,  "lr": 0.001},
    {"name": "宽度=64 (基线)",     "hidden_dim": 64,  "lr": 0.001},
    {"name": "宽度=256 (大容量)",  "hidden_dim": 256, "lr": 0.001},
    
    # 第二组：学习率对比实验（固定宽度64，改变学习率）
    {"name": "lr=0.1 (步子太大)",  "hidden_dim": 64,  "lr": 0.1},
    {"name": "lr=0.0001 (步子太小)","hidden_dim": 64,  "lr": 0.0001}
]
# 创建一个空的字典,保存实验结果，方便最后打印表格
results = {}
# 循环跑实验
for exp in experiments: #exp是临时变量
    print(f"\n----- 正在训练: {exp['name']} -----")
    print(f"参数设置: 隐藏层宽度={exp['hidden_dim']}, 学习率={exp['lr']}")
    
    # 每次实验要重新创建一个全新模型，防止上次训练结果残留
    exp_model = MLP(hidden_dim=exp['hidden_dim'])
    # 调用写的train函数训练
    # epoch_num=100固定，保证所有实验训练轮数一致
    t_loss, v_loss, t_acc, v_acc = train(
        exp_model, train_loader, val_loader, 
        lr=exp['lr'], epoch_num=100
    )
    
    # 训练结束，只记录最后一轮验证集Loss和准确率作为实验的最终成绩
    results[exp['name']] = {
        "val_loss": v_loss[-1],  # 取列表最后一个元素
        "val_acc": v_acc[-1]
    }
# 打印最终的对比表格
print("\n\n" + "="*50)
print("对照实验最终结果对比表")
print("="*50)
#使用格式化字符串对齐输出，看起来像表格(字符串乘法,会打印50个等号,起分隔作用,让控制台输出更美观)
print(f"{'实验设置 (配置名)':<25} | {'验证集Loss':<12} | {'验证集准确率':<12}")
print("-" * 55)
#:<25左对齐,并且强制占25个字符宽度(如 "宽度=16" 只有5个字符，自动在后面补20个空格,打印出来的各列能上下对齐)
for name, res in results.items():
    print(f"{name:<25} | {res['val_loss']:<12.4f} | {res['val_acc']:<12.4f}")
print("="*50)
#.items()：遍历字典，每次取出一个键name,如“宽度=16”)和一个值(res,就是{"val_loss":0.25,"val_acc": 0.89}
# 加载模型
loaded_model = MLP(hidden_dim=64)
loaded_model.load_state_dict(torch.load("mlp_model.pth"))
loaded_model.eval()
# 补充：混淆矩阵与错误样本分析
from sklearn.metrics import confusion_matrix
import seaborn as sns
print("\n开始生成混淆矩阵和错误样本图 ")
# 1. 加载模型（必须在画图前加载）
loaded_model = MLP(hidden_dim=64)
loaded_model.load_state_dict(torch.load("mlp_model.pth"))
loaded_model.eval()
# 2. 跑测试集收集预测结果
all_preds, all_labels = [], []
with torch.no_grad():
    for xb, yb in test_loader:
        pred = loaded_model(xb)
        pred_label = torch.argmax(pred, dim=1)
        all_preds.extend(pred_label.cpu().numpy())
        all_labels.extend(yb.cpu().numpy())
# 3. 画混淆矩阵
cm = confusion_matrix(all_labels, all_preds)
plt.figure(figsize=(5, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=['预测0', '预测1'], yticklabels=['真实0', '真实1'])
plt.title("混淆矩阵 Confusion Matrix")
plt.savefig("confusion_matrix.png")
plt.show()
# 4. 画错误样本图
error_indices = [i for i in range(len(all_preds)) if all_preds[i] != all_labels[i]]
plt.figure(figsize=(6, 5))
plt.scatter(X_test[:, 0], X_test[:, 1], c='gray', alpha=0.3, label='正确分类样本')
if len(error_indices) > 0:
    plt.scatter(X_test[error_indices, 0], X_test[error_indices, 1], 
                c='red', marker='x', s=100, label='错误分类样本')
plt.title("错误样本可视化")
plt.legend()
plt.savefig("error_samples.png")
plt.show()
print("混淆矩阵和错误样本图已保存！")